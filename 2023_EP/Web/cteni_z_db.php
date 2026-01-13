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

echo "Připojení k db úspěšně";

$cteni_mest = "SELECT id, nazev FROM `2023EP_Mesto`";

$result = $conn->query($cteni_mest);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Název: " . $row["nazev"] . "<br>";
  }
} else {
  echo "0 měst";
}
$conn->close();

