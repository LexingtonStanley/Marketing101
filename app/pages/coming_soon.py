from nicegui import ui, app, APIRouter
from datetime import datetime, timedelta
import os
#from app.helper_funcs.DirectoryFinder import DirectoryFinder as DF

coming_soon = APIRouter()
#static_path = DF().get_data_dir('static', create_if_missing=False, project_markers=['main.py'])

#app.add_media_files('/static', static_path)

@coming_soon.page('/coming_soon', dark=True)
def create_coming_soon():
    # Add CSS to ensure full height for parent elements
    ui.add_head_html('''
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
        </style>
    ''')

    with ui.element('div').style(
            'width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; padding: 2rem;'
    ):
        #ui.video('static/tandemexit_sunset_clouds.mov', autoplay=True, controls=False, loop=True)
        ui.label('Coming Soon...')
        print('hello')

#if __name__ in {"__main__", "__mp_main__"}:
 #   print(static_path)