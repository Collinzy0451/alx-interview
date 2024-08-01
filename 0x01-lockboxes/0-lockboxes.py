#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            # Add keys from the current box to the stack if they lead to unvisited boxes
            for key in boxes[box]:
                if key < n and key not in visited:
                    stack.append(key)
                    
    # If all boxes have been visited, return True; otherwise, return False
    return len(visited) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

