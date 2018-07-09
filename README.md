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

Datatables will always be written to file _**datatable.txt**_.

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

	python create-sensor-datatable.py sensor_data.json -i 10.1.28.200 82.202.196.66 61.136.101.103 10.1.100.2 -e 10.1.1.46 -s 2403472 2403431 2403334 2403456 -x 2403331

### Example Datatable
Below is an example datatable of running the command shown in the **Multiple Filters** section

	+-------+-----------------+--------------------------------------------------------------------+-------------+----------+------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Count |       Sid       |                              Message                               |   Category  | Priority |    Host    | Alert Count Sum |                                                                                                                                                                                                                                                                                                                                                                                                  Communication Pairs                                                                                                                                                                                                                                                                                                                                                                                                   |
	+-------+-----------------+--------------------------------------------------------------------+-------------+----------+------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	|   1   | 1:2403456:40807 | ET CINS Active Threat Intelligence Poor Reputation IP TCP group 79 | Misc Attack |    2     | Sensor #42 |        20       | [{'source_ip': '91.243.80.111', 'dest_ip': '10.1.100.2', 'alert_count_sum': 3}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.28.124', 'alert_count_sum': 1}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.1.252', 'alert_count_sum': 1}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.1.14', 'alert_count_sum': 1}, {'source_ip': '91.228.89.100', 'dest_ip': '10.1.1.40', 'alert_count_sum': 1}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.28.113', 'alert_count_sum': 1}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.28.164', 'alert_count_sum': 1}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.1.77', 'alert_count_sum': 1}, {'source_ip': '91.216.114.201', 'dest_ip': '10.1.28.30', 'alert_count_sum': 1}, {'source_ip': '91.243.80.111', 'dest_ip': '10.1.28.7', 'alert_count_sum': 1}] |
	|   2   | 1:2403472:40807 | ET CINS Active Threat Intelligence Poor Reputation IP TCP group 87 | Misc Attack |    2     | Sensor #42 |        18       |  [{'source_ip': '96.83.211.226', 'dest_ip': '10.1.1.55', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.121', 'alert_count_sum': 1}, {'source_ip': '98.172.185.17', 'dest_ip': '10.1.1.237', 'alert_count_sum': 1}, {'source_ip': '96.86.30.197', 'dest_ip': '10.1.100.59', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.1.26', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.148', 'alert_count_sum': 1}, {'source_ip': '98.100.98.105', 'dest_ip': '10.1.1.23', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.158', 'alert_count_sum': 1}, {'source_ip': '98.100.98.105', 'dest_ip': '10.1.28.119', 'alert_count_sum': 1}, {'source_ip': '98.192.81.94', 'dest_ip': '10.1.28.200', 'alert_count_sum': 1}]   |
	|   3   | 1:2403334:40639 | ET CINS Active Threat Intelligence Poor Reputation IP TCP group 18 | Misc Attack |    2     | Sensor #42 |        8        |                                                                                 [{'source_ip': '36.110.88.169', 'dest_ip': '10.1.1.32', 'alert_count_sum': 1}, {'source_ip': '31.208.92.150', 'dest_ip': '10.1.1.215', 'alert_count_sum': 1}, {'source_ip': '31.207.47.86', 'dest_ip': '10.1.28.160', 'alert_count_sum': 1}, {'source_ip': '31.207.47.86', 'dest_ip': '10.1.28.148', 'alert_count_sum': 1}, {'source_ip': '31.207.47.86', 'dest_ip': '10.1.1.166', 'alert_count_sum': 1}, {'source_ip': '31.202.117.8', 'dest_ip': '10.1.28.216', 'alert_count_sum': 1}, {'source_ip': '31.3.88.166', 'dest_ip': '10.1.28.200', 'alert_count_sum': 1}, {'source_ip': '36.110.88.169', 'dest_ip': '10.1.28.106', 'alert_count_sum': 1}]                                                                                 |
	|   4   | 1:2403431:40807 | ET CINS Active Threat Intelligence Poor Reputation IP UDP group 66 | Misc Attack |    2     | Sensor #42 |        8        |                                                                              [{'source_ip': '83.143.246.30', 'dest_ip': '10.1.28.214', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.28.69', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.1.137', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.28.91', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.28.200', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.28.154', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.28.92', 'alert_count_sum': 1}, {'source_ip': '83.143.246.30', 'dest_ip': '10.1.1.135', 'alert_count_sum': 1}]                                                                               |
	+-------+-----------------+--------------------------------------------------------------------+-------------+----------+------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+