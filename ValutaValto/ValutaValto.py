import PySimpleGUI as sg
import DataHandler
import Valto

def open_reviews_window():
    layout=[[sg.Text('Keresés az alábbi szerint:',size=(20, 1), font='Lucida',justification='left')],
            [sg.Combo(('Dátum','Valuta'), default_value='Dátum', readonly=True, enable_events=True, size=(8, 2),key='keresesAlap'), sg.Combo(Valto.Valto.penznemek, readonly=True, enable_events=True, size=(5, 6),key='keresendoValuta', visible=False), sg.InputText(size=(20, 1), key='keresendoDatum', tooltip='Minta: 2020-08-24')],
            [sg.Button("Keresés", key="SearchButton")],
            [sg.Listbox(values= DataHandler.DataHandler.GetFileLists(), key='tranzList', size=(30, 10))]]

    window = sg.Window("Előzmények", layout, modal=True)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "keresesAlap" and values['keresesAlap'] == 'Dátum':
            window.Element('keresendoValuta').Update(visible=False)
            window.Element('keresendoDatum').Update(visible=True)
        if event == "keresesAlap" and values['keresesAlap'] == 'Valuta':
            window.Element('keresendoValuta').Update(visible=True)
            window.Element('keresendoDatum').Update(visible=False)
        if event == "SearchButton" and values['keresesAlap'] == "Dátum":
            window['tranzList'].update([])
            window['tranzList'].update(DataHandler.DataHandler.GetFileListByDates(values['keresendoDatum']))
        if event == "SearchButton" and values['keresesAlap'] == "Valuta":
            window['tranzList'].update([])
            window['tranzList'].update(DataHandler.DataHandler.GetFileListByValuta(values['keresendoValuta']))

        
    window.close

def open_options_window():
    layout=[[sg.Text('Keresések mentésének elérési útja:',size=(30, 1), font='Lucida',justification='left')],
            [sg.InputText(size=(20, 1), key='pathInput', default_text=DataHandler.DataHandler.GetPath(), tooltip='Minta: C:\\ValutaMentes'), sg.Button("Mentés", key="SaveButton")]]

    window = sg.Window("Előzmények", layout, modal=True)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "SaveButton":
            DataHandler.DataHandler.SetPath(values['pathInput'])
            sg.Popup('A mentés sikeresen megtörtént.', keep_on_top=True)

        
    window.close

def main():
    layout = [[sg.Text('Írja be mennyit, majd válassza ki mit mire szeretne átváltani.', size=(50, 1), font='Lucida',justification='left')],
              [sg.InputText(size=(22, 2), key='mennyit', enable_events=True), sg.Combo(Valto.Valto.GetValutaListWithFirstFive(),default_value=Valto.Valto.GetValutaListWithFirstFive()[0], readonly=True, enable_events=True, size=(5, 6),key='mit'), sg.Combo(Valto.Valto.GetValutaListWithFirstFive(),default_value=Valto.Valto.GetValutaListWithFirstFive()[1], readonly=True, enable_events=True, size=(5, 6),key='mire')],
              [sg.Text('', size=(50, 1), font='Lucida',justification='left', key='valtoztat')],
              [sg.Button("Előzmények", size=(10, 1), key="OpenReviewsWindow"), sg.Button("Beállítások", size=(10, 1), key="OpenOptionsWindow")]]

    window = sg.Window("Valuta átváltás", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "OpenReviewsWindow":
            open_reviews_window()
        if event == "OpenOptionsWindow":
            open_options_window()
        if event == "mennyit" and values['mennyit'] is '':
            window.Element('valtoztat').Update('')
        if event == "mennyit" and values['mennyit'] is not '':
            window.Element('valtoztat').Update(Valto.Valto.atvalt(values['mit'], values['mire'], values['mennyit']))
        if event == "mit" and values['mennyit'] is not '':
            window.Element('valtoztat').Update(Valto.Valto.atvalt(values['mit'], values['mire'], values['mennyit']))
        if event == "mire" and values['mennyit'] is not '':
            window.Element('valtoztat').Update(Valto.Valto.atvalt(values['mit'], values['mire'], values['mennyit']))
        
    window.close()

if __name__ == "__main__":
    main()