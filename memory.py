from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Frame:
    page: Optional[int] = None # The page currently loaded in the frame (None if empty)
    valid: bool = False # Indicates if the frame is currently holding a valid page
    last_used: int = -1 # Time when the page was last accessed
    loaded_time: int = -1 # Time when the page was loaded into the frame

class Memory:
    # Initializes the memory with a specified number of frames.
    def __init__(self, num_frames: int):
        if num_frames <= 0:
            raise ValueError("Number of frames must be greater than zero.")
        self.frames: List[Frame] = [Frame() for _ in range(num_frames)]
    
    # Finds the index of the frame containing the specified page, or None if not found.
    def find_page(self, page: int) -> Optional[int]:
        for index, frame in enumerate(self.frames):
            if frame.valid and frame.page == page:
                return index
        return None
    
    # Finds the index of the first free frame, or None if all frames are occupied.
    def find_free_frame(self) -> Optional[int]:
        for index, frame in enumerate(self.frames):
            if not frame.valid:
                return index
        return None

    # Loads a page into the specified frame at the given time.
    def load_page(self, frame_index: int, page: int, time: int) -> None:
        self.frames[frame_index].page = page # Set the page number in the frame
        self.frames[frame_index].valid = True # Mark the frame as valid since it now contains a page
        self.frames[frame_index].last_used = time # Set last used time to the current time when the page is loaded
        self.frames[frame_index].loaded_time = time # Set loaded time to the current time when the page is loaded

    # Updates the last used time for the page in the specified frame.
    def update_last_used(self, frame_index: int, time: int) -> None:
        self.frames[frame_index].last_used = time # Set last used time to the current time when the page is accessed
    
    # Creates a snapshot of the current state of the memory frames, showing the page numbers or "-" for empty frames.
    def snapshot(self) -> List[str]:
        result: List[str] = []
        for frame in self.frames:
            result.append(str(frame.page) if frame.valid else "-")
        return result
    
    # Displays the current state of the memory frames.
    def display(self) -> None:
        print("Frame:", self.snapshot())