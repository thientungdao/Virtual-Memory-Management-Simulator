# trace.py
# This module defines the load_trace function, which reads a trace file 
# containing page requests and returns a list of page numbers.
from typing import List


def load_trace(file_path: str) -> List[int]:
    requests: List[int] = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                stripped = line.strip()

                if not stripped or stripped.startswith("#"):
                    continue

                parts = stripped.split()
                for part in parts:
                    try:
                        requests.append(int(part))
                    except ValueError as exc:
                        raise ValueError(
                            f"Invalid token '{part}' in {file_path} at line {line_number}"
                        ) from exc
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Trace file not found: {file_path}") from exc

    if not requests:
        raise ValueError("Trace file is empty")

    return requests