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
'''
Hi Dan,
Welcome to the code equivalent of duct tape and hot glue,
where we stick things together and hope they don't fall apart.

Don't worry though, I did actually have to put some safety precautions into this.
You know, things like error handling, logging, testing... OK, maybe not testing.
But hey, who needs testing when you have faith? And by faith, I mean ChatGPT,
fingers crossed it all works perfectly.

Technically, I've not been able to test all of the features.
But that's your job now. Congratulations! You get to be the guinea pig for this masterpiece of code.
Just make sure you don't touch anything that looks important.

Except the safety stuff. I like triple checked those.
Because safety first, right? Well, maybe not first.
But definitely somewhere in the top ten. Anyway, good luck and have fun!

all the bits you need to edit are down here \/
read all comments!!
'''

#I'll give you 10 guesses for what you have to put in here                                  
WIFI_SSID = "Mellow-home-Fibre"
WIFI_PASSWORD = "cxs96whbaf"
#to confirm Wi-Fi information please run wifi_test.py

#this is using my YouTube API key feel free to change it if you want to
API_KEY = "AIzaSyCYOjpH0jJsXTK85G986QRdVEuvf6AIBMQ"
CHANNEL_ID = "UCswAdKEco21t8YbIIKNIYbQ"

#this is the update subscriber count interval
TIMER_INTERVAL = 600000  # 10 Minute units = milliseconds

#To disable change to False

#runs a test sequence on boot testing individual components one at the time
test_on_boot = False

#hooray! you got to the safety stuff

gears = True #disables the stepper motor
spark = True #disables the igniter
screen = True #disables the screen
spray = True #disables the air freshener

#all of these parts can operate individually so if need to be this can just be a simple air freshener
#or as I like to call it wife friendly mode

'''
To complete configuration rename 'boot_hellow.py' to 'boot.py'
do not run the boot script on USB power!!! 
'''