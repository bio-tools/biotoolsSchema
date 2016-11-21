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
 * ELIXIR node.
 * 
 * @author Dmitry Repchevsky
 */

@XmlEnum(EnumType.class)
public enum ElixirNode {
    @XmlEnumValue("Belgium") BELGIUM,
    @XmlEnumValue("Czech Republic") CZHECH_REPUBLIC,
    @XmlEnumValue("Denmark") DENMARK,
    @XmlEnumValue("EMBL") EMBL,
    @XmlEnumValue("Estonia") ESTONIA,
    @XmlEnumValue("Finland") FINLAND,
    @XmlEnumValue("France") FRANCE,
    @XmlEnumValue("Germany") GERMANY,
    @XmlEnumValue("Greece") GREECE,
    @XmlEnumValue("Netherlands") NETHERLANDS,
    @XmlEnumValue("Norway") NORWAY,
    @XmlEnumValue("Ireland") IRELAND,
    @XmlEnumValue("Israel") ISRAEL,
    @XmlEnumValue("Italy") ITALY,
    @XmlEnumValue("Luxembourg") LUXEMBURG,
    @XmlEnumValue("Portugal") PORTUGAL,
    @XmlEnumValue("Slovenia") SLOVENIA,
    @XmlEnumValue("Spain") SPAIN,
    @XmlEnumValue("Sweden") SWEDEN,
    @XmlEnumValue("Switzerland") SWITZERLAND,
    @XmlEnumValue("UK") UK;
}
