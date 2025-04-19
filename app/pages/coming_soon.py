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

    # Add head elements with modern, high-impact fonts and enhanced styles
    ui.add_head_html('''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Montserrat:wght@300;400;600;800&display=swap" rel="stylesheet">
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
                overflow: hidden;
                font-family: 'Montserrat', sans-serif;
            }
            .abril-fatface {
                font-family: 'Abril Fatface', cursive;
            }
            .input-placeholder::placeholder {
                color: rgba(189, 224, 56, 0.6);
                font-weight: 400;
            }
            @keyframes pulse {
                0% { transform: scale(1); opacity: 0.8; }
                50% { transform: scale(1.05); opacity: 1; }
                100% { transform: scale(1); opacity: 0.8; }
            }
            .pulse-animation {
                animation: pulse 3s infinite ease-in-out;
            }
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
                100% { transform: translateY(0px); }
            }
            .float-animation {
                animation: float 6s infinite ease-in-out;
            }
            .btn-signup:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 15px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
            }
            .main-container {
                transition: all 0.5s ease-in-out;
            }
            .main-container:hover {
                box-shadow: 0 15px 45px rgba(0,31,63,0.2);
            }
        </style>
    ''')

    with ui.element('div').style(
            'width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; padding: 0;'
    ):
        # Fullscreen video background with darker overlay for better contrast
        ui.element('div').style(
            'position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.3); z-index: 0;'
        )

        ui.video('/static/tandemexit_sunset_clouds.mp4',
                 autoplay=True,
                 controls=False,
                 muted=True,
                 loop=True,
                 ).style(
            'position: absolute; top: 0; left: 0; z-index: -1; width: 100%; height: 100%; object-fit: cover;')

        # Modern glass container with refined styling
        with ui.element('div').classes('main-container').style(
                'position: relative; z-index: 1; background-color: rgba(16,69,79,0.15); backdrop-filter: blur(1px); '
                'padding: 3.5rem; border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.15); '
                'box-shadow: 0 15px 35px rgba(0,0,0,0.25); display: flex; flex-direction: column; align-items: center; '
                'text-align: center; max-width: 1200px; transition: all 0.3s ease;'):
            # Logo section
            with ui.element('div').classes('float-animation').style('margin-bottom: 2rem;'):
                ui.label('Free Fall Central').classes('abril-fatface').style(
                    'color: #BDE038; font-size: 5rem; margin-bottom: 0.5rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.7); '
                    'font-weight: 1000; letter-spacing: 2px;')

            # Subtitle with more modern styling
            ui.label('Your Ultimate Skydiving Journey Awaits').style(
                'color: white; font-size: 1.75rem; margin-bottom: 2rem; font-weight: 600; '
                'text-shadow: 1px 1px 4px rgba(0,0,0,0.7); letter-spacing: 1px;')

            # Coming Soon with animated effect
            ui.label('Coming Soon...').classes('abril-fatface pulse-animation').style(
                'color: #BDE038; font-size: 3.5rem; font-weight: bold; margin-bottom: 2.5rem; '
                'text-shadow: 1px 1px 8px rgba(0,0,0,0.7); letter-spacing: 3px;')

            # Description text with improved readability
            ui.label("We're crafting a hub for the ultimate skydiving experiences!").style(
                'color: white; font-size: 1.5rem; margin-bottom: 1.5rem; font-weight: 500; '
                'text-shadow: 1px 1px 3px rgba(0,0,0,0.7); max-width: 90%;')

            ui.label("Be the first to know about our exclusive launch offers").style(
                'color: white; margin-bottom: 2.5rem; font-size: 1.5rem; font-weight: 500; '
                'text-shadow: 1px 1px 3px rgba(0,0,0,0.7); max-width: 90%;')

            # Sign up form with modern, sleek styling
            with ui.row().classes('w-full').style(
                    'display: flex; align-items: center; gap: 1rem; width: 100%; justify-content: center; margin-top: 1rem;'):
                with ui.row().classes('w-full').style(
                        'display: flex; align-items: center; gap: 1rem; width: 100%; justify-content: center; margin-top: 1rem;'):
                    # Modern input field
                    name_input = ui.input(placeholder="What shall we call you?").classes('input-placeholder').props(
                        'input-style="color: white; font-weight: 500;" input-class="font-mono"').style(
                        'padding: 1rem 1.25rem; border-radius: 0.75rem; border: 1px solid rgba(189,224,56,0.3); '
                        'background: rgba(16,69,79,0.5); width: 20rem; font-size: 1.1rem; '
                        'box-shadow: inset 0 2px 4px rgba(0,0,0,0.3); '
                        'backdrop-filter: blur(4px); transition: all 0.3s ease;'
                    )

                    email_input = ui.input(placeholder="Enter your email address").classes('input-placeholder').props(
                        'input-style="color: white; font-weight: 500;" input-class="font-mono"').style(
                        'padding: 1rem 1.25rem; border-radius: 0.75rem; border: 1px solid rgba(189,224,56,0.3); '
                        'background: rgba(16,69,79,0.5); width: 20rem; font-size: 1.1rem; '
                        'box-shadow: inset 0 2px 4px rgba(0,0,0,0.3); '
                        'backdrop-filter: blur(4px); transition: all 0.3s ease;'
                )

                # High-impact button styling
                ui.button('SIGN UP', on_click=lambda: handle_signup(email_input.value), color=None).classes(
                    'btn-signup').style(
                    'background: linear-gradient(135deg, #BDE038 66%, #506266 100%); color: #10454F; font-weight: 800; '
                    'padding: 1rem 2rem; border-radius: 0.75rem; border: none; cursor: pointer; '
                    'box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-transform: uppercase; letter-spacing: 2px; '
                    'transition: all 0.3s ease; font-size: 1.1rem;')

            # Social proof or additional trust elements
            with ui.element('div').style('margin-top: 2.5rem; opacity: 0.9;'):
                ui.label("'He who leaps into the void, owes no explanation to those who merely stand and watch'").style(
                    'color: rgba(255,255,255,0.8); font-size: 1rem; font-weight: 400; letter-spacing: 0.5px; text-shadow: 1px 3px 8px #000000;')


def handle_signup(email):
    # You can implement your signup logic here
    print(f"Signup requested with email: {email}")
    # Add database insertion, email confirmation, etc.

    # Example of showing a confirmation dialog
    ui.notify('Thanks for signing up! We\'ll notify you when we launch.', type='positive', position='bottom')