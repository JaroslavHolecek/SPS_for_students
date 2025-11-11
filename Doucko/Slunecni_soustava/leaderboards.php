<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles/style.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shachy</title>
</head>
<body>
    <header>
        <a href="index.html" class="nadpis">Shachy</a>
        <nav class="topnav">
            <a href="login.html">Přihlásit se</a>
            <a href="register.html">Zaregistrovat se</a>
        </nav>
    </header>
    <nav class="bottomnav">
        <a href="download.html">Stáhnout</a>
        <a href="aboutus.html">O nás</a>
        <a href="leaderboards.php">Žebříčky</a>
    </nav> 
    <div class="zebricek">
      <?php
        $servername = "dbs.spskladno.cz";
        $username = "student10";
        // $username = "student15";
        $password = "spsnet";
        $database = "vyuka10";
        // $database = "Shachy";
        
        $conn = new mysqli($servername, $username, $password, $database);
        
        if ($conn->connect_error) {
          die("Connection failed: " . $conn->connect_error);
        }
        
        // function vypsatLeaderboard($result){
        //   if ($result->num_rows > 0) {
        //     echo('<table class="leaderboard">
        //     <tr>
        //     <th>Pořadí</th>
        //     <th>Jméno hráče</th>
        //     <th>Počet vyhraných her</th>
        //     </tr>');
            
        //     $i = 1;
        //     while($row = $result->fetch_assoc()) {
        //       echo("\n<tr>\n".
        //       '<td class="cislo">'.$i."</td>
        //       <td>".$row["user_name"]."</td>
        //       <td class="cislo">".$row["won_games"]."</td>
        //       \n</tr>");
        //       $i++;
        //     }
          
        //     echo("\n</table>");
        //     } else {
        //     echo("0 vysledku");
        //   }
        // };
        
        echo("<h2>Pořadí hráčů</h2>");
        // $sql = 'SELECT user_name, won_games FROM User ORDER BY won_games';
        $sql = 'SELECT id, znacka, max_rychlost FROM Automobil';
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
          echo('<table class="leaderboard">
          <tr>
          <th>znacka</th>
          <th>rychlost</th>
          <th>id</th>
          </tr>');
          
          while($row = $result->fetch_assoc()) {
            echo("\n<tr>\n".
            '<td class="cislo">'.$row["znacka"]."</td>
            <td>".$row["max_rychlost"].'</td>
            <td class="cislo">'.$row["id"]."</td>
            \n</tr>");
          }
        
          echo("\n</table>");
          } else {
          echo("0 vysledku");
          }

        // vypsatLeaderboard($result);
        
      ?>
    </div>
</body>
</html>