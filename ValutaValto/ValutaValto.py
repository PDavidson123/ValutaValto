import PySimpleGUI as sg
import DataHandler
import Valto

def open_reviews_window():
    layout=[[sg.Text('Keresés az alábbi szerint:',size=(20, 1), font='Lucida',justification='left')],
            [sg.Combo(('Dátum','Valuta'), default_value='Dátum', readonly=True, enable_events=True, size=(8, 2),key='searchDefault'), sg.Combo(Valto.Valto.penznemek, Valto.Valto.penznemek[0], readonly=True, enable_events=True, size=(5, 6),key='searchCurr', visible=False), sg.InputText(size=(20, 1), key='searchDate', tooltip='Minta: 2020-08-24')],
            [sg.Button("Keresés", key="SearchButton")],
            [sg.Listbox(values= DataHandler.DataHandler.get_file_lists(), key='tranzList', size=(30, 10))]]

    window = sg.Window("Előzmények", layout, modal=True)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "searchDefault" and values['searchDefault'] == 'Dátum':
            window.Element('searchCurr').Update(visible=False)
            window.Element('searchDate').Update(visible=True)
        if event == "searchDefault" and values['searchDefault'] == 'Valuta':
            window.Element('searchCurr').Update(visible=True)
            window.Element('searchDate').Update(visible=False)
        if event == "SearchButton" and values['searchDefault'] == "Dátum":
            window['tranzList'].update([])
            window['tranzList'].update(DataHandler.DataHandler.get_file_list_by_dates(values['searchDate']))
        if event == "SearchButton" and values['searchDefault'] == "Valuta":
            window['tranzList'].update([])
            window['tranzList'].update(DataHandler.DataHandler.get_file_list_by_currency(values['searchCurr']))

        
    window.close

def open_options_window():
    layout=[[sg.Text('Keresések mentésének elérési útja:',size=(30, 1), font='Lucida',justification='left')],
            [sg.InputText(size=(20, 1), key='pathInput', default_text=DataHandler.DataHandler.getPath(), tooltip='Minta: C:\\ValutaMentes'), sg.Button("Mentés", key="SaveButton")]]

    window = sg.Window("Előzmények", layout, modal=True)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "SaveButton":
            DataHandler.DataHandler.setPath(values['pathInput'])
            sg.Popup('A mentés sikeresen megtörtént.', keep_on_top=True)

        
    window.close

def main():
    layout = [[sg.Text('Írja be mennyit, majd válassza ki mit mire szeretne átváltani.', size=(50, 1), font='Lucida',justification='left')],
              [sg.InputText(size=(22, 2), key='amount', enable_events=True),
               sg.Combo(Valto.Valto.get_valuta_list_with_first_five(),default_value=Valto.Valto.get_valuta_list_with_first_five()[0], readonly=True, enable_events=True, size=(5, 6),key='from_curr'),
               sg.Combo(Valto.Valto.get_valuta_list_with_first_five(),default_value=Valto.Valto.get_valuta_list_with_first_five()[1], readonly=True, enable_events=True, size=(5, 6),key='to_curr')],
              [sg.Text('', size=(40, 1), font='Lucida',justification='left', key='exchangeText'), sg.Button("Átváltás", size=(10, 1), key="SaveTranzButton", visible=False)],
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
        if event == "amount" and values['amount'] is '':
            window.Element('exchangeText').Update('')
            window.Element('SaveTranzButton').Update(visible=False)
        if event == "amount" and values['amount'] is not '':
            window.Element('exchangeText').Update(Valto.Valto.atvalt(values['from_curr'], values['to_curr'], float(values['amount'])))
            window.Element('SaveTranzButton').Update(visible=True)
        if event == "from_curr" and values['amount'] is not '':
            window.Element('exchangeText').Update(Valto.Valto.atvalt(values['from_curr'], values['to_curr'], float(values['amount'])))
            window.Element('SaveTranzButton').Update(visible=True)
        if event == "to_curr" and values['amount'] is not '':
            window.Element('exchangeText').Update(Valto.Valto.atvalt(values['from_curr'], values['to_curr'], float(values['amount'])))
            window.Element('SaveTranzButton').Update(visible=True)
        if event == "SaveTranzButton":
            Valto.Valto.atvalt(values['from_curr'], values['to_curr'], float(values['amount']), True)
            sg.Popup('A váltás sikeresen megtörtént.', keep_on_top=True)
            window.Element('from_curr').Update(values = Valto.Valto.get_valuta_list_with_first_five(), value = Valto.Valto.get_valuta_list_with_first_five()[0])
            window.Element('to_curr').Update(values = Valto.Valto.get_valuta_list_with_first_five(), value = Valto.Valto.get_valuta_list_with_first_five()[1])
        
    window.close()

if __name__ == "__main__":
    main()