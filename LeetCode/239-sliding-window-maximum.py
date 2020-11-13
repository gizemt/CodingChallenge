''' Leetcode 239: sliding-window-maximum
# Question  : You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

# Link      : https://leetcode.com/problems/sliding-window-maximum/
# Runtime   : 1376 ms   - 63%
# Memory    : 30.6 MB - 13%
'''

class Solution:
    def maxSlidingWindow(self, sequence: List[int], m: int) -> List[int]:
        # Naive solution (O(N*m))
        # return [max(sequence[i:i+m]) for i in range(len(sequence)-m+1)]
        # O(n) solution
        maximums = []
        deque = [0]
        max_idx = 0
        if m == 1:
            return sequence
        for i in range(1, len(sequence)):
            if i >= (deque[max_idx] + m):
                max_idx += 1
            if (sequence[i] >= sequence[deque[max_idx]]):
                deque = [i]
                max_idx = 0
            else:
                while sequence[deque[-1]] <= sequence[i] and len(deque)-max_idx>0:
                    deque.pop()
                deque.append(i)
            if i >= m-1:
                maximums.append(sequence[deque[max_idx]])
        return maximums
    
        maximums = [max(sequence[:m])]
        for i in range(m, len(sequence)):
            maximums.append()