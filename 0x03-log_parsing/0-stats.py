#!/usr/bin/python3

"""A Script that reads stdin line by line and computes metrics"""

import sys

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip, dash, date, method, url, protocol, status, size = parts[:8]
        try:
            size = int(size)
            status = int(status)
            total_size += size
            if status in status_counts:
                status_counts[status] += 1
        except ValueError:
            continue
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)

print_stats(total_size, status_counts)