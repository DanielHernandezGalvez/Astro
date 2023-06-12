<?php 
  include_once './includes/header.php'; 
?>

<?php
  function saludar($nombre){
    echo "bienvenido {$nombre}<br/>";
  }

  saludar("dani");
  saludar("puto");

  function suma($a, $b){
    echo $a + $b;
  }
  suma(10, 30);
?>
