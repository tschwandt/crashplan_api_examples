#
# File: getInfoByDeviceGUID.py
# Author: AJ LaVenture, Code 42 Software
# Last Modified: 08-23-2013
#
# From a list of Device GUIDS, pull device and user information into CSV Format
# 

from c42SharedLibrary import c42Lib
import math
import sys
import json
import csv
import base64
import logging
import requests
import math
from dateutil.relativedelta import *
import datetime
import calendar


#Test values
c42Lib.cp_host = "http://aj-proappliance"
c42Lib.cp_port = "4280"
c42Lib.cp_username = "admin"
c42Lib.cp_password = "admin"


c42Lib.cp_logLevel = "INFO"
c42Lib.cp_logFileName = "getInfoByDeviceGUID.log"
c42Lib.setLoggingLevel()


AJ_TEST_DEVICE_GUID_LIST = [597897713966645505,597724554922036354,597893957280654977,597153934331668098]


GUID_LIST = AJ_TEST_DEVICE_GUID_LIST


csvFile = csv.writer(open("deviceReport.csv", "wb+"))
csvHeaders = ['guid','deviceName','osName','lastCompletedBackup','percentComplete','archiveBytes','selectedBytes','userId','userName','email',
			'firstName','lastName']

csvFile.writerow(csvHeaders)
print csvHeaders

for index, guid in enumerate(GUID_LIST):
	printValues = []
	printValues.extend([str(guid)])

	deviceList = c42Lib.getDeviceByGuid(guid)
	deviceObject = deviceList['computers']
	# print deviceObject
	
	deviceName = deviceObject[0]['name']
	printValues.extend([deviceName])

	deviceOsName = deviceObject[0]['osName']
	printValues.extend([deviceOsName])

	if deviceObject[0]['backupUsage']:

		deviceObjectBackupUsage = deviceObject[0]['backupUsage']

		lastCompletedBackup = deviceObjectBackupUsage[0]['lastCompletedBackup']
		# print str(lastCompletedBackup)
		printValues.extend([str(lastCompletedBackup)])

		percentComplete = deviceObjectBackupUsage[0]['percentComplete']
		printValues.extend([str(percentComplete)])

		archiveBytes = deviceObjectBackupUsage[0]['archiveBytes']
		printValues.extend([str(archiveBytes)])

		selectedBytes = deviceObjectBackupUsage[0]['selectedBytes']
		printValues.extend([str(selectedBytes)])

	else:
		emptyBlock = ",,,,"
		printValues.extend([emptyBlock])

	userId = deviceObject[0]['userId']
	printValues.extend([str(userId)])

	userList = c42Lib.getUserById(userId)
	# userObject = userList['users']

	username = userList['username']
	printValues.extend([str(username)])

	email = userList['email']
	printValues.extend([str(email)])

	firstName = userList['firstName']
	printValues.extend([str(firstName)])

	lastName = userList['lastName']
	printValues.extend([str(lastName)])
	
	csvFile.writerow(printValues)
	print printValues




# script request for fahad:

# list of device guids


# lastCompletedBackup
# percentComplete
# archiveBytes (bytes already backed up)
# selectedBytes

# userId


# get user id and this info
# username
# email
# firstName
# lastName



# list object = 

# add csv