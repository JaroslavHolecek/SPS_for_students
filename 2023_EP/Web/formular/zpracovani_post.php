<?php session_start(); ?>
<html>
<body>

<?php
    $zadane_jmeno = $_POST["jmeno"]; // $_GET[]
    $zadane_heslo = $_POST["heslo"];

    // password_hash() vrátí řetězec, ve kterém je // "1234" + sůl (náhodná) + použitý algoritmus
    $vsichni_uzivatele = array(
        "Adam" => "\$2y\$12\$h7vZWCaU0VHDfmPJGA8yuOszwQ1FsmN39UVeofGV92lao973OjOZO",
        "Bara" => "\$2y\$12\$ELDYoaGII2YWRHD23yuiruHuXFbrNlN3U9YIXHPP3brdDL0S37OxC",
        "Cecilie" => "\$2y\$12\$.jB8ddxwVWFQD9ja6zxyXeHW1LTLF9RW8Y55Lo8qv7s2bAK36jfdq");

    $prihlaseny = null;

   // echo password_hash("1234", PASSWORD_DEFAULT);
    if ( ! isset($vsichni_uzivatele[$zadane_jmeno]) ){
        die("Neznámý uživatel"); // pro ilustraci, ve skutečnosti se nerozlišuje chybné jméno a heslo
    }

    if ( password_verify($zadane_heslo, $vsichni_uzivatele[$zadane_jmeno]) ) {
        $prihlaseny = $zadane_jmeno;
        echo "Úspěšně jsi se přihlásil, $prihlaseny";
    }else{
        $prihlaseny = null;
        echo "Chybně zadané heslo";
    }

    $_SESSION["prihlaseny_uzivatel"] = $prihlaseny;

?>

</body>
</html>
