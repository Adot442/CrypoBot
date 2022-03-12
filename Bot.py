import time

from CryptoData import CryptoData
from Email import Email

class Bot:
    def __init__(self):
        self.data = CryptoData()
        self.email = Email()

    def runProgram(self):
        self.data.update()
        btcPrice = -1
        while(btcPrice == -1):
            btcPrice = self.data.getBitcoin()["price"]
            time.sleep(2)

        self.email.sendEmail("Bitcoin Price", btcPrice)

if __name__ == "__main__":
    bot = Bot()
    time.sleep(5)
    while(True):
        bot.runProgram()
        time.sleep(86400)

