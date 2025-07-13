<!DOCTYPE html>
<html>
  <head>
    <title>The password?</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
     <?php
				if($_COOKIE["chicken"]) {
					echo "You have cookies. I want cookies!";
				} else {
					echo "The password is cuckoo";
				}
		 ?>
  </body>
</html>