# main.py
# This is the main entry point for the virtual memory simulator. It loads the page request trace, 
# initializes the simulator with the specified configuration, and runs the simulation while printing the results.
from config import INPUT_FILE, NUM_FRAMES, REPLACEMENT_ALGORITHMS, VERBOSE
from replacement import get_algorithm
from simulator import Simulator
from trace import load_trace


def main() -> None:
    requests = load_trace(INPUT_FILE)
    policy = get_algorithm(REPLACEMENT_ALGORITHMS[2]) # [0] for Optimal, [1] for LRU, [2] for FIFO

    print("--- Virtual Memory Simulator ---")
    print(f"Input File: {INPUT_FILE}")
    print(f"Frames: {NUM_FRAMES}")
    print(f"Policy: {policy.name}")
    #print(f"Requests: {requests}")
    print()

    simulator = Simulator(
        num_frames=NUM_FRAMES,
        replacement_policy=policy,
        verbose=VERBOSE,
    )
    simulator.run(requests)
    simulator.print_results()


if __name__ == "__main__":
    main()