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

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;

/**
 * 
 * @author Dmitry Repchevsky
 */

@XmlType(name = "", propOrder = {"name",
                                 "version",
                                 "biotoolsId",
                                 "doi",
                                 "shortDescription",
                                 "description",
                                 "homepage",
                                 "mirrors",
                                 "repositories",
                                 "socialMedias"})
public class Summary {

    private NameType name;
    private String version;
    private BiotoolsIdType biotoolsId;
    private DoiType doi;
    private String shortDescription;
    private TextType description;
    private UrlType homepage;
    private List<UrlType> mirrors;
    protected List<UrlFtpType> repositories;
    protected List<UrlType> socialMedias;

    @XmlElement(required = true)
    public NameType getName() {
        return name;
    }

    public void setName(NameType name) {
        this.name = name;
    }

    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    @XmlElement(required = true)
    public BiotoolsIdType getBiotoolsId() {
        return biotoolsId;
    }

    public void setBiotoolsId(BiotoolsIdType biotoolsId) {
        this.biotoolsId = biotoolsId;
    }

    @XmlElement(required = true)
    public DoiType getDoi() {
        return doi;
    }

    public void setDoi(DoiType doi) {
        this.doi = doi;
    }

    public String getShortDescription() {
        return shortDescription;
    }

    public void setShortDescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }

    public TextType getDescription() {
        return description;
    }

    public void setDescription(TextType description) {
        this.description = description;
    }

    @XmlElement(required = true)
    public UrlType getHomepage() {
        return homepage;
    }

    public void setHomepage(UrlType homepage) {
        this.homepage = homepage;
    }

    @XmlElement(name = "mirror")
    public List<UrlType> getMirrors() {
        if (mirrors == null) {
            mirrors = new ArrayList<>();
        }
        return mirrors;
    }

    @XmlElement(name = "repository")
    public List<UrlFtpType> getRepositories() {
        if (repositories == null) {
            repositories = new ArrayList<>();
        }
        return repositories;
    }

    @XmlElement(name = "socialMedia")
    public List<UrlType> getSocialMedias() {
        if (socialMedias == null) {
            socialMedias = new ArrayList<>();
        }
        return socialMedias;
    }
}