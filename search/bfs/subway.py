from collections import deque

class Station():

    def __init__(self, line, name):
        self.line = line
        self.name = name

    def __str__(self):
        return "%d호선 %s역" % (self.line, self.name)

    def __repr__(self):
        return "%d호선 %s역" % (self.line, self.name)

bangogae = Station(1, "반고개")
naedang = Station(1, "내당")
sinnam = Station(1, "신남")
banwoldang = Station(1, "반월당")
seomun = Station(3, "서문시장")
namsan = Station(3, "남산")
center = Station(2, "중앙로")
gyeongdae_hospital = Station(1, "경대병원")


stations = {}


stations[bangogae] = [naedang, sinnam]
stations[naedang] = [bangogae]
stations[sinnam] = [bangogae, seomun, namsan]
stations[banwoldang] = [sinnam, center, gyeongdae_hospital]
stations[seomun] = [sinnam]
stations[center] = [banwoldang]
stations[gyeongdae_hospital] = [banwoldang]




def search_route(origin, destination, stations):

    search_queue = deque()
    search_queue += stations[origin]
    print("시작 큐: ", search_queue)
    searched = []

    station_count = 0
    transfer_count = 0

    while search_queue:
        station_name = search_queue.popleft()
        print("탐색중인 역: ", station_name)
        if station_name in searched:
            print(station_name, "은 이미 탐색했습니다.")
            continue

        if is_correct_station(destination, station_name):
            return "목적지가 노선에 있습니다."

        else:
            searched.append(station_name)
            if station_name in stations:
                search_queue += stations[station_name]

            print(search_queue)

    return


def is_correct_station(destination, station):
    return destination.name in station.name

def is_transfer(station_origin, station_compare):

    if isinstance(station_origin, Station) == False or isinstance(station_compare, Station) == False:
        return False

    return station_origin.line != station_compare.line

print(search_route(gyeongdae_hospital, seomun, stations))

station_by_class = Station(2, "경대병원")
another_station_by_class = Station(1, "중앙로")

print(is_transfer(station_by_class, another_station_by_class))