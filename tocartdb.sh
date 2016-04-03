#!/bin/bash

read -p "Enter file name to be uploaded to CartoDB :" filename
mycurl=`curl -v -F file=@$filename "https://cartodb_username.cartodb.com/api/v1/imports/?api_key=your_api_key"`
$mycurl
