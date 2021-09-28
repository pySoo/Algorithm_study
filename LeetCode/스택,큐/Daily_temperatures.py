def dailyTemperatures(self, T):
    answer = [] * len(T)
    stack = []
    for i, cur in enumerate(T):
    	# 과거 온도보다 높을 때
    	while stack and cur > T[stack[-1]]:
        	last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer
