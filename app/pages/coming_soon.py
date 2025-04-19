from nicegui import ui, app, APIRouter
from datetime import datetime, timedelta
import os

from pandas.core.dtypes.common import classes

from app.helper_funcs.DirectoryFinder import DirectoryFinder

coming_soon = APIRouter()
df = DirectoryFinder()
static_path = df.get_data_dir('static', create_if_missing=True, project_markers=['main.py'])

# This should be in main.py, not in the router file
# app.add_static_files('/static', static_path)

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
        ui.video('/static/tandemexit_sunset_clouds.mov', autoplay=True, controls=False, loop=True),classes('w-full h-full')
        ui.label('Coming Soon...').style('position: absolute; color: white; font-size: 2rem; font-weight: bold;')
        print('hello3')