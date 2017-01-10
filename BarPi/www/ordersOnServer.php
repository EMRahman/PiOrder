<!DOCTYPE html>
<html>

<head>
<script src="./jquery-1.10.2.js"></script>
<script src="./jquery-ui.js"></script>
<title>Orders on Printer</title>

</head>
<body>

<div id="result"></div>
<script>

var processedOrders_JavaScript = null;

$(document).ready(function(){
    $(".print_cust_receipt").click(function(){
	$(this).effect("highlight",{color: '#FF4500'}, 1000);
	var orderId= $(this).attr('orderId');
	postData(orderId,"printCustomerReceipt");
    });
    $(".reprint_at_bar").click(function(){
	$(this).effect("highlight",{color: '#FF4500'}, 1000);
	var orderId= $(this).attr('orderId');
	postData(orderId,"printAtBar");
    });
    $(".reprint_at_kitchen").click(function(){
	$(this).effect("highlight",{color: '#FF4500'}, 1000);
	var orderId= $(this).attr('orderId');
	postData(orderId,"sendToKitchen");
    });
    $(".print_at_bar_for_kitchen").click(function(){
	$(this).effect("highlight",{color: '#FF4500'}, 1000);
	var orderId= $(this).attr('orderId');
	postData(orderId,"printAtBarForKitchen");
    });
});

function postData(key,destination)
{

	//var payload = localStorage.getItem(key);
	var payload = processedOrders_JavaScript[key];
	//alert(key);
        var jqxhr = $.post( "reprintOrder.php", {'key':key,'order': payload,'destination':destination}, function() {
                //alert('Made it here');
		//window.location.href = "./";
                })
         .fail(function() {
                alert("Error sending data");
        });
}

    var countKeys= 0; 
    var results = ''; 
    //TODO: to order by timestamp as this is more reliable	
    //Array to put the previous orders in using a their timestamp to order them by time (most recent first)
    localOrdersByTimestamp = [];

    //Check for processed orders on the server, load it into a javascript array
<?php
$processedOrders = array();
$directory='/tmp/kpos/';
$output = shell_exec('find /tmp/kpos | grep printAtBar | grep processed | grep order');
$output = explode("\n",$output);

foreach ($output as $filePath){
        //Strip out the filename to the key
        $key = basename($filePath);
	//Get the order content
        $orderContent = shell_exec('cat '.$filePath);
	//Put into an array
	$processedOrders[$key]=$orderContent;
}
?>
    processedOrders_JavaScript = $.parseJSON('<?php echo json_encode($processedOrders); ?>');

    for (var key in processedOrders_JavaScript){

        var res = key.indexOf("order");
        //Verify the key (or the filename) contains the term "order"; this will weed out the null key
        if( res < 0) {
                continue;
        }

	countKeys++; //increase the order count

        //Put timestamp, key and html in an array for ordering the output
	resultOrder = [];
	var result = '';
        result += '<tr><td bgcolor=#20B2AA>';
        result += '<textarea rows=6 cols=40 style="border:none;" readonly>';
        var orderXML = processedOrders_JavaScript[key];
        var parser = new DOMParser();
        var xmlDoc = parser.parseFromString(orderXML,"text/xml");
	result += key;
	result += '\n';

        resultOrder['timestamp']=xmlDoc.getElementsByTagName("timestamp")[0].childNodes[0].nodeValue;
	takeoutOrInhouse = xmlDoc.getElementsByTagName("takeoutOrInhouse")[0].childNodes[0].nodeValue;
	
	if(takeoutOrInhouse == 'TAKEOUT'){
		orderTime = xmlDoc.getElementsByTagName("orderTime")[0].childNodes[0].nodeValue;
       		result += "\nOrder Time: "+ orderTime 
		collectionTime = xmlDoc.getElementsByTagName("collectionTime")[0].childNodes[0].nodeValue;
       		result+= "\nCollection Time: "+ collectionTime + "\n"
	}else{
		printTime = xmlDoc.getElementsByTagName("printTime")[0].childNodes[0].nodeValue;
       		result += "\nPrint Time: "+ printTime 
		inhouseReadyTime = xmlDoc.getElementsByTagName("inhouseReadyTime")[0].childNodes[0].nodeValue;
       		result += "\nInhouse Ready Time: "+ inhouseReadyTime + "\n"
	}
	result += 'Total: ' + xmlDoc.getElementsByTagName("total")[0].childNodes[0].nodeValue + "\n";

	var items = xmlDoc.getElementsByTagName("item");
	var prevCategory = '';
	for (var i = 0; i < items.length; i++) {   

		var category = items[i].getElementsByTagName("category")[0].childNodes[0].nodeValue;
		var qty = items[i].getElementsByTagName("qty")[0].childNodes[0].nodeValue;
		var foodDesc = items[i].getElementsByTagName("foodDesc")[0].childNodes[0].nodeValue;
		var subtotal = items[i].getElementsByTagName("subtotal")[0].childNodes[0].nodeValue;
		if (prevCategory != category) {
			result += '\n' + category;
			prevCategory = category;
		}
		result += '\n' + qty + ' ' + foodDesc + ' ' + subtotal;
	} 
	result += '\n';
	result += '\n';
	result += 'Qty: ' + xmlDoc.getElementsByTagName("totalQty")[0].childNodes[0].nodeValue;
	result += '\n';
        if(xmlDoc.getElementsByTagName("chutneysCharge").length != 0){
                result += 'Chutneys: ' + xmlDoc.getElementsByTagName("chutneysCharge")[0].childNodes[0].nodeValue;
                result += '\n';
        }
	result += 'Service: ' + xmlDoc.getElementsByTagName("serviceCharge")[0].childNodes[0].nodeValue;
	result += '\n';
	result += 'Total: ' + xmlDoc.getElementsByTagName("total")[0].childNodes[0].nodeValue;
        result += '</textarea>';
        result += '</td>';
        result += '<td bgcolor=#F08080 align=center class=print_cust_receipt orderId='+key+'>Print Customer Receipt</td>';
        result += '<td bgcolor=#F08080 align=center class=reprint_at_bar orderId='+key+'>Reprint at Bar</td>';
        result += '<td bgcolor=#F08080 align=center class=reprint_at_kitchen orderId='+key+'>Reprint at Kitchen</td>';
        result += '<td bgcolor=#F08080 align=center class=print_at_bar_for_kitchen orderId='+key+'>Print at Bar for Kitchen</td>';
        result += '</tr>';

        resultOrder['htmlResult']=result;
	localOrdersByTimestamp.push(resultOrder);

        //results = result + results; //for ordering the most recent to be at the top
    }

    var header = ''; 
    //Number of locally saved orders
    header = '<tr><td bgcolor=#20B2AA colspan=5><b>Processed orders on the server: ' + countKeys + '</b></td></tr>';

    //Order the local orders by timestamp, newest order at the top
    localOrdersByTimestamp.sort(function(a,b){return b['timestamp']-a['timestamp']});

    //Loop through HTML results and populate them
    for (var index in localOrdersByTimestamp){
       results += localOrdersByTimestamp[index]['htmlResult'];
    }

    results = '<table width=100% border=1 bgcolor=#20B2AA>'+header+results+'</table>';
    document.getElementById("result").innerHTML = results;
</script>
</body>
</html>
