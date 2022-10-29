from time
import sleep
print("I'm executing")
try:
print("Wake up Ctrl-C!")
sleep(600)
except KeyboardInterrupt:
    print("I woke up!")
else:
    print("I'm executing again.")
