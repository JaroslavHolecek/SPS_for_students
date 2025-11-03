<?php
	$servername = "dbs.spskladno.cz";
	$username = "student22";
	$password = "spsnet";
	$dbname = "vyuka22";
	$conn = new mysqli($servername, $username, $password, $dbname);

	if ($conn->connect_error) {
	exit("Spojení se nezdařilo. Chyba: " . $conn->connect_error);
	}
	$conn->set_charset("utf8mb4");
	echo("<h1> Pripojení k databázi je v pořádku </h1>");

	$sql_insert = "INSERT INTO TrainingGroup (Name) VALUES ('Pondělí - odpoledne')";
/*
	$result = $conn->query($sql_insert);
	if ($result === TRUE) {
		echo "Data vložena.";
	} else {
		echo "Data se nepodařilo vložit. Chyba: " . $conn->error;
	}
*/
	$sql_select = "SELECT id, Name FROM TrainingGroup";
	$result = $conn->query($sql_select);

	if ($result->num_rows > 0) {

		while($row = $result->fetch_assoc()) {
			var_dump($row);
			echo "id: ". $row["id"]. " - Název: ". $row["Name"] . "<br>";
		}

	} else {
		echo "Ve výsledku nejsou žádné řádky.";
	}


	$conn->close();
?>