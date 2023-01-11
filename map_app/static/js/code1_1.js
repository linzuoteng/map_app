
function initMap() {
  
  var target = document.getElementById('map'); //マップを表示する要素を指定
  var todoufuken = b[0].textContent.substr(5);
  var shityoson = c[0].textContent.substr(5);
  var address = todoufuken +" "+ shityoson; //住所を指定
  console.log("検索場所:" + address);
  var geocoder = new google.maps.Geocoder();  

  geocoder.geocode({ address: address }, function(results, status){
    if (status === 'OK' && results[0]){

      console.log(results[0].geometry.location);

       var map = new google.maps.Map(target, {  
         center: results[0].geometry.location,
         zoom: 18
       });

       var marker = new google.maps.Marker({
         position: results[0].geometry.location,
         map: map,
         animation: google.maps.Animation.DROP
       });

       var coment = "<img src='/content/img/ajax/gmapv3/sphinx.gif' align='left' />いいちこ";

       const infowindow = new google.maps.InfoWindow({
        content: coment,
        ariaLabel: "Uluru",
      });

      marker.addListener("click", () => {
        infowindow.open({
          anchor: marker,
          map,
        });
      });

    }else{ 
      //住所が存在しない場合の処理
      alert('住所が正しくないか存在しません。');
      target.style.display='none';
    }
  });
}

window.initMap = initMap;