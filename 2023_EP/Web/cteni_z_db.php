<!DOCTYPE html>
<html>
<head> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Čtení z DB <?php echo "na Xeonu"; ?></title>
	<link rel="stylesheet" href="styl.css">
</head> 
<body>  

<?php
$servername = "dbs.spskladno.cz";
$username = "student1";
$password = "spsnet";
$dbname = "vyuka1";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$conn->set_charset("utf8");

echo "<p>Připojení k db úspěšně</p>";

$cteni_mest = "SELECT id, nazev FROM `2023EP_Mesto`";

$result = $conn->query($cteni_mest);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "<div>";
    echo "<p>" . $row["id"] . "</p> <p>" . $row["nazev"] . "</p>";
    echo "</div>";
  }
} else {
  echo "<p>0 měst</p>";
}
$conn->close();

?>

</body>
</html>

