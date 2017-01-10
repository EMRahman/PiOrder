<?php 

$logFile = '/tmp/kpos.log';

$a = $_POST['order'];
$order = implode($a);
$order = $order.""; #Convert to string

#Implement a counter file, user the counter to track the file name
$fp = fopen("/tmp/kpos/kpos_counter.txt", "r");
$count = fread($fp, 1024); 
fclose($fp);
$count = $count + 1; 
$fp = fopen("/tmp/kpos/kpos_counter.txt", "w"); 
fwrite($fp, $count); 
fclose($fp);


#Logging
$log_fp = fopen("/tmp/kpos/kpos_print.log", "a"); 

#Get the name of the customer and order time; to put into the filename too
$orderXML = new SimpleXMLElement($order);

$orderRef = '';

#Get order type: takeout or inhouse
$takeoutOrInhouse = $orderXML->takeoutOrInhouse;
if ($takeoutOrInhouse == 'TAKEOUT'){
	$customer = $orderXML->customer; 
	$customer = preg_replace('/\s+/', '', $customer);
	$orderRef  = $customer;
} else {
	$table = 'Table'.$orderXML->tableNumber.'_'.$orderXML->numbOfCust.'people';
	$orderRef = $table;
}

$orderTime = date('Ymd_Hi');

#Create /tmp/kpos folder
if (!file_exists('/tmp/kpos/')) {
	$old_umask = umask(0);
	mkdir('/tmp/kpos/', 0777);
	umask($old_umask);
}

foreach($orderXML->printTerminal as $printer){
	$printerPath = '';
	if($printer == 'BAR'){
		$printerPath = 'printAtBar';
	}
	if($printer == 'KITCHEN'){
		$printerPath = 'sendToKitchen';
	}
	
	$outputFile= '/tmp/kpos/'.$printerPath.'/order_'.$count.'_'.$takeoutOrInhouse.'_'.$orderRef.'_'.$orderTime;
	file_put_contents($outputFile, $order, FILE_APPEND);
	chmod($outputFile, 0777);
	fwrite($log_fp, "\n".'Output file created: '.$outputFile);
}

#Daemon service kpos will print and move the file

#Close the log file

fclose($log_fp);

?>
