#! /usr/bin/python
######################################################
#
# Author: Isaac Ma
# Date Created: July 9th, 2018
# Latest Revision: N/A
# Copyright 2018, Isaac Ma, All rights reserved.
#
# Description: A file that contains two classes, Sensor
# and Communication Pair, serving to make the process of
# sorting and filtering sensor data (formatted in JSON)
# easier. 
#
######################################################

class _CommunicationPair:
    """
    A protected class only used by Sensor to store
    information about each of its communication pairs.
    
    Attributes:
        sourceIp: the source ip of the communication pair
        destIp: the destination ip of the communication 
                pair
        alertCountSum: the alert count sum of the communication
                       pair
    """
    def __init__(self,
                 sourceIp,
                 destIp,
                 alertCountSum):
        self.__sourceIp = sourceIp
        self.__destIp = destIp
        self.__alertCountSum = alertCountSum

    def getSourceIp(self):
        """
        A function that returns the source ip of the 
        communication pair.
        """
        return self.__sourceIp

    def getDestIp(self):
        """
        A function that returns the destination ip of the 
        communication pair.
        """
        return self.__destIp

    def getAlertCountSum(self):
        """
        A function that returns the alert count sum of the 
        communication pair.
        """
        return self.__alertCountSum

class Sensor:
    """
    A class that contains information about a Sensor object
    that will be used to display information in a datatable.
    
    Attributes:
        sid: the sid (formatted gid:snort_rule_id:revision) of
             the sensor
        message: the message of the sensor
        category: the category of the sensor
        priority: the priority of the sensor
        host: the host of the sensor
        alertCountSum: the alert count sum of the sensor
        communicationPairs: the communication pairs of the 
                            sensor
    """
    def __init__(self,
                 sid,
                 message,
                 category,
                 priority,
                 host,
                 alertCountSum,
                 communicationPairs):
        self.sid = sid
        self.message = message
        self.category = category
        self.priority = priority
        self.host = host
        self.alertCountSum = alertCountSum
        self.communicationPairs = []
        for item in communicationPairs:
            self.communicationPairs.append(
                _CommunicationPair(item["source_ip"],
                                   item["dest_ip"],
                                   item["alert_count_sum"]))

    def getHighestAlertCountSumCPs(self):
        """
        A function that returns the communication pairs with
        the highest alert count sums (up to 10).
        """
        self.communicationPairs.sort(
            key=lambda x: x.getAlertCountSum(), reverse=True)
        returnList = []
        for i in range(len(self.communicationPairs)):
            if i == 10:
                break
            returnList.append(
                {'source_ip': self.communicationPairs[i].getSourceIp(),
                 'dest_ip': self.communicationPairs[i].getDestIp(),
                 'alert_count_sum': self.communicationPairs[i].getAlertCountSum()})
        return returnList