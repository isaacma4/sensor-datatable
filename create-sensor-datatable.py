#! /usr/bin/python
######################################################
#
# Author: Isaac Ma
# Date Created: July 9th, 2018
# Latest Revision: N/A
# Copyright 2018, Isaac Ma, All rights reserved.
#
# Description: A script that takes a a JSON formatted 
# input file and creates and displays a datatable of 
# sensor data in rows that are sorted by alert count 
# sum (in descending order), displays only the top 10 
# communication pairs with regards to alert count sum
# (in descending order) for each row, include and 
# exclude rows based on IP address and snort rule id 
# (contained in a properly formatted sid) and displays 
# the count of rows.
#
######################################################

import os
import argparse
import json
from sensor import Sensor
from prettytable import PrettyTable

Filename = os.path.dirname(__file__)
OutputFile = os.path.join(Filename, 'sensor-datatable-app', 'datatable.html')

def filterListExcludingIp(list, sensor, ipAddresses):
    """
    Returns a list of sensor objects that are filtered 
    excluding rows based on ip addresses found in the 
    source_ip or dest_ip in a communication pair belonging 
    to the sensor
    
    Inputs: - A list of sensors
            - The sensor to in which to check the communation
              pair of for the ip addresses
            - The the ip addresses to exclude
    
    Outputs: A list of sensors excluding rows that contained
             any of the ip addresses
    """
    list.append(sensor)
    for cp in sensor.getHighestAlertCountSumCPs():
        if cp["source_ip"] in ipAddresses or cp["dest_ip"] in ipAddresses:
            list = list[:-1]
            break
    return list

def filterListIncludingIp(list, sensor, ips):
    """
    Returns a list of sensor objects that are filtered 
    including rows based on ip addresses found in the 
    source_ip or dest_ip in a communication pair belonging 
    to the sensor
    
    Inputs: - A list of sensors
            - The sensor to in which to check the communication
              pair of for the ip addresses
            - The the ip addresses to include
    
    Outputs: A list of sensors including rows that contained
             any of the ip addresses
    """
    for cp in sensor.getHighestAlertCountSumCPs():
        if cp["source_ip"] in ips or \
           cp["dest_ip"] in ips:
            list.append(sensor)
    return list

def _filterListbySnort(list, sensor, snortIds, filterType):
    snortRuleId = parseSnortRuleId(sensor.sid)
    if filterType == 'include':
        if snortRuleId in snortIds:
            list.append(sensor)
    elif filterType == 'exclude':
        if snortRuleId not in snortIds:
            list.append(sensor)
    return list

def filterListExcludingSnort(list, sensor, snortIds):
    """
    Returns a list of sensor objects that are filtered 
    excluding rows based on snort rule ids
    
    Inputs: - A list of sensors
            - The sensor to in which to check the snort rule 
              id of
            - The snort rule ids to exclude
    
    Outputs: A list of sensors excluding rows that contained
             any of the snort rule ids
    """
    return _filterListbySnort(
        list, sensor, snortIds, 'exclude')

def filterListIncludingSnort(list, sensor, snortIds):
    """
    Returns a list of sensor objects that are filtered 
    including rows based on snort rule ids
    
    Inputs: - A list of sensors
            - The sensor to in which to check the snort rule 
              id of
            - The snort rule ids to include
    
    Outputs: A list of sensors including rows that contained
             any of the snort rule ids
    """
    return _filterListbySnort(
        list, sensor, snortIds, 'include')

def getArgs():
    parser = argparse.ArgumentParser(description='Create Sensor Datatable')
    parser.add_argument('dataJson', metavar='data_json',
                        action='store', type=str,
                        help='the JSON formatted data of sensor telemetry \
                        data collected to parse and create datatable from')
    parser.add_argument('-i', '--include-ip', dest='ipAddressInc', action='store', 
                        type=str, nargs='+',
                        help='filtered data to include ip addresses given')
    parser.add_argument('-e', '--exclude-ip', dest='ipAddressEx', action='store', 
                        type=str, nargs='+',
                        help='filtered data to exclude ip addresses given')
    parser.add_argument('-s', '--include-snort', dest='snortInc', action='store', 
                        type=str, nargs='+',
                        help='filtered data to include snort rule ids given')
    parser.add_argument('-x', '--exclude-snort', dest='snortEx', action='store', 
                        type=str, nargs='+',
                        help='filtered data to exclude snort rule ids given')
    args = parser.parse_args()
    return args

def parseSnortRuleId(sid):
    """
    Retrieves snort rule id from sid which is formatted
    in this way: gid:snort_rule_id:revision
    
    Inputs: A properly formatted sid
    
    Outputs: Snort rule id found in the sid
    """
    return sid.split(':')[1]

def printSensorsDatatable(sensors):
    """
    Prints to a file a data table based on sensor data 
    that has been sorted and been filtered through.
    
    Inputs: List of sensor objects
    
    Outputs: A datatable written to file (datatable.txt)
    """
    table = PrettyTable(['Count',
                         'Sid',
                         'Message',
                         'Category',
                         'Priority',
                         'Host',
                         'Alert Count Sum',
                         'Communication Pairs'])
    i = 1
    for sensor in sensors:
        table.add_row([str(i),
                       sensor.sid,
                       sensor.message,
                       sensor.category,
                       sensor.priority,
                       sensor.host,
                       sensor.alertCountSum,
                       sensor.getHighestAlertCountSumCPs()])
        i += 1
    htmlText = """<html>
<head>
  <link rel="stylesheet" type="text/css" href="styles.css" media="screen" />
  <title>Sensors Datatable</title>
</head>
<body><font face="courier new">{0}</font></body>
</html>""".format(str(table).replace('\n', '<br>'))
    with open(OutputFile, 'w') as f:
        f.write(htmlText)

def sortSensorsByAlertCountSum(sensorsList):
    """
    Sorts an existing sensors object list based on alert 
    count sum.
    
    Inputs: List of sensor objects
    
    Outputs: None
    """
    sensorsList.sort(key=lambda x: x.alertCountSum, 
                     reverse=True)

def main():
    args = getArgs()
    with open(args.dataJson, 'r') as f:
        loadedJson = json.load(f)
        sensors = []
        for item in loadedJson:
            sensor = Sensor(item["sid"],
                            item["message"],
                            item["category"],
                            item["priority"],
                            item["host"],
                            item["alert_count_sum"],
                            item["communication_pairs"])
            sensors.append(sensor)
        filteredSensorsList = []
        if args.ipAddressInc != None:
            for sensor in sensors:
                filteredSensorsList = \
                    filterListIncludingIp(filteredSensorsList,
                                          sensor,
                                          args.ipAddressInc)
        if args.ipAddressEx != None:
            # if list is already being filtered then filter based on new list
            if filteredSensorsList:
                newSensorsList = []
                for sensor in filteredSensorsList:
                    newSensorsList = \
                        filterListExcludingIp(newSensorsList,
                                              sensor,
                                              args.ipAddressEx)
                filteredSensorsList = newSensorsList
            else:
                for sensor in sensors:
                    filteredSensorsList = \
                        filterListExcludingIp(filteredSensorsList,
                                              sensor,
                                              args.ipAddressEx)
        if args.snortInc != None:
            # if list is already being filtered then filter based on new list
            if filteredSensorsList:
                newSensorsList = []
                for sensor in filteredSensorsList:
                    newSensorsList = \
                        filterListIncludingSnort(newSensorsList,
                                                 sensor,
                                                 args.snortInc)
                filteredSensorsList = newSensorsList
            else:
                for sensor in sensors:
                    filteredSensorsList = \
                        filterListIncludingSnort(filteredSensorsList,
                                                 sensor,
                                                 args.snortInc)
        if args.snortEx != None:
            # if list is already being filtered then filter based on new list
            if filteredSensorsList:
                newSensorsList = []
                for sensor in filteredSensorsList:
                    newSensorsList = \
                        filterListExcludingSnort(newSensorsList,
                                                 sensor,
                                                 args.snortEx)
                filteredSensorsList = newSensorsList
            else:
                for sensor in sensors:
                    filteredSensorsList = \
                        filterListExcludingSnort(filteredSensorsList,
                                                 sensor,
                                                 args.snortEx)
        if filteredSensorsList:
            sortSensorsByAlertCountSum(filteredSensorsList)
            printSensorsDatatable(filteredSensorsList)
        else:
            sortSensorsByAlertCountSum(sensors)
            printSensorsDatatable(sensors)

if __name__ == "__main__":
    main()