import pandas as pd
from pykml import parser

import requests

class FAILED_TO_FETCH_WARD_FROM_POSTCODE(Exception):
    pass

def postCodeToWard(postcode):
    res = requests.get('https://api.postcodes.io/postcodes/'+postcode)
    if res.ok:
        ward_name = res.json()['result']['admin_ward'].lower()
        return all_data[ward_name]
    else:
        raise FAILED_TO_FETCH_WARD_FROM_POSTCODE("ERROR "+str(res.status_code) + " " + res.json()['error'])

KML_FILE = 'resources/Wards_December_2016_Full_Clipped_Boundaries_in_the_UK.kml'
CSV_FILE = 'resources/data.csv'

def read_kml(fname):
    root = parser.fromstring(open(fname, 'r').read().encode('utf-8'))
    folder = root.Document.Folder
    kml_data = {}
    for p in folder.Placemark:
        ward_name = str(p.ExtendedData.SchemaData.SimpleData[2])
        ward_name = ward_name.lower()
        kml_data[ward_name] = {
            'long': p.ExtendedData.SchemaData.SimpleData[8],
            'lat': p.ExtendedData.SchemaData.SimpleData[9],
        }

        coordinates = ''
        try:
            for poly in p.MultiGeometry.Polygon:
                coordinates += poly.outerBoundaryIs.LinearRing.coordinates
            kml_data[ward_name]['coordinates'] = coordinates
        except:
            for poly in p.Polygon:
                coordinates += poly.outerBoundaryIs.LinearRing.coordinates
            kml_data[ward_name]['coordinates'] = coordinates
            continue

    return kml_data


def read_csv(fname):
    df = pd.read_csv(fname)

    ward_data = {}
    for idx, ward in enumerate(df['Ward']):
        if not isinstance(ward, str):
            continue

        ward = ward.lower()
        if ward not in ward_data:
            ward_data[ward] = {}
            ward_data[ward]['Total'] = int(df['Total'][idx])
            ward_data[ward]['Male'] = int(df['Male'][idx])
            ward_data[ward]['Female'] = int(df['Female'][idx])
        else:
            ward_data[ward]['Total'] += int(df['Total'][idx])
            ward_data[ward]['Male'] += int(df['Male'][idx])
            ward_data[ward]['Female'] += int(df['Female'][idx])

    return ward_data


def combine_data(csv_data, kml_data):
    skipped = 0
    gathered = 0

    for ward in csv_data:
        try:
            csv_data[ward]['long'] = str(kml_data[ward]['long'])
            csv_data[ward]['lat'] = str(kml_data[ward]['lat'])
            csv_data[ward]['coordinates'] = str(kml_data[ward]['coordinates'])
            gathered += 1
        except KeyError:
            skipped += 1
            pass

    print(f'Finished combining kml and csv data. Gathered= {gathered}. Skipped = {skipped}')


    return csv_data


kml_data = read_kml(KML_FILE)
csv_data = read_csv(CSV_FILE)
all_data = combine_data(csv_data, kml_data)
