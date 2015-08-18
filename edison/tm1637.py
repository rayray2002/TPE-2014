import time, signal
import pyupm_tm1637 as tm1637

display = tm1637.TM1637(4, 5)

while True:
    display.write("123"")