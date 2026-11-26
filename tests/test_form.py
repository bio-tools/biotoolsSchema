import json
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.request import Request, urlopen


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "jsonschema"


class FormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            [sys.executable, str(SCHEMA_DIR / "serve.py"), "--port", "0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        cls.addClassCleanup(cls.server.stdout.close)
        cls.addClassCleanup(cls.stop_server)
        startup = cls.server.stdout.readline().strip()
        if not startup.startswith("Open "):
            raise RuntimeError(f"Browser form failed to start: {startup}")
        cls.url = startup.removeprefix("Open ")

    @classmethod
    def stop_server(cls):
        cls.server.terminate()
        cls.server.wait(timeout=5)

    def request(self, path, data=None):
        headers = {"Content-Type": "application/json"} if data is not None else {}
        request = Request(self.url + path, data=data, headers=headers)
        with urlopen(request, timeout=5) as response:
            return response.read()

    def test_form_assets_and_schema_are_served(self):
        self.assertIn(b"Metadata editor", self.request(""))
        self.assertTrue(self.request("form.js"))
        self.assertTrue(self.request("style.css"))
        self.assertEqual(self.request("biotoolsj.json"), (SCHEMA_DIR / "biotoolsj.json").read_bytes())

    def test_form_uses_single_tool_validation(self):
        minimal = (SCHEMA_DIR / "examples" / "minimal.json").read_bytes()
        self.assertEqual(json.loads(self.request("validate", minimal)), [])
        issues = json.loads(self.request("validate", b'{"homepage":"invalid"}'))
        self.assertIn("$.homepage", [issue["path"] for issue in issues])
        self.assertTrue(json.loads(self.request("validate", b"[{}]")))


if __name__ == "__main__":
    unittest.main()
