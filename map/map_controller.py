def write_place_to_html(place_items):
    with open("map/map_view.html", "w", encoding="utf-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>My Route Map</title>
  <style>
    html, body {{ height: 100%; margin: 0; }}
    #map {{ width: 100%; height: 100%; }}
  </style>
</head>
<body>
  <div id="map"></div>

  <script src="https://dapi.kakao.com/v2/maps/sdk.js?appkey=239c166a0d6fa6c315878a19616393c2&libraries=services&autoload=false"></script>
  <script>
    kakao.maps.load(function () {{
      const mapContainer = document.getElementById('map');
      const mapOption = {{
        center: new kakao.maps.LatLng(37.5665, 126.9780),
        level: 5
      }};
      const map = new kakao.maps.Map(mapContainer, mapOption);
      const geocoder = new kakao.maps.services.Geocoder();

      const places = {place_items};

      const coordsList = [];

      function haversine(lat1, lon1, lat2, lon2) {{
        const toRad = (x) => x * Math.PI / 180;
        const R = 6371;  // km
        const dLat = toRad(lat2 - lat1);
        const dLon = toRad(lon2 - lon1);
        const a = Math.sin(dLat/2)**2 + Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon/2)**2;
        return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      }}

      let totalDistance = 0;

      function process(i) {{
        if (i >= places.length) {{
          if (coordsList.length > 1) {{
            const polyline = new kakao.maps.Polyline({{
              map: map,
              path: coordsList,
              strokeWeight: 4,
              strokeColor: '#FF0000',
              strokeOpacity: 0.7,
              strokeStyle: 'solid'
            }});
            alert("총 이동 거리: " + totalDistance.toFixed(2) + " km");
          }}
          return;
        }}

        geocoder.addressSearch(places[i].place, function (result, status) {{
          if (status === kakao.maps.services.Status.OK) {{
            const coord = new kakao.maps.LatLng(result[0].y, result[0].x);
            coordsList.push(coord);
            new kakao.maps.Marker({{
              map: map,
              position: coord,
              title: places[i].note || places[i].place
            }});
            if (i === 0) map.setCenter(coord);
            if (i > 0) {{
              const prev = coordsList[i - 1];
              totalDistance += haversine(prev.getLat(), prev.getLng(), coord.getLat(), coord.getLng());
            }}
          }}
          process(i + 1);
        }});
      }}

      process(0);
    }});
  </script>
</body>
</html>
""")