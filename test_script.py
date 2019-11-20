# Import the Earth Engine Python Package
import ee
import wget
import threading

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()
roi = ee.Geometry.Polygon([[-150.60058593749994, 74.81042419434962],[-146.11816406249997, 74.81042419434962],[-146.11816406249997, 75.74812548842993],[-150.60058593749994, 75.74812548842993],[-150.60058593749994, 74.81042419434962]])
col = ee.ImageCollection('COPERNICUS/S1_GRD').filterBounds(roi).filterDate('2019-11-06','2019-11-09').filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'HH')).filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'HV')).filter(ee.Filter.eq('instrumentMode', 'EW'))
img_list = col.toList(col.size())

scale = 1024
# Change scale to ~128? 
# I think that may be what we want for images scaled down by 4 in each dimension, since it is about 4000x4000
# The minimum scale for downloading like this is ~44.4

# If you want to download larger scenes, see code below, it downloads to your google drive (until it's full)
# Problem with it is it only downloads 1 tif file per scene? not sure why. 
# for i in range(img_list.size().getInfo()):
#     img = ee.Image(img_list.get(i))
#     img = img.toFloat() # converts to float32 from double, necessary for drive download
#     task=ee.batch.Export.image.toDrive(image=img, folder='SAR', scale=scale, maxPixels=10**9)
#     task.start()

# This code downloads one file at a time
# for i in range(img_list.size().getInfo()):
#     img = ee.Image(img_list.get(i))
#     img = img.toFloat() # converts to float32 from double
#     wget.download(img.getDownloadURL(params={'scale': scale})) 

# This code downloads in parallel using threading, it is faster
def download(url):
    wget.download(url)
    return

for i in range(img_list.size().getInfo()):
    img = ee.Image(img_list.get(i))
#     img = img.toFloat() # converts to float32 from double
    download_thread = threading.Thread(target=download, args=(img.getDownloadURL(params={'scale': scale}),))
    download_thread.start()