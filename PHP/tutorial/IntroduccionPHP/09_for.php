<?php 
  include_once './includes/header.php'; 
?>

<?php
  for($i = 1; $i <= 10; $i++){
    if($i == 10){
      echo "El numero es 10 <br/>";
      continue;
      // break;
    }
    echo $i."<br/>";
  }
?>
