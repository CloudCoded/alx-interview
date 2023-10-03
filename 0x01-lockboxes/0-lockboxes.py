#!/usr/bin/python3

def canUnlockAll(boxes):
    # Initialize a list to keep track of the visited boxes.
    visited = [False] * len(boxes)
    visited[0] = True  # Start with the first box unlocked.

    # Initialize a queue for BFS, starting with the first box.
    queue = [0]

    # Perform BFS to check if all boxes can be opened.
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited (unlocked).
    return all(visited)

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True
