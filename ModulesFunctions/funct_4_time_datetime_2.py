import time
from time import time as my_timer
# time.time() function returns the number of seconds passed since epoch.
import random

input("Press ENTER to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)  # The program will sleep for X amount of seconds.
start_time = my_timer()  # Only then, after the program wakes up, does
# start_time start functioning

# start_time = time.localtime().tm_sec

input("Press ENTER to stop")
end_time = my_timer()  # Right after the user presses ENTER again, end_time
# is called

# end_time = time.localtime().tm_sec

print("You started at the following time: " +
      time.strftime("%X", time.localtime(start_time)))
print("You finished at the following time: " +
      time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was: {}".format(end_time - start_time))
# Calculates the difference between end_time and start_time