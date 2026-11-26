const fields = document.querySelector("#fields");
const preview = document.querySelector("#preview");
const status = document.querySelector("#status");
const errors = document.querySelector("#errors");
const openButton = document.querySelector("#open");
const fileInput = document.querySelector("#file");
const validateButton = document.querySelector("#validate");
const downloadButton = document.querySelector("#download");

const sections = [
  ["Classification", [
    "toolType", "topic", "operatingSystem", "language", "license", "maturity",
    "cost", "accessibility", "collectionID", "elixirCommunity", "elixirNode", "elixirPlatform",
  ]],
  ["Identifiers and versions", ["biotoolsID", "biotoolsCURIE", "version", "otherID"]],
  ["Functions", ["function"]],
  ["Links and publications", ["link", "download", "documentation", "relation", "publication"]],
  ["Credits", ["credit"]],
];

let schema;
let record = {};
let nextId = 0;

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function button(text, onClick) {
  const node = element("button", "", text);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function resolve(node) {
  if (!node.$ref) return node;
  const target = node.$ref.slice(2).split("/").reduce(
    (value, key) => value[key.replaceAll("~1", "/").replaceAll("~0", "~")], schema,
  );
  return { ...resolve(target), ...node };
}

function valueAt(path) {
  return path.reduce((value, key) => value?.[key], record);
}

function setValue(path, value) {
  const parent = path.slice(0, -1).reduce((object, key) => (object[key] ??= {}), record);
  const key = path.at(-1);
  if (value === undefined) {
    delete parent[key];
  } else {
    parent[key] = value;
  }
  preview.textContent = JSON.stringify(record, null, 2);
  showStatus("Edited");
}

function labelFor(key) {
  const words = key.replace(/([a-z])([A-Z])/g, "$1 $2");
  return words[0].toUpperCase() + words.slice(1);
}

function renderFields(node, path, container, names = Object.keys(node.properties)) {
  for (const key of names) {
    const field = resolve(node.properties[key]);
    const label = field.title || labelFor(key);
    const fieldPath = [...path, key];
    const required = node.required?.includes(key) ?? false;
    container.append(renderField(field, label, fieldPath, required, key));
  }
}

function renderField(field, label, path, required, key) {
  if (field.type === "array") return renderArray(field, label, path, required, key);
  if (field.type === "object") {
    const group = element("fieldset", "nested");
    group.append(element("legend", "", label));
    renderFields(field, path, group);
    return group;
  }

  const wrapper = element("div", "field");
  const caption = element("label", "", label);
  const input = element(field.enum ? "select" : key === "description" || key === "note" ? "textarea" : "input");
  input.id = `field-${++nextId}`;
  caption.htmlFor = input.id;
  input.required = required;
  if (required) caption.append(element("span", "required", " (required)"));
  if (field.description) input.title = field.description;

  if (field.enum) {
    input.add(new Option("Select a value", ""));
    for (const option of field.enum) input.add(new Option(option, option));
  } else if (input.tagName === "TEXTAREA") {
    input.rows = 4;
  }

  input.value = valueAt(path) ?? "";
  input.addEventListener("input", () => {
    setValue(path, input.value || (typeof path.at(-1) === "number" ? "" : undefined));
  });
  wrapper.append(caption, input);
  return wrapper;
}

function renderArray(field, label, path, required, key) {
  const group = element("fieldset", "array");
  const legend = element("legend", "", label);
  if (required) legend.append(element("span", "required", " (required)"));
  const list = element("div", "array-list");
  const item = resolve(field.items);
  const add = button("Add entry", () => {
    setValue(path, [...(valueAt(path) ?? []), item.type === "object" ? {} : ""]);
    renderItems();
    list.lastElementChild.querySelector("input, select, textarea, button")?.focus();
  });
  add.setAttribute("aria-label", `Add entry to ${label}`);

  function renderItems() {
    list.replaceChildren();
    for (const [index] of (valueAt(path) ?? []).entries()) {
      const row = element("div", "array-row");
      const remove = button("Remove", () => {
        const entries = valueAt(path).filter((_, position) => position !== index);
        setValue(path, entries.length || required ? entries : undefined);
        renderItems();
        add.focus();
      });
      remove.className = "remove";
      remove.setAttribute("aria-label", `Remove ${label} entry ${index + 1}`);
      const itemLabel = item.title || `${label} entry`;
      row.append(renderField(item, itemLabel, [...path, index], false, key), remove);
      list.append(row);
    }
  }

  renderItems();
  group.append(legend, list, add);
  return group;
}

function renderRecord() {
  const tool = schema.$defs.tool;
  const required = tool.required ?? [];
  const shown = new Set(required);
  fields.replaceChildren();
  renderFields(tool, [], fields, required);
  const groups = sections.map(([title, keys]) => [
    title, keys.filter((key) => Object.hasOwn(tool.properties, key) && !shown.has(key)),
  ]);
  for (const [, keys] of groups) for (const key of keys) shown.add(key);
  groups.push(["Other fields", Object.keys(tool.properties).filter((key) => !shown.has(key))]);

  for (const [title, keys] of groups) {
    if (!keys.length) continue;
    const group = element("details", "section");
    group.open = keys.some((key) => Object.hasOwn(record, key));
    const content = element("div", "section-fields");
    renderFields(tool, [], content, keys);
    group.append(element("summary", "", title), content);
    fields.append(group);
  }
  preview.textContent = JSON.stringify(record, null, 2);
}

function showStatus(message, issues = []) {
  status.textContent = message;
  status.classList.toggle("invalid", issues.length > 0);
  errors.replaceChildren();
  for (const { path, message: issue } of issues) {
    const row = element("li");
    row.append(element("code", "", path), document.createTextNode(` ${issue}`));
    errors.append(row);
  }
  errors.hidden = !issues.length;
}

async function validate(json) {
  const response = await fetch("./validate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: json,
  });
  if (!response.ok) throw new Error("The validator could not check this record.");
  return response.json();
}

