<?php
    /**
     * Hacer un programa que tenga un array de 5 números enteros
     * y hacer lo siguiente con él:
     * - Recorrerlo u mostrarlo
     * - Ordenarlo y Mostrarlo
     * - Mostrar su longitud
     * - Buscar en el Array
     */

    $numeros = array(20,70,30,10,50, 5);

    echo "<h2>Recorrer y mostrar</h2>";

    foreach($numeros as $numero){
        echo $numero."<br/>";
    };

    echo "<h2>Ordenar y mostrar</h2>";
    // ordenar
    sort($numeros);
    foreach($numeros as $numero){
        echo $numero."<br/>";
    };

    echo "<h2>Mostrar su longitud</h2>";
    echo count($numeros);
    // echo siseof($numeros);

    echo "<h2>Buscar en el Array</h2>";
    if(!array_search(50, $numeros)){
        echo "<p>El numero no existe</p>";
    }else{
        echo "<p>El numero si existe</p>";

    }

?>