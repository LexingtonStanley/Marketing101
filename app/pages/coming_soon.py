import re
import os
from nicegui import ui, app, APIRouter
from datetime import datetime, timedelta
import json

from app.helper_funcs.DirectoryFinder import DirectoryFinder
from app.helper_funcs.database.database_functions import Freefallcentral_Database

db = Freefallcentral_Database()
coming_soon = APIRouter()
df = DirectoryFinder()
static_path = df.get_data_dir('static', create_if_missing=True, project_markers=['main.py'])


# This should be in main.py, not in the router file
# app.add_static_files('/static', static_path)

@coming_soon.page('/coming_soon', dark=True)
def create_coming_soon():
    video_path = os.path.join(static_path, 'tandemexit_sunset_clouds.mp4')

    # Track coming_soon page view
    ui.add_body_html('''
    <script>
        gtag('event', 'page_view', {
            'page_title': 'Coming Soon',
            'page_location': window.location.href,
            'page_path': '/coming_soon'
        });
    </script>
    ''')

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

    # Advanced tracking scripts for background data collection
    ui.add_body_html('''
    <script>
        // Enhanced tracking for skydiving website

        // 1. Track scroll depth for engagement measurement
        window.scrollDepthTracked = {};
        window.addEventListener('scroll', function() {
            let scrollPercentage = Math.floor((window.scrollY + window.innerHeight) / document.body.scrollHeight * 100);

            // Report at 25%, 50%, 75%, and 100% scroll depth
            if (scrollPercentage >= 25 && !window.scrollDepthTracked['25']) {
                window.scrollDepthTracked['25'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '25%',
                    'page': 'coming_soon'
                });
            } else if (scrollPercentage >= 50 && !window.scrollDepthTracked['50']) {
                window.scrollDepthTracked['50'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '50%',
                    'page': 'coming_soon'
                });
            } else if (scrollPercentage >= 75 && !window.scrollDepthTracked['75']) {
                window.scrollDepthTracked['75'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '75%',
                    'page': 'coming_soon' 
                });
            } else if (scrollPercentage >= 95 && !window.scrollDepthTracked['100']) {
                window.scrollDepthTracked['100'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '100%',
                    'page': 'coming_soon'
                });
            }
        });

        // 2. Track time on page
        let startTime = new Date();
        window.addEventListener('beforeunload', function() {
            let endTime = new Date();
            let timeSpent = Math.floor((endTime - startTime) / 1000);  // in seconds

            gtag('event', 'time_on_page', { 
                'seconds': timeSpent,
                'page': 'coming_soon'
            });
        });

        // 3. Track clicks on different elements
        document.addEventListener('click', function(e) {
            // Try to identify what was clicked
            let targetElement = e.target;
            let elementType = targetElement.tagName;
            let elementClass = targetElement.className;
            let elementId = targetElement.id;

            // Only track meaningful clicks (not just background)
            if (elementType || elementClass || elementId) {
                gtag('event', 'element_click', {
                    'element_type': elementType,
                    'element_class': elementClass,
                    'element_id': elementId
                });
            }
        });

        // 4. Try to get user's location for weather data (with IP address fallback)
        function getLocationData() {
            // First try to get precise location from browser
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    // Send precise location data to Google Analytics
                    gtag('event', 'location_captured', {
                        'source': 'browser_geolocation',
                        'latitude': position.coords.latitude,
                        'longitude': position.coords.longitude,
                        'accuracy': position.coords.accuracy
                    });

                    // Store for form submission
                    window.userLocation = {
                        source: 'browser_geolocation',
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                        accuracy: position.coords.accuracy
                    };

                    // Try to get weather data based on coordinates
                    try {
                        fetch(`https://api.open-meteo.com/v1/forecast?latitude=${position.coords.latitude}&longitude=${position.coords.longitude}&current=temperature,wind_speed,wind_direction,weather_code`)
                        .then(response => response.json())
                        .then(data => {
                            if (data && data.current) {
                                gtag('event', 'weather_data', {
                                    'temperature': data.current.temperature,
                                    'wind_speed': data.current.wind_speed,
                                    'wind_direction': data.current.wind_direction,
                                    'weather_code': data.current.weather_code
                                });

                                // Store weather data for later use
                                window.weatherData = data.current;
                            }
                        });
                    } catch (e) {
                        console.log("Weather API call failed");
                    }
                }, function(error) {
                    // User declined location sharing - fallback to IP geolocation
                    gtag('event', 'location_declined', {
                        'error_code': error.code,
                        'error_message': error.message
                    });

                    // Fall back to IP-based geolocation
                    getIPBasedLocation();
                });
            } else {
                // Browser doesn't support geolocation - fallback to IP
                getIPBasedLocation();
            }
        }

        // Fallback function to get location from IP address
        function getIPBasedLocation() {
            // Use a free IP geolocation service
            fetch('https://ipapi.co/json/')
            .then(response => response.json())
            .then(data => {
                // Log the IP-based location data
                gtag('event', 'location_captured', {
                    'source': 'ip_geolocation',
                    'ip': data.ip,
                    'city': data.city,
                    'region': data.region,
                    'country': data.country_name,
                    'latitude': data.latitude,
                    'longitude': data.longitude
                });

                // Store for later use
                window.userLocation = {
                    source: 'ip_geolocation',
                    ip: data.ip,
                    city: data.city,
                    region: data.region,
                    country: data.country_name,
                    lat: data.latitude,
                    lng: data.longitude
                };

                // Now get weather data based on these coordinates
                if (data.latitude && data.longitude) {
                    try {
                        fetch(`https://api.open-meteo.com/v1/forecast?latitude=${data.latitude}&longitude=${data.longitude}&current=temperature,wind_speed,wind_direction,weather_code`)
                        .then(response => response.json())
                        .then(weatherData => {
                            if (weatherData && weatherData.current) {
                                gtag('event', 'weather_data', {
                                    'source': 'ip_geolocation',
                                    'temperature': weatherData.current.temperature,
                                    'wind_speed': weatherData.current.wind_speed,
                                    'wind_direction': weatherData.current.wind_direction,
                                    'weather_code': weatherData.current.weather_code
                                });

                                // Store weather data
                                window.weatherData = weatherData.current;
                            }
                        });
                    } catch (e) {
                        console.log("Weather API call failed");
                    }
                }
            })
            .catch(error => {
                console.log("IP geolocation failed: ", error);
                // Could add another fallback here if needed
            });
        }

        // 5. Track device capabilities
        function trackDeviceCapabilities() {
            // Screen dimensions
            gtag('event', 'device_info', {
                'screen_width': window.screen.width,
                'screen_height': window.screen.height,
                'pixel_ratio': window.devicePixelRatio,
                'is_mobile': /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent),
                'browser': navigator.userAgent,
                'language': navigator.language,
                'timezone': Intl.DateTimeFormat().resolvedOptions().timeZone,
                'connection_type': navigator.connection ? navigator.connection.effectiveType : 'unknown'
            });
        }

        // 6. Track form interactions
        function setupFormTracking() {
            // Track form field focus and blur events
            document.querySelectorAll('input, button').forEach(function(element) {
                element.addEventListener('focus', function() {
                    gtag('event', 'form_field_focus', {
                        'field_type': element.type,
                        'field_name': element.name || element.id || element.placeholder
                    });
                });

                if (element.type === 'text' || element.type === 'email') {
                    element.addEventListener('blur', function() {
                        gtag('event', 'form_field_completed', {
                            'field_type': element.type,
                            'field_name': element.name || element.id || element.placeholder,
                            'has_value': element.value.length > 0
                        });
                    });
                }
            });
        }

        // Run all our tracking functions when page loads
        window.addEventListener('load', function() {
            getLocationData();
            trackDeviceCapabilities();
            setupFormTracking();

            // Start session timer
            gtag('event', 'session_start', {
                'timestamp': new Date().toISOString(),
                'referrer': document.referrer
            });
        });
        // Function to get and store client info
        function storeClientInfo() {
            // Create a hidden form field with the user agent
            let hiddenUA = document.createElement('input');
            hiddenUA.type = 'hidden';
            hiddenUA.id = 'hidden_user_agent';
            hiddenUA.name = 'user_agent';
            hiddenUA.value = navigator.userAgent;
            document.body.appendChild(hiddenUA);
            
            // Use a service to get IP
            fetch('https://api.ipify.org?format=json')
            .then(response => response.json())
            .then(data => {
                let hiddenIP = document.createElement('input');
                hiddenIP.type = 'hidden';
                hiddenIP.id = 'hidden_ip_address';
                hiddenIP.name = 'ip_address';
                hiddenIP.value = data.ip;
                document.body.appendChild(hiddenIP);
            });
        }
        
        // Run when page loads
        window.addEventListener('load', storeClientInfo);
    </script>
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
                ui.label('Your Ultimate Skydiving Adventure Awaits').style(
                    'color: white; font-size: 1.75rem; margin-bottom: 2rem; font-weight: 700; '
                    'text-shadow: 2px 2px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7); letter-spacing: 1px; '
                    'text-decoration: underline;')

                # Coming Soon with animated effect
                ui.label('Coming Soon...').classes('abril-fatface pulse-animation').style(
                    'color: #BDE038; font-size: 3.5rem; font-weight: bold; margin-bottom: 2.5rem; '
                    'text-shadow: 2px 2px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7); letter-spacing: 3px;')

                # Description text with improved readability and shadow
                ui.label(
                    "From Tandem Skydives with the experts, to Accelerated Free Fall Courses (AFF) and licenced skydiving. We're crafting a hub for the ultimate skydiving experience!").style(
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
                    ui.button('SIGN UP',
                              on_click=lambda: handle_signup_with_client_info(name_input.value, email_input.value),
                              color=None).classes('btn-signup').style(
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



async def handle_signup_with_client_info(name, email):
    # Get client info from JavaScript
    ip_result = await ui.run_javascript('return document.getElementById("hidden_ip_address").value;')
    ua_result = await ui.run_javascript('return document.getElementById("hidden_user_agent").value;')

    ip_address = ip_result if ip_result else 'unknown'
    user_agent = ua_result if ua_result else 'unknown'
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Validate email format
    if not re.match(email_pattern, email):
        ui.notify('Please enter a valid email address', type='negative', position='bottom')
        return

    # Get the current timestamp
    timestamp = datetime.now()

    # Store data in database
    try:
        await db.check_and_create_table('coming_soon')

        async with db.db_connector.get_cursor() as cur:
            await cur.execute(
                "INSERT INTO coming_soon (name, email, ip_address, user_agent, timestamp) VALUES (%s, %s, %s, %s, %s)",
                (name, email, ip_address, user_agent, timestamp)
            )

        print(f"Successfully stored signup: {name} ({email}) from IP: {ip_address}")
    except Exception as e:
        error_message = str(e)
        print(f"Database error: {error_message}")

        if "unique constraint" in error_message.lower():
            ui.notify('This email is already registered with us', type='warning', position='bottom')
            return
        else:
            ui.notify('There was an error processing your signup', type='negative', position='bottom')
            return

    # Track this signup event in Google Analytics with all the data we have
    ui.add_body_html(f'''
    <script>
        // Get any location data we might have collected (browser or IP-based)
        let locationData = window.userLocation || {{}};
        let weatherData = window.weatherData || {{}};

        // Track the signup event with all available data
        gtag('event', 'signup_complete', {{
            'event_category': 'conversion',
            'event_label': 'newsletter',
            'user_name': '{name}',
            'timestamp': '{timestamp}',
            'ip_address': '{ip_address}',  // Always include IP address
            'location_data': locationData,
            'weather_data': weatherData,
            'device_info': {{
                'screen_width': window.screen.width,
                'screen_height': window.screen.height,
                'is_mobile': /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
            }}
        }});

        // If no location data was obtained yet, try IP geolocation now
        if (!locationData.lat && !locationData.lng) {{
            fetch('https://ipapi.co/json/')
            .then(response => response.json())
            .then(data => {{
                // Send this data to Google Analytics
                gtag('event', 'location_captured_at_signup', {{
                    'source': 'ip_geolocation_at_signup',
                    'ip': data.ip,
                    'city': data.city,
                    'region': data.region,
                    'country': data.country_name,
                    'latitude': data.latitude,
                    'longitude': data.longitude
                }});

                // Also try to get weather data for this location
                if (data.latitude && data.longitude) {{
                    fetch(`https://api.open-meteo.com/v1/forecast?latitude=${{data.latitude}}&longitude=${{data.longitude}}&current=temperature,wind_speed,wind_direction,weather_code`)
                    .then(response => response.json())
                    .then(weatherData => {{
                        if (weatherData && weatherData.current) {{
                            gtag('event', 'weather_data_at_signup', {{
                                'source': 'ip_geolocation',
                                'temperature': weatherData.current.temperature,
                                'wind_speed': weatherData.current.wind_speed,
                                'wind_direction': weatherData.current.wind_direction,
                                'weather_code': weatherData.current.weather_code
                            }});
                        }}
                    }});
                }}
            }});
        }}

        // Set user properties for better segmentation
        gtag('set', 'user_properties', {{
            'signed_up': true,
            'signup_date': '{timestamp.strftime("%Y-%m-%d")}',
            'email_domain': '{email.split("@")[1] if "@" in email else "unknown"}'
        }});
    </script>
    ''')

    # Show confirmation notification
    ui.notify(f'Thanks for signing up, {name}! We\'ll notify you when we launch.',
              type='positive', position='bottom')