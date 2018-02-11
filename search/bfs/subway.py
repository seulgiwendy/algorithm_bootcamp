from collections import deque

stations = {}

stations["반고개"] = ["내당", "신남"]
stations["내당"] = ["반고개"]
stations["신남"] = ["반고개", "서문시장", "남산"]
stations["반월당"] = ["신남", "중앙로", "경대병원"]
stations["서문시장"] = ["신남"]
stations["중앙로"] = ["반월당"]
stations["경대병원"] = ["중앙로"]

def search_route(destination, stations):

    search_queue = deque()
    search_queue += stations

    searched = []

    while search_queue:
        station_name = search_queue.popleft()

        if station_name in searched:
            continue

        if is_correct_station(destination, station_name):
            return "목적지가 노선에 있습니다."

        else:
            searched.append(station_name)
            if station_name in stations:
                search_queue += stations[station_name]

    return


def is_correct_station(destination, station):
    return destination in station

print(search_route("서문시장", stations))