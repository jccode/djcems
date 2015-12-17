#!/bin/sh

curl -H "Content-Type: application/json" -X POST -u tapi:tapi -d \
     '{"CarID":"10112321","CarTMileage":"10000","CarFMileage":"1023","CarXMileage":"3211","CarStatus":"2",
     "CarRBatteryStatus":"1", "CarH2Left":"50" }' \
     http://127.0.0.1:8000/vehicle/tapi/
