from buses import *


bus_count = 0
bus_list = []


for R in routes:
    route_count = 0
    count = 0
    while count <= R['duration']:
            if count % R['t1']['frequency'] == 0:
                    route_count += 1
            count += 10
    bus_count += route_count


print(bus_count)
