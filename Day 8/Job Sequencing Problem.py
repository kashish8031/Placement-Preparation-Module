# Job Sequencing Problem
# Medium

# Companies:
# Tekion-corp
# Walmart
# Microsoft
# Flipkart
# Google
# Amazon
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi


# Given a set of N jobs where each jobi has a deadline and profit associated with it.

# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

# Find the number of jobs done and the maximum profit.

# Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


# Example 1:

# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).
# Example 2:

# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).

# Your Task :
# You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit as a list or vector of 2 elements.


# Expected Time Complexity: O(NlogN)
# Expected Auxilliary Space: O(N)


# Constraints:
# 1 <= N <= 105
# 1 <= Deadline <= N
# 1 <= Profit <= 500

class Solution:
    def cmp(a, b):
        return a.profit > b.profit

    def JobScheduling(self, arr, n):
        arr.sort(key=lambda x: x.profit, reverse=True)

        mx = arr[0].dead
        for i in range(n):
            mx = max(mx, arr[i].dead)

        slot = [-1] * (mx + 1)
        mxprofit = 0
        count = 0
        for i in range(n):
            for j in range(arr[i].dead, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    mxprofit += arr[i].profit
                    count += 1
                    break

        ans = []
        ans.append(count)
        ans.append(mxprofit)
        return ans

    # time complexity: O(n^2)
    # space complexity: O(n)