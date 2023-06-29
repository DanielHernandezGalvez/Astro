<?php
    /**
     * Escribe un programa que muestre la dirección IP del
     * usuario que visita nuestra web y si usa Google Chrome
     * darle la enorabuena, se ganó un iphone
     */

     $ip = $_SERVER["REMOTE_ADDR"];
     $browser = $_SERVER["HTTP_USER_AGENT"];

     echo "Tu IP es ".$ip;

     if(strstr($browser, "Google Chrome") == true){
        echo "<br/>"."el navegador que usas es chrome, Ganaste un aifon";
     } else {
        echo "<p>No es Chrome, Perdiste</p>";
     };
?>