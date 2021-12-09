import time
from time import perf_counter as my_timer  # perf_counter counts the actual
# amount of time that has passed, ignoring differences in terms of daylight
# saving time and such
import random

# from time import monotonic as my_timer -> monotonic and perf_counter perform
# similar tasks

# from time import process_time as my_timer -> process_time is not very
# adequate for our program because it calculates the amount of time the
# CPU processes a certain task, not the elapsed time

input("Press ENTER to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input("Press ENTER to stop")
end_time = my_timer()

print("You started at the following time: " +
      time.strftime("%X", time.localtime(start_time)))
print("You finished at the following time: " +
      time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was: {}".format(end_time - start_time))