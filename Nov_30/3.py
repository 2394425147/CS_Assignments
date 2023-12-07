from collections import deque


def hanoi(stack_size: int, max_iteration: int = 1_000_000) -> bool:
    stacks = [deque([stack_size - i for i in range(stack_size)]), 
              deque(),
              deque()]

    iteration = 0
    source = 0
    target = 2 if stack_size % 2 == 1 else 1

    pointer_increment = 1 if stack_size % 2 == 1 else 2

    while len(stacks[2]) != stack_size and iteration <= max_iteration:
        iteration += 1

        source_value = stacks[source][-1] if len(stacks[source]) > 0 else (stack_size + 1)
        target_value = stacks[target][-1] if len(stacks[target]) > 0 else (stack_size + 1)

        if source_value > target_value:
            source, target = target, source

        disk_moved = stacks[source].pop()
        stacks[target].append(disk_moved)

        print(f"\nStep {iteration} =======================")
        print(f"[{source}] -- {disk_moved} -> [{target}]")
        print("[0]", stacks[0], sep="\t")
        print("[1]", stacks[1], sep="\t")
        print("[2]", stacks[2], sep="\t")

        source = (source + pointer_increment) % 3
        target = (target + pointer_increment) % 3

    if len(stacks[2]) != stack_size:
        return False

    return True


def main():
    while True:
        rawNumber = input("请输入一个数字 (输入0g结束): ")
        if not rawNumber.removeprefix("-").isdigit():
            print("输入的不是数字，请重新输入")
            continue
        number = int(rawNumber)
        if number <= 0:
            break
        print(hanoi(number))


if __name__ == "__main__":
    main()
