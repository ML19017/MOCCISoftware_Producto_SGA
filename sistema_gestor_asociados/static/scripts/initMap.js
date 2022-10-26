/*
    # ID mapDiv
    # Script de Mapa
*/
function initMap() {
    const argCoords = { lat: 13.6976, lng: -88.896 }
    const map = new google.maps.Map(document.getElementById("mapDiv"), {
      zoom: 8,
      center: argCoords,
    });
  const marker = new google.maps.Marker({
    position: argCoords,
    map,
  });

  button.addEventListener('click',()=> {
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(
            ({ coords: {latitude, longitude } } ) => {
                const coords = {
                    lat: latitude,
                    lng: longitude,
                };
                map.setCenter(coords);
                marker.setPosition(coords);
                map.setZoom(15);
                console.log(coords);
            },
            () => {
                alert("Ocurrió un error!");
            }
        )
    }
    else {
        alert("Este navegador no es compatible con los servicios de ubicación, por favor actualice el navegador!");
    }
  });
}