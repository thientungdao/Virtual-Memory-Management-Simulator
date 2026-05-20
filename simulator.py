# simulator.py
# This module defines the Simulator class, which orchestrates the page replacement simulation. 
# It manages the memory, processes page requests, and tracks performance metrics using the Stats class. 
# The Simulator handles page hits, page faults, and page replacements according to the specified replacement policy, 
# and provides detailed output of the simulation process when verbose mode is enabled.
from typing import List

from memory import Memory
from process import Process
from replacement import ReplacementAlgorithm
from stats import Stats


class Simulator:
    def __init__(
        self,
        num_frames: int,
        replacement_policy: ReplacementAlgorithm,
        verbose: bool = True,
    ) -> None:
        self.memory = Memory(num_frames) # Initialize memory with the specified number of frames
        self.policy = replacement_policy # Set the replacement policy to be used in the simulation
        self.stats = Stats() # Initialize statistics tracking for the simulation
        self.process = Process(pid=1) # Create a single process with PID 1 for the simulation
        self.time = 0 # Initialize a time counter to track the order of page requests and usage
        self.verbose = verbose # Set verbose mode to control detailed output during the simulation

    def handle_request(self, page: int, requests: List[int], request_index: int) -> None:
        frame_index = self.memory.find_page(page)

        if frame_index is not None:
            self.stats.record_hit() # Record a hit in the statistics
            self.memory.frames[frame_index].last_used = self.time # Update last used time for LRU

            if self.verbose:
                print(f"Request {page}: HIT")
                self.memory.display()
                print()

            return

        self.stats.record_fault() # Record a page fault in the statistics

        # If verbose mode is enabled, print a message indicating that a page fault has occurred for the requested page.
        if self.verbose:
            print(f"Request {page}: PAGE FAULT")

        free_index = self.memory.find_free_frame()

        # If a free frame is available, load the requested page into the free frame and update the process's page table accordingly.
        if free_index is not None:
            self.memory.load_page(free_index, page, self.time)
            self.process.map_page(page, free_index)

            if self.verbose:
                print(f"Loaded page {page} into free frame {free_index}")
        else:
            victim_index = self.policy.select_victim(
                self.memory.frames,
                current_index=request_index,
                future_requests=requests,
                current_time=self.time,
            )

            victim_page = self.memory.frames[victim_index].page # Get the page number of the victim frame before replacement
            if victim_page is not None:
                self.process.unmap_page(victim_page) # Unmap the victim page from the process's page table before replacement

            self.memory.load_page(victim_index, page, self.time) # Load the new page into the selected victim frame
            self.process.map_page(page, victim_index) # Map the new page to the frame in the process's page table
            self.stats.replacements += 1 # Increment the replacement count in the statistics

            if self.verbose:
                print(
                    f"Replaced page {victim_page} in frame {victim_index} with page {page}"
                )

        if self.verbose:
            self.memory.display()
            print()

    # The run method processes a list of page requests sequentially, handling each request using the handle_request method and updating the simulation state accordingly.
    def run(self, requests: List[int]) -> None:
        for request_index, page in enumerate(requests):
            self.handle_request(page, requests, request_index) # Handle each page request and update the simulation state accordingly
            self.time += 1 # Increment the time counter after each request to track the order of page accesses

    # The print_results method outputs a summary of the simulation results, including total requests, hits, page faults, replacements, 
    # hit rate, and fault rate, as well as the final state of the memory frames and the process's page table.
    def print_results(self) -> None:
        print(self.stats.summary()) # Print a summary of the simulation results, including total requests, hits, page faults, replacements, hit rate, and fault rate
        print(f"Replacement Policy: {self.policy.name}") # Print the name of the replacement policy used in the simulation
        print("Final Frames:", self.memory.snapshot()) # Print the final state of the memory frames after the simulation
        print("Page Table:", self.process.page_table) # Print the page table mapping of the process