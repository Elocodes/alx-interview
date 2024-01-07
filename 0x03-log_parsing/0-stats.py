#!/usr/bin/python3

import sys

totalfile_size = 0
status_dict = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        try:
            items = line.split()
            ip_addr = items[0]
            date = items[3][1:-1]
            status_code = int(items[8])
            file_size = int(items[9])

            totalfile_size += file_size
            # keep track of how many times each status cod eappears
            status_dict[status_code] = status_dict.get(status_code, 0) + 1
            # print output afetr 10 lines
            if i % 10 == 0: #len(status_dict) == 10:
                print ("File size: {}".format(totalfile_size))
                for k, v in sorted(status_dict.items()):
                    print("{}: {}".format(k, v))
                #status_dict.clear()
                sys.stdout.flush()
        except (IndexError, ValueError):
            line.strip()
except KeyboardInterrupt:
    # print statistics if ctrl c is pressed
    print ("File size: {}".format(totalfile_size))
    for k, v in sorted(status_dict.items()):
        print("{}: {}".format(k, v))
    sys.exit(0)
