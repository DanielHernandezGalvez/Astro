<?php
    /**
     * Escribir un programa que calcule el factorial de cualquier número
     * almacenado en una variable
     */

    $factorial = 1;
    $numero = $_GET["numero"];
    
    for($cont = 1; $cont <= $numero; $cont++) {
        $factorial *= $cont;
    };

    echo "el factorial de ".$numero." es ",$factorial;


?>