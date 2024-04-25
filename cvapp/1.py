import time

from nicegui import ui, core
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

def hide(event: ValueChangeEventArguments):
    print(core.app.native.main_window.hide())
    name = type(event.sender).__name__
    ui.notify(f'{name}')
    time.sleep(2)
    core.app.native.main_window.show()

ui.button('hide', on_click=hide)

with ui.row():
    ui.table(columns=[{1:2}], rows=[{1:2},{1:2},{1:2},{1:2},])
    ui.checkbox('Checkbox', on_change=show)
    ui.switch('Switch', on_change=show)
ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')
# print(dir(core))
# print(dir(ui))
ui.run(native=True)