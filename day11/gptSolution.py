from collections import defaultdict


def apply_transformation(stone):
    # Rule 1: If the stone is engraved with the number 0, it becomes 1.
    if stone == 0:
        return [1]

    # Rule 2: If the stone has an even number of digits, split it into two stones.
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        half_len = len(stone_str) // 2
        left = int(stone_str[:half_len])
        right = int(stone_str[half_len:])
        return [left, right]

    # Rule 3: Otherwise, the stone is replaced by a new stone multiplied by 2024.
    return [stone * 2024]


def simulate_blinks(initial_stones, num_blinks):
    # Use a dictionary to count occurrences of each stone
    stone_count = defaultdict(int)

    # Initialize the count dictionary with the initial stones
    for stone in initial_stones:
        stone_count[stone] += 1

    # Simulate the blinking process
    for _ in range(num_blinks):
        new_stone_count = defaultdict(int)

        # For each stone in the current count dictionary, apply transformations
        for stone, count in stone_count.items():
            next_stones = apply_transformation(stone)
            for next_stone in next_stones:
                new_stone_count[next_stone] += count

        # Update the stone count dictionary
        stone_count = new_stone_count

    # Total number of stones after all blinks
    total_stones = sum(stone_count.values())
    return total_stones


# Example usage:
initial_stones = [125, 17]
num_blinks = 75
result = simulate_blinks(initial_stones, num_blinks)
print(result)
