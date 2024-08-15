#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0

def print_stats():
    """Prints the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption signal."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        # Validate the format
        if len(parts) != 9 or parts[3] != '-' or not parts[5].startswith('"GET') or not parts[7].isdigit():
            continue

        # Extract the relevant parts
        file_size = int(parts[8])
        status_code = int(parts[7])

        # Update total file size and status codes count
        total_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
