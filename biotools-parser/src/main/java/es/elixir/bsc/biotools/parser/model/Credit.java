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

import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;

/**
 * 
 * @author Dmitry Repchevsky
 */

@XmlType(name = "", propOrder = {"name",
                                 "url",
                                 "gridId",
                                 "orcidId",
                                 "entity",
                                 "role",
                                 "comment"})
public class Credit {

    private Object name;
    private String url;
    private String gridId;
    private String orcidId;
    private EntityType entity;
    private RoleType role;
    private TextType comment;

    public Object getName() {
        return name;
    }

    public void setName(Object value) {
        this.name = value;
    }

    @XmlSchemaType(name = "anyURI")
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    public String getGridId() {
        return gridId;
    }

    public void setGridId(String gridId) {
        this.gridId = gridId;
    }

    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    public String getOrcidId() {
        return orcidId;
    }

    public void setOrcidId(String orcidId) {
        this.orcidId = orcidId;
    }

    public EntityType getEntity() {
        return entity;
    }

    public void setEntity(EntityType entity) {
        this.entity = entity;
    }

    public RoleType getRole() {
        return role;
    }

    public void setRole(RoleType role) {
        this.role = role;
    }

    public TextType getComment() {
        return comment;
    }

    public void setComment(TextType comment) {
        this.comment = comment;
    }
}
