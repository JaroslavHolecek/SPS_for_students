<html>
    <body>

    <?php
        $default_value=15;


         echo "Koupil jsme $default_value jablek";

         var_dump($default_value);
    ?>

   

 <form action="soubor_pro_zpracovani.php" method="post">
 Počet řádků:
 <input type="number" name="radky" value=<?php echo $default_value+1; ?> >
 <br>
 Počet sloupců:
 <input type="number" name="sloupce" value=<?php echo $default_value; ?> >
 <br>
 <input type="submit" value="Zobraz tabulku">
 </form>

</body>
</html>