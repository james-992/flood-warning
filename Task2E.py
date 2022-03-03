from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import *
from floodsystem.datafetcher import *

def run():
    #   build and update the lsit of stations
    stations = build_station_list()
    update_water_levels(stations)

    #   set variable N, which is the number of stations being considered (ignoring letcombe bassett)
    N = 5

    #number of days the graph should go across
    dt=10

    #This part finds the station objects in stations from the names given by 
    # the stations_highest_rel_level function
    for station in stations_highest_rel_level(stations, (N+1)):

        station_name = station[0]
        #ignores letcombe bassett because it's data is problematic
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
            plot_water_levels(specific_station, dates, levels)
            

if __name__ == "__main__":
    print("Task 2E Running...")
    run()


        

