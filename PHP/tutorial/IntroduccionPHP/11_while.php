<?php 
  include_once './includes/header.php'; 
?>

<?php
  $frutas = array("manzana", "naranja", "melón", "Uvas");
  
    for($i = 0; $i < count($frutas); $i++){
      echo $frutas[$i]."<br/>";
    }

    $i = 0;
    while($i < count($frutas)) {
      echo $frutas[$i]."<br/>";
      $i++;
    }

?>
