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
                font-family: 'Montserrat', sans-serif;
                /* Remove overflow: hidden to allow scrolling */
            }
            /* Add text stroke to make text pop on any background */
            .text-with-stroke {
                -webkit-text-stroke: 1px rgba(0,0,0,0.3);
                text-stroke: 1px rgba(0,0,0,0.3);
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
            /* New styles for scroll container */
            .scroll-container {
                min-height: 100vh;
                width: 100%;
                position: relative;
                overflow-y: auto;
                overflow-x: hidden;
                scroll-behavior: smooth;
            }
            /* Make sure the video covers the entire area even when scrolling */
            .video-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
            }
            .content-wrapper {
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 2rem 1rem;
                position: relative;
                z-index: 2;
            }
        </style>
    ''')

    # Create a scrollable container for the entire page
    with ui.element('div').classes('scroll-container'):
        # Fixed video background
        with ui.element('div').classes('video-container'):
            # Overlay for better contrast - darker for better text readability
            ui.element('div').style(
                'position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5); z-index: 0;'
            )

            # Video element
            ui.video('/static/tandemexit_sunset_clouds.mp4',
                     autoplay=True,
                     controls=False,
                     muted=True,
                     loop=True,
                     ).style(
                'position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;')

        # Content wrapper that ensures proper centering and spacing
        with ui.element('div').classes('content-wrapper'):
            # Modern glass container with refined styling and darker background for better contrast
            with ui.element('div').classes('main-container').style(
                    'position: relative; z-index: 1; background-color: rgba(16,69,79,0.35); backdrop-filter: blur(1.5px); '
                    'padding: 3.5rem; border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.15); '
                    'box-shadow: 0 15px 35px rgba(0,0,0,0.4); display: flex; flex-direction: column; align-items: center; '
                    'text-align: center; max-width: 1200px; transition: all 0.3s ease; margin: 2rem 0;'):
                # Logo section with enhanced visibility
                with ui.element('div').classes('float-animation').style('margin-bottom: 2rem;'):
                    ui.label('Free Fall Central').classes('abril-fatface text-with-stroke').style(
                        'color: #BDE038; font-size: 5rem; margin-bottom: 0.5rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.9), 0 0 30px rgba(0,0,0,0.7); '
                        'font-weight: 1000; letter-spacing: 2px;')

                # Subtitle with more modern styling and enhanced shadow
                ui.label('Your Ultimate Skydiving Journey Awaits').style(
                    'color: white; font-size: 1.75rem; margin-bottom: 2rem; font-weight: 700; '
                    'text-shadow: 2px 2px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7); letter-spacing: 1px;')

                # Coming Soon with animated effect
                ui.label('Coming Soon...').classes('abril-fatface pulse-animation').style(
                    'color: #BDE038; font-size: 3.5rem; font-weight: bold; margin-bottom: 2.5rem; '
                    'text-shadow: 2px 2px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7); letter-spacing: 3px;')

                # Description text with improved readability and shadow
                ui.label("From Tandem Skydives with the experts, to Accelerated Free Fall Courses (AFF) and licenced skydiving. We're crafting a hub for the ultimate skydiving experience!").style(
                    'color: white; font-size: 1.5rem; margin-bottom: 1.5rem; font-weight: 600; '
                    'text-shadow: 2px 2px 6px rgba(0,0,0,0.9), 0 0 15px rgba(0,0,0,0.8); max-width: 90%;')

                ui.label("Be the first to know about our exclusive launch offers").style(
                    'color: white; margin-bottom: 2.5rem; font-size: 1.5rem; font-weight: 600; '
                    'text-shadow: 2px 2px 6px rgba(0,0,0,0.9), 0 0 15px rgba(0,0,0,0.8); max-width: 90%;')

                # Sign up form with modern, sleek styling
                with ui.element('div').style(
                        'display: flex; flex-direction: column; align-items: center; gap: 1.5rem; width: 100%; justify-content: center; margin-top: 1rem;'):
                    # Input fields row
                    with ui.element('div').style(
                            'display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; width: 100%; justify-content: center;'):
                        # Modern input field
                        name_input = ui.input(placeholder="What shall we call you?").classes('input-placeholder').props(
                            'input-style="color: white; font-weight: 500;" input-class="font-mono"').style(
                            'padding: 1rem 1.25rem; border-radius: 0.75rem; border: 1px solid rgba(189,224,56,0.3); '
                            'background: rgba(16,69,79,0.5); width: 20rem; font-size: 1.1rem; '
                            'box-shadow: inset 0 2px 4px rgba(0,0,0,0.3); '
                            'backdrop-filter: blur(8px); transition: all 0.3s ease;'
                        )

                        email_input = ui.input(placeholder="Enter your email address").classes(
                            'input-placeholder').props(
                            'input-style="color: white; font-weight: 500;" input-class="font-mono"').style(
                            'padding: 1rem 1.25rem; border-radius: 0.75rem; border: 1px solid rgba(189,224,56,0.3); '
                            'background: rgba(16,69,79,0.5); width: 20rem; font-size: 1.1rem; '
                            'box-shadow: inset 0 2px 4px rgba(0,0,0,0.3); '
                            'backdrop-filter: blur(8px); transition: all 0.3s ease;'
                        )

                    # Button in its own container for better mobile layout
                    # High-impact button styling
                    ui.button('SIGN UP', on_click=lambda: handle_signup(name_input.value, email_input.value),
                              color=None).classes(
                        'btn-signup').style(
                        'background: linear-gradient(135deg, #BDE038 66%, #506266 100%); color: #10454F; font-weight: 800; '
                        'padding: 1rem 2rem; border-radius: 0.75rem; border: none; cursor: pointer; '
                        'box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-transform: uppercase; letter-spacing: 2px; '
                        'transition: all 0.3s ease; font-size: 1.1rem;')

                # Social proof or additional trust elements
                with ui.element('div').style('margin-top: 2.5rem; opacity: 0.9;'):
                    ui.separator()
                    ui.label(
                        "'He who leaps into the void, owes no explanation to those who merely stand and watch'").style(
                    'color: white; margin-bottom: 1.5rem; margin-top: 1.5rem; font-size: 1.1rem; font-weight: 300; '
                    'text-shadow: 2px 2px 6px rgba(0,0,0,0.9), 0 0 15px rgba(0,0,0,0.8); max-width: 100%;')
                    ui.separator()
def handle_signup(name, email):
    # Enhanced signup logic that includes name field
    print(f"Signup requested for {name} with email: {email}")
    # Add database insertion, email confirmation, etc.

    # Example of showing a confirmation dialog
    ui.notify(f'Thanks for signing up, {name}! We\'ll notify you when we launch.', type='positive', position='bottom')