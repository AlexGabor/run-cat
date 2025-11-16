function drawMap(geopath, container, bb1, bb2, bb3, bb4) {
    const map = new maplibregl.Map({
        container: container, // container id
        style: 'http://127.0.0.1:3000/style/style.json', // style URL
        zoom: 14, // starting zoom
        attributionControl: false,
    });

    map.on('load', () => {
        map.addSource('route', {
            type: 'geojson',
            data: '/static/activity/' + geopath
        })
        map.addLayer({
            'id': 'route',
            'type': 'line',
            'source': 'route',
            'layout': {
                'line-join': 'round',
                'line-cap': 'round'
            },
            'paint': {
                'line-color': '#FF4100',
                'line-width': 3
            }
        });
        const bounds = new maplibregl.LngLatBounds([bb1, bb2], [bb3, bb4])
        map.fitBounds(bounds, { padding: 30, animate: false })
    });
}