<?php
$mysqli = new mysqli("db", "usuario", "senha", "vulneravel");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

$query = "SELECT * FROM usuarios WHERE id = " . $_GET['id'];
$result = $mysqli->query($query);

if (!$result) {
    die("Query failed: " . $mysqli->error);
}

while ($row = $result->fetch_assoc()) {
    echo $row['nome'];
}
?>