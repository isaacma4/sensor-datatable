# sensor-datatable
A script that takes a JSON formatted file of sensor data and creates and displays a datatable with sorted rows by alert count sum (in descending order), displaying the highest alert count sum data (up to 10) for each communication pair for each row, filtered by rows including or excluding ip addresses and snort rule ids, and a count of the rows displayed.

## Before running
Make sure to do the following before running this script on your machine:

1. Install latest version of Python for your OS (Windows: 3.7, Linux: 2.7)
2. Run from command line 'pip install -r requirements.txt'

## How to run
The script takes various inputs and creates a datatable.txt file containing the desired datatable of sensor data. All commands shown are to be run from the command line.

### Display all information
This is how you would display all your information in your JSON in a datatable:

	python create-sensor-datatable.py sensor_data.json

### Filtering by IP addresses
This is how you would filter based on **IP addresses** found in a row:

	python create-sensor-datatable.py sensor_data.json -i 51.15.83.201 76.10.2.189

Therefore, this will only display sensors that contain these IPs. You may enter any number of IP addresses to filter by.

This is how you would filter based on **IP addresses** not found in a row:

	python create-sensor-datatable.py sensor_data.json -e 58.246.12.122 10.1.1.251 10.1.28.121

Therefore, this will only display ALL sensors that DO NOT contain these IPs. You may enter any number of IP addresses to filter by.

### Filtering by Snort Rule IDs
This is how you would filter based on **Snort Rule ID** found in a row:

	python create-sensor-datatable.py sensor_data.json -s 2012888 2024930 2403426 2400000 2403352

Therefore, this will only display sensors that contain the snort rule ids. You may enter any number of snort rule ids to filter by.

This is how you would filter based on **Snort Rule ID** not found in a row:

	python create-sensor-datatable.py sensor_data.json -x 2403312 2012888

Therefore, this will only display ALL sensors that DO NOT contain the snort rule ids. You may enter any number of snort rule ids to filter by.

### Multiple Filters
The script allows to filter through the data using all four filter types listed above.

This is an example for how you would do so:

	create-sensor-datatable.py sensor_data.json -i 10.1.28.200 -e 10.1.1.46 -s 2403464 2403324 2403420 2403472 2101201 -x 2403331

### Example Datatable
Below is an example datatable of running the command shown in the **Multiple Filters** section

	+-------+-----------------+--------------------------------------------------------------------+-------------+----------+------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Count |       Sid       |                              Message                               |   Category  | Priority |    Host    | Alert Count Sum |                                                                                                                                                                                                                                                                                                                                                                                                 Communication Pairs                                                                                                                                                                                                                                                                                                                                                                                                 |
	+-------+-----------------+--------------------------------------------------------------------+-------------+----------+------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|   1   | 1:2403472:40807 | ET CINS Active Threat Intelligence Poor Reputation IP TCP group 87 | Misc Attack |    2     | Sensor #42 |        18       | [{'source_ip': '96.83.211.226', 'dest_ip': '10.1.1.55', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.121', 'alert_count_sum': 1}, {'source_ip': '98.172.185.17', 'dest_ip': '10.1.1.237', 'alert_count_sum': 1}, {'source_ip': '96.86.30.197', 'dest_ip': '10.1.100.59', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.1.26', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.148', 'alert_count_sum': 1}, {'source_ip': '98.100.98.105', 'dest_ip': '10.1.1.23', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.158', 'alert_count_sum': 1}, {'source_ip': '98.100.98.105', 'dest_ip': '10.1.28.119', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.200', 'alert_count_sum': 1}] |
	+-------+-----------------+--------------------------------------------------------------------+-------------+----------+------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+