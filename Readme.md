
Run:
```
docker run --rm -p 3000:3000 -v ${pwd}/files:/files ghcr.io/maplibre/martin /files/tiles.mbtiles --style /files/style.json
```

```
docker run --rm --name versatiles -p 3000:8080 -v ${pwd}/files:/data versatiles/versatiles:latest serve --config /data/versatile_config.yaml
```

```
docker run -it --rm -p 8888:8000 ghcr.io/maplibre/maputnik:main
```

```
ogr2ogr -f GeoJSON activity_20775840672.geojson activity_20775840672.gpx tracks -lco WRITE_BBOX=YES
```

```
./gpx2post.py
```