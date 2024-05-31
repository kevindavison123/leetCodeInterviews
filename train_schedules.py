# Trains depart from a train station the train times are in an unsorted array, find when they intersect and print the times
from collections import Counter
from typing import List


def train_schedules(train_schedules: List[List[int]]):
    combined_list = []
    unique_list = []
    duplicate_list = []
    for train_schedule in train_schedules:
        train_schedule_set = set(train_schedule)
        combined_list.extend(train_schedule_set)
    for i in range(len(combined_list)):
        if combined_list[i] not in unique_list:
            unique_list.append(combined_list[i])
        elif combined_list[i] in unique_list:
            duplicate_list.append(combined_list[i])
    return duplicate_list




if __name__ == '__main__':
    print(train_schedules([[1, 2, 3, 4, 5], [5, 8, 3, 2, 1]]))
