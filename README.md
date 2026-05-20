# Virtual Memory Management Simulator

This project is a Python simulator for virtual memory page replacement. It models how an operating system handles page requests, page hits, page faults, and page replacement when physical memory is full.

The simulator supports three page replacement algorithms:

- **FIFO**: First-In, First-Out
- **LRU**: Least Recently Used
- **Optimal**: Replaces the page used farthest in the future

## Project Structure

```text
.
├── config.py          # Stores simulator settings
├── main.py            # Main program entry point
├── memory.py          # Defines memory frames and memory operations
├── process.py         # Defines the process and page table
├── replacement.py     # Contains FIFO, LRU, and Optimal algorithms
├── simulator.py       # Runs the simulation logic
├── stats.py           # Tracks hits, page faults, replacements, and rates
├── trace.py           # Loads page requests from the input file
├── random_input.py    # Generates a random input trace for testing
└── input/
    └── trace.txt      # Page request input file
```

## Requirements

This project only uses standard Python libraries.

Recommended version:

```bash
python3 --version
```

Use Python 3.8 or newer.

## How to Run the Simulator

### 1. Create the input folder

If the `input` folder does not already exist, create it:

```bash
mkdir input
```

### 2. Create a trace file

Create a file named `trace.txt` inside the `input` folder:

```text
input/trace.txt
```

The trace file should contain page numbers. Each number represents one page request.

Example:

```text
1 2 3 4 1 2 5 1 2 3 4 5
```

You may also write one page request per line:

```text
1
2
3
4
1
2
5
```

Blank lines and lines starting with `#` are ignored.

### 3. Configure the simulator

Open `config.py`:

```python
NUM_FRAMES = 3
PAGE_SIZE = 4096
INPUT_FILE = "input/trace.txt"
REPLACEMENT_ALGORITHMS = "Optimal", "LRU", "FIFO"
VERBOSE = True
```

Explanation:

- `NUM_FRAMES`: Number of physical memory frames.
- `PAGE_SIZE`: Page size in bytes. It is included for realism and future extension.
- `INPUT_FILE`: Path to the trace file.
- `REPLACEMENT_ALGORITHMS`: Algorithms available in the simulator.
- `VERBOSE`: If `True`, the simulator prints each step.

### 4. Choose a replacement algorithm

Open `main.py` and find this line:

```python
policy = get_algorithm(REPLACEMENT_ALGORITHMS[2])
```

Change the index to select a different algorithm:

```python
REPLACEMENT_ALGORITHMS[0]  # Optimal
REPLACEMENT_ALGORITHMS[1]  # LRU
REPLACEMENT_ALGORITHMS[2]  # FIFO
```

For example, to run LRU:

```python
policy = get_algorithm(REPLACEMENT_ALGORITHMS[1])
```

### 5. Run the program

In the terminal, run:

```bash
python3 main.py
```

or:

```bash
python main.py
```

## Example Output

The program prints the input file, number of frames, selected policy, page requests, step-by-step simulation output, and final results.

Example summary:

```text
--- Simulation Results ---
Total Requests: 100
Hits: 6
Page Faults: 94
Replacements: 91
Hit Rate: 6.00%
Fault Rate: 94.00%

Replacement Policy: FIFO
Final Frames: ['13', '16', '11']
Page Table: {...}
```

## Generate a Random Trace File

You can use `random_input.py` to generate a random trace file automatically.

Run:

```bash
python3 random_input.py
```

By default, it generates 100 page requests with page numbers between 0 and 50.

You can change these values in `random_input.py`:

```python
generate_random_trace(INPUT_FILE, num_requests=100, max_page=50)
```

## How the Simulator Works

For each page request:

1. The simulator checks whether the page is already in memory.
2. If the page is found, it records a page hit.
3. If the page is not found, it records a page fault.
4. If a free frame exists, the page is loaded into the free frame.
5. If memory is full, the selected replacement algorithm chooses a victim frame.
6. The old page is removed, the new page is loaded, and statistics are updated.

## Algorithms

### FIFO

FIFO replaces the page that has been in memory the longest.

It uses each frame's `loaded_time` value to choose the oldest loaded page.

### LRU

LRU replaces the page that has not been used for the longest time.

It uses each frame's `last_used` value to choose the least recently used page.

### Optimal

Optimal replaces the page that will not be used for the longest time in the future.

It looks ahead in the future request list. This usually gives the best result, but it is not practical in a real operating system because the OS does not know future requests.

## Results Produced

The simulator reports:

- Total requests
- Hits
- Page faults
- Replacements
- Hit rate
- Fault rate
- Final memory frames
- Final page table

## Troubleshooting

### Trace file not found

Make sure this file exists:

```text
input/trace.txt
```

Also check that `INPUT_FILE` in `config.py` matches the correct path.

### Trace file is empty

Add page numbers to `input/trace.txt`.

### Invalid token error

The trace file should contain only integers, blank lines, or comment lines starting with `#`.

Correct:

```text
1 2 3 4
# this is a comment
5 6 7
```

Incorrect:

```text
page1 page2 page3
```

## Possible Future Improvements

Possible extensions include:

- Automatically compare FIFO, LRU, and Optimal in one run
- Add more algorithms such as Clock or Second Chance
- Support multiple processes
- Simulate TLB behavior
- Simulate dirty bits and disk I/O
- Convert virtual addresses into page numbers using `PAGE_SIZE`

## Author

Thien Tung Dao
Generated by ChatGPT 5.5