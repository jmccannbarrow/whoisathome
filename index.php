<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>
Who is at home?
</title>
<style>

  body
            {
                font-family: arial,verdana,sans-serif,Georgia, "Times New Roman", Times, serif;
                text-align:center;
                background:#ffffff;
            }
            h1
            {
                text-shadow: 5px 5px 5px #aaaaaa;
            }
        </style>
</head>
<body>
 <h1>Who is at home?</h1>
<p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdxsv2QGnvxMjwnNpN8Mc9ozY9aojvZqKiGCWPloDRWG6z7-VjQQ&s" alt="home"></p>
<?php



$hostname = "localhost";
$username = "root";
$password = "Liverpool2020!";
$db = "whoisathome";

$dbconnect=mysqli_connect($hostname,$username,$password,$db);

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

?>

<table bgcolor="#FBE9AD"  border="2" bordercolor="#687576"  align="center">
<tr>
  
  <th>User</th>
  <th>StatusTime</th>
  <th>Status</th>
 
</tr>

<?php

$query = mysqli_query($dbconnect, "SELECT * FROM tbl_statuslog ORDER by statusTime DESC")
   or die (mysqli_error($dbconnect));

while ($row = mysqli_fetch_array($query)) {
  echo
   "<tr>
    
    <td>{$row['User']}</td>
    <td>{$row['StatusTime']}</td>
    <td>{$row['Status']}</td>
   
   </tr>\n";

}

?>
</table>
</body>
</html>







