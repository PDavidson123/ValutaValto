import PySimpleGUI as sg

def open_reviews_window():
    layout=[[sg.Text('Keresés az alábbi szerint:',size=(20, 1), font='Lucida',justification='left')],
            [sg.Combo(('Dátum','Valuta'), default_value='Dátum', readonly=True, enable_events=True, size=(8, 2),key='keresesAlap'), sg.Combo(Valto.penznemek, readonly=True, enable_events=True, size=(5, 6),key='keresendoValuta', visible=False), sg.InputText(size=(20, 1), key='keresendoDatum', tooltip='Minta: 2020-08-24')],
            [sg.Button("Keresés", key="SearchButton")],
            [sg.Listbox(values= [], key='fac', size=(30, 10))]]

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

        
    window.close

def open_options_window():
    layout=[[sg.Text('Keresések mentésének elérési útja:',size=(30, 1), font='Lucida',justification='left')],
            [sg.InputText(size=(20, 1), key='pathInput', tooltip='Minta: C:\\ValutaMentes')]]

    window = sg.Window("Előzmények", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        
    window.close

def main():
    layout = [[sg.Text('Írja be mennyit, majd válassza ki mit mire szeretne átváltani.', size=(50, 1), font='Lucida',justification='left')],
              [sg.InputText(size=(22, 2), key='mennyit', enable_events=True), sg.Combo(Valto.penznemek,default_value='HUF', readonly=True, enable_events=True, size=(5, 6),key='mit'), sg.Combo(Valto.penznemek,default_value='EUR', readonly=True, enable_events=True, size=(5, 6),key='mire')],
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
        #if event == "mennyit" and values['valtoztat'] == '' and values['mennyit'] is '':
        #    window.Element('valtoztat').Update('')
        if event == "mennyit" and values['mennyit'] is not '':
            window.Element('valtoztat').Update(Valto.atvalt(values['mit'], values['mire'], values['mennyit']))
        if event == "mit" and values['mennyit'] is not '':
            window.Element('valtoztat').Update(Valto.atvalt(values['mit'], values['mire'], values['mennyit']))
        if event == "mire" and values['mennyit'] is not '':
            window.Element('valtoztat').Update(Valto.atvalt(values['mit'], values['mire'], values['mennyit']))
        
    window.close()


class Valto:

    penznemek = ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL')
    
    def atvalt(mit, mire, mennyit):

        valtasEredmeny = 123456

        return mennyit + " " + mit + " = " + str(valtasEredmeny) + " " + mire

if __name__ == "__main__":
    main()