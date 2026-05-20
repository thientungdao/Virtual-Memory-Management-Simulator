# replacement.py
# Generate by ChatGPT Thinking 5.4 on 2026-05-03
# This module defines the base class for page replacement algorithms. 
# Each specific algorithm (e.g., LRU, FIFO, Optimal) will inherit from this base class and 
# implement the select_victim method to determine which page to replace when a page fault occurs.

from abc import ABC, abstractmethod
from typing import List, Optional
from memory import Frame, Memory


class ReplacementAlgorithm(ABC):
    @abstractmethod
    def select_victim(
        self, 
        frames: List[Frame], # The current state of the memory frames
        current_index: Optional[int] = None, # The index of the current page being accessed (if applicable)
        future_requests: Optional[List[int]] = None, # The list of future page requests (if applicable)
        current_time: Optional[int] = None, # The current time step in the simulation (if applicable)
    ) -> int: # Returns the index of the frame to be replaced
        pass
    
    @property
    def name(self) -> str:
        return self.__class__.__name__

# The LRU (Least Recently Used) algorithm selects the page that has not been used for the longest time.    
class LRU(ReplacementAlgorithm):
    def select_victim(
        self,
        frames: List[Frame],
        current_index: Optional[int] = None,
        future_requests: Optional[List[int]] = None,
        current_time: Optional[int] = None,
    ) -> int:
        return min(range(len(frames)), key=lambda i: frames[i].last_used)
    
# The FIFO (First-In-First-Out) algorithm selects the page that has been in memory the longest.
class FIFO(ReplacementAlgorithm):
    def select_victim(
        self,
        frames: List[Frame],
        current_index: Optional[int] = None,
        future_requests: Optional[List[int]] = None,
        current_time: Optional[int] = None,
    ) -> int:
        return min(range(len(frames)), key=lambda i: frames[i].loaded_time)
    
# The Optimal algorithm selects the page that will not be used for the longest time in the future.
class Optimal(ReplacementAlgorithm):
    def select_victim(
        self,
        frames: List[Frame],
        current_index: Optional[int] = None,
        future_requests: Optional[List[int]] = None,
        current_time: Optional[int] = None,
    ) -> int:
        if future_requests is None or current_index is None:
            raise ValueError("Optimal algorithm requires future_requests and current_index parameters.")
        
        next_use_positions = []
        for frame in frames:
            if frame.page is None:
                next_use_positions.append(float('inf'))  # If the frame is empty, it won't be used again
                continue
            try:
                next_use = future_requests.index(frame.page, current_index + 1)
            except ValueError:
                next_use = float('inf')  # If the page is not found in future requests, it won't be used again
            next_use_positions.append(next_use) # Store the position of the next use for each page in the frames
        return next_use_positions.index(max(next_use_positions)) # The page with the farthest next use is selected for replacement
    
# Factory function to create an instance of the specified replacement algorithm based on its name.
def get_algorithm(name: str) -> ReplacementAlgorithm:
    normalized = name.strip().upper()
    if normalized == "LRU":
        return LRU()
    elif normalized == "FIFO":
        return FIFO()
    elif normalized == "OPTIMAL":
        return Optimal()
    else:
        raise ValueError(f"Unknown replacement algorithm: {name}")