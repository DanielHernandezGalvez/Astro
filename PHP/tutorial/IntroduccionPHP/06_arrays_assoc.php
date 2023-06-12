<?php 
  include_once './includes/header.php'; 
?>

<?php
    $estudiantes = [
      "nombre" => "Dani",
      "apellido" => "Galvez",
      "pais" => "Mexico"
    ];

    // echo "<pre>";
    // var_dump($estudiantes);
    // echo "<pre>";

    // echo $estudiantes["nombre"]

    echo $estudiantes["nombre"]." ".$estudiantes["apellido"];
  
?>
