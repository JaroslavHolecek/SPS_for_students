<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="styl.css">
</head>




<body>
	<?php
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