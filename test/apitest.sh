#!/bin/sh

#curl -H "Content-Type: application/json" -X POST -u tapi:tapi -d \
#     '{"CarID":"10112322",
#     "CarTMileage":"12000",
#     "CarFMileage":"1023",
#     "CarXMileage":"3211",
#     "CarStatus":"2",
#     "CarRBatteryStatus":"1",
#     "CarH2Left":"50"}' \
#     http://127.0.0.1:8000/vehicle/tapi/


curl -H "Content-Type: application/json" -X POST -u tapi:tapi -d \
     '{"CarID":"9527",
     "CarTMileage": "143200",
     "CarFMileage": "102100",
     "CarXMileage": "211",
     "CarStatus": "1",
     "CarRBatteryStatus": "0",
     "CarH2Left": "85",
     "CarH2Tmp": "32",
     "CarDBatteryStatus": "0",
     "CarDBatteryLeft": "60",
     "CarDBatteryTmp": "35",
     "CarSpeed": "120",
     "CarGeal": "1",
     "CarFault": "0",
     "CarRpm": "240",
     "CarTorque": "120",
     "CarVoltage": "12",
     "CarCurrent": "10",
     "CarTmp": "30",
     "CarRBatteryVoltage": "12",
     "CarRBatteryCurrent": "10",
     "CarRBatteryTmp": "32",
     "CarDBatteryVoltage": "12",
     "CarDBatteryCurrent": "10",
     "CarLng": "121.5000",
     "CarLat": "31.2000",
     "CarCarbon": "20",
     "CarEnergy": "24",
     "CarSum": "100"}' \
     http://127.0.0.1:8000/vehicle/tapi/
