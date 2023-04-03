import socket, threading
from timeit import default_timer as timer
from colorama import Fore
from time import sleep
from os import system, name as osname
from fade import greenblue
w=Fore.WHITE
black=Fore.LIGHTBLACK_EX
y=Fore.LIGHTYELLOW_EX
r=Fore.LIGHTRED_EX
g=Fore.GREEN
lg=Fore.LIGHTGREEN_EX
pinging = False

def entrypoint():
        try:
            clear()
            drawbanner()
            global ip, port
            ip = input(f"{lg}[{w}>>>{lg}] {black}IP:{y} ")
            print("")
            port = int(input(f"{lg}[{w}>>>{lg}] {black}Port:{y} "))
            print("")
        except KeyboardInterrupt:
            print("")
            print(f"{lg}[{r}!{lg}] {r}You pressed CTRL+C, exiting...")
            sleep(1)
            exit()
        except ValueError:
            print("")
            print(f"{lg}[{r}!{lg}] {r}You must enter a valid port number!")
            sleep(1)
            entrypoint()


def clear():
    if osname == 'nt': 
        system('cls')
    else:
        system('clear')
def drawbanner():
    gui="""
        __________    _____   ___________  _________ __________ .___  _______     ________ _____________________ 
        \______   \  /  _  \  \__    ___/ /   _____/ \______   \|   | \      \   /  _____/ \_   _____/\______   \\
         |     ___/ /  /_\  \   |    |    \_____  \   |     ___/|   | /   |   \ /   \  ___  |    __)_  |       _/
         |    |    /    |    \  |    |    /        \  |    |    |   |/    |    \\\\    \_\  \ |        \ |    |   \\
         |____|    \____|__  /  |____|   /_______  /  |____|    |___|\____|__  / \______  //_______  / |____|_  /
                           \/                    \/                          \/         \/         \/         \/
                                                                                                     P A T A P
"""
    faded_gui=greenblue(gui)
    print(faded_gui)


def tcpping(ip, port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        s_start = timer()
        sock.connect((ip, port))
        s_stop = timer()
        s_runtime = "%.2f" % (1000 * (s_stop - s_start))
        print(f"                {lg}[{w}OK{lg}] {g}Connection to {y}{ip} {lg}in port {y}{port} time %s ms {lg}[{w}OK{lg}]" % s_runtime)
    except:
        print(f"                        {r}[DEAD] {g}The fat cunt {y}{ip} {g}was raped")

def run_spinnintitle():
     while True:
        if pinging == False:
            system(f"title ^| 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 ^| Made by 𝓟𝓪𝓽𝓪𝓹 ^|")
            sleep(0.3)
            system(f"title ^\\ 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 ^\\ Made by 𝓟𝓪𝓽𝓪𝓹 ^\\")
            sleep(0.3)
            system(f"title - 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 - Made by 𝓟𝓪𝓽𝓪𝓹 -")
            sleep(0.3)
            system(f"title / 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 / Made by 𝓟𝓪𝓽𝓪𝓹 /")
            sleep(0.3)
        else:
            if pinging == True:
                system(f"title ^| 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 ^| Made by 𝓟𝓪𝓽𝓪𝓹 ^| Pinging {ip} on port {port} ^|")
                sleep(0.3)
                system(f"title ^\\ 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 ^\\ Made by 𝓟𝓪𝓽𝓪𝓹 ^\\ Pinging {ip} on port {port} ^\\")
                sleep(0.3)
                system(f"title - 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 - Made by 𝓟𝓪𝓽𝓪𝓹 - Pinging {ip} on port {port} -")
                sleep(0.3)
                system(f"title / 𝓟𝓪𝓽𝓼 𝓟𝓲𝓷𝓰𝓮𝓻 / Made by 𝓟𝓪𝓽𝓪𝓹 / Pinging {ip} on port {port} /")
                sleep(0.3)

threading.Thread(target=run_spinnintitle).start()

entrypoint()

pinging = True

while True:
    try:
        sleep(1)
        tcpping(ip, port)
    except KeyboardInterrupt:
        entrypoint()

