# BDM-DDD
Bid Data Management and Analysis Project

Important Directories: 

Filtered 311 data to contain only noise complaints: 
/gws/classes/bdma/ccny/groups/2/noise_data/noise.csv

Reduced 311 noise data to process less columns: 
/gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv

Number of calls per day:
/gws/classes/bdma/ccny/groups/2/calls_per_day/calls_per_day.csv

Number of calls per time of day (Hour only, if minutes need it let me know):
/gws/classes/bdma/ccny/groups/2/calls_per_time/calls_per_time_of_day.csv

Music complaints per day: 
/gws/classes/bdma/ccny/groups/2/music_per_day/music_per_day.csv

Music complaints per hour:
/gws/classes/bdma/ccny/groups/2/music_per_time/music_per_time_day.csv

Construction complaints per day:
/gws/classes/bdma/ccny/groups/2/construction_per_day/construction_per_day.csv

Construction complaints per hour: 
/gws/classes/bdma/ccny/groups/2/construction_per_time/construction_per_time_day.csv

To run 311_processing files use the following commands: 

./run_311_processing.sh filter311_noise.py /gws/classes/bdma/ccny/share/311_Service_Requests_from_2010_to_Present.csv /gws/classes/bdma/ccny/groups/2/noise_data/ noise.csv 64

./run_311_processing.sh reduce311_size.py /gws/classes/bdma/ccny/share/311_Service_Requests_from_2010_to_Present.csv /gws/classes/bdma/ccny/groups/2/reduced_noise_data/ reduced_noise.csv 64

./run_311_processing.sh calls_per_day.py /gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv /gws/classes/bdma/ccny/groups/2/calls_per_day/ calls_per_day.csv 4

./run_311_processing.sh calls_per_time_of_day.py /gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv /gws/classes/bdma/ccny/groups/2/calls_per_time/ calls_per_time_of_day.csv 4

./run_311_processing.sh music_per_day.py /gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv /gws/classes/bdma/ccny/groups/2/music_per_day/ music_per_day.csv 4

./run_311_processing.sh music_per_time_of_day.py /gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv /gws/classes/bdma/ccny/groups/2/music_per_time/ music_per_time_day.csv 4

./run_311_processing.sh construction_per_day.py /gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv /gws/classes/bdma/ccny/groups/2/construction_per_day/ construction_per_day.csv 4
                            
./run_311_processing.sh construction_per_time_of_day.py /gws/classes/bdma/ccny/groups/2/reduced_noise_data/reduced_noise.csv /gws/classes/bdma/ccny/groups/2/construction_per_time/ construction_per_time_day.csv 4
