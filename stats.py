# stats.py
# This module defines the Stats class, which is responsible for 
# tracking the performance metrics of the page replacement simulation.

from dataclasses import dataclass
# This module defines the Stats class, which is responsible for 
# tracking the performance metrics of the page replacement simulation.
# It keeps track of the total number of page requests, hits, page faults, 
# and replacements, and provides methods to record hits and faults, as well as calculate hit and fault rates.
@dataclass
class Stats:
    total_requests: int = 0
    hits: int = 0
    page_faults: int = 0
    replacements: int = 0

    def record_hit(self) -> None:
        self.total_requests += 1
        self.hits += 1

    def record_fault(self) -> None:
        self.total_requests += 1
        self.page_faults += 1

    @property
    def hit_rate(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return self.hits / self.total_requests

    @property
    def fault_rate(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return self.page_faults / self.total_requests

    def summary(self) -> str:
        return (
            "\n--- Simulation Results ---\n"
            f"Total Requests: {self.total_requests}\n"
            f"Hits: {self.hits}\n"
            f"Page Faults: {self.page_faults}\n"
            f"Replacements: {self.replacements}\n"
            f"Hit Rate: {self.hit_rate:.2%}\n"
            f"Fault Rate: {self.fault_rate:.2%}\n"
        )