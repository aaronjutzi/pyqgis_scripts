# Code created by Aaron Jutzi on December 8, 2021
# This code is to be used within the python console in QGIS
# This code will display general information about your specified raster

# Enter your raster's file path below
# e.g. uri = "C:/GIS/tavistock/aci_2020_on_v1/aci_2020_on.tif"
uri = " "
rlayer = iface.addRasterLayer(uri,"my raster","gdal")
 
if rlayer.isValid():
    print("This is a valid raster layer!")
    # get the raster type: 0 = GrayOrUndefined (single band), 1 = Palette (single band), 2 = Multiband
    print("Raster types: 0 = GrayOrUndefined (single band), 1 = Palette (single band), 2 = Multiband")
    print("Raster Type: {}".format(rlayer.rasterType()))
    print("Band Count: {}".format(rlayer.bandCount())
    print("Width: {}px".format(rlayer.width()))
    print("Height: {}px".format(rlayer.height()))
    print("Extent: {}".format(rlayer.extent().toString()))
    
    # band statistics
    stats = rlayer.dataProvider().bandStatistics(1)
    print("Min value: {}".format(stats.minimumValue))
    print("Max value: {}".format(stats.maximumValue))
    print("Mean: {}".format(stats.mean))
    print("Range: {}".format(stats.range))
    print("Standard Deviation: {}".format(stats.stdDev))
    print("Sum: {}".format(stats.sum))
    print("Sum of Squares: {}".format(stats.sumOfSquares))

else:
    print("This raster layer is invalid!")
