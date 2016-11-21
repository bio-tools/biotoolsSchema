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
public enum LicenseType {
    @XmlEnumValue("Adaptive Public License 1.0") APL_1,
    @XmlEnumValue("Apache License 2.0") ASL_2,
    @XmlEnumValue("Apple Public Source License 2.0") APSL_2,
    @XmlEnumValue("Artistic License 2.0") ARTISTIC_2,
    @XmlEnumValue("BSD 2-Clause License") BSD_2,
    @XmlEnumValue("BSD 3-Clause License (Revised)") BSD_3,
    @XmlEnumValue("CeCILL v2") CeCILL_2,
    @XmlEnumValue("Common Development and Distribution License (CDDL-1.0)") CDDL_1,
    @XmlEnumValue("Common Public Attribution License Version 1.0") CPAL_1,
    @XmlEnumValue("Common Public License 1.0") CPL_1,
    @XmlEnumValue("Creative Commons Attribution NonCommercial NoDerivs") CC_BY_NC_ND,
    @XmlEnumValue("Creative Commons Attribution NoDerivs") CC_BY_ND,
    @XmlEnumValue("Creative Commons Attribution 3.0 Unported") CC_BY_3,
    @XmlEnumValue("Creative Commons Attribution 4.0 International") CC_BY_4,
    @XmlEnumValue("Creative Commons Attribution NonCommercial") CC_BY_NC,
    @XmlEnumValue("Creative Commons Attribution NonCommercial ShareAlike") CC_BY_SA_NC,
    @XmlEnumValue("Creative Commons Attribution-NonCommercial 2.0 Generic") CC_BY_NC_2,
    @XmlEnumValue("Creative Commons Attribution Share Alike") CC_BY_SA,
    @XmlEnumValue("Creative Commons CC0 1.0 Universal") CC0_1,
    @XmlEnumValue("Eclipse Public License 1.0") EPL_1,
    @XmlEnumValue("Educational Community License Version 2.0") ECL_2,
    @XmlEnumValue("European Union Public License 1.1") EUPL_1_1,
    @XmlEnumValue("GNU Affero General Public License v3") AGPL_3,
    @XmlEnumValue("GNU Free Documentation License v1.3") FDL_1_3,
    @XmlEnumValue("GNU General Public License v2") GPL_2,
    @XmlEnumValue("GNU General Public License v3") GPL_3,
    @XmlEnumValue("GNU Lesser General Public License v2.1") LGPL_2_1,
    @XmlEnumValue("IBM Public License") IPL,
    @XmlEnumValue("ISC License") ISC,
    @XmlEnumValue("Microsoft Public License") MS_PL,
    @XmlEnumValue("Microsoft Shared Source Community License") MS_CL,
    @XmlEnumValue("Microsoft Reciprocal License") MS_RL,
    @XmlEnumValue("MIT License") MIT,
    @XmlEnumValue("Mozilla Public License 1.1") MPL_1_1,
    @XmlEnumValue("Mozilla Public License 2.0") MPL_2,
    @XmlEnumValue("Non-Profit Open Software License 3.0") NPOSL_3,
    @XmlEnumValue("ODC Open Database License") ODBL,
    @XmlEnumValue("ODC Public Domain Dedication and License 1.0") PDDL_1,
    @XmlEnumValue("Open Public License v1.0") OPL_1,
    @XmlEnumValue("Open Software Licence 3.0") OSL_3,
    @XmlEnumValue("PHP License 3.0") PHP_3,
    @XmlEnumValue("Proprietary") PROPRIETARY,
    @XmlEnumValue("Simple Public License 2.0") SIMPL_2,
    @XmlEnumValue("Reciprocal Public License 1.5") RPL_1_5,
    @XmlEnumValue("Other") OTHER;
}
