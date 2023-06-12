<?php 
  include_once './includes/header.php'; 
?>


<?php

  $numero_1 = 20;
  $numero_2 = 20;

  if($numero_1 < $numero_2) {
    echo "El numero 2 es mayor";
  } else if ($numero_1 == $numero_2) {
    echo "son iguales";
  } else {
    echo "El numero 1 es mayor";
  }

?>