import time
import logging

logging.basicConfig(level=logging.INFO)

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@execution_time
def expensive_task(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

# Example usage:
print(expensive_task(1000000))  # Should log execution time
