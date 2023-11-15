import PySimpleGUI as sg

#######################
#Window Initialization#
#######################

def main():
    sg.theme('LightBrown7')
    
    extensions = ['png', 'jpg']
    layout = [[sg.Input("", font=('Times\ New\ Roman 16'), key='-INPUT-')], [sg.FileBrowse('Select', font=('Georgia 18'), file_types=(('PDF Files', '*.pdf'),))], [sg.Combo(extensions, key="inp", disabled=True, default_value="png", enable_events= True, font=('Arial 18')), sg.Button('Convert', disabled=True, font=('Arial 17'), enable_events=True)]]
    
    window = sg.Window('PDF to Image', layout, size=(370, 160), resizable=False, element_justification='c')
    
    while True:
    	event, values = window.read()
    	if event == sg.WIN_CLOSED or event == 'Cancel':
    		break
    
main()
