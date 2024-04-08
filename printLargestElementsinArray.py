# Given an array arr[] of size N,
# the task is to printing K largest elements in an array.
# Note: Elements in output array can be in any order
import heapq


def main(input, k):
    input.sort(reverse=True)
    output_size = 0
    result_list = []
    if len(input) > k:
        output_size = k
    else:
        output_size = len(input)-1
    for i in range(output_size):
        result_list.append(input[i])
    print(result_list)


def main_heap_queue(input, k):
    priority_queue = []
    heapq.heapify(priority_queue)
    for i in range(len(input)):
        #Insert into the queue
        heapq.heappush(priority_queue, input[i])
        if (len(priority_queue) > k):
            heapq.heappop(priority_queue)
    while(len(priority_queue) != 0):
        print(heapq.heappop(priority_queue), end=' ')
    print()

if __name__ == '__main__':
    main([1, 23, 12, 9, 30, 2, 50], 3)
    main_heap_queue([1, 23, 12, 9, 30, 2, 50], 3)
