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
public enum LanguageType {
    @XmlEnumValue("ActionScript") ACTION_SCRIPT,
    @XmlEnumValue("Ada") ADA,
    @XmlEnumValue("AppleScript") APPLE_SCRIPT,
    @XmlEnumValue("Assembly language") ASSEMBLY_LANGUAGE,
    @XmlEnumValue("AWK") AWK,
    @XmlEnumValue("Bash") BASH,
    @XmlEnumValue("C") C,
    @XmlEnumValue("C#") CSharp,
    @XmlEnumValue("C++") CPP,
    @XmlEnumValue("COBOL") COBOL,
    @XmlEnumValue("ColdFusion") COLD_FUSION,
    @XmlEnumValue("CWL") CWL,
    @XmlEnumValue("D") D,
    @XmlEnumValue("Delphi") DELPHI,
    @XmlEnumValue("Dylan") DYLAN,
    @XmlEnumValue("Eiffel") EIFFEL,
    @XmlEnumValue("Forth") FORTH,
    @XmlEnumValue("Fortran") FORTRAN,
    @XmlEnumValue("Groovy") GROOVY,
    @XmlEnumValue("Haskell") HASKELL,
    @XmlEnumValue("Icarus") ICARUS,
    @XmlEnumValue("Java") JAVA,
    @XmlEnumValue("Javascript") JAVASCRIPT,
    @XmlEnumValue("JSP") JSP,
    @XmlEnumValue("LabVIEW") LABVIEW,
    @XmlEnumValue("Lisp") LISP,
    @XmlEnumValue("Lua") LUA,
    @XmlEnumValue("Maple") MAPLE,
    @XmlEnumValue("Mathematica") MATHEMATICA,
    @XmlEnumValue("MATLAB") MATLAB,
    @XmlEnumValue("MLXTRAN") MLXTRAN,
    @XmlEnumValue("NMTRAN") NMTRAN,
    @XmlEnumValue("Pascal") PASCAL,
    @XmlEnumValue("Perl") PERL,
    @XmlEnumValue("PHP") PHP,
    @XmlEnumValue("Prolog") PROLOG,
    @XmlEnumValue("PyMOL") PYMOL,
    @XmlEnumValue("Python") PYTHON,
    @XmlEnumValue("R") R,
    @XmlEnumValue("Racket") RACKET,
    @XmlEnumValue("REXX") REXX,
    @XmlEnumValue("Ruby") RUBY,
    @XmlEnumValue("SAS") SAS,
    @XmlEnumValue("Scala") SCALA,
    @XmlEnumValue("Scheme") SCHEME,
    @XmlEnumValue("Shell") SHELL,
    @XmlEnumValue("Smalltalk") SMALLTALK,
    @XmlEnumValue("SQL") SQL,
    @XmlEnumValue("Turing") TURING,
    @XmlEnumValue("VHDL") VHDL,
    @XmlEnumValue("Verilog") VERILOG,
    @XmlEnumValue("Visual Basic") VISUAL_BASIC,
    @XmlEnumValue("Other") OTHER;
}
