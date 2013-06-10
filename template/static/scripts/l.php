<?php

//open up the log file
$file = fopen('log.txt', 'a');
$u = $_GET["p"];
$r = $_GET["r"];

// ip address of the visitor
$ipadress = $_SERVER['REMOTE_ADDR'];

$hostname = gethostbyaddr($_SERVER['REMOTE_ADDR']);

// date of the visit that will be formated this way: 29/May/2011
$date = date('d/F/Y h:i:s');

// visitor's browser information
$browser = $_SERVER['HTTP_USER_AGENT'];


// Opening the text file and writing the visitor's data

fwrite($file, $ipadress.'	'.$hostname.'	'.$date.'	'.$u.'	'.$browser.'	'.$r."\n");

//and finial, close the log file
fclose( $file );

?>
