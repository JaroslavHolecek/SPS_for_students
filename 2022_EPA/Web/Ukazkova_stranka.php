 <!DOCTYPE html>
<html>
<body>

<?php
 
$x = 0;
echo "My first PHP script!";
/*datove typy -
int - cele cislo
float - cislo  s desetinnou carkou
string - text
boolean - true/false
Jak zjistit datovy typ 
----------------------*/
$VelikostNadpisu= 0;
var_dump($VelikostNadpisu); 


while ($VelikostNadpisu <= 10){
	$VelikostNadpisu = $VelikostNadpisu+1;
	if ($VelikostNadpisu %6 == 0) {
		break;	# code...
	}
	if ($VelikostNadpisu %2 == 0) {
		continue;	# code...
	}
	

	echo ("ghghgg $VelikostNadpisu<br>");
	
	
}

for ($i=0; $i < 5; $i+=2 ){ 
	echo "$i";
}
?>

<h1>nadpis1</h1>
<h3>nadpi3</h3>


<h<?php echo $VelikostNadpisu; ?>>
 		měnící se nadpis
</h<?php echo $VelikostNadpisu; ?>>

</body>
</html> 