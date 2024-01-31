# manuscript-waste-reuse-finder

Code and research description to be presented at the 2024 [Family History Technology Conference](https://fhtw.byu.edu/). Research and Development on a tool to find document images where manuscript waste (a.k.a. binder's waste, somewhat-a.k.a. manuscript fragments) was used to bind other documents. Such reused manuscripts have been found to contain info relating to such diverse fields as genealogy and family history, manuscript studies, paleography, codicology, and of course fragmentology. It will be shown that it is extendable to finding such things as manuscript repairs (e.g. stitching) and iron-gall-ink corrosion.

# Fragment Finder

## Examples of Reused Manuscript Fragments (and of what are not so classified)

Before my description of the tool, I want to put here several images that illustrate Reused Manuscript Fragments. "Reused Manuscript Fragments" will be the term I use to describe what this tool is designed to find. I will also use <b>RMF</b> and such phrases as, "examples of reuse". The images are part of the original dataset.

If you're impatient to know about the tool and the accompanying research, you can see my [submission for a Research Talk](./BLACK-David_-_FHTC_2024_-_Reused_Manuscript_Fragments.pdf) as a PDF, or you can use this [LINK FOR THE AFTER-IMAGE PART](#Tool-Description-for-the-Family-History-Technology-Workshop).


### Example 1 : Universitätsbibliothek Heidelberg, Codex Salemitana VII,73

Title: _Ordinarium cisterciense_ 

Citation link: https://doi.org/10.11588/diglit.9273

[Public Domain Mark 1.0 Universal (No Copyright)](https://creativecommons.org/publicdomain/mark/1.0/)

[More information (bballdave025's metadata)](./Heidelberg_-_salVII73_URL.txt)


### Example 1.1 : Image of Binding Containing Manuscript Reuse Fragment

<b>This is in the positive class.</b>

<br/>
<div>
  <img src="./Heidelberg_-_salVII73_front-cover_500wid.jpg"
       alt="Front cover of Ordinarium cisterciense, Heidelberg Codex Salemitana VII,73. Example of Manuscript Reuse Fragment"
       width="250px">
</div>
<br/>

Binding (front cover) for the main book, _Ordinarium cisterciense_. The fragment appears to come from a large, decorated manuscript. Note the capital letters in red. [Image 1.1 Citation Link](https://doi.org/10.11588/diglit.9273#0001)


### Example 1.2 : Image without any Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./Heidelberg_-_salVII73_00186_500wid.jpg"
       alt="One of the leaves/pages inside Ordinarium cisterciense. Example without Manuscript Reuse."
       width="250px">
</div>
<br/>

One of the interior pages of _Ordinarium cisterciense_. One might call this a standard manuscript page. [Image 1.1 Citation Link](https://doi.org/10.11588/diglit.9273#0186)


### Example 2 : FamilySearch DGS 007996631 (item 1)

Catalog Record: Hausbücher 1397-1746

Film/Digital Note: 	Hausbücher 1493-1521 Altstadt: Hausbücher 1522-1716

Geographic Location for FamilySearch Catalog: Germany, Mecklenburg-Schwerin, Rostock

Citation:

> No citation is available

(Quoted from the FamilySearch Information Tab in the Record Viewer for this image,) but see [this small note](#Example-2---Appendix-A).


### Example 2.1 : Image of Binding Without Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS007996631_00009_500w.jpg"
       alt="The manuscript cover, shown in FamilySearch DGS 7996631, frame 9. No manuscript reuse."
       width="250px">
</div>
<br/>

A front-cover binding from a Rostock (Germany) Hausbücher. To me, it seems a very cool, antique binding. However, there is no evidence of another manuscript having been used to help protect the book.


### Example 2.2 : Image of Binding Pastedown Without Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS007996631_00010_-_stitchTrue_500w.jpg"
       alt="The pastedown part of the binding, shown in FamilySearch DGS 7996631, frame 10. No manuscript reuse."
       width="250px">
</div>
<br/>

This inside part of the cover is called a pastedown. It's used to help keep the wrapping parts of the binding in place as well as to reinforce the binding's protection of the book. This one shows no trace of being reused manuscript.


### Example 2.3 : Image without any Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS007996631_00062_-_stitchTrue_500w.jpg"
       alt="A standard manuscript page (no reuse) from FamilySearch DGS 7796631, frame 62."
       width="250px">
</div>
<br/>

This is another standard manuscript page. It comes from the same book as the previous two images.


### Example 2.4 : Image without any Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS007996631_00991_500w.jpg"
       alt="A standard manuscript page (no reuse) from FamilySearch DGS 7796631, frame 991."
       width="250px">
</div>
<br/>

This is another standard manuscript page. It comes from the same DGS - though not the same book, as the previous three images.


### Example 2 - Appendix A

There was no official citation for this document. However, the microfilm's information board has the following:

```
STAATL. ARCHIVVERW. DER DDR
RAT DES BEZIRKES ROSTOCK
GENEALOGISCHE DOKUMENTE
STADTARCHIV ROSTOCK
RAT. STADTBUCHER
1-3.1 45
```

While the GDR is no longer extant, nor is its State Archive Management department, I imagine the Rostock City Archives still exist.


### Other Examples, whose citation and usage I have, but don't have time to write up.

<b> Positive (has reuse), Rear Pastedown, Bibliothèque Nationale de France. Ms French 837</b>

<br/>
<div>
  <img src="./BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00743_500w.jpg"
       alt="French National Library, Ms French 837"
       width="250px">
</div>
<br/>

This looks like it might be a land-grant, or perhaps a deed, or perhaps I'm way off. This is the right-hand side of what makes up the pastedown - part of the original document was obviously cut off on the right. The left-hand side of what's left is the front pastedown. 

<hr/>

<b> Positive (has reuse), Binding Reinforcers, FamilySearch DGS 4535287 frame 182</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS004534287_00172_-_reuseTrue_1000w.jpg"
       alt="Swedish document on FamilySearch"
       width="375px">
</div>
<br/>

This is a document from Sweden. The reuse in in those four, detached binding strengtheners, which would have originally glued to the wood on the left-hand side. Look closely (maybe click on the image to see a larger version) and you can see the writing.

<hr/>

<b> Positive (has reuse), Outside Binding - Front and Back, FamilySearch DGS 4535287 frame 360</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS004534287_00360_-_reuseTrue_1000w.jpg"
       alt="Another Swedish Document from FamilySearch"
       width="375px">
</div>
<br/>

<hr/>

<b> Positive (has reuse), Front Binding, FamilySearch DGS 8104286 frame 897</b>

<br/>
<div>
  <img src="./FamilySearch_-_DGS008104286_00897_-_reuseTrue_500w.jpg"
       alt="Words and music"
       width="250px">
</div>
<br/>

This is the first such image I saw in the FamilySearch collections. I was taking an online class in paleography and codicology (manuscript studies) while working at the Granite Mountain Records Vault, and this was an image on one of the microfilms I digitized. If I understand correctly, it has readings and music for a specific Mass.

<hr/>

## Tool Description for the Family History Technology Workshop

I am working on a tool, now informally referred to as "Fragment Finder", that will open up new sources of names, dates, etc. applicable to family history. These interesting and useful fragments will be defined and discussed in the second paragraph. The purpose of this tool is to take large numbers of document images from archives, libraries, and collections and find those images which contain reused manuscript fragments. The prototype tool consists of a Neural-Network model created by using transfer learning from ResNet-50. The fragment images used to train and test the tool were retrieved from FamilySearch as well as from university and national libraries. We – I and Keith Prisbrey, who deferred to me for this presentation – used a labeled dataset of 622 images, of which approximately 1 in 10 showed fragments. After training, our accuracy on the test set was 96.77%. Our tool, with continued development and training, will permit finding reused manuscript fragments.

Manuscript fragments are, quite simply, pages or groups of pages which have handwriting on them, but which do not contain the complete original work. The present tool is especially concerned with single pieces of so-called waste parchment – or even waste paper – that were reused to make bindings or book covers for new codices/books. Some reused manuscript fragments originated from fancy, expensive, and literary sources called Decorated or Illuminated Manuscripts – the Book of Kells being one conspicuous example. Others include contracts, arrest records, deeds, land-grants, notes of debts due to the bookmaker, and other records that include names, dates, locations, professions, and relationships.


## Details of the Model

Coming soon!

For now, you're welcome to look at my [submission for a Research Talk](./BLACK-David_-_FHTC_2024_-_Reused_Manuscript_Fragments.pdf) as a PDF.
