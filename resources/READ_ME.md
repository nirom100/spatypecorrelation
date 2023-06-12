# BA Nina Romanow

## Name
Spa-Type Clustering / Geographical Data

## Description
A detailed description of the functionality is provided in Thesis.pdf found in ALBI_thesis_template. 

## Description of files

files necessary for code to work: 
- countrylist.txt
- locdata.txt
- spatypessorted.txt 

unnecessary files get deleted after compiling and running the code

**python scripts**
 
- alignment.py: creates n x n matrix and applies HED. strings are encoded to chars, since HED does not differentiate between 12 and 1 2, for example. Each individual repeat is mapped to a char 

- clustering.py: uses the distance matrix created in alignment.py as input and creates a dendrogram. cut-offs and leaf labels can be modified as commented in the script 

- coordinates.py: was used to get the alpha-02 codes for every spa-type country and print them into txt file 

- correlation.py: creates correlation scatterplot for genetic and geographic distance matrices, also calculates the Pearson correlation coefficient based on data given 

- countrycharts.py: was designed to create some pie charts for clusters, but not used in final version 

- distance.py: reads all coordinates for n selection of spa-types and calculates a geographic distance matrix, matching the genetic distance matrix, using haversine formula 

- getcountries.py: webscraping to get all locations for spa-types and save them into a local list. WARNING: It only seems to grab up to 1000 entries in one run, so the code has to be run multiple times to get all data and the input needs to be adjusted accordingly, country entries also get selected and cleared up

- map.py: creates folium map, based on alignment & clustering results, can be viewed as a html file. has to be run separately after spatypecorrelation.py 

- readdata.py: prints clustering results sorted into txt file

- selection.py: selects N amount of spa-types, N is terminal input, random seed value used: 20 

- spatypecorrelation.py: runs all needed scripts in one run 



**txt-files**

before compiling: 
- countrylist.txt : list of max country, as explained in the thesis, for all spa-types 
- countrylistfrequency.txt : analog to country.txt, but with the amount of the location found specified 
- locdata.txt : coordinates fetched with GeoPandas including the alpha-02 code and country name for every spa-type
- spatypessorted : cleaned up list of spa-types used 

after compiling: 
- genetic.pdf : shows the computed dendrogram based on the cut-off specified in clustering.py
- correlation.pdf : correlation scatter plot

- distancematrix.txt : calculated homo-edit distance matrix 
- geodistancematrix.txt : calculated geographic distance matrix 
- genclusterresults.txt : clusters and spa-types inside (format: cluster number X = ( list of: spa-type ID, country, repeat succession))
- mapinput.txt : is used as input for map.py 
- spaselection.txt : n spa-types selected, all results are based on this selection 





## Installation
Check GeoPandas Documentary for an extensive installation guide. 
All used Python packages are listed in the requirements file in the folder code. They can be installed inside the code directory with: 
```
$ pip3 install -r requirements.txt
```

## Usage
Start the program with 
```
$ python3 spatypecorrelation.py 
```
type in your n desired amount of spa-types to be evaluated

after the program has terminated, you can run 
```
$ python3 map.py 
```
for a HTML map created based on the output of the previous program

## Roadmap
Future implementation ideas are listed in Section 5 of Thesis.pdf 


