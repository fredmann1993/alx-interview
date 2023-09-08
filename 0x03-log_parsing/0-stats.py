#!/usr/bin/python3

''' 
log parser
'''

from collections import defaultdict

def print_statistics(file_sizes, status_codes):
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")

    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        print(f"{code}: {status_codes[code]}")

def main():
    file_sizes = []
    status_codes = defaultdict(int)
    line_count = 0

    try:
        while True:
            try:
                line = input().strip()
            except EOFError:
                break

            parts = line.split()
            if len(parts) != 10:
                continue

            ip, _, _, method, path, _, status_code, size, *_ = parts
            if method != "GET" or not path.startswith("/projects/") or not status_code.isdigit():
                continue

            file_sizes.append(int(size))
            status_codes[int(status_code)] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(file_sizes, status_codes)
                print()

    except KeyboardInterrupt:
        pass

    if line_count > 0:
        print_statistics(file_sizes, status_codes)

if __name__ == "__main__":
    main()

