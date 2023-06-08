<meta charset="utf-8" />
<?php
    /* 
    Escribe un programa que multiplique los primeros
    20 numeros naturales 
    */

    $numero = 1;
    $contador = 2;

    while($contador <= 20){
        
        $numero *= $contador;

        echo $numero."<br/>";

        $contador++;
    }

    echo "El resultado de multiplicar los 20 primeros numeros es: ".$numero;

?>