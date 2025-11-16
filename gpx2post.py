from os import listdir
from os.path import isfile, join
import subprocess
import json
import sys


gpxPath = "./gpx/"
geoJsonPath = "./static/activity/"
postPath = "_posts/"

files = [f for f in listdir(gpxPath) if isfile(join(gpxPath, f))]

for gpxFile in files:
    filename = gpxFile.split('.')[0] 

    geojsonFile = filename + '.geojson'
    subprocess.run(["ogr2ogr", "-f", "GeoJSON", geoJsonPath+geojsonFile, gpxPath+gpxFile, "tracks", "-lco", "WRITE_BBOX=YES"])

    with open(geoJsonPath+geojsonFile) as json_data:
        geoJson = json.load(json_data)
        json_data.close()
        bb1, bb2, bb3, bb4 = geoJson['bbox']

    date, location, distance = filename.split('_')
    y, m, d = date.split('-')

    postFile = filename.replace("_", "-") + ".md"
    with open(postPath+postFile, "w") as sys.stdout: 
        print("---")
        print("title: " + location + " " + distance)
        print("layout: post")
        print("categories: post")
        print("")
        print("display-date: " + d + "." + m + "." + y)
        print("location: " + location)
        print("distance: " + distance)
        print("")
        print("geopath: " + filename + ".geojson")
        print("")
        print("bb1: ", bb1)
        print("bb2: ", bb2)
        print("bb3: ", bb3)
        print("bb4: ", bb4)
        print("---")
