# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0
    time = 0
    while len(truck_weights):
        time += 1

        total_weight -= bridge.popleft()

        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            total_weight += truck
        else:
            truck = 0

        bridge.append(truck)

    return time + bridge_length


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))
