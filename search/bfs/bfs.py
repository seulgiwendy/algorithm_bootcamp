from collections import deque

map = {}

map["me"] = ["honux", "pobi", "jk"]
map["honux"] =["dayoungle-java", "dongjun"]
map["pobi"] = ["tobi", "jojoldu-java"]
map["jk"] = ["jobs"]

def search_for_java_dev(map):
    search_queue = deque()

    search_queue += map

    while search_queue:
        person = search_queue.popleft()
        print("currently indexing " + person)
        if is_java_developer(person):
            print(person + " is a java dev!")
            return True
        else:
            search_queue += map[person]

def is_java_developer(name):
    return "java" in name

search_for_java_dev(map)


