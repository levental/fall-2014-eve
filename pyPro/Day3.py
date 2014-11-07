#Wednesday Oct 23

from qgis.core import *
import qgis.utils


oregon_cities = http://navigator.state.or.us/sdl/data/shapefile/m2/cities.zip
oregon_cityLimits = http://navigator.state.or.us/sdl/data/shapefile/k24/citylim_2013.zip


oregon_cities30 = buffer(oregon_cities,20,20)
mapRenderer = iface.mapCanvas().mapRenderer()
c = oregon_cities30(mapRenderer)
c.setPlotStyle(QgsComposition.Print)

