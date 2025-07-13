<?php
	$components = parse_url($_SERVER['REQUEST_URI']);
  parse_str($components['query'], $params);
	$ip = $params['ip'];
	$host = gethostbyaddr($ip);
	echo "$host";