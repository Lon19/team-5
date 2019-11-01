import pandas as pd
from pykml import parser


kml_file = 'Wards_December_2016_Full_Clipped_Boundaries_in_the_UK.kml'
root = parser.fromstring(open(kml_file, 'r').read().encode('utf-8'))
folder = root.Document.Folder
names = list()
center_long = list()
center_lat = list()
coods = list()
for p in folder.Placemark:
    names.append(p.ExtendedData.SchemaData.SimpleData[2])
    center_long.append(p.ExtendedData.SchemaData.SimpleData[8])
    center_lat.append(p.ExtendedData.SchemaData.SimpleData[9])
    coordinates = ""
    try:
        for poly in p.MultiGeometry.Polygon:
            coordinates += poly.outerBoundaryIs.LinearRing.coordinates
        coods.append(coordinates)
    except:
        for poly in p.Polygon:
            coordinates += poly.outerBoundaryIs.LinearRing.coordinates
        coods.append(coordinates)
        continue

df = pd.read_csv('claimant-count-all-wards.csv')

ward_data = {}

for idx, ward in enumerate(df['2011 census frozen ward']):
    ward_data[ward] = {'Total': df['Total'][idx],
                       'Male': df['Male'][idx],
                       'Female': df['Female'][idx],
                       }
