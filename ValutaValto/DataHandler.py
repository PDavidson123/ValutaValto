import os.path
from os import listdir
from os.path import isfile, join
from datetime import date

class DataHandler:

    defPath = "C:\\VV"
    realpath = ""

    today = date.today()

    if os.path.isfile("C:\\VV\\VVPath.ki"):
        text_file = open("C:\\VV\\VVPath.ki", "r")
        realpath = text_file.read()
        text_file.close()
    else:
        realpath = defPath

    def saveTranz(mit, mennyit, mire, mennyire):
        date = DataHandler.today.strftime("%Y-%m-%d")
        localpath = (DataHandler.realpath + "\\" + date + "--" + str(mennyit) + "_" + mit + "_" + str(mennyire) + "_" + mire).replace('.',',')
        text_file = open(localpath, "w")
        text_file.close()

    def getPath():
        return DataHandler.realpath

    def setPath(mire):
        if not os.path.isdir('C:\\VV'):
            os.mkdir('C:\\VV')
        text_file = open("C:\\VV\\VVPath.ki", "w")
        text_file.write(mire)
        text_file.close()
        DataHandler.realpath = mire
        if not os.path.isdir(DataHandler.realpath):
            os.makedirs(DataHandler.realpath)
        
    def get_good_format(list):
        retlist = []

        for i in list:
            splitted = i.split("_")
            retlist.append(splitted[0] + " " + splitted[1] + " átváltva " + splitted[2] + " " + splitted[3] + "-ra/re")

        return retlist

    def get_file_lists():
        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        justnames = [i.split("--").pop() for i in fullnames] # Dátumot kivesszük
        return DataHandler.get_good_format(justnames)

    def get_file_list_by_dates(date):
        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        goodTranz = [i.split("--").pop() for i in fullnames if i.split("--")[0] == date]
        return DataHandler.get_good_format(goodTranz)

    def get_file_list_by_currency(currency):
        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        goodTranz = [i.split("--").pop() for i in fullnames if currency in i.split("--")[1].split("_")]
        return DataHandler.get_good_format(goodTranz)

    """
        Az utolsó 5 használt valuta
    """
    def get_last_five_valuta():
        fivelist = []

        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        formedTranz = reversed([i.split("--").pop() for i in fullnames]) # Idő nélküli tranzakció nevek

        for i in formedTranz: # Az első 5 valuta hozzáadása a listához
            splitted = i.split("_")
            if len(fivelist) < 5 and splitted[1] not in fivelist:
                fivelist.append(splitted[1])
            if len(fivelist) < 5 and splitted[3] not in fivelist:
                fivelist.append(splitted[3])
            if len(fivelist) == 5: # A sebesség kedvéért ugorjunk ki ha megvan
                break

        return fivelist