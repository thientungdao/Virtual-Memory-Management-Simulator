# config.py

NUM_FRAMES = 10
PAGE_SIZE = 4096 # Not used in the current implementation, but can be useful for future extensions (e.g., simulating different page sizes)
INPUT_FILE = "input/trace.txt"

# Replacement algorithms
REPLACEMENT_ALGORITHMS = "Optimal", "LRU", "FIFO" # You can change the index in main.py to select a different algorithm

#Show step by step simulation output
VERBOSE = False