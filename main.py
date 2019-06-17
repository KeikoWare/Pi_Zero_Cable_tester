import shiftpi
from time import sleep
import atexit
'''
Functions
'''
def _test_all_LEDs():
    all_pins = 16
    for pin in range(all_pins -1, -1, -1):
        shiftpi.digitalWrite(pin, shiftpi.HIGH)
        shiftpi.delay(300)
        shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

def ButtonA_Action():
    res = '{'
    shiftpi.pinSsetupInputStart()
    pinList = [shiftpi._DB_1, shiftpi._DB_2, shiftpi._DB_3, shiftpi._DB_4, shiftpi._DB_5, shiftpi._DB_6, shiftpi._DB_7, shiftpi._DB_8, shiftpi._DB_9]
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
    rotate_pins = 8
    for pin in range(0,rotate_pins,1):
        shiftpi.digitalWrite(8, shiftpi.LOW)
        shiftpi.delay(100)
        shiftpi.digitalWrite(8, shiftpi.HIGH)
        print('Checking RJ45 pin ' + str(pin+1))
        res = res + '[' + str(pin+1) +',"'
        shiftpi.digitalWrite(pin, shiftpi.HIGH)
        shiftpi.delay(100)
        #Test all inputs and return result
        for pinNum in range(0,9,1):
#            print(' ... checking connection to Sub D pin ' + str(pinNum+1))
            if shiftpi.readPin(shiftpi.subD[pinNum]) == 1:
                res = res + str(pinNum+1) + '_'
#                1f pin == 9 :
#                    shiftpi.digitalWrite(15, shiftpi.HIGH)
#                    shiftpi.digitalWrite(8, shiftpi.HIGH)
#                else:
#                    shiftpi.digitalWrite(15-pin, shiftpi.HIGH)
#                shiftpi.delay(300)
#                if pin == 9 :
#                    shiftpi.digitalWrite(15, shiftpi.LOW)
#                    shiftpi.digitalWrite(8, shiftpi.LOW)
#                else:
#                    shiftpi.digitalWrite(15-pin, shiftpi.LOW)
        shiftpi.digitalWrite(pin, shiftpi.LOW)
        if pin < 7:
            res = res + '"],'
        else:
          res = res + '"]}'
    shiftpi.digitalWrite(8, shiftpi.LOW)
    shiftpi.delay(100)
    shiftpi.digitalWrite(8, shiftpi.HIGH)
    #Qualify the result
    # Blue RJ45 <-> RJ45 + STD SUB D (First is when black mark pointing towards SUB D & second is when black mark pointing towards RJ45)
    if res == '{[1,"3_"],[2,"4_"],[3,"6_"],[4,"1_"],[5,"2_"],[6,"5_"],[7,"8_"],[8,"7_"]}' or res == '{[1,"2_"],[2,"1_"],[3,"6_"],[4,"3_"],[5,"7_"],[6,"8_"],[7,"4_"],[8,"5_"]}':
        shiftpi.digitalWrite(9, shiftpi.HIGH)
        
    # Red (CROSS OVER) Male RJ45 <-> Male RJ45 (Symetrical) + STD SUB D
    # Red (CROSS OVER) Female RJ45 <-> Male Rj45 + STD SUB D
    if res == '{[1,"6_"],[2,"3_"],[3,"8_"],[4,"2_"],[5,"1_"],[6,"7_"],[7,"5_"],[8,"4_"]}':
        shiftpi.digitalWrite(10, shiftpi.HIGH)
#    if res == '{[1,"6_"],[2,"3_"],[3,"8_"],[4,"2_"],[5,"1_"],[6,"7_"],[7,"5_"],[8,"4_"]}':
#        shiftpi.digitalWrite(12, shiftpi.HIGH)
        
    # Blue Female RJ45 <-> Male Rj45 (ROLLOVER) + STD SUB D
    if res == '{[1,"1_"],[2,"2_"],[3,"3_"],[4,"4_"],[5,"5_"],[6,"6_"],[7,"7_"],[8,"8_"]}':
        shiftpi.digitalWrite(11, shiftpi.HIGH)

    # Straight or Standard Sub D cable: Female RJ 45 -> Male Sub D
    if res == '{[1,"8_"],[2,"7_"],[3,"6_"],[4,"5_"],[5,"4_"],[6,"3_"],[7,"2_"],[8,"1_"]}':
        shiftpi.digitalWrite(12, shiftpi.HIGH)

    # Black Female RJ 45 -> Female Sub D
    if res == '{[1,"3_"],[2,"5_"],[3,"2_"],[4,"7_"],[5,"4_"],[6,"5_"],[7,"8_"],[8,"1_6_"]}':
        shiftpi.digitalWrite(14, shiftpi.HIGH)

    # Grey (HP) Female RJ 45 -> Female Sub D
    if res == '{[1,"7_"],[2,"4_"],[3,"3_"],[4,"5_"],[5,"5_"],[6,"2_"],[7,"6_"],[8,"8_"]}':
        shiftpi.digitalWrite(15, shiftpi.HIGH)
    
    shiftpi.pinSsetupInputStop()
    print(res)


def ButtonB_Action():
    all_pins = 16
    for pin in range(all_pins -1, -1, -1):
        shiftpi.digitalWrite(pin, shiftpi.HIGH)
        shiftpi.delay(300)
        shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

@atexit.register
def goodbye():
    print("You are now leaving the Python sector.")
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
        
'''
Main Loop
'''
shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
shiftpi.digitalWrite(8, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(9, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(10, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(11, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(12, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(13, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(14, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(15, shiftpi.HIGH)
shiftpi.delay(200)
shiftpi.digitalWrite(8, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(9, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(10, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(11, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(12, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(13, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(14, shiftpi.LOW)
shiftpi.delay(200)
shiftpi.digitalWrite(15, shiftpi.LOW)

shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
shiftpi.digitalWrite(8, shiftpi.HIGH)

'''
WHILE LOOP
'''
while True:
    input_state_A = shiftpi.readPin(shiftpi._BTN_A_pin)
    input_state_B = shiftpi.readPin(shiftpi._BTN_B_pin)
    #print(input_state_A)
    #print(input_state_B)
        
    if input_state_A == 0:
        print('Button A Pressed')
        ButtonA_Action()
        sleep(0.2)
         
    if input_state_B == 0:
        print('Button B Pressed')
        ButtonB_Action()
        sleep(0.2)
