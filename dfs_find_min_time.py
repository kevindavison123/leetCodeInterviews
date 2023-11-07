from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Setup our time relationship with each class
        # Add time based on max of each level
        # graph: next, value,
        # for each set, if second value is not N, add the time to list, max list, add max and return overall
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            graph[prev - 1].append(next - 1)
        memo = [-1] * n

        def calculateTime(course):
            if memo[course] != -1:
                return memo[course]

            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            max_preq_time = 0
            for prereq in graph[course]:
                max_preq_time = max(max_preq_time, calculateTime(prereq))

            memo[course] = max_preq_time + time[course]
            return memo[course]

        min_time = 0
        for course in range(n):
            min_time = max(min_time, calculateTime(course))

        return min_time


