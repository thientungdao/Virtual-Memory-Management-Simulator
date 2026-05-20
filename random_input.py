# random_input.py
# This module generates a random trace file containing page requests for testing the virtual memory simulator.
import random
from config import INPUT_FILE
def generate_random_trace(file_path: str, num_requests: int, max_page: int) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        for _ in range(num_requests):
            page = random.randint(0, max_page)
            file.write(f"{page}\n")

if __name__ == "__main__":
    generate_random_trace(INPUT_FILE, num_requests=1000, max_page=50)