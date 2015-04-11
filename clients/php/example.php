<?php
require_once 'includes/jsonRPCClient.php';


define('JSON_RPC_SERVER', 'http://localhost:8888/json-rpc/');


$client = new jsonRPCClient(JSON_RPC_SERVER);

// Usage above:

// Get all metrics
$client->{"battery.get_data"}();

// Get all metrics by name
$client->{"battery.get_data"}('name');

// Add new metric (name, value (int or float))
// Use notification for faster interaction
$client->setRPCNotification(true);
$client->{"battery.charge"}('name', 1);
$client->setRPCNotification(false);

// Get and flush average metric value
$client->{"battery.discharge"}('test');

// Get and flush minimal metric value
$client->{"battery.discharge"}('test', 'min');

// Get and flush maximum metric value
$client->{"battery.discharge"}('test', 'max');