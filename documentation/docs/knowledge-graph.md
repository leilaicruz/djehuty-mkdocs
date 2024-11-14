# Knowledge graph

djehuty processes its information using the Resource Description Framework ([Lassila](#Xlassila-99-rdf), [1999](#Xlassila-99-rdf)). This chapter
describes the parts that make up the data model of djehuty.
### 3\.1  Use of vocabularies


Throughout this chapter, abbreviated references to ontologies are used. Table [3\.1](#x1-29001r1) lists these
abbreviations.



---




| Abbreviation | Ontology URI |
| djht | [https://ontologies.data.4tu.nl/djehuty/24\.10\.1/](https://ontologies.data.4tu.nl/djehuty/24.10.1/) |
| rdf | [http://www.w3\.org/1999/02/22\-rdf\-syntax\-ns\#](http://www.w3.org/1999/02/22-rdf-syntax-ns) |
| rdfs | [http://www.w3\.org/2000/01/rdf\-schema\#](http://www.w3.org/2000/01/rdf-schema) |
| xsd | [http://www.w3\.org/2001/XMLSchema\#](http://www.w3.org/2001/XMLSchema) |
|  |


   Table 3\.1: Lookup table for vocabulary URIs and their abbreviations.   



---





### 3\.2  Notational shortcuts


In addition to abbreviating ontologies with their prefix we use another notational shortcut. To effectively
communicate the structure of the RDF graph used by djehuty we introduce a couple of shorthand
notations.

#### 3\.2\.1  Notation for typed triples


When the object in a triple is typed, we introduce the shorthand to only show the type, rather than the
actual value of the object. Figure [3\.1](#x1-31001r1) displays this for URIs, and figure [3\.2](#x1-31002r2) displays this for
literals.


---




 ![PIC](figures/typed-notation-.png)





  
    Figure 3\.1: Shorthand notation for triples with an rdf:type which features a hollow
predicate arrow and a colored type specifier with rounded corners.   



---


Literals are depicted by rectangles (with sharp edges) in contrast to URIs which are depicted as rectangles
with rounded edges.


---




 ![PIC](figures/typed-literals-notation-.png)





  
    Figure 3\.2: Shorthand notation for triples with a literal, which features a hollow predicate
arrow and a colored rectangular type specifier.   



---


When the subject of a triple is the shorthand type, assume the subject is not the type itself but the subject
which has that type.
#### 3\.2\.2  Notation for rdf:List


To preserve the order in which lists were formed, the data model makes use of rdf:List with numeric
indexes. This pattern will be abbreviated in the remainder of the figures as displayed in figure
[3\.3](#x1-32001r3).


---




 ![PIC](figures/rdf-list-abbrev-.png)





  
    Figure 3\.3: Shorthand notation for rdf:List with numeric indexes, which features a
hollow double\-arrow. Lists have arbitrary lengths, and the numeric indexes use 1\-based
indexing.   



---


The hollow double\-arrow depicts the use of an rdf:List with numeric indexes.
### 3\.3  Datasets


Datasets play a central role in the repository system because every other type links in one way or another
to it. The user submits files along with data about those bytes as a single record which we
call a djht:Dataset. Figure [3\.4](#x1-33001r4) shows how the remainder of types in this chapter relate to a
djht:Dataset.


---




 ![PIC](figures/dataset-.png)





  
    Figure 3\.4: The RDF pattern for a djht:Dataset. For a full overview of djht:Dataset
properties, use the exploratory from the administration panel.   



---


Datasets are versioned records. The data and metadata between versions can differ, except all versions of a
dataset share an identifier. We use djht:DatasetContainer to describe the version\-unspecific properties of
a set of versioned datasets.


---




 ![PIC](figures/dataset-container-.png)





  
    Figure 3\.5: The RDF pattern for a djht:DatasetContainer. All versions of a dataset
share a djht:dataset\_id and a UUID in the container URI.   



---


The data model follows a natural expression of published versions as a linked list. Figure [3\.5](#x1-33002r5) further
reveals that the view, download, share and citation counts are stored in a version\-unspecific
way.
### 3\.4  Accounts


djehuty uses an external identity provider, but stores an e\-mail address, full name, and preferences for
categories.


---




 ![PIC](figures/account-.png)





  
    Figure 3\.6: The RDF pattern for an djht:Account.   



---


### 3\.5  Funding


When the djht:Dataset originated out of a funded project, the funders can be listed using djht:Funding.
Figure [3\.7](#x1-35001r7) displays the details for this structure.


---




 ![PIC](figures/funding-.png)





  
    Figure 3\.7: The RDF pattern for a djht:Funding.   



---







