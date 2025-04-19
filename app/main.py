from nicegui import ui, app
from datetime import datetime, timedelta
import os

from app.pages.coming_soon import coming_soon, static_path

ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=falling" />
''')

# Add static files here in main.py, not in the router
app.add_static_files('/static', static_path)

@ui.page('/')
def index():
    print('hello2')
    ui.navigate.to('/coming_soon')

app.include_router(coming_soon)

if __name__ in {"__main__", "__mp_main__"}:
    print('hello')

    ui.run(title='Free Fall Central', port=8080)