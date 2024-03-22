import subprocess as sp#Subprocess Linux komutlarını kullanma
import optparse
print("""
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
def mac():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change.")
    parser.add_option("-m","--mac_addres",dest="mac_addres",help="new mac addres")
    (user_input,arguments)=parser.parse_args()
    if not user_input.interface or not user_input.mac_addres:
        print("Please mac addres and interface")
        return
    user_interface=user_input.interface
    user_mac_addres=user_input.mac_addres

    sp.call(["ifconfig",user_interface,"down"])
    sp.call(["ifconfig",user_interface,"hw","ether",user_mac_addres])
    sp.call(["ifconfig",user_interface,"up"])
    print("Changed Mac addres new mac addres ",user_mac_addres)

mac()
