var batch = require('users/fitoprincipe/geetools:batch')

var roi = ee.Geometry.Rectangle([-133, 71, -155, 74]);
Map.addLayer(roi, {}, 'ROI')
Map.centerObject(roi, 8)

//Load Sentinel-1 SAR collection and filter according to data collection type
var S1 = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filterBounds(roi)
  .filterDate('2016-07-01','2016-11-01')
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))

// //Add first image to map to get an idea of what a SAR image looks like  
// Map.addLayer(S1.first(),{bands: 'VV',min: -18, max: 0}, 'SAR image')

// Export the image, specifying scale and region.
batch.Download.ImageCollection.toDrive(S1, 'SAR', 
                {scale: 10, 
                 type: 'float'})
