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

from machine import Pin
from time import sleep
import config

# Define a function to spray the pin
def spray_it_up():
    if config.spray:
        # Create a Pin object for GPIO 4 and turn it on
        spray_pin = Pin(4, Pin.OUT)
        spray_pin.on()
        # Wait for 0.2 seconds and then turn the pin off
        sleep(0.2)
        spray_pin.off()
    else:
        print('Spray disabled')

'''
malibu ken - tuesday
There's something you should probably know before we go too far
My neighbor found a mushroom growing inside of my car
She called me up on tour sounding emotionally scarred
Although it may have scared her more that i wasn't really alarmed
'''