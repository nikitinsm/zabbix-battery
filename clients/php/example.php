<?php
define('JSON_RPC_SERVER', 'http://localhost:8888/json-rpc/');

require_once 'includes/jsonRPCClient.php';

$client = new jsonRPCClient(JSON_RPC_SERVER);

//Get all metrics
$client->{"battery.get_data"}();

//Add new metric (name, value (int or float))
$client->setRPCNotification(true);
$client->{"battery.charge"}('name', 1);
$client->setRPCNotification(false);

//Get and flush average metric value
$client->{"battery.discharge"}('test');

//Get and flush minimal metric value
$client->{"battery.discharge"}('test', 'min');

//Get and flush maximum metric value
$client->{"battery.discharge"}('test', 'min');