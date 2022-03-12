import requests
import time 

class CryptoData:
    def __init__(self):
        self.response = self.apiCall()

    def apiCall(self):
        response = [{"price": -1}, {"price": -1}]

        fd = open("./secret/apikey.txt", "r")
        url = fd.readline()
        fd.close()

        response = requests.get(url).json()
        return response


    def update(self):
        self.response  = self.apiCall()

    def getBitcoin(self):
        bitcoin = self.response[0]
        return bitcoin 

    def getEtherium(self):
        etherium = self.response[1]
        return etherium 

    def printCryptoPrice(self, coin): 
        while(True):
            print(coin['price'])
            time.sleep(5)

if __name__ == "__main__":
    data = CryptoData()
    data.printCryptoPrice(data.getBitcoin())
    #printCryptoPrice(getBitcoin())
