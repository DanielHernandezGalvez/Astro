<?php
    /*
    Modifica el ejercicio anterior para que muestre al 
    lade de cada cuadrado si es par o impar.
    */

    for($i = 1; $i <= 30; $i++){
        $cuadraro = $i*$i;
        echo "El cuadrado de ".$i." es ".($i*$i);
        if($cuadraro % 2 == 0){
            echo " y es PAR";
        } else {
            echo " y es IMPAR";
        }
        echo "<br/>";
    }

?>
