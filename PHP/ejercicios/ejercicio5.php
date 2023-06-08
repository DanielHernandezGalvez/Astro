<?php
    /*
    imprimir por pantalla la tabla de miltiplicar del
    número pasado en un parametro GET por la URL 
    */

    // url =http://localhost:3000/backend/PHP/ejercicios/ejercicio5.php?numero=2


    if(isset($_GET["numero"]) && is_numeric($_GET["numero"])){
        $numero = $_GET["numero"];
    }else {
        $numero = 5; // por defecto
        echo "<p>Numero por defecto</p>";
    }

    echo "<h2>Tabla de multiplicar de ".$numero."</h2>";

    for($i = 1; $i <=10; $i++){
        echo $i." x ".$numero." = ".($i * $numero)."<br/>";
    }
?>