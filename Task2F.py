
import matplotlib.pyplot as plt

from floodsystem.datafetcher import *
from floodsystem.analysis import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import *
from floodsystem.datafetcher import *


def run():
    p = 4
    #   build and update the lsit of stations
    stations = build_station_list()
    update_water_levels(stations)

    #   set variable N
    N = 5
    dt=2

    #   Print out stations as the questions requests
    for station in stations_highest_rel_level(stations, (N+1)):
        station_name = station[0]
        #specific_station = None
        if station[0] == "Letcombe Bassett":
            pass 
        else: 
            for station_obj in stations:
                if station_obj.name == station_name:
                    specific_station = station_obj

                else:
                    pass


                
            dates, levels = (fetch_measure_levels(specific_station.measure_id,
                                                dt=datetime.timedelta(days=dt)))
            plot_water_level_with_fit(specific_station, dates, levels, p)

       

if __name__ == "__main__":
    print("Task 2E Running...")
    run()





"""
station_name = "Abingdon Lock"
dt = 2
# Build list of stations
stations = build_station_list()
station_of_interest = None
for station in stations:
    if station.name == station_name:
        station_of_interest = station
        break

if not station_of_interest:
    raise ValueError("Station {} could not be found".format(station_name))

# find the dates and the levels associated 

dates, levels = (fetch_measure_levels(station_of_interest.measure_id,
                                     dt=datetime.timedelta(days=dt)))

p = 10
"""

"""
for 
plot_water_level_with_fit(station_of_interest, dates, levels, p)

poly, d0 =polyfit(dates, levels, 5)

print ("poly is", poly)
print("d0 is " , d0)
"""