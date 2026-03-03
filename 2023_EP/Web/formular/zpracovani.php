<html>
<body>

<?php
    $zadane_jmeno = $_POST["jmeno"]; // $_GET[]
    $zadany_vek = $_POST["vek"];


    echo "<p>Ahoj, $zadane_jmeno, narodil jsi se ". 2026-$zadany_vek ."</p>";

?>

</body>
</html>
