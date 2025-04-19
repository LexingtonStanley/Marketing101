from nicegui import ui, app
from datetime import datetime, timedelta
import os

from app.pages.coming_soon import coming_soon, static_path

ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=falling" />

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XS13949XKS"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-XS13949XKS', {
            'send_page_view': true,
            'cookie_flags': 'samesite=none;secure',
            'anonymize_ip': false
        });
    </script>
''')

# Add static files here in main.py, not in the router
app.add_static_files('/static', static_path)


@ui.page('/')
def index():
    print('hello2')
    # Track page navigation event
    ui.add_body_html('''
    <script>
        gtag('event', 'page_view', {
            'page_title': 'Home',
            'page_location': window.location.href,
            'page_path': '/'
        });
    </script>
    ''')
    ui.navigate.to('/coming_soon')


app.include_router(coming_soon)

if __name__ in {"__main__", "__mp_main__"}:
    print('hello')

    ui.run(title='Free Fall Central - The Skydiving Hub', port=8080)