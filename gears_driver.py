#                                                    .-'''-.                                                     
#                                      .---..---.   '   _    \               .---.                               
#   __  __   ___         __.....__     |   ||   | /   /` '.   \              |   |          /|                   
#  |  |/  `.'   `.   .-''         '.   |   ||   |.   |     \  '       _     _|   |          ||                   
#  |   .-.  .-.   ' /     .-''"'-.  `. |   ||   ||   '      |  '/\    \\   //|   |          ||                   
#  |  |  |  |  |  |/     /________\   \|   ||   |\    \     / / `\\  //\\ // |   |    __    ||  __               
#  |  |  |  |  |  ||                  ||   ||   | `.   ` ..' /    \`//  \'/  |   | .:--.'.  ||/'__ '.       _    
#  |  |  |  |  |  |\    .-------------'|   ||   |    '-...-'`      \|   |/   |   |/ |   \ | |:/`  '. '    .' |   
#  |  |  |  |  |  | \    '-.____...---.|   ||   |                   '        |   |`" __ | | ||     | |   .   | / 
#  |__|  |__|  |__|  `.             .' |   ||   | ________________           |   | .'.''| | ||\    / ' .'.'| |// 
#                      `''-...... -'   '---''---'|________________|          '---'/ /   | |_|/\'..' /.'.'.-'  /  
#                                                                                 \ \._,\ '/'  `'-'` .'   \_.'   
#@Mellow_labs                                                                      `--'  `"
from machine import Pin, ADC
import time
import config
import Stepper
import screen_driver

# Create pins for the stepper motor
In4 = Pin(32, Pin.OUT)
In3 = Pin(33, Pin.OUT)
In2 = Pin(25, Pin.OUT)
In1 = Pin(26, Pin.OUT)

# Create the stepper motor object
stepper = Stepper.create(In1, In2, In3, In4, delay=1)

# Define a function to calibrate the stepper motor
def calibrate_stepper():
    if config.gears:
        # Wait until the button is pressed to begin calibration
        button = Pin(13, Pin.OUT, Pin.PULL_UP)
        while button.value() == 1:
            stepper.step(1)
    else:
        print('Gears disabled')

# Define a function to move the stepper motor to a specific number
def move_to_num(num):
    if config.gears:
        calibrate_stepper()
        # Define a dictionary mapping numbers to step counts
        num_steps = {0: 520, 1: 420, 2: 320, 3: 220, 4: 120, 5: 23, 6: 920, 7: 810, 8: 715, 9: 610}
        # Move the stepper motor to the desired number of steps
        stepper.step(num_steps[num])
    else:
        print('Gears disabled')

# Define a function to count down
def count_down():
    if config.gears:
        calibrate_stepper()
        for num in range(9, -1, -1):
            stepper.step(610 if num == 9 else 100)
            screen_driver.show_on_screen(str(num))
            time.sleep(0.2)