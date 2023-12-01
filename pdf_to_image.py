import PySimpleGUI as sg
from pdf2image import convert_from_path
import os

def matcher(a, b, c):
    if a == True and b == 'png':
        first_page_as_png(c)
    elif a == True and b == 'jpg':
        first_page_as_jpg(c)
    elif a == False and b == 'png':
        multi_pages_as_png(c)
    else:
        multi_pages_as_jpg(c)

def first_page_as_png(url):
    parent_folder = os.path.dirname(url)
    base_name = os.path.basename(url)
    base_name_without_extension = os.path.splitext(base_name)[0]
    base_name_formatted = str(base_name_without_extension)
    os.chdir(parent_folder)
    images = convert_from_path(url)
    images[0].save(base_name_formatted + '.png')


def first_page_as_jpg(url):
    parent_folder = os.path.dirname(url)
    base_name = os.path.basename(url)
    base_name_without_extension = os.path.splitext(base_name)[0]
    base_name_formatted = str(base_name_without_extension)
    os.chdir(parent_folder)
    images = convert_from_path(url)
    images[0].save(base_name_formatted + '.jpg')

#######################
#Window Initialization#
#######################


def main():
    sg.theme('LightBrown7')
    
    extensions = ['png', 'jpg']
    layout = [[sg.Input(key='-file_path-', visible=False), sg.FileBrowse('Select', font=('Georgia 18'), file_types=(('PDF Files', '*.pdf'),), enable_events=True)], [sg.Checkbox('First Page Only', default=True, key='-CHECKED-')], [sg.Combo(extensions, key="inp", default_value="png", enable_events= True, font=('Arial 18')), sg.Button('Convert', font=('Arial 17'), enable_events=True)]]
    
    window = sg.Window('PDF to Image', layout, size=(370, 160), resizable=False, element_justification='c')
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        if event == 'Convert':
            checkbox_status = values['-CHECKED-']
            combobox_status = values['inp']
            file_paths = values['-file_path-']
            matcher(checkbox_status, combobox_status, file_paths)



main()

