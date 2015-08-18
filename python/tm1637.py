import time, signal
import pyupm_tm1637 as tm1637

# Register exit handler for normal Ctrl+C exit
def SIGINTHandler(signum, frame):
    raise SystemExit
signal.signal(signal.SIGINT, SIGINTHandler)

# Create a display object on pins 0 CLK and 1 DIO
display = tm1637.TM1637(0, 1)
dots = True

# Get local time
myTime = time.localtime(time.time())
print time.strftime("System time: %H:%M", myTime)
print ("You can adjust your time zone by setting the TZ environment variable.")

# Draw a box for 3 seconds using 7-segment encoding
display.write(0x39, 0x09, 0x09, 0x0f)
time.sleep(3)

# Loop indefinitely
while True:
    # Update and display time
    timeString = time.strftime("%H%M", time.localtime(time.time()))
    display.write(timeString)
    # Toggle colon
    display.setColon(dots)
    dots = not dots

    # Sleep for 1 s
    time.sleep(1)