# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

info_time = "time"
info_perf_counter = "perf_counter"
info_monotonic = "monotonic"
info_process_time = "process_time"
info_thread_time = "thread_time"

print("Information about time.time method: \n", time.get_clock_info(
    info_time))
print("-" * 80)
print("Information about time.perf_counter method: \n", time.get_clock_info(
    info_perf_counter))
print("-" * 80)
print("Information about time.monotonic method: \n", time.get_clock_info(
    info_monotonic))
print("-" * 80)
print("Information about time.process_time method: \n", time.get_clock_info(
    info_process_time))
print("-" * 80)
print("Information about time.thread_time method: \n", time.get_clock_info(
    info_thread_time))

# adjustable=True means the clock changes with daylight saving time
# adjustable=False means the clock doesn't change with daylight saving

# Tim's output and mine were different because he was using a Mac, and I
# am using Windows 10