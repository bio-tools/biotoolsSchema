/**
 * *****************************************************************************
 * Copyright (C) 2016 ELIXIR ES, Spanish National Bioinformatics Institute (INB)
 * and Barcelona Supercomputing Center (BSC)
 *
 * Modifications to the initial code base are copyright of their respective
 * authors, or their employers as appropriate.
 * 
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301  USA
 *****************************************************************************
 */
package es.elixir.bsc.biotools.parser.model;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;

/**
 *
 * @author Dmitry Repchevsky
 */

@XmlEnum(EnumType.class)
public enum DownloadType {
    @XmlEnumValue("Biological data") BIOLOGICAL_DATA,
    @XmlEnumValue("Binaries") BINARIES,
    @XmlEnumValue("Command-line specification") COMMANDLINE_SPECIFICATION,
    @XmlEnumValue("CWL file") CWL,
    @XmlEnumValue("Debian source package") DEBIAN_SOURCE_PACKAGE,
    @XmlEnumValue("Galaxy wrapper") GALAXY_WRAPPER,
    @XmlEnumValue("Icon") ICON,
    @XmlEnumValue("Package (other)") OTHER_PACKAGE,
    @XmlEnumValue("Source code") SOURCE_CODE,
    @XmlEnumValue("Taverna wrapper") TAVERNA_WRAPPER,
    @XmlEnumValue("Test data") TEST_DATA,
    @XmlEnumValue("Test script") TEST_SCRIPT,
    @XmlEnumValue("Tool wrapper (other)") OTHER_TOOL_WRAPPER,
    @XmlEnumValue("Debian binary package") DEBIAN_BINARY_PACKAGE;
}
