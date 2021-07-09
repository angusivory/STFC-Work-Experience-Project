import logging
import graypy
import datetime
import random


# weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# now = datetime.datetime.now()
# today = weekdays[now.weekday()]
# print(today)
# tomorrow = weekdays[(now.weekday() + 1)%7]
# print(tomorrow)

instruments = ["ENGINX", "GEM", "HRPD", "INES", "PEARL", "POLARIS", "SXD", "WISH"]
users = ["Bob", "Graham", "Ellie", "Chris", "Jack", "Wendy", "Lauren", "Alex", "Robin", "Hannah"]

def send(message):
    print(message)
    my_logger.debug(message)

class instrumentFilter(logging.Filter):
    def __init__(self):
        self.instrument = instrument
        self.user = user

    def filter(self, record):
        record.instrument = instrument
        record.user = user
        return True

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('localhost', 12201)
my_logger.addHandler(handler)

# initial transmission
send("The instruments have been turned on...")

instrument = random.choice(instruments)
user = random.choice(users)
packet = instrumentFilter()
my_logger.addFilter(packet)

#log five instruments and five users
for x in range(0, 5):
    instrument = random.choice(instruments)
    user = random.choice(users)
    packet.instrument = instrument
    packet.user = user
    
    send(f"An instrument, {instrument}, was used by {user}.")

send("The instruments have been turned off now.")
# my_logger.critical("something broke")

print("finished")