<?php 

$uri  = "http://chile.rutificador.com/get_generic_ajax/";

$headers = [
      'Cookie: csrftoken=ioAfP80sm4cafdC8qgT9OoeCFb53KXGh;',
      'Content-type: application/x-www-form-urlencoded; charset=UTF-8',
      ];

$data = [
      'csrfmiddlewaretoken' => 'ioAfP80sm4cafdC8qgT9OoeCFb53KXGh', 
      'entrada'             => 'sebastian andres iturra valdes'
      //'entrada' => '18765525-0'
      ];

$data = http_build_query($data);

$ch   = curl_init();
curl_setopt($ch, CURLOPT_URL, $uri);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch); #Enviamos una petición curl y el resultado lo almacenamos en '$response'
curl_close($ch); 

echo $response; #Imprimimos el resultado.

?>
