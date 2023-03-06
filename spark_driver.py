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

# Define a function to spark the pin
def spark_it_up():
    if config.spark:
        # Create a Pin object for GPIO 22 and turn it on
        spark_pin = Pin(22, Pin.OUT)
        spark_pin.on()
        # Wait for one second and then turn the pin off
        sleep(1)
        spark_pin.off()
    else:
        print('Spark disabled')

'''
if you see this you owe me $10
'''