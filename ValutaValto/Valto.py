import DataHandler
import requests

class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_curr, to_curr, amount): 
        initial_amount = amount 
        if from_curr != 'HUF' : # Ha nem HUF, akkor azzá alakítjuk majd később ez alapján kapjuk meg az átváltást
            amount = amount / self.currencies[from_curr] 
  
        amount = round(amount * self.currencies[to_curr], 3) 
        return amount

class Valto:

    url = 'https://api.exchangerate-api.com/v4/latest/HUF' # Forint alap lekérés
    converter = RealTimeCurrencyConverter(url)

    penznemek = sorted(list(converter.currencies.keys()))

    def atvalt(from_curr, to_curr, amount, realTranz = False):

        valtasEredmeny = Valto.converter.convert(from_curr,to_curr,int(amount))

        if realTranz:
            DataHandler.DataHandler.saveTranz(from_curr, amount, to_curr, valtasEredmeny)
            return str(amount) + " " + from_curr + " átváltva " + str(valtasEredmeny) + " " + to_curr + "-ra/re"

        return str(amount) + " " + from_curr + " = " + str(valtasEredmeny) + " " + to_curr

    def get_valuta_list_with_first_five():
        thatfive = DataHandler.DataHandler.get_last_five_valuta()
        anothers = set(Valto.penznemek)

        lastItems = anothers.difference(thatfive)

        makedList = []

        for i in thatfive:
            makedList.append(i)
        for i in sorted(list(lastItems)):
            makedList.append(i)

        return makedList

