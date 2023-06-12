<?php 
  include_once './includes/header.php'; 
?>

<?php
    $frutas = array("manzana", "naranja", "melón", "Uvas");

    $estudiantes = [
      "nombre" => "Dani",
      "apellido" => "Galvez",
      "pais" => "Mexico"
    ];

    echo "<pre>";
    var_dump($estudiantes);
    echo "<pre>";

    echo "<pre>";
    print_r($estudiantes);
    echo "<pre>";

?>
