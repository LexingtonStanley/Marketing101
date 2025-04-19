from nicegui import ui, app, APIRouter
from datetime import datetime, timedelta
import os

from app.helper_funcs.DirectoryFinder import DirectoryFinder


coming_soon = APIRouter()
df = DirectoryFinder()
static_path = df.get_data_dir('static', create_if_missing=True, project_markers=['main.py'])


# This should be in main.py, not in the router file
# app.add_static_files('/static', static_path)

@coming_soon.page('/coming_soon', dark=True)
def create_coming_soon():
    video_path = os.path.join(static_path, 'tandemexit_sunset_clouds.mp4')
    print(f"Looking for video at: {video_path}")
    print(f"File exists: {os.path.exists(video_path)}")

    # Add head elements with custom font and styles
    ui.add_head_html('''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap" rel="stylesheet">
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            .abril-fatface {
                font-family: 'Abril Fatface', cursive;
            }
            .custom-input::value {
                color: #10454F;
                opacity: 0.1;
            }
        </style>
    ''')

    with ui.element('div').style(
            'width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; padding: 2rem;'
    ):
        # Keep your original video implementation
        ui.video('/static/tandemexit_sunset_clouds.mp4',
                 autoplay=True,
                 controls=False,
                 loop=True,
                 ).style(
            'position: absolute; top: 0; left: 0; z-index: 0; width: 100%; height: 100%; object-fit: cover;')

        # Updated styling for the content container - using glass morphism effect
        with ui.element('div').style(
                'position: relative; z-index: 1; background-color: rgba(255,255,255,0.15); backdrop-filter: blur(1px); padding: 3rem; border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 8px 32px rgba(0,31,63,0.1); display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 650px;'):
            # Title with Abril Fatface font
            ui.label('Free Fall Central').classes('abril-fatface').style(
                'color: #10454F; font-size: 4.5rem; margin-bottom: 0.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.5), 0px 0px 30px rgba(255,255,255,0.7); font-weight: 1000; letter-spacing: 1px;')

            # Subtitle
            ui.label('Your Ultimate Skydiving Journey Awaits').style(
                'color: #3f4d4f; font-size: 1.75rem; margin-bottom: 1.5rem; font-weight: 750; text-shadow: 1px 1px 4px rgba(0,0,0,0.5), 4px 4px 8px rgba(255,255,255,0.5);')

            # Coming Soon with Abril Fatface for impact
            ui.label('Coming Soon...').classes('abril-fatface').style(
                'color: #BDE038; font-size: 3rem; font-weight: bold; margin-bottom: 2rem; text-shadow: 1px 1px 4px rgba(0,0,0,0.5), 0px 0px 8px rgba(255,255,255,0.8); letter-spacing: 2px;')

            # Description text
            ui.label("We're working hard to create the perfect skydiving booking experience!").style(
                'color: #3f4d4f; font-size: 1.5rem; margin-bottom: 1rem; font-weight: 600; text-shadow: 1px 1px 4px rgba(0,0,0,0.5), 0px 0px 8px rgba(255,255,255,0.8); max-width: 90%;')
            ui.label("Enter your details below to receive Offers with our Grand Opening").style(
                'color: #3f4d4f; margin-bottom: 1.5rem; font-size: 1.5rem; font-weight: 600; text-shadow: 1px 1px 4px rgba(0,0,0,0.5), 0px 0px 8px rgba(255,255,255,0.8); max-width: 90%;')

            ui.separator().style('width: 80%; margin-bottom: 1.5rem; opacity: 0.3;')

            # Sign up form with improved styling
            with ui.row().classes('w-full').style(
                    'display: flex; align-items: center; gap: 1rem; width: 100%; justify-content: center;'):
                email_input = ui.input(placeholder="Enter your email address").props(
                    'input-style="color: #BDE038; font-weight: bold" input-class="font-mono"').style(
                    'padding: 0.75rem 1rem; border-radius: 0.5rem; border: 1px solid rgba(0,0,0,0.1); '
                    'background: linear-gradient(285deg, #3f4d4f 95%, #BDE038 100%); width: 25rem; font-size: 1rem; '
                    'box-shadow: inset 0 2px 4px rgba(0,0,0,0.5); '
                    'text-shadow: 0px 0px 10px rgba(0,0,0,0.5);'
                )

                # Energetic button styling
                ui.button('SIGN UP', on_click=lambda: print('hello'), color=None).style(
                    'background: linear-gradient(135deg, #10454F 0%, #506266 100%); color: #BDE038; font-weight: bold; padding: 0.75rem 2rem; border-radius: 0.5rem; border: none; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-transform: uppercase; letter-spacing: 1px;')

        print('hello3')