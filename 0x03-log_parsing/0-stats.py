#!/usr/bin/python3
"""
log parsing
"""
import sys
import signal


def print_metrics(total_size, status_counts):
    """ metrics """
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


def process_line(line, total_size, status_counts):
    """ print each line """
    parts = line.split()
    if len(parts) >= 9 and parts[8].isdigit():
        file_size = int(parts[8])
        total_size += file_size

        status_code = parts[7]
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                status_counts[status_code] += 1

    return total_size, status_counts


def main():
    """ main func """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                     500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_counts = process_line(line, total_size,
                                                     status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
