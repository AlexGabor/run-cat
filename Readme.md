
Run:
```
docker run --rm -p 3000:3000 -v ${pwd}/files:/files ghcr.io/maplibre/martin /files/tiles.mbtiles --style /files/style.json
```

```
docker run -it --rm -p 8888:8000 ghcr.io/maplibre/maputnik:main
```

```
ogr2ogr -f GeoJSON activity_20775840672.geojson activity_20775840672.gpx tracks -lco WRITE_BBOX=YES
```