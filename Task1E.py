from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

stations = build_station_list()


print(rivers_by_station_number(stations, 13))

samplelist = rivers_by_station_number(stations, 40) 

#several assertions which check if the type of output is the wanted type, and that the relative lenghts are correct

assert type(samplelist) == list
assert type(samplelist[0]) == tuple
assert len(rivers_by_station_number(stations, 40)) == 48
assert len(rivers_by_station_number(stations, 20)) < len(samplelist)
assert len(rivers_by_station_number(stations, 13)) == len(rivers_by_station_number(stations, 14))