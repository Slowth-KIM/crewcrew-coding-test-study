from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_queue1, sum_queue2 = sum(queue1), sum(queue2)

    for _ in range(3 * len(queue1)):
        if sum_queue1 > sum_queue2:
            sum_queue1 -= queue1[0]
            sum_queue2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum_queue1 < sum_queue2:
            sum_queue1 += queue2[0]
            sum_queue2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer

        answer += 1

    return -1