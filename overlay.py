import skimage 
from skimage import data, io, filters, measure
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize
import numpy as np

cell = io.imread("Cell.png")
img = data.astronaut()
mask = img < 100
mask2 = img >= 100
img[mask] = 0
img[mask2] = 255


count = 0
for x in img:
	for y in x:
		for z in y:
			if z == 0:
				count += 1
area = count/img.size
print(area)

plt.imshow(img)
plt.show()




protien = io.imread("Protien.png")
protien = resize(protien, (400,400))

overlap = protien + cell

cell_mask = skimage.measure.label(cell)
protien_mask = skimage.measure.label(protien)
overlap_mask = skimage.measure.label(overlap)

regions = [cell_mask, protien_mask, overlap_mask]
properties = skimage.measure.regionprops(cell_mask)

#print(properties[0].area)



#plt.imshow(overlap)

#plt.show()