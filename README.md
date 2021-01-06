# Photomosaic

<p> Photomosaic - a large-scale detailed picture or map built up by combining photographs of small areas. </p>
   
<p> Program starts by taking target image and splits it into a grid. Then finds RGB color average of each input image. It then loops 
through each grid item and finds best replacement out of the input images. A K-D Tree is used to find nearest neighbors index. </p>

<p> User can decide grid size, resulting in more or less accurate photomosaic. As well as having the option of naming the new image </p>

<p float="center">
  <img src="target-images/MonaLisa.jpg" width = "240" height = "490" />
  <img src="results/MonaLisaMosaic.png" width = "240" height = "490" />
  <img src="results/MonaLisa100.png" width = "240" height = "490" />
</p>

<p float="center">
  <img src="target-images/NYC.jpg" width = "365" height = "400" />
  <img src="results/NYCmosaic.png" width = "365" height = "400" />
</p>

## Usage
<p> main.py --target-image TARGET_IMAGE --input-folder INPUT_FOLDER --grid-size GRID_SIZE GRID_SIZE [--output-file OUTFILE] </p>
