import subprocess as sp
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

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface to change.")
parser.add_option("-m", "--mac_address", dest="mac_address", help="new mac address")

(options, arguments) = parser.parse_args()

user_interface = options.interface
user_mac_address = options.mac_address

sp.call(["ifconfig", user_interface, "down"])
sp.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
sp.call(["ifconfig", user_interface, "up"])
print("Mac changed")
