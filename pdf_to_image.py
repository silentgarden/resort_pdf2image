import PySimpleGUI as sg
from pdf2image import convert_from_path

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

def pdf_maker_single_page():
    url = r'C:\Users\Admin\Documents\Invoice Recipts\doc files\doc new\Monka Walch.pdf'
    images = convert_from_path(url)
    images[0].save('pagex'+'.jpg', 'JPEG')

