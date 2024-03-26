import subprocess as sp#Subprocess Linux komutlarını kullanma
import optparse # optparse kütüphanesi
import re #regex kütüphanesi
import colorama 
green=colorama.Fore.GREEN
print(green+"""
#---------------------------------------------------------------------#
#    _     _____   _  _____   ____ ___ ____ _     _____               #
#   / \   |__  /  / \|_   _| |  _ \_ _/ ___| |   | ____|              #
#  / _ \    / /  / _ \ | |   | | | | | |   | |   |  _|                #
# / ___ \  / /_ / ___ \| |   | |_| | | |___| |___| |___               #
#/_/   \_\/____/_/   \_\_|   |____/___\____|_____|_____|              #
#                                                                     #
# __  __    _    ____    ____ _   _    _    _   _  ____ _____ ____    #
#|  \/  |  / \  / ___|  / ___| | | |  / \  | \ | |/ ___| ____|  _ \   #
#| |\/| | / _ \| |     | |   | |_| | / _ \ |  \| | |  _|  _| | |_) |  #
#| |  | |/ ___ \ |___  | |___|  _  |/ ___ \| |\  | |_| | |___|  _ <   #
#|_|  |_/_/   \_\____|  \____|_| |_/_/   \_\_| \_|\____|_____|_| \_\  #
#---------------------------------------------------------------------#
                   @azatdicle Mac Changer
""")
def get_user_input():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change.")
    parser.add_option("-m","--mac_addres",dest="mac_addres",help="new mac addres")
    return parser.parse_args()
def changemac(user_interface,user_mac_addres):
    sp.call(["ifconfig",user_interface,"down"])
    sp.call(["ifconfig",user_interface,"hw","ether",user_mac_addres])
    sp.call(["ifconfig",user_interface,"up"])
def mac_control(interface):
    ifconfig=sp.check_output(["ifconfig",interface])
    ifconfig=ifconfig.decode("utf-8")
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if new_mac:
        return new_mac.group(0)
    else:
        return None
(user_input,arguments) = get_user_input()
changemac(user_input.interface,user_input.mac_addres)    
final_mac = mac_control(user_input.interface)
if final_mac == user_input.mac_addres:
    print("Sucess")
    print("Changed Mac addres new mac addres",user_input.mac_addres)
else:
    print("Error!")
    
