<?php session_start(); ?>
<html>
<body>

<?php 
    if (!isset($_SESSION["prihlaseny_uzivatel"])){
        $_SESSION["prihlaseny_uzivatel"] = null;
    }

    echo  "Přihlášen je uživatel " . $_SESSION["prihlaseny_uzivatel"];
?>

<form action="zpracovani_post.php" method="post">
Jmeno: <input type="text" name="jmeno"><br>
Heslo: <input type="password" name="heslo"><br>
<input type="submit">
</form>

<form action="zpracovani_get.php" method="get">
Název: <input type="text" name="nazev"><br>
Barva: <input type="color" name="barva"><br>
<input type="submit">
</form>

</body>
</html>