<?php

session_start();
$prihlaseny_id = null;
if (isset($_SESSION["uzivatel_id"])){
    $prihlaseny_id = $_SESSION["uzivatel_id"];
}   

$zprava = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if ( !(isset($_POST["email"]) && isset($_POST["heslo"]))){
        die("Při registraci musíš zadat oba údaje!");
    }

    $zadany_email = $_POST["email"];
    $zadane_heslo = $_POST["heslo"];

    $hashovane_heslo = password_hash($zadane_heslo, PASSWORD_DEFAULT);

    try {
        $pdo = new PDO("mysql:host=dbs.spskladno.cz;dbname=vyuka1;charset=utf8mb4", "student1", "spsnet");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        $stmt = $pdo->prepare("INSERT INTO JH_Ucty (email, heslo_hash) VALUES (?, ?)");
        $stmt->execute([$zadany_email, $hashovane_heslo]);
        
        $zprava = "Registrace úspěšná!";
    } catch (PDOException $e) {
        die("Chyba: " . $e->getMessage());
    }
    
}

?>


<html>
<body>
<h1>Přihlášený je <?php echo $prihlaseny_id; ?> - Zaregistruj se:</h1>
<form action="" method="post"> <!-- method="get" -->
Email: <input type="email" name="email" placeholder="example@example.com" required><br>
Heslo: <input type="password" name="heslo" placeholder="Heslo" required><br>
<input type="submit" value="Zaregistrovat">
</form>

<?php
if ($zprava !== "") {
    echo "<p>" . htmlspecialchars($zprava, ENT_QUOTES, 'UTF-8') . "</p>";
}
?>



</body>
</html>