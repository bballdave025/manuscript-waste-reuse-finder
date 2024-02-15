# manuscript-waste-reuse-finder

Code and research description to be presented at the 2024 [Family History Technology Conference](https://fhtw.byu.edu/). Research and Development on a tool to find document images where manuscript waste (a.k.a. binder's waste, somewhat-a.k.a. manuscript fragments) was used to bind other documents. Such reused manuscripts have been found to contain info relating to such diverse fields as genealogy and family history, manuscript studies, paleography, codicology, and of course fragmentology. It will be shown that it is extendable to finding such things as manuscript repairs (e.g. stitching) and iron-gall-ink corrosion.

# Fragment Finder

## Examples of Reused Manuscript Fragments (and of what are not so classified)

Before my description of the tool, I want to put here several images that illustrate Reused Manuscript Fragments. "Reused Manuscript Fragments" will be the term I use to describe what this tool is designed to find. I will also use <b>RMF</b> and such phrases as, "examples of reuse". The images are part of the original dataset.

If you're impatient to know about the tool and the accompanying research, you can see my <b>(2024-02-05) UPDATED</b> [submission for a Research Talk](./BLACK-D_and_PRISBREY-K_-_FHTC_2024_-_Reused_Manuscript_Fragments_update_2024-02-05.pdf) as a PDF, or you can use this [LINK FOR THE AFTER-IMAGE PART](#Tool-Description-for-the-Family-History-Technology-Workshop). There's also the option of looking at [the model-training code](./fndtnl_cnn_ms_reuse_clssfctn_trn.py).


### Example 1 : Universitätsbibliothek Heidelberg, Codex Salemitana VII,73

Title: _Ordinarium cisterciense_ 

Citation link: https://doi.org/10.11588/diglit.9273

[Public Domain Mark 1.0 Universal (No Copyright)](https://creativecommons.org/publicdomain/mark/1.0/)

[More information (bballdave025's metadata)](./Heidelberg_-_salVII73_URL.txt)


### Example 1.1 : Image of Binding Containing Manuscript Reuse Fragment

<b>This is in the positive class.</b>

<br/>
<div>
  <img src="./img/Heidelberg_-_salVII73_front-cover_500wid.jpg"
       alt="Front cover of Ordinarium cisterciense, Heidelberg Codex Salemitana VII,73. Example of Manuscript Reuse Fragment"
       width="250px">
</div>
<br/>

Binding (front cover) for the main book, _Ordinarium cisterciense_. The fragment appears to come from a large, decorated manuscript. Note the capital letters in red. [Image 1.1 Citation Link](https://doi.org/10.11588/diglit.9273#0001)


### Example 1.2 : Image without any Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./img/Heidelberg_-_salVII73_00186_500wid.jpg"
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
  <img src="./img/FamilySearch_-_DGS007996631_00009_500w.jpg"
       alt="The manuscript cover, shown in FamilySearch DGS 7996631, frame 9. No manuscript reuse."
       width="250px">
</div>
<br/>

A front-cover binding from a Rostock (Germany) Hausbücher. To me, it seems a very cool, antique binding. However, there is no evidence of another manuscript having been used to help protect the book.


### Example 2.2 : Image of Binding Pastedown Without Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./img/FamilySearch_-_DGS007996631_00010_-_stitchTrue_500w.jpg"
       alt="The pastedown part of the binding, shown in FamilySearch DGS 7996631, frame 10. No manuscript reuse."
       width="250px">
</div>
<br/>

This inside part of the cover is called a pastedown. It's used to help keep the wrapping parts of the binding in place as well as to reinforce the binding's protection of the book. This one shows no trace of being reused manuscript.


### Example 2.3 : Image without any Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./img/FamilySearch_-_DGS007996631_00062_-_stitchTrue_500w.jpg"
       alt="A standard manuscript page (no reuse) from FamilySearch DGS 7796631, frame 62."
       width="250px">
</div>
<br/>

This is another standard manuscript page. It comes from the same book as the previous two images.


### Example 2.4 : Image without any Manuscript Reuse

<b>This is in the negative class.</b>

<br/>
<div>
  <img src="./img/FamilySearch_-_DGS007996631_00991_500w.jpg"
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
  <img src="./img/BNFrance_-_Recueil_de_fabliaux_dits_contes_-_MsFr837-btv1b55013464t_00743_500w.jpg"
       alt="French National Library, Ms French 837"
       width="250px">
</div>
<br/>

This looks like it might be a land-grant, or perhaps a deed, or perhaps I'm way off. This is the right-hand side of what makes up the pastedown - part of the original document was obviously cut off on the right. The left-hand side of what's left is the front pastedown. 

<hr/>

<b> Positive (has reuse), Binding Reinforcers, FamilySearch DGS 4535287 frame 182</b>

<br/>
<div>
  <img src="./img/FamilySearch_-_DGS004534287_00172_-_reuseTrue_1000w.jpg"
       alt="Swedish document on FamilySearch"
       width="375px">
</div>
<br/>

This is a document from Sweden. The reuse in in those four, detached binding strengtheners, which would have originally glued to the wood on the left-hand side. Look closely (maybe click on the image to see a larger version) and you can see the writing. The writing on the very left of the image - what's wrapped over from the front binding - is also reuse and is much more visible to me.

<hr/>

<b> Positive (has reuse), Outside Binding - Front and Back, FamilySearch DGS 4535287 frame 360</b>

<br/>
<div>
  <img src="./img/FamilySearch_-_DGS004534287_00360_-_reuseTrue_1000w.jpg"
       alt="Another Swedish Document from FamilySearch"
       width="375px">
</div>
<br/>

<hr/>

<b> Positive (has reuse), Front Binding, FamilySearch DGS 8104286 frame 897</b>

<br/>
<div>
  <img src="./img/FamilySearch_-_DGS008104286_00897_-_reuseTrue_500w.jpg"
       alt="Words and music"
       width="250px">
</div>
<br/>

This is the first such image I saw in the FamilySearch collections. I was taking an online class in paleography and codicology (manuscript studies) while working at the Granite Mountain Records Vault, and this was an image on one of the microfilms I digitized. If I understand correctly, it has readings and music for a specific Mass.

<hr/>

## Tool Description for the Family History Technology Workshop

I am working on a tool, now informally referred to as "Fragment Finder", that will open up new sources of names, dates, etc. applicable to family history. These interesting and useful fragments will be defined and discussed in the second paragraph. The purpose of this tool is to take large numbers of document images from archives, libraries, and collections and find those images which contain reused manuscript fragments. The prototype tool consists of a Neural-Network model created by using transfer learning from ResNet-50. The fragment images used to train and test the tool were retrieved from FamilySearch as well as from university and national libraries. We – I and Keith Prisbrey, who deferred to me for this presentation – used a labeled dataset of 622 images, of which approximately 1 in 10 showed fragments. After training, our accuracy on the test set was 96.77%. Our tool, with continued development and training, will permit finding reused manuscript fragments.

Manuscript fragments are, quite simply, pages or groups of pages which have handwriting on them, but which do not contain the complete original work. The present tool is especially concerned with single pieces of so-called waste parchment – or even waste paper – that were reused to make bindings or book covers for new codices/books. Some reused manuscript fragments originated from fancy, expensive, and literary sources called Decorated or Illuminated Manuscripts – the Book of Kells being one conspicuous example. Others include contracts, arrest records, deeds, land-grants, notes of debts due to the bookmaker, and other records that include names, dates, locations, professions, and relationships.


## Useful Commands for Dave

### Rename

```bash
find . -type f -iname "*.png" > fnames.lst; \
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" | tee -a rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
echo;
echo "orig: ${orig}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
echo "my_first: ${my_first}";
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
echo "my_end: ${my_end}";
my_second=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
echo "my_second: $my_second";
my_num=0;
my_unpad=$(echo "${my_second}+1" | bc);
echo "my_unpad: ${my_unpad}";
my_num=0;
if [ $my_unpad -lt 10 ]; then
  my_num="0000${my_unpad}";
elif [ $my_unpad -lt 100 ]; then
  my_num="000${my_unpad}";
elif [ $my_unpad -lt 1000 ]; then
  my_num="00${my_unpad}";
elif [ $my_unpad -lt 10000 ]; then
  my_num="0${my_unpad}";
else
  my_num="${my_unpad}";
fi;
echo "my_num: ${my_num}";
new_fname="${my_first}${my_num}${my_end}";
echo "  Command will be:" | tee -a rename.out;
echo "mv \"${orig}\" \"${new_fname}\"" | tee -a rename.out;
echo "    ..." | tee -a rename.out;
mv "${orig}" "${new_fname}" \
  && echo -e "        ... success\n" | tee -a rename.out \
  || echo -e "        ... FAILURE\n" | tee -a rename.out
'
```

### Converts

#### 0

```bash
identify -format "\n\n%f\n%[magick] %[colorspace] %[type] %[extension] %[bit-depth] %[channels]\n" *.tiff # e.g.
```

#### 1

```bash
magick mogrify -colorspace srgb -type truecolor *.jpg
```

#### 2

```bash
mogrify -format jpg -quality 92 -colorspace srgb -type truecolor *.png
```

#### 3

```bash
mogrify -format jpg -quality 92 *.tiff
```

#### 4

```bash

# hopefully it's faster when not working on files on the external hard drive
```

### Oft-used files

#### classifier.param

```
<?xml version="1.0" encoding="UTF-8"?>

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
<!--  classifier_try.param     David Wallace BLACK     2017-04-  
~~Now classifier.param                                 2024-02-12  
~~
~~   This "<CustomClassificationParameters>" section is the one that will
~~   give all information necessary for the GUI. This includes information
~~	 for instruction, for setting up how the document to be classified will
~~	 be visualized, for setting up the actual classifications, any input
~~	 and output information necessary, and any other customizations to be
~~	 made to the GUI.
~~	 There should be only one "<CustomClassificationParameters>" field.
~~	 
~~	 Inside of it should be 1 of each of the following
~~	   <Info4Gui>
~~	   <Info4IO>
~~	 
~~	 and 0 or more
~~	   <ClassificationGroup>
-->
<CustomClassificationParameters>
  
  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       This "<Info4Gui>" section will give the information about things 
       that will allow customization of the GUI - such things as 
	   instructions, presentation of the document(s) to be classified, 
	   and some visual aspects of the presentation of the possible
       classifications.
	   There should be:
	   
	     1 <Instructions>
	    
		 1 or 2      <InputPanel>
		   These can be created with any of the following 
		   <InputPanelType> :
		     "static-image"      (scrollable)
			 "zoomable-image"    (scrollable)
			 "text-field"        (scrollable, not editable)
			 "formatted-text"    (scrollable, e.g. html output)
			 !! Maybe later:
			 !! "zoomable-zoned-image"
			 !! "purplized-image"
			 !! "entity-tagger-output"
			 !! "relation-tagger-output"
			 !! "text-field-editable"
		 
		 0 or more   <SelectionPanel>
		   If there are no <SelectionPanel>, only the comment field
		   will be shown.
		   These can be created with any of the following
		   <SelectionPanelType> :
		     "radio-buttons"         ("round select" buttons, only one
			                          can be selected at a time.)
			 "drop-down-menu"        (useful when there are many, many
			                          classifications. only one can
									  be selected at a time)
			 "checkboxes"            (more than one can be selected
			                          at the same time)
			 "text-input"             (where each needs to be typed)
       
       
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
  <Info4Gui>
    <!-- For now, this is not read, but will, in the future, -->
	  <!-- allow customization of the GUI for different input. -->
	  <!-- Now, we'll just use JRadioButtons                   -->
    
	  <!-- Give instructions for how to select. Depending on the
	       decided scope of this classifier, this might never
		     change. There should not be more than two lines, and
		     the text should not go further than 
      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|  
	                                                         -->
	  <Instructions>
	    On your keyboard, press the letter in parentheses
	    next to the best descritpion of the document.
	  </Instructions>
	
	  <!-- These will be inserted horizontally, with the first  
         panel at the left.                                  -->
	  <!-- For input images, the possible file extensions are:
	     
		   If nothing is listed in the "<ImageExtensions>", or
		   the tag is blank, all extensions will be allowed.    -->
    <!-- For input images, the possible file extensions are:
	     
		   If nothing is listed in the "<ImageExtensions>", all
		   extensions will be allowed.                         -->
    <!-- For input text, for now, the possible file 
	       extensions are:
		     .txt
		   Pat will likely have other extensions which can be
		   used for input text (I'm thinking about the text-
		   tiling ".param" files                               -->
    
  	<InputPanel id="n0">
	    <InputPanelType>"zoomable-image"</InputPanelType>
	    <ImageExtensions>jpg</ImageExtensions> <!-- space-delimit -->
	    <Title>"FHTC 2024: RMF|Stitch|Gall|Manicule"</Title>
	  
  	</InputPanel>
	
	  <!-- Stacked Vertically -->
	  <SelectionPanel id="s0" class="radio-buttons">
	    <SelectionPanelType>radio-buttons</SelectionPanelType>
	    <RelevantGroups>"g0"</RelevantGroups> <!-- space-delimit -->
	  </SelectionPanel>
    
  </Info4Gui>
  
  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       This "<Info4IO>" section will 
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
  <InfoForIO>
    
    <!-- If no "<DefaultInputDirectory>" tag exists, if the 
	     directory doesn't exist, or if the tag is empty,
	     the directory from which the classifier is run 
		   will become the default directory.             -->
    <DefaultInputDirectory>
      <!--WindowsInPath>C:\Users\bball\Desktop\cropped_document_images_skinny\holder\input\</WindowsInPath-->
	    <WindowsInPath>D:\Datasets_and_Models\P2_RMFs_Less_Noisy\Classifying_Folder\input\</WindowsInPath>
	    <LinuxInPath>"/mnt/d/Datasets_and_Models/P2_RMFs_Less_N oisy/Classifying_Folder/input/"</LinuxInPath>
	    <MacOSInPath>"/mnt/d/Datasets_and_Models/P2_RMFs_Less_N oisy/Classifying_Folder/input/"</MacOSInPath>
	    
	    <DoRandomizeInputFiles>false</DoRandomizeInputFiles>
      
      <DoIncludeFilenameEnding>false</DoIncludeFilenameEnding>
	    
	  </DefaultInputDirectory>
	
	
	  <!-- If no "<DefaultOutputDirectory>" tag exists, if 
	       the directory doesn't exist, or if the tag is
	       empty, the directory from which the classifier is 
		     run will become the default directory.         -->
	  <DefaultOutputDirectory>
      <!--WindowsOutPath>C:\Users\bball\Desktop\cropped_document_images_skinny\holder\output\</WindowsOutPath-->
	    <WindowsOutPath>D:\Datasets_and_Models\P2_RMFs_Less_Noisy\Classifying_Folder\output\</WindowsOutPath>
	    <LinuxOutPath>"/mnt/d/Datasets_and_Models/P2_RMFs_Less_N oisy/Classifying_Folder/output/"</LinuxOutPath>
	    <MacOSOutPath>"/mnt/d/Datasets_and_Models/P2_RMFs_Less_N oisy/Classifying_Folder/output/"</MacOSOutPath>
	  
	  </DefaultOutputDirectory>
	
  </InfoForIO>
  
  
  <ClassificationGroup id="g0">
    
	  <!-- This next, "choose one" button should always be put in. -->
	  <Classification id="c0">
      <DisplayName>Or click type btn and submit</DisplayName>
      <DirectoryName></DirectoryName>
      <KeyboardShortcut></KeyboardShortcut>
	    <AddedFilenameEnding></AddedFilenameEnding>
	    <Description>
	      Select this button to clear the selection.
	    </Description>
      <Examples>
        
      </Examples>
      
    </Classification>
	
	
    <Classification id="c1">
      <DisplayName>ms Reuse</DisplayName>
	    <KeyboardShortcut>R</KeyboardShortcut>
	    <DirectoryName>MS_Reuse</DirectoryName>
	    <AddedFilenameEnding>rmf</AddedFilenameEnding>
	    <Description>
	      Image shows an instance of a reused manuscript fragment used to help with binding. Note that if the binding helper is actually printed, it should still be included. The important part is that something with information encoded as writing is used to bind the codex.
	    </Description>
	    <Examples>
	      
	    </Examples>
      
    </Classification>
	
	  <Classification id="c2">
      <DisplayName>Stitching</DisplayName>
	    <KeyboardShortcut>S</KeyboardShortcut>
	    <DirectoryName>Stitching</DirectoryName>
	    <AddedFilenameEnding>stc</AddedFilenameEnding>
	    <Description>
	      Image shows an example of stitching - parchment-maker
		  repair or embroidery.
	    </Description>
	    <Examples>
	      
	    </Examples>
      
    </Classification>
	
	  <Classification id="c3">
      <DisplayName>ink corrosion Thru</DisplayName>
	    <KeyboardShortcut>T</KeyboardShortcut>
	    <DirectoryName>Iron_Gall_Ink_Corroded_Thru</DirectoryName>
	    <AddedFilenameEnding>igt</AddedFilenameEnding>
	    <Description>
	      Image shows iron gall ink corrosion where the acid in the ink has corroded all the way through the page, leaving a hole - usually in the shape of a word, a letter, or a drawing.
	    </Description>
	    <Examples>
	      
	    </Examples>
    </Classification>
	  
    <Classification id="c4">
      <DisplayName>Manicule</DisplayName>
	    <KeyboardShortcut>M</KeyboardShortcut>
	    <DirectoryName>Manicule</DirectoryName>
	    <AddedFilenameEnding>mnc</AddedFilenameEnding>
	    <Description>
	      Image shows a manicule - a drawing of a hand pointing a finger towards part of the document like a Nota Bene - or multiple manicules. If there are printed manicules, they should be included here.
	    </Description>
	    <Examples>
	      
	    </Examples>
    </Classification>
    
	  <Classification id="c5">
      <DisplayName>Various</DisplayName>
	    <KeyboardShortcut>V</KeyboardShortcut>
	    <DirectoryName>More_Than_One</DirectoryName>
	    <AddedFilenameEnding>mlt</AddedFilenameEnding>
	    <Description>
	      Image has more than one of the characteristics described above. It will need to be sent through and given each of the classifications, so these should be well-taken-care-of.
	    </Description>
	    <Examples>
	      
	    </Examples>
    </Classification>
    
	<Classification id="c11">
      <DisplayName>Nothing interesting</DisplayName>
	    <KeyboardShortcut>N</KeyboardShortcut>
	    <DirectoryName>Nothing_Interesting</DirectoryName>
	    <AddedFilenameEnding>noi</AddedFilenameEnding>
	    <Description>
	      Image doesn't have any of the characteristics above. It will be a false for all.
	    </Description>
	    <Examples>
	      
	    </Examples>
    </Classification>
	
	<Classification id="c12">
      <DisplayName>Do not use</DisplayName>
	    <KeyboardShortcut>D</KeyboardShortcut>
	    <DirectoryName>Do_Not_Use</DirectoryName>
	    <AddedFilenameEnding>dnu</AddedFilenameEnding>
	    <Description>
	      Something that you think would throw off the model, or something you're really not sure about.
	    </Description>
	    <Examples>
		
		</Examples>
    </Classification>
	
	<Classification id="c13">
      <DisplayName>Unsure</DisplayName>
	    <KeyboardShortcut>U</KeyboardShortcut>
	    <DirectoryName>Unsure</DirectoryName>
	    <AddedFilenameEnding></AddedFilenameEnding>
	    <Description>
	      Something you would like someone to return to.
	    </Description>
	    <Examples>
	      
	    </Examples>
    </Classification>
	
  </ClassificationGroup>

</CustomClassificationParameters>

```


## Details of the Model

Coming soon!

For now, you're welcome to look at my <b>(2024-02-05) UPDATED</b> [submission for a Research Talk](./BLACK-D_and_PRISBREY-K_-_FHTC_2024_-_Reused_Manuscript_Fragments_update_2024-02-05.pdf) as a PDF.

You're also welcome to have a look at [the model-training code](./fndtnl_cnn_ms_reuse_clssfctn_trn.py).
