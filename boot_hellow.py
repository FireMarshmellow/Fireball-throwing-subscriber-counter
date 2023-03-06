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
from time import sleep
import network
import urequests
import json
import machine
from machine import Timer
import screen_driver
import gears_driver
import spark_driver
import spray_driver
import config

fire_button = machine.Pin(34, machine.Pin.IN, machine.Pin.PULL_DOWN)
sub_count = 0
last_sub_count = 0

def your_fierd():
    gears_driver.count_down()
    spray_driver.spray_it_up()
    spark_driver.spark_it_up()

def boot_tests():
    if config.test_on_boot == True:
        screen_driver.show_on_screen('Booting')
        sleep(1)
        screen_driver.show_on_screen('testing')
        sleep(1)
        screen_driver.show_on_screen('Gears')
        gears_driver.move_to_num(0)
        sleep(2)
        screen_driver.show_on_screen('spray')
        spray_driver.spray_it_up()
        sleep(2)
        screen_driver.show_on_screen('Spark')
        spark_driver.spark_it_up()
        sleep(1)
    else:
        print('Boot tests disabled')


def connect_to_wifi(ssid, password):
    try:
        # Connect to WiFi
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(ssid, password)
        while not wifi.isconnected():
            pass
        return wifi
    except OSError as e:
        print('Error connecting to WiFi:', e)

def start_up():
    screen_driver.show_on_screen('Wifi')
    wifi = connect_to_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)
    print("WiFi connected. IP address: ", wifi.ifconfig()[0])
    screen_driver.show_on_screen(wifi.ifconfig()[0][-8:])
    sleep(1)
    get_subs(config.API_KEY,config.CHANNEL_ID)

def get_subs(api_key, channel_id):
    global sub_count
    response = urequests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}")
    data = json.loads(response.text)
    sub_count = int(data["items"][0]["statistics"]["subscriberCount"])

def display_subs():
    global last_sub_count
    if sub_count != last_sub_count:
        screen_driver.show_on_screen(str(sub_count))
        if last_sub_count >= 10 and sub_count >= 10 and sub_count // 10 > last_sub_count // 10:
            your_fierd()
        if sub_count >= 10:
            gears_driver.move_to_num(int(str(sub_count)[-1]))
        else:
            gears_driver.move_to_num(int(str(sub_count)))
    last_sub_count = sub_count


def handle_interrupt(timer):
    get_subs(config.API_KEY,config.CHANNEL_ID)

boot_tests()
start_up()

timer = Timer(0)
timer.init(period=config.TIMER_INTERVAL, mode=Timer.PERIODIC, callback=handle_interrupt)

while True:
    if fire_button.value() == 0:
        your_fierd()
        sleep(1)
        gears_driver.move_to_num(int(str(sub_count)[-1]))
        screen_driver.show_on_screen(str(sub_count))
        
    display_subs()
    sleep(0.2)
