<?php
	$FLAGWEB6 = (file_get_contents("flag.txt"));
	$PASSWORD =  (file_get_contents("flag.txt")); //haha


	if(isset($_GET['password'])){

	if(strcmp($PASSWORD, $_GET['password']) == 0){
			$success = true;
		}
		else{
			$success = false;
		}

	}
	else {
		$success = false;
	}



?>
