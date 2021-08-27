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

    def SaveTranz(mit, mennyit, mire, mennyire):
        date = DataHandler.today.strftime("%Y-%m-%d")
        text_file = open(DataHandler.realpath + "\\" + date + "--" + str(mennyit) + "_" + mit + "_" + str(mennyire) + "_" + mire, "w")
        text_file.close()

    def GetPath():
        return DataHandler.realpath

    def SetPath(mire):
        if not os.path.isdir('C:\\VV'):
            os.mkdir('C:\\VV')
        text_file = open("C:\\VV\\VVPath.ki", "w")
        text_file.write(mire)
        text_file.close()
        if not os.path.isdir(DataHandler.realpath):
            os.mkdir(DataHandler.realpath)
        
    def GetGoodFormat(list):
        retlist = []

        for i in list:
            splitted = i.split("_")
            retlist.append(splitted[0] + " " + splitted[1] + " átváltva " + splitted[2] + " " + splitted[3] + "-ra/re")

        return retlist

    def GetFileLists():
        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        justnames = [i.split("--").pop() for i in fullnames] # Dátumot kivesszük

        return DataHandler.GetGoodFormat(justnames)

    def GetFileListByDates(date):
        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        goodTranz = [i.split("--").pop() for i in fullnames if i.split("--")[0] == date]

        return DataHandler.GetGoodFormat(goodTranz)

    def GetFileListByValuta(valuta):
        fullnames = [i for i in listdir(DataHandler.realpath) if isfile(join(DataHandler.realpath, i))] # Csak a file nevek megkapása
        goodTranz = [i.split("--").pop() for i in fullnames if valuta in i.split("--")[1].split("_")]

        return DataHandler.GetGoodFormat(goodTranz)

    def GetLastFiveValuta():
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