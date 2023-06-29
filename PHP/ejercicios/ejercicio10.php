<h1>Números múltiplos de <?= $_GET["numero"]; ?></h1>
<!-- esa sintaxis < ? = es para no poner echo -->
<?php
    /**
     * Mostrar los números múltiplos de un número
     *  pasado por la URL que hay del 1 al 100
     */

    for($i = 1; $i <= 100; $i++){
        if(isset($_GET["numero"]) && $i % $_GET["numero"] == 0){
            echo $i." es múltiplo de ".$_GET["numero"]."<br/>";
        };
    };


?>