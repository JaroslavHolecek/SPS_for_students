<?php
    session_start();
?>

<html>
<body>

<form action="" method="post"> <!-- method="get" -->
Název: <input type="text" name="nazev"><br>
Barva: <input type="color" name="barva"><br>
<input type="submit">
</form>

<?php

if (isset($_SESSION["nazev"])){
    $zadany_nazev = $_SESSION["nazev"];
}
if (isset($_SESSION["barva"])){
    $zadana_barva = $_SESSION["barva"];
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $zadana_barva = $_POST["barva"] ?? ">> nezadáno <<";    
    
    if (isset($_POST["nazev"]) && !empty($_POST["nazev"])){
        $zadany_nazev = $_POST["nazev"];
    }else{
        $zadany_nazev = ">> chybí název <<";
        echo "<p><strong>Zadej název!</strong></p>";
    }

    $_SESSION["nazev"] = $zadany_nazev;
    $_SESSION["barva"] = $zadana_barva;
    
}

if (isset($zadany_nazev) && isset($zadana_barva)){
    echo "<p>Zadal jsi, $zadany_nazev, a ". $zadana_barva ."</p>";
}else{
    echo "Zatím jsi nic neposlal...";   
}

?>

</body>
</html>