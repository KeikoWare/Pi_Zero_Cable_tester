'''
A library that allows simple access to 74HC595 shift registers on a Raspberry Pi using any digital I/O pins.
Credit to https://github.com/mignev/shiftpi/blob/master/shiftpi.py
'''
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

version = "0.1"
version_info = (0, 1)

# Define MODES
ALL  = -1
HIGH = 1
LOW  = 0

# Define pins
_DATA_pin   = 4    #pin 14 on the 75HC595
_CLOCK_pin  = 17    #pin 12 on the 75HC595
_LATCH_pin  = 27    #pin 11 on the 75HC595

_DB_1 = 5
_DB_2 = 6
_DB_3 = 12
_DB_4 = 13
_DB_5 = 19
_DB_6 = 16
_DB_7 = 26
_DB_8 = 20
_DB_9 = 21
subD = [_DB_1, _DB_2, _DB_3, _DB_4, _DB_5, _DB_6, _DB_7, _DB_8, _DB_9]

_BTN_A_pin = 24
_BTN_B_pin = 23

# is used to store states of all pins
_registers = list()

#How many of the shift registers - you can change them with shiftRegisters method
_number_of_shiftregisters = 2

def pinsSetup():
    global _DATA_pin, _CLOCK_pin, _LATCH_pin

    GPIO.setwarnings(False)

    GPIO.setup(_DATA_pin, GPIO.OUT)
    GPIO.setup(_CLOCK_pin, GPIO.OUT)
    GPIO.setup(_LATCH_pin, GPIO.OUT)
    GPIO.setup(_BTN_A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_BTN_B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def pinSsetupInputStart():
    GPIO.setup(_DB_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_DB_9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def pinSsetupInputStop():
    GPIO.setup(_DB_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(_DB_9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def startupMode(mode, execute = False):
    '''
    Allows the user to change the default state of the shift registers outputs
    '''
    if isinstance(mode, int):
        if mode is HIGH or mode is LOW:
            _all(mode, execute)
        else:
            raise ValueError("The mode can be only HIGH or LOW or Dictionary with specific pins and modes")
    elif isinstance(mode, dict):
        for pin, mode in mode.iteritems():
            _setPin(pin, mode)
        if execute:
            _execute()
    else:
        raise ValueError("The mode can be only HIGH or LOW or Dictionary with specific pins and modes")


def shiftRegisters(num):
    '''
    Allows the user to define the number of shift registers are connected
    '''
    global _number_of_shiftregisters
    _number_of_shiftregisters = num
    _all(LOW)

def digitalWrite(pin, mode):
    '''
    Allows the user to set the state of a pin on the shift register
    '''
    if pin == ALL:
        _all(mode)
    else:
        if len(_registers) == 0:
            _all(LOW)

        _setPin(pin, mode)
    _execute()

def readPin(pin):
    return GPIO.input(pin)


def delay(millis):
    '''
    Used for creating a delay between commands
    '''
    millis_to_seconds = float(millis)/1000
    return sleep(millis_to_seconds)

def _all(mode, execute = True):
    all_shr = _number_of_shiftregisters * 8

    for pin in range(0, all_shr):
        _setPin(pin, mode)
    if execute:
        _execute()

    return _registers

def _setPin(pin, mode):
    try:
        _registers[pin] = mode
    except IndexError:
        _registers.insert(pin, mode)

def _execute():
    all_pins = _number_of_shiftregisters * 8
    GPIO.output(_CLOCK_pin, GPIO.LOW)

    for pin in range(all_pins -1, -1, -1):
        GPIO.output(_LATCH_pin, GPIO.LOW)

        pin_mode = _registers[pin]

        GPIO.output(_DATA_pin, pin_mode)
        GPIO.output(_LATCH_pin, GPIO.HIGH)

    GPIO.output(_CLOCK_pin, GPIO.HIGH)

pinsSetup()