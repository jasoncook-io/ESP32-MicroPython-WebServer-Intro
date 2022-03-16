import network
from utime import sleep

def connect():
    ssid = "DOME_RDS"
    password = "Eq3Dom51319"
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    print("connecting to network")
    while station.isconnected() == False:
        print('.', end='')
        sleep(.1)
    print("\n ---- Connection successful ----")
    print(station.ifconfig())
    ipData = station.ifconfig()
    print("my IP address is: ", ipData[0])

