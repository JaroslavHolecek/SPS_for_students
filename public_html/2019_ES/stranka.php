<?php

echo("<h1>Moje dynamická stránka</h1>");

?>


<?php

$servername = "dbs.spskladno.cz";
$username = "student22";
$password = "spsnet";
$dbname = "vyuka22";

$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
	exit("Spojení se nezdařilo. Chyba: " . $conn->connect_error);
}else{
	echo("<p>Připojeno.</p>");
}
$conn->set_charset("utf8mb4");


$sql_insert = "INSERT INTO TrainingGroup (Name) VALUES ('Úterý - večer')";

$result = $conn->query($sql_insert);
if ($result === TRUE) {
	echo "Data vložena.";
} else {
	echo "Data se nepodařilo vložit Chyba: " . $conn->error;
}

try {
	

	$sql_select = "SELECT id, Name FROM TrainingGroup";
	$result = $conn->query($sql_select);

	if ($result->num_rows > 0) {

		while($row = $result->fetch_assoc()) {
			echo "<p>Trénink ". $row["Name"]. " má ID ". $row["id"]. "</p>";
		}

	} else {
		echo "Ve výsledku nejsou žádné řádky.";
	}

} catch (Exception $e) {
	echo("<p>Chyba</p>");
	echo($e);
}



	$conn->close();
?>
