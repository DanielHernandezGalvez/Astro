<?php 
  include_once './includes/header.php'; 
?>

<?php
  $frutas = array("manzana", "naranja", "melón", "Uvas");

  $frutas_2 = ["manzana", "naranja", "melón", "Uvas"];

  array_push($frutas, "pera");

  // unset($frutas[2]);

  echo "<pre>";
  var_dump($frutas_2);
  echo "<pre>";

 

?>

