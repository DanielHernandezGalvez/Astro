<?php 
  include_once './includes/header.php'; 
?>

<?php
    $frutas = array("manzana", "naranja", "melón", "Uvas");

    for($i = 0; $i < count($frutas); $i++){
        echo $frutas[$i]."<br/>";
    }
    // echo count($frutas)

    foreach($frutas as $fruta) {
      echo $fruta . "<br/>";
    }

?>
