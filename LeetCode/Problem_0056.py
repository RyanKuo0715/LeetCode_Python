# LeetCode Problem 56: Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merge_list = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= temp[1]:
                if intervals[i][1] > temp[1]:
                    temp[1] = intervals[i][1]
            elif intervals[i][0] > temp[1]:
                merge_list.append(temp)
                temp = intervals[i]
        merge_list.append(temp)
        return merge_list

        # merge_dict = defaultdict(lambda: None)
        # merge_list = []
        # min_max = [float('inf'), float('-inf')]
        # for interval in intervals:
        #     for i in range(interval[0]*2, interval[1]*2+1):
        #         merge_dict[i/2]
        #         if i/2 < min_max[0]:
        #             min_max[0] = i/2
        #         if i/2 > min_max[1]:
        #             min_max[1] = i/2
        # temp = temp_min = min_max[0]
        # for key in sorted(merge_dict):
        #     if key - temp > 0.5:
        #         merge_list.append([int(temp_min), int(temp)])
        #         temp_min = key
        #     temp = key
        # merge_list.append([int(temp_min), int(min_max[1])])
        # return merge_list
