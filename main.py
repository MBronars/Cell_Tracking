from overlap import getOverlap
def main():
	cell = "Test.tif"
	protien = "Protein.png"
	over = getOverlap(cell, protien, False)
	print(over)
if __name__ == "__main__":
    main()
 