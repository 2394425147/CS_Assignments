import math

def is_prime_brute_force(number: int) -> bool:
    if number <= 1:
        return False

    evaluator = 2

    while evaluator < number:
        if number % evaluator == 0 == 0:
            return False
        
        evaluator += 1

    return True

def is_prime_sqrt_optimized(number: int) -> bool:
    if number <= 1:
        return False

    evaluator = 2
    number_sqrt = math.sqrt(number)

    while evaluator <= number_sqrt:
        if number % evaluator == 0 == 0:
            return False
        
        evaluator += 1

    return True

def is_prime_theorem_optimized(number: int) -> bool:
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    # 大于3的所有素数都能表达为6k+/-1 (k为整数)
    evaluator = 5
    number_sqrt = math.sqrt(number)

    while evaluator <= number_sqrt:
        if number % evaluator == 0 or number % (evaluator + 2) == 0:
            return False
        
        evaluator += 6

    return True

prime_cache = []

def is_prime_cache_optimized(number: int) -> bool:
    global prime_cache

    if number in prime_cache:
        return True

    if number <= 1:
        return False

    if number == 2 or number == 3:
        prime_cache.append(number)
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    evaluator = 5
    prime_index = 0
    number_sqrt = math.sqrt(number)

    while evaluator <= number_sqrt:
        if number % evaluator == 0:
            return False

        if len(prime_cache) > 0 and evaluator <= prime_cache[-2]:
            prime_index += 1
            evaluator = prime_cache[prime_index]
        else:
            evaluator += 1

    prime_cache.append(number)
    return True



def benchmark(prime_validator):
    import time
    stub_numbers_light = [i for i in range(1, 1_000)]
    stub_numbers_medium = [i for i in range(1, 100_000)]
    print("上限", f"计算时间", sep="\t")
    time_start = time.perf_counter()
    for number in stub_numbers_light:
        prime_validator(number)
    time_end = time.perf_counter()
    print("1K", f"{(time_end - time_start):.6f}秒", sep="\t")
    time_start = time.perf_counter()
    for number in stub_numbers_medium:
        prime_validator(number)
    time_end = time.perf_counter()
    print("1M", f"{(time_end - time_start):.6f}秒", sep="\t")


print("\nBrute-force: ")
benchmark(is_prime_brute_force)

print("\nSquare-root optimized: ")
benchmark(is_prime_sqrt_optimized)

print("\nCached: ")
benchmark(is_prime_cache_optimized)

print("\n6+/-1 Theorem optimized: ")
benchmark(is_prime_theorem_optimized)
