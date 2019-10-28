# Import the Earth Engine Python Package
import ee
from geetools import batch

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

roi = ee.Geometry.Rectangle([-133, 71, -155, 74]);
col = ee.ImageCollection('COPERNICUS/S1_GRD').filterBounds(roi).filterDate('2019-07-01','2019-10-31').filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'HH')).filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'HV')).filter(ee.Filter.eq('instrumentMode', 'EW'))

img_list = col.toList(col.size())
n=0

img = ee.Image(img_list.get(n))
img = img.toFloat()
task=ee.batch.Export.image.toDrive(image=img, folder='SAR', maxPixels=10**9)
task.start()

# while True:
#     try:
#         img = ee.Image(img_list.get(n))

#         # convert data type
#         img = img.toFloat()

#         task = ee.batch.Export.image.toDrive(image=img, folder='SAR', maxPixels=10**9)
#         task.start()
#         tasklist.append(task)
#         n += 1
#     except Exception as e:
#         error = str(e).split(':')
#         if error[0] == 'List.get':
#             break
#         else:
#             raise e

# img = ee.Image(img_list.get(n))
# img.getDownloadURL(params={'scale':640})
