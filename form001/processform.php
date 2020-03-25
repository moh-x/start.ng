<?php

if(isset($_POST['first_name']))
{
$unique = $_POST['first_name'];
$file = $unique.".txt";

$name="Full Name: ".$_POST['first_name']." ".$_POST['last_name']."\n";
$email="Email Address: ".$_POST['email']."\n";
$gender="Gender: ".$_POST['gender']."\n";
$dept="To: ".$_POST['department']."\n";
$message="Message: ".$_POST['message']."\n";

$fp = fopen($file, 'w');
fwrite($fp, $name);
fwrite($fp, $email);
fwrite($fp, $gender);
fwrite($fp, $dept);
fwrite($fp, $message);
fclose($fp);
}
?>