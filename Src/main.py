from machine import Pin, ADC # import the Pin & ADC modules from the machine library
from utime import sleep # import the sleep module from the utime library

# method: setup
def setup():
    # global variable
    global Sensor, Led1, Led2, Led3, Led4, Led5, Led6, Led7, Led8, Led9, Value
    
    # variable initialization
    Sensor = ADC(26) # sensor using analog pins as input
    Led1 = Pin(2, Pin.OUT) # led 1 using GP2 pin as output
    Led2 = Pin(3, Pin.OUT) # led 2 using GP3 pin as output
    Led3 = Pin(4, Pin.OUT) # led 3 using GP4 pin as output
    Led4 = Pin(6, Pin.OUT) # led 4 using GP6 pin as output
    Led5 = Pin(7, Pin.OUT) # led 5 using GP7 pin as output
    Led6 = Pin(8, Pin.OUT) # led 6 using GP8 pin as output
    Led7 = Pin(10, Pin.OUT) # led 7 using GP10 pin as output
    Led8 = Pin(11, Pin.OUT) # led 8 using GP11 pin as output
    Led9 = Pin(12, Pin.OUT) # led 9 using GP12 pin as output

# method: loop
def loop():
    while True:
        Value = Sensor.read_u16() # reads the adc value from the sensor
        print(Value) # print the adc value from the sensor
        
        if Value >= 55000: # if the adc value is greater than 55000 then:
            Led1.high() # led 1 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 50000: # if the adc value is greater than 50000 then:
            Led2.high() # led 2 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 45000: # if the adc value is greater than 45000 then:
            Led3.high() # led 3 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 40000: # if the adc value is greater than 40000 then:
            Led4.high() # led 4 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 35000: # if the adc value is greater than 35000 then:
            Led5.high() # led 5 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 30000: # if the adc value is greater than 30000 then:
            Led6.high() # led 6 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 25000: # if the adc value is greater than 25000 then:
            Led7.high() # led 7 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 20000: # if the adc value is greater than 20000 then:
            Led8.high() # led 8 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off
        elif Value >= 15000: # if the adc value is greater than 15000 then:
            Led9.high() # led 9 on
            sleep(0.1) # delay 0,1 second
            all_off() # all leds turned off

# method: all_off
def all_off():
    Led1.low()
    Led2.low()
    Led3.low()
    Led4.low()
    Led5.low()
    Led6.low()
    Led7.low()
    Led8.low()
    Led9.low()

# main method
if __name__ == '__main__':
    try:
        setup() # calling the setup() method
        loop() # calling the loop() method
          
    except error:
        all_off() # all leds turned off
