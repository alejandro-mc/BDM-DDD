# BDM-DDD
Bid Data Management and Analysis Project

To run 311_processing files use the following commands: 

./run_311_processing.sh filter311_noise.py /gws/classes/bdma/ccny/share/311_Service_Requests_from_2010_to_Present.csv /gws/classes/bdma/ccny/groups/2/noise_data/ noise.txt 32

./run_311_processing.sh filter311_noise.py /gws/classes/bdma/ccny/share/311_Service_Requests_from_2010_to_Present.csv /gws/classes/bdma/ccny/groups/2/noise_data/ reduced_noise.txt 32

./run_311_processing.sh calls_per_day.py /gws/classes/bdma/ccny/groups/2/noise_data/reduced_noise.txt /gws/classes/bdma/ccny/groups/2/calls_counts/ calls_per_day.txt 32

./run_311_processing.sh calls_per_time_of_day.py /gws/classes/bdma/ccny/groups/2/noise_data/reduced_noise.txt /gws/classes/bdma/ccny/groups/2/calls_counts/ calls_per_time_of_day.txt 32
