//path = getDirectory("/Users/mbronars/Documents/sohn/Sohn/AnnotatedData");
//names = getFileList(path);
//print(names[0]);
setBatchMode(true);
imgArray = newArray(nImages);
  for (i=0; i<nImages; i++) {
    selectImage(i+1);
    imgArray[i] = getImageID();
  }
for(i = 0; i <imgArray.length;i++){
	selectImage(imgArray[i]);
	//File.open(dir+list[i]);
	for(N=0;N<Overlay.size;N++){
		Overlay.activateSelection(N);
		roiManager("add");
	}
	newImage("tester-"+i, "RGB black", 308, 308, 1);
	color = 255;
	dif = 255/(N+1);
	for(I=0;I<roiManager("count");I++){
		roiManager("select", I);
		setForegroundColor(color,color,color);
		if(Roi.getName == "DEAD"){
			setForegroundColor(255, 0, 0);
		}
		if(Roi.getName == "ignore"){
			roiManager("deselect");
			continue;
		}
		roiManager("fill");
		roiManager("deselect");
		color = color - dif;
	}
	saveAs("Jpeg","/Users/mbronars/Documents/sohn/Sohn/ProcessedData/c"+i+".jpeg");
	close("tester-"+i);;
	roiManager("delete");
}
