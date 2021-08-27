import DataHandler
import requests

class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'HUF' : # Ha nem HUF, akkor azzá alakítjuk majd később ez alapján kapjuk meg az átváltást
            amount = amount / self.currencies[from_currency] 
  
        amount = round(amount * self.currencies[to_currency], 3) 
        return amount

class Valto:

    url = 'https://api.exchangerate-api.com/v4/latest/HUF' # Forint alap lekérés
    converter = RealTimeCurrencyConverter(url)

    penznemek = converter.currencies.keys()
    
    def atvalt(mit, mire, mennyit, realTranz = False):

        valtasEredmeny = Valto.converter.convert(mit,mire,int(mennyit))

        if realTranz:
            DataHandler.DataHandler.SaveTranz(mit, mennyit, mire, valtasEredmeny)
            return str(mennyit) + " " + mit + " átváltva " + str(valtasEredmeny) + " " + mire + "-ra/re"

        return str(mennyit) + " " + mit + " = " + str(valtasEredmeny) + " " + mire

    def GetValutaListWithFirstFive():
        thatfive = DataHandler.DataHandler.GetLastFiveValuta()
        anothers = set(Valto.penznemek)

        lastItems = anothers.difference(thatfive)

        makedList = []

        for i in thatfive:
            makedList.append(i)
        for i in sorted(list(lastItems)):
            makedList.append(i)

        return makedList

