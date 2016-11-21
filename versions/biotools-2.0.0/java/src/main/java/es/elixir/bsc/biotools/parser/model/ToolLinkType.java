package es.elixir.bsc.biotools.parser.model;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;

/**
 *
 * @author Dmitry Repchevsky
 */

@XmlEnum(EnumType.class)
public enum ToolLinkType {
    @XmlEnumValue("Browser") BROWSER,
    @XmlEnumValue("Helpdesk") HELPDESK,
    @XmlEnumValue("Issue tracker") ISSUE_TRACKER,
    @XmlEnumValue("Mailing list") MAILING_LIST,
    @XmlEnumValue("Mirror") MIRROR,
    @XmlEnumValue("Registry") REGISTRY,
    @XmlEnumValue("Repository") REPOSITORY,
    @XmlEnumValue("Social media") SOCIAL_MEDIA;
}
