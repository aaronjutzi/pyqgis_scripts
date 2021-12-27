# This script can be used to load generic vector layers into your QGIS project
# It will load the script with the CRS of your choosing and change the colour to black

CRS = "" # Enter EPSG number in between the quotations (Example: "26917" for NAD83/ UTM Zone 17N)

QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(CRS))


# Complete these variables for the addVectorLayer method to work
file_path = ""
layer_name = ""
data_type = "" # Example: "OGR"

layer = iface.addVectorLayer(file_path, layer_name, data_type)

layer.renderer().symbol().setColor(QColor("black"))
layer.triggerRepaint()
