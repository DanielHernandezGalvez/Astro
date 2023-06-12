<?php 
  include_once './includes/header.php'; 
?>

<?php
  $estudiantes = [
    "nombre" => "Dani",
    "apellido" => "Galvez",
    "pais" => "Mexico"
  ];

  echo "<h1>Holis ".$estudiantes["nombre"]."</h1>";


?>

<h1>Hola <?php echo $estudiantes["nombre"]; ?></h1>

