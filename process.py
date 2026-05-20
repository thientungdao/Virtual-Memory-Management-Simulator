# process.py
# This module defines the Process class, which represents a process in the page replacement simulation.
# Each process has a unique PID and a page table that maps virtual pages to physical frame indices. 
# The Process class provides methods to map and unmap pages in the page table.
from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Process:
    pid: int
    page_table: Dict[int, Optional[int]] = field(default_factory=dict)

    def map_page(self, page: int, frame_index: int) -> None:
        self.page_table[page] = frame_index

    def unmap_page(self, page: int) -> None:
        if page in self.page_table:
            self.page_table[page] = None