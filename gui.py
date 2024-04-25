from random import randint
import PySimpleGUI as sg

def random_color():
    return '#%02X%02X%02X' % (randint(0,255), randint(0,255), randint(0,255))

class Button(sg.Column):

    def __init__(self, *args, bd_color='yellow', **kwargs):
        self.button = sg.Button(*args, **kwargs)
        super().__init__([[self.button]], background_color=bd_color, key=self.button.Key+' Border')

    def bd_color(self, color):
        self.button.widget.master.configure(bg=color)

sg.theme("Black")
sg.set_options(font=("Courier New", 16))

layout = [
    [
        Button("TK Button",disabled=True,use_ttk_buttons=False,disabled_button_color="black", border_width=0, bd_color='green',  mouseover_colors=('white', 'white'), pad=(2, 3)),
        Button("TTK Button", disabled=True,use_ttk_buttons=True,disabled_button_color="white", border_width=0, bd_color='yellow', mouseover_colors=('white', 'white'), pad=(5, 0,0,5)),
    ],
]

window = sg.Window('Title', layout, finalize=True)

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event.endswith('Button'):
        window[event+' Border'].bd_color(random_color())

window.close()