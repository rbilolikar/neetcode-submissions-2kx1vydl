class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #insert into stack based on decreasing values.
        #Decreasing Monotonic Stack
        #Store indices in stack
        # while stack and ( temp < stack[-1]):
        #tempList = stack.pop() 
        # insert temp and then append tempList
        # Calculate differences for output array
        stack = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and ( temp > temperatures[stack[-1]]):
                idx = stack.pop()
                output[idx] = i - idx
            stack.append(i)
        return output
