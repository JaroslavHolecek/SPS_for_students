<?php

session_start();

$prihlaseny_id = null;
if (isset($_SESSION["uzivatel_id"])) {
	$prihlaseny_id = $_SESSION["uzivatel_id"];
}

$zprava = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	if (!(isset($_POST["email"]) && isset($_POST["heslo"]))) {
		die("Při přihlášení musíš zadat oba údaje!");
	}

	$zadany_email = trim($_POST["email"]);
	$zadane_heslo = $_POST["heslo"];

	try {
		$pdo = new PDO(
			"mysql:host=dbs.spskladno.cz;dbname=vyuka1;charset=utf8mb4",
			"student1",
			"spsnet"
		);
		$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

		$stmt = $pdo->prepare("SELECT id, heslo_hash FROM JH_Ucty WHERE email = ? LIMIT 1");
		$stmt->execute([$zadany_email]);
		$ucet = $stmt->fetch(PDO::FETCH_ASSOC);

		if ($ucet && password_verify($zadane_heslo, $ucet["heslo_hash"])) {
			session_regenerate_id(true);
			$_SESSION["uzivatel_id"] = $ucet["id"];
			$prihlaseny_id = $ucet["id"];
			$zprava = "Přihlášení úspěšné.";
		} else {
			$zprava = "Neplatný email nebo heslo.";
		}
	} catch (PDOException $e) {
		die("Chyba při přihlášení: " . $e->getMessage());
	}
}

?>

<html>
<body>
<h1>Přihlášený je <?php echo $prihlaseny_id; ?> - Přihlas se:</h1>
<form action="" method="post">
Email: <input type="email" name="email" placeholder="example@example.com" required><br>
Heslo: <input type="password" name="heslo" required><br>
<input type="submit" value="Přihlásit">
</form>

<?php
if ($zprava !== "") {
	echo "<p>" . htmlspecialchars($zprava, ENT_QUOTES, 'UTF-8') . "</p>";
}
?>

</body>
</html>
