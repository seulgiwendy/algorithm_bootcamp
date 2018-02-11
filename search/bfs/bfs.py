from collections import deque

map = {}

map["me"] = ["honux", "pobi", "jk"]
map["honux"] =["dayoungle", "dongjun"]
map["pobi"] = ["tobi", "jojoldu-java"]
map["jk"] = ["jobs"]

def search_for_java_dev(map):
    search_queue = deque()

    search_queue += map
    searched = []

    while search_queue:
        person = search_queue.popleft()
        print("currently searching " + person)
        if person in searched:
            print("we've already inspected you, so we'll pass to next iteration.")
            continue

        if is_java_developer(person):
            print(person + " is a java dev!")
            return True
        else:
            print("no! you don't speak java.")
            searched.append(person)
            if person in map:
                search_queue += map[person]
                print(search_queue)

def is_java_developer(name):
    return "java" in name

search_for_java_dev(map)


