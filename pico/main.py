
from utime import sleep
from time import ticks_ms, ticks_diff
from dht import DHT11
from machine import Pin

d = DHT11(machine.Pin(4)) # the dht pin is connected to GPIO 4
start_time = ticks_ms()       # board boot time
led = Pin(25, Pin.OUT)        # led pin
led.on()
while True:
    try:
        # measure temperature, humidity and time
        d.measure()
        temp = d.temperature()
        hum  = d.humidity()
        elapsed = int(ticks_diff(ticks_ms(), start_time)/1000) # time in seconds since boot

        print(f"{elapsed}s, {temp}, {hum}")

        # write the data to flash memory
        with open("data.csv", "a") as f:
            f.write(f"{elapsed}, {temp}, {hum}\n")

        sleep(60)
    except KeyboardInterrupt:
        break
led.off()
print("Finished.")
