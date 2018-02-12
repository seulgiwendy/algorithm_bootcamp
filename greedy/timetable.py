from collections import deque


class Classtime:

    def __init__(self, start_time, end_time, subject):
        self.start_time = start_time
        self.end_time = end_time
        self.subject = subject

    def is_conflict(self, another_class):
        return self.end_time > another_class.start_time

    def __str__(self):
        return "%s : %d시 ~ %d시" % (self.subject, self.start_time, self.end_time)

    def __repr__(self):
        return "%s : %d시 ~ %d시" % (self.subject, self.start_time, self.end_time)

class_list = []


class1 = Classtime(9, 11, "알고리즘")
class2 = Classtime(10, 12, "웹프로그래밍")
class3 = Classtime(8, 9, "정신교육")
class4 = Classtime(13, 14, "React.js 특강")

print(class1.is_conflict(class2))

class_list.append(class1)
class_list.append(class2)
class_list.append(class3)
class_list.append(class4)

def arrange_schedule(sessions_list):

    selected_list = []

    sessions_queue = deque()
    sessions_queue += sessions_list

    selected_list.append(first_class(sessions_list))

    while sessions_queue:
        searching_session = sessions_queue.popleft()
        last_selected_session = selected_list[-1]

        if last_selected_session.is_conflict(searching_session) == False:
            selected_list.append(searching_session)

    return selected_list

def first_class(sessions_list):
    earliest_class = sessions_list[0]
    earliest_class_time = earliest_class.start_time

    for i in range(len(sessions_list)):
        searching_class = sessions_list[i]
        if searching_class.start_time < earliest_class_time:
            earliest_class = searching_class
            earliest_class_time = searching_class.start_time

    return earliest_class

print(first_class(class_list))
print(arrange_schedule(class_list))





