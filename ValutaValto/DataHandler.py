import os.path

class DataHandler:

    defPath = "C:\\ValutaValto"
    realpath = ""

    if os.path.isfile("C:\\VV\\VVPath.ki"):
        text_file = open("C:\\VV\\VVPath.ki", "r")
        realpath = text_file.read()
        text_file.close()
    else:
        realpath = defPath

    def SaveTranz(mit, mennyit, mire, mennyire):
        text_file = open(realpath + "\\" + mit + "-" + mennyit + "-" + mire + "-" + mennyire, "w")
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
        