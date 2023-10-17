 <?php
// Start the session
session_start();

function NastavUzivatele() {
    $_SESSION["uzivatel"] = "Jarda";
}


?>

 <!DOCTYPE html>

<?php
$cookie_name = "barvapozadi";
$cookie_value = "blue";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
?>

<html>

    <head>
        <link rel="stylesheet" href="grafika.css">
        <title>Moje stránka</title>
        <style>
        body{
            background-color:<?php echo $_COOKIE[$cookie_name];   ?>
        }
        </style>
    </head>

    <body>

        <form  method="post">
            Name: <input type="text" name="vstup"><br>        
            <input type="submit">
        </form>

        <?php
          if ($_SERVER["REQUEST_METHOD"] == "POST"){
              echo $_POST["vstup"]; 
          }  

          NastavUzivatele(); 
        ?>

        <h1>E-shop: <?php echo $_SESSION["uzivatel"];?> </h1>
        <h2>Výrobky:</h2>

        <?php
            $vyrobky = array("myš", "klávesnice", "sluchátka" , "monitor");
            $pocet_vyrobku = count($vyrobky);
            echo "I like " . $vyrobky[0] . ", " . $vyrobky[1] . " and " . $vyrobky[2] . ".<br>"; 

            for ($i=0; $i < $pocet_vyrobku; $i++) { 
                echo $vyrobky[$i] . "<br>";
            }
            echo "===== <br>";
            foreach ($vyrobky as $cislo => $nazev) {
                echo "$cislo $nazev <br>";
            }
            /* Dodělat asociativní pole */
        ?>



        <?php
            $jmeno="jarda";
            $vek = 20;
            if ($jmeno=="honza") {
                echo("ahoj honzo<br>");
                if ($vek < 18) {
                    echo("jsi mladý<br>");# code...
                }
            
            }else{
                echo("ahoj ne  honzo<br>");

            }
            echo("nazdar <br>");
            $pocetjablek=3;
            
            switch ($pocetjablek) {
                case '1':
                    echo "to jsem se moc nenajedl";  # code...
                    break;
                case '2':
                    echo "trochu jsem se najedl";  # code...
                    break;
                case '3':
                    echo "uz nemam hlad";  # code...
                    break;
                
                default:
                    echo "jablka mi zbyla";
                    break;
            }
        ?>

        <a href="#druhy_obrazek">Skoč na druhý obrázek</a>

        <h1 class="oranzova" id="prvni_nadpis">This is a heading</h1>
        <h1 class="oranzova s_pozadim" id="druhy_nadpis">This is a heading</h1>
        <h1 class="s_pozadim">This is a heading</h1>

        <form>
            <input type="text" value="např. 18" name="username" id="policko1">
            <input type="number" placeholder="18"  name="vek" id="policko2">
            <select id="cars" name="cars">
              <option value="volvo">Volvo</option>
              <option value="saab">Saab</option>
              <option value="fiat">Fiat</option>
              <option value="audi">Audi</option>
            </select>
            <input type="date" name="datum_narozeni" id="policko3">
            <input type="color" name="pozadi" id="policko4"> <br>

            <label for="policko5">Chcete zaslat newsletter</label>
            <input type="checkbox" name="newsletter" id="policko5">
            <input type="submit" id="policko5">
        </form>

        <a href=""><img src=""></a>

        <p>This is a paragraph Dlouhý odstavec, který se nevejde na jeden řádek</p>
        <h2>This is a heading</h2>
        <h6>This is a heading</h6>
        <p><strong>This is a</strong> paragraph Dlouhý odstavec, který se nevejde na jeden řádek</p>

        <a href="https://www.spskladno.cz/index2.php">Odkaz </a>
        <div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Ponte_Vasco_da_Gama_25.jpg/1024px-Ponte_Vasco_da_Gama_25.jpg">
            <p class>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor <span>incididunt ut labore</span> et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>

        <div>
            <img id="druhy_obrazek" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Ponte_Vasco_da_Gama_25.jpg/1024px-Ponte_Vasco_da_Gama_25.jpg">
            <p class>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor <span>incididunt ut labore</span> et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>

        <i>Zvýrazněný</i>

        <ul>
            <li>mléko</li>
            <li>maso</li>
            <li>
                <ul>
                    <li>mléko</li>
                    <li>maso</li>
                    <li>vejce</li>
                </ul>
            </li>
        </ul>

        <ol>
            <li>Franta</li>
            <li>Eliška</li>
                <ol>
                    <li>Franta</li>
                    <li>Eliška</li>
                    <li>Bára</li>
                </ol>
        </ol>

    <table>
        <thead>
            <caption>Moje tabulka</caption>
            <tr> <th>I</th> <th>II</th> <th>III</th> <th>IV</th> <th>V</th> </tr>
        </thead>
        <tr>
            <td>A1</td>
            <td>B1</td>
            <td>C1</td>
            <td>A1</td>
            <td>B1</td>
            <td>C1</td>
            <td>A1</td>
            <td>B1</td>
            <td>C1</td>
            <td>A1</td>
            <td>B1</td>
            <td>C1</td>
        </tr>
        <tr>
            <td>A2</td> <td>B2</td> <td>C2</td><td>A2</td> <td>B2</td> <td>C2</td><td>A2</td> <td>B2</td> <td>C2</td><td>A2</td> <td>B2</td> <td>C2</td>
        </tr>
        <tr>
            <td>A3</td> <td>B3</td> <td>C3</td><td>A3</td> <td>B3</td> <td>C3</td><td>A3</td> <td>B3</td> <td>C3</td><td>A3</td> <td>B3</td> <td>C3</td>
        </tr>
    </table>

    </body>

</html> 