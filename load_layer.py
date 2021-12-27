# This script can be used to load generic vector layers into your QGIS project
# It will load the script with the CRS of your choosing and change the colour to black
# Use for reference: https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/loadlayer.html


CRS = "" # Enter EPSG number in between the quotations (Example: "26917" for NAD83/ UTM Zone 17N)

QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(CRS))


# Complete these variables for the addVectorLayer method to work
file_path = ""
layer_name = ""
data_type = "" # Example: "ogr"

# layer is added
layer = iface.addVectorLayer(file_path, layer_name, data_type)


# Feel free to change the layer colour if you want to
colour = "black"

# Changes layer colour
layer.renderer().symbol().setColor(QColor("colour"))

# Refreshes QGIS so colour change can be seen
layer.triggerRepaint()
