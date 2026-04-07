<?php

$heslo = "132";
echo $heslo . " >>> " . password_hash($heslo, PASSWORD_DEFAULT) . "<br>";

$heslo = "456";
echo $heslo . " >>> " . password_hash($heslo, PASSWORD_DEFAULT) . "<br>";

$heslo = "789";
echo $heslo . " >>> " . password_hash($heslo, PASSWORD_DEFAULT) . "<br>";

?>