from nicegui import ui, app
from datetime import datetime, timedelta
import os

from app.pages.coming_soon import coming_soon

ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=falling" />
''')

@ui.page('/')
def index():
    print('hello')
    ui.navigate.to('/coming_soon')

app.include_router(coming_soon)

if __name__ in {"__main__", "__mp_main__"}:
    print('hello')

    ui.run(title='Free Fall Central', port=8080)
