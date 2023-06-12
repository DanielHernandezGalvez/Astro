<?php 
  include_once './includes/header.php'; 
?>

<?php
  function the_title() {
    echo "Titulo del blog";
  }
  function the_date() {
    echo date("d m Y");
  }
  function the_author() {
    echo "Dani";
  }
?>

<div>
  <h2><?php the_title(); ?></h2>
  <p><?php the_date(); ?></p>
  <p><?php the_author(); ?></p>
</div>
