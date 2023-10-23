<!DOCTYPE html>
<?php

setcookie("pozadi" , "red", time() + (86400 * 30), "/"); // 86400 = 1 day
?>

<html>
<head>
	<link rel="stylesheet" href="styl.css">
	<style type="text/css">
		body{
			background-color: <?php
								echo $_COOKIE["pozadi"];
										  ?>
		}
	</style>
</head>

<body>
	<?php
	/*
	foreach ($_SERVER as $key => $value) {
	echo "$key $value<br>";
	}
	*/
	?> 
	<!-- bez vyplněného atributu action se data odesílají do souboru s formulářem
		při vyplněném action, se odešlou do souboru zapsaném do action -->
	<form method="post">
		Name: <input type="text" name="name"><br>
		E-mail: <input type="text" name="email"><br>
		<input type="submit">
	</form>
	<?php
	   if($_SERVER["REQUEST_METHOD"] == "POST"){
	   	    $jmeno = $_POST['name'];
	   	    $adresa = $_POST['email'];
	   		echo("Welcome $jmeno <br>");
	   		echo("Welcome $adresa <br>");
	   } else {
	   		echo "Nepřišly žádné informace pomocí POST";
	   }   		
	?>

	<form method="get">
		Name: <input type="text" name="name"><br>
		E-mail: <input type="text" name="email"><br>
		<input type="submit">
   	</form>
	<?php
		if($_SERVER["REQUEST_METHOD"] == "GET"){		
			if (isset($_GET['name'])) {
			 	$jmeno = $_GET['name'];
				echo("Welcome $jmeno <br>");
            }
            if (isset($_GET['name'])) {
            	$adresa = $_GET['email'];
				echo("Welcome $adresa <br>");
			}

		} else {
			echo "Nepřišly žádné informace pomocí GET";
		}   		
	?>

	<?php
		$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
		if (isset($age['Jarda'])){
			echo "Peter is " . $age['Jarda'] . " years old.<br>";
		}else{
			echo("Neplatné údaje<br>");
		}	
	?>

	<?php
		$predmety = array("Matematika", "cesky jazyk", "programovani", "angličtina");
		echo "Předměty jménem " . $predmety[0] . ", " . $predmety[1] . " and " . $predmety[2] . ".<br>";
		$pocet_predmetu = count($predmety);

		for ($i=0; $i < $pocet_predmetu; $i++) { 
			echo "$predmety[$i]<br>";
		}

		foreach ($predmety as $key => $value) {
			echo "$key $value<br>";
		}
		$zkratky_predmetu = array("Matematika"=>"mat", "cesky jazyk"=>"cj", "programovani"=>"prg", "angličtina"=>"aj");

		foreach ($zkratky_predmetu as $key => $value) {
			echo "$key $value<br>";
		}
	?>










	<table>
		<?php
			$radky = 5;
			$sloupky = 10;
			for ($i=0; $i < $radky ; $i++) { 
				echo "<tr>" ;						   
					for ($j=0; $j < $sloupky ; $j++) { 
						echo "<td>$i - $j</td>";
					}
				echo "</tr>" ;
			}
		?>
	</table>

	<?php
	$pocitadlo = 0;
	$n = 36;
	while($n > 1){
		if ($n % 2 == 0) {
			$n = $n/2;
		}else { 
			$n = 3*$n+1;
		}
		echo "$n <br>";
		$pocitadlo = $pocitadlo+1;
	}

	echo "počet opakování bylo $pocitadlo </br>";

	$napis = "slovo";
	$int = 123;
	$float = 123.52;
	$null = null;
	$bool = true;
	$array = array("slovo1", "slovo2", "slovo3");
	echo("$napis $int $float $null $bool"); echo("<br>");
	var_dump($napis); echo("<br>");
	var_dump($int); echo("<br>");
	var_dump($float); echo("<br>");
	var_dump($null); echo("<br>");
	var_dump($bool); echo("<br>");
	var_dump($array); echo("<br>");

	$velikostnadpisu = 2;
	$barva="red";
	$jmeno = "jarda";
	echo 1+1;
    if ($jmeno == "pepa") {
    	if ($velikostnadpisu < 3) {
    		$barva="green";
    	}else {
    		$barva="lightgreen";
    	}

    }else {
    	$barva="blue";
    }
/* 
$colournumber = 3;
switch ($colournumber) {
	case 1:
		$barva="orange";	
		break;
	case 2:
		$barva="blue";	
		break;
	case 3:
		$barva="green";	
		break;
	
	default:
		# code...
		break;
}
*/
	?>
	
	<div style="background-color:<?php echo $barva;?>;">
		<p>první</p>
		<p>druhý</p>
		<p>třetí</p>
	</div>

	

	<h1>velky nadpis</h1>
	<h5>maly nadpis</h5>

	<br>
	<?php
	echo ("<h$velikostnadpisu>Měnící se nadpis</h$velikostnadpisu>");
	echo $jmeno;
	?>
	<br>
	<?php
	echo ("My first PHP script!");
	?>
	<?php
	echo ("Ahoj $jmeno");
	?>


</body>
</html>