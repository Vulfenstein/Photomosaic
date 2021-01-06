# Photomosaic

<p> Photomosaic - a large-scale detailed picture or map built up by combining photographs of small areas. </p>
   
<p> Program starts by taking target image and splits it into a grid. Then finds RGB color average of each input image. It then loops 
through each grid item and finds best replacement out of the input images. A K-D Tree is used to find nearest neighbors index. </p>

<p float="center">
  <img src="target-images/MonaLisa.jpg" width = "240" height = "490" />
  <img src="results/MonaLisaMosaic.jpg" width = "240" height = "490" />
  <img src="results/MonaLisa100.jpg" width = "240" height = "490" />
