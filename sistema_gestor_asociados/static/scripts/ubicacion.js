function initMap(){

    window.addEventListener("load", function(){    

        const myLatLng = {
            lat: 13.69835,
            lng: -89.2136
        }

        const options = {
            center: myLatLng,
            zoom: 15
        }

        var map = document.getElementById('map');

        const mapa = new google.maps.Map(map, options);

        const marcador = new google.maps.Marker({
            map: mapa
        });

        var informacion = new google.maps.InfoWindow({});
        
        marcador.addListener('click', function(){
            informacion.open(mapa, marcador);
        });

        var autocomplete = document.getElementById('autocomplete');
        const search = new google.maps.places.Autocomplete(autocomplete);
        search.bindTo("bounds",mapa );
        search.addListener('place_changed', function(){
            marcador.setVisible(false);

            var place = search.getPlace();

            if(!place.geometry.viewport){
                    window.alert("Error al mostrar el lugar");
                    return;
            }
            if(place.geometry.viewport){
                mapa.fitBounds(place.geometry.viewport);
            }
            else{
                mapa.setCenter(place.geometry.location);
                mapa.setZoom(15);
            }

        marcador.setPosition(place.geometry.location);
        marcador.setVisible(true);
        const direccion = document.getElementById("direccion");

        var address = "";

        if(place.address_components){
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || ''),
            ];
        }
        direccion.innerHTML =  address ;
        informacion.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        informacion.open(mapa, marcador);
        });            
    });
}