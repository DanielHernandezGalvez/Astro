<?php 
  include_once './includes/header.php'; 
?>

<?php
  function calcular_total($cantidad) {
    $total = $cantidad * 1.16;
    return $total;
  }

  $cantidad_pagar = calcular_total(1000);

  function pagar($total){
    $balance = 500;

    if($total > $balance) {
      echo "Hubo un error al pagar";
    } else {
      echo "Pago exitoso";
    }
  }

  pagar($cantidad_pagar)

?>