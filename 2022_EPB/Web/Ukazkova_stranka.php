<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="styl.css">
</head>




<body>
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