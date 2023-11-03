import PySimpleGUI as sg

#######################
#Window Initialization#
#######################

sg.theme('LightBrown7')

extensions = ['png', 'jpg']
layout = [[sg.Input()], [sg.Button('Select', font=('Georgia 18'))], [sg.Combo(extensions, key="inp", font=('Forte', 18)), sg.Button('Convert', font=('OCR\ B\ MT 18'))]]

window = sg.Window('PDF to Image', layout, size=(370, 135), resizable=False, element_justification='c')

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel':
		break