async function checkRecord(download) {
  const snapshot = JSON.stringify(record);
  showStatus("Validating…");
  try {
    const issues = await validate(snapshot);
    if (snapshot !== JSON.stringify(record)) return;
    showStatus(issues.length ? "Needs changes" : "Valid", issues);
    if (issues.length || !download) return;

    const data = JSON.parse(snapshot);
    const file = new Blob([JSON.stringify(data, null, 2) + "\n"], { type: "application/json" });
    const url = URL.createObjectURL(file);
    const link = element("a");
    link.href = url;
    link.download = `${data.biotoolsID || data.name.replace(/[^A-Za-z0-9_.-]+/g, "-")}.tool.json`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  } catch (error) {
    if (snapshot === JSON.stringify(record)) showStatus(error.message);
  }
}

fileInput.addEventListener("change", async () => {
  const file = fileInput.files[0];
  fileInput.value = "";
  if (!file) return;
  const before = JSON.stringify(record);
  try {
    const candidate = JSON.parse(await file.text());
    const issues = await validate(JSON.stringify(candidate));
    if (before !== JSON.stringify(record)) return;
    if (issues.length) {
      showStatus("Could not open the record", issues);
      return;
    }
    record = candidate;
    renderRecord();
    showStatus("Loaded");
  } catch (error) {
    if (before === JSON.stringify(record)) showStatus(error.message);
  }
});

fields.addEventListener("submit", (event) => event.preventDefault());
openButton.addEventListener("click", () => fileInput.click());
validateButton.addEventListener("click", () => checkRecord(false));
downloadButton.addEventListener("click", () => checkRecord(true));

try {
  const response = await fetch("./biotoolsj.json");
  if (!response.ok) throw new Error("Could not load the schema.");
  schema = await response.json();
  renderRecord();
  showStatus("Ready");
  for (const control of [openButton, validateButton, downloadButton]) control.disabled = false;
} catch (error) {
  showStatus(error.message);
}
