import re
import os
import json
from nicegui import ui, app, APIRouter
from datetime import datetime, timedelta

from app.helper_funcs.DirectoryFinder import DirectoryFinder
from app.helper_funcs.database.database_functions import Freefallcentral_Database

db = Freefallcentral_Database()
coming_soon = APIRouter()
df = DirectoryFinder()
static_path = df.get_data_dir('static', create_if_missing=True, project_markers=['main.py'])


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

    # Modified tracking scripts with FIXED weather and location data collection
    ui.add_body_html('''
    <script>
        // Global object to store all tracking data that will be sent to the database
        window.trackingData = {
            location: {},
            weather: {},
            device: {},
            session: {},
            scrollDepth: {},
            timeOnPage: 0
        };

        // 1. Track scroll depth for engagement measurement
        window.scrollDepthTracked = {};
        window.addEventListener('scroll', function() {
            let scrollPercentage = Math.floor((window.scrollY + window.innerHeight) / document.body.scrollHeight * 100);

            // Report at 25%, 50%, 75%, and 100% scroll depth
            if (scrollPercentage >= 25 && !window.scrollDepthTracked['25']) {
                window.scrollDepthTracked['25'] = true;
                window.trackingData.scrollDepth['25'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '25%',
                    'page': 'coming_soon'
                });
            } else if (scrollPercentage >= 50 && !window.scrollDepthTracked['50']) {
                window.scrollDepthTracked['50'] = true;
                window.trackingData.scrollDepth['50'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '50%',
                    'page': 'coming_soon'
                });
            } else if (scrollPercentage >= 75 && !window.scrollDepthTracked['75']) {
                window.scrollDepthTracked['75'] = true;
                window.trackingData.scrollDepth['75'] = true;
                gtag('event', 'scroll_depth', { 
                    'depth': '75%',
                    'page': 'coming_soon' 
                });
            } else if (scrollPercentage >= 95 && !window.scrollDepthTracked['100']) {
                window.scrollDepthTracked['100'] = true;
                window.trackingData.scrollDepth['100'] = true;
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
            window.trackingData.timeOnPage = timeSpent;

            gtag('event', 'time_on_page', { 
                'seconds': timeSpent,
                'page': 'coming_soon'
            });
        });

        // Update time on page for database storage during signup
        function updateTimeOnPage() {
            let currentTime = new Date();
            let timeSpent = Math.floor((currentTime - startTime) / 1000);  // in seconds
            window.trackingData.timeOnPage = timeSpent;
        }

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

        // FIXED: Get location details from coordinates using OpenStreetMap
        function getLocationDetails(latitude, longitude) {
            console.log(`Getting location details for: ${latitude}, ${longitude}`);

            return fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&accept-language=en`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Network response was not ok: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("Reverse geocoding response:", data);
                    if (data && data.address) {
                        // Find the most appropriate locality name
                        const city = data.address.city || data.address.town || data.address.village || data.address.hamlet || data.address.suburb || null;
                        const region = data.address.state || data.address.county || null;
                        const country = data.address.country || null;

                        console.log(`Location resolved to: ${city}, ${region}, ${country}`);

                        return {
                            city: city,
                            region: region,
                            country: country,
                            display_name: data.display_name || null
                        };
                    }
                    return {};
                })
                .catch(error => {
                    console.log("Reverse geocoding failed:", error);
                    return {};
                });
        }

        // FIXED: Get weather data with cloud cover
        // FIXED: Get weather data with cloud cover as text description
        function getWeatherData(latitude, longitude) {
            console.log(`Getting weather data for: ${latitude}, ${longitude}`);
        
            // Keep the cloud_cover numeric parameter in the API request
            return fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature,weather_code,wind_speed_10m,wind_direction_10m,is_day,cloud_cover`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Network response was not ok: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("Weather data response:", data);
                    if (data && data.current) {
                        // Extract numeric values
                        let cloudCoverNumeric = data.current.cloud_cover;
                        let weatherCode = data.current.weather_code;
                        
                        // If cloud_cover is missing but we have a weather code, estimate it
                        if (cloudCoverNumeric === undefined && weatherCode !== undefined) {
                            // Estimate cloud cover based on weather code
                            if (weatherCode === 0) cloudCoverNumeric = 0;           // Clear sky
                            else if (weatherCode === 1) cloudCoverNumeric = 15;     // Mainly clear
                            else if (weatherCode === 2) cloudCoverNumeric = 50;     // Partly cloudy
                            else if (weatherCode === 3) cloudCoverNumeric = 95;     // Overcast
                            else if ([45, 48].includes(weatherCode)) cloudCoverNumeric = 75; // Fog
                            else if ([51, 53, 55, 56, 57].includes(weatherCode)) cloudCoverNumeric = 85; // Drizzle
                            else if ([61, 63, 65, 66, 67].includes(weatherCode)) cloudCoverNumeric = 90; // Rain
                            else if ([71, 73, 75, 77].includes(weatherCode)) cloudCoverNumeric = 90; // Snow
                            else if ([80, 81, 82, 85, 86].includes(weatherCode)) cloudCoverNumeric = 80; // Showers
                            else if ([95, 96, 99].includes(weatherCode)) cloudCoverNumeric = 95; // Thunderstorm
                        }
                        
                        // Convert numeric cloud cover to text description
                        let cloudCoverText;
                        if (cloudCoverNumeric !== undefined) {
                            if (cloudCoverNumeric < 10) cloudCoverText = "Clear";
                            else if (cloudCoverNumeric < 30) cloudCoverText = "Mostly Clear";
                            else if (cloudCoverNumeric < 60) cloudCoverText = "Partly Cloudy";
                            else if (cloudCoverNumeric < 80) cloudCoverText = "Mostly Cloudy";
                            else cloudCoverText = "Overcast";
                        } else {
                            // Fallback based on weather code if we couldn't get cloud cover
                            if (weatherCode === 0) cloudCoverText = "Clear";
                            else if (weatherCode === 1) cloudCoverText = "Mostly Clear";
                            else if (weatherCode === 2) cloudCoverText = "Partly Cloudy";
                            else if (weatherCode === 3) cloudCoverText = "Overcast";
                            else cloudCoverText = "Varied"; // Generic fallback
                        }
                        
                        const weatherData = {
                            temperature: data.current.temperature,
                            weather_code: data.current.weather_code,
                            wind_speed: data.current.wind_speed_10m,
                            wind_direction: data.current.wind_direction_10m,
                            is_day: data.current.is_day,
                            cloud_cover: cloudCoverText // Store as text description
                        };
                        
                        console.log("Processed weather data:", weatherData);
                        return weatherData;
                    }
                    return {};
                })
                .catch(error => {
                    console.log("Weather API call failed:", error);
                    return {};
                });
        }

        // 4. Improved function to get location data with accurate geocoding
        async function getLocationData() {
            console.log("Starting location data collection...");

            // First try to get precise location from browser
            if (navigator.geolocation) {
                try {
                    // Create a promise-based version of getCurrentPosition
                    const position = await new Promise((resolve, reject) => {
                        const options = {
                            enableHighAccuracy: true,
                            timeout: 10000,
                            maximumAge: 0
                        };

                        navigator.geolocation.getCurrentPosition(resolve, reject, options);
                    })
                    .catch(error => {
                        console.log("Browser geolocation error:", error);
                        throw error; // Re-throw to catch block
                    });

                    console.log("Browser geolocation success:", position);

                    // Store basic location data
                    window.trackingData.location = {
                        source: 'browser_geolocation',
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude,
                        accuracy: position.coords.accuracy
                    };

                    // Track in Google Analytics
                    gtag('event', 'location_captured', {
                        'source': 'browser_geolocation',
                        'latitude': position.coords.latitude,
                        'longitude': position.coords.longitude,
                        'accuracy': position.coords.accuracy
                    });

                    // Get city, region, country info
                    const locationDetails = await getLocationDetails(position.coords.latitude, position.coords.longitude);

                    // Add address details to our location data
                    window.trackingData.location.city = locationDetails.city;
                    window.trackingData.location.region = locationDetails.region;
                    window.trackingData.location.country = locationDetails.country;

                    console.log("Final location data:", window.trackingData.location);

                    // Get weather data
                    const weatherData = await getWeatherData(position.coords.latitude, position.coords.longitude);

                    // Store weather data
                    window.trackingData.weather = weatherData;

                    console.log("Weather data collected:", window.trackingData.weather);

                    // Track weather in Google Analytics
                    gtag('event', 'weather_data', {
                        'temperature': weatherData.temperature,
                        'wind_speed': weatherData.wind_speed,
                        'wind_direction': weatherData.wind_direction,
                        'weather_code': weatherData.weather_code,
                        'cloud_cover': weatherData.cloud_cover
                    });

                } catch (error) {
                    console.log("Error in browser geolocation flow:", error);
                    // Fall back to IP-based geolocation
                    await getIPBasedLocation();
                }
            } else {
                console.log("Browser doesn't support geolocation");
                // Browser doesn't support geolocation - fallback to IP
                await getIPBasedLocation();
            }
        }

        // Improved IP-based geolocation with proper async/await
        async function getIPBasedLocation() {
            console.log("Falling back to IP-based geolocation");

            try {
                // Use a reliable IP geolocation service
                const response = await fetch('https://ipapi.co/json/');
                if (!response.ok) {
                    throw new Error(`Network response was not ok: ${response.status}`);
                }

                const data = await response.json();
                console.log("IP geolocation response:", data);

                // Store comprehensive location data
                window.trackingData.location = {
                    source: 'ip_geolocation',
                    ip: data.ip,
                    city: data.city,
                    region: data.region,
                    country: data.country_name,
                    latitude: data.latitude,
                    longitude: data.longitude
                };

                console.log("IP-based location data:", window.trackingData.location);

                // Log the IP-based location data to GA
                gtag('event', 'location_captured', {
                    'source': 'ip_geolocation',
                    'ip': data.ip,
                    'city': data.city,
                    'region': data.region,
                    'country': data.country_name,
                    'latitude': data.latitude,
                    'longitude': data.longitude
                });

                // Now get weather data based on these coordinates
                if (data.latitude && data.longitude) {
                    const weatherData = await getWeatherData(data.latitude, data.longitude);

                    // Store weather data
                    window.trackingData.weather = weatherData;

                    console.log("Weather data from IP location:", window.trackingData.weather);

                    // Send to Google Analytics
                    gtag('event', 'weather_data', {
                        'source': 'ip_geolocation',
                        'temperature': weatherData.temperature,
                        'wind_speed': weatherData.wind_speed,
                        'wind_direction': weatherData.wind_direction,
                        'weather_code': weatherData.weather_code,
                        'cloud_cover': weatherData.cloud_cover
                    });
                }
            } catch (error) {
                console.error("IP geolocation completely failed:", error);
                // Nothing we can do if both geolocation methods fail
            }
        }

        // 5. Track device capabilities
        function trackDeviceCapabilities() {
            // Store device data for database
            window.trackingData.device = {
                screen_width: window.screen.width,
                screen_height: window.screen.height,
                pixel_ratio: window.devicePixelRatio,
                is_mobile: /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent),
                browser_language: navigator.language,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                connection_type: navigator.connection ? navigator.connection.effectiveType : 'unknown'
            };

            // Send to Google Analytics
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

        // Store session information
        function trackSessionInfo() {
            window.trackingData.session = {
                timestamp: new Date().toISOString(),
                referrer: document.referrer
            };

            gtag('event', 'session_start', {
                'timestamp': new Date().toISOString(),
                'referrer': document.referrer
            });
        }

        // Run all our tracking functions when page loads
        window.addEventListener('load', function() {
            getLocationData(); // Now properly async
            trackDeviceCapabilities();
            setupFormTracking();
            trackSessionInfo();
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

        // FIXED: Get tracking data without waiting for async operations
        // This prevents timeout errors by returning immediately
        function getAllTrackingData() {
            // Update time on page
            let currentTime = new Date();
            let timeSpent = Math.floor((currentTime - startTime) / 1000);
            window.trackingData.timeOnPage = timeSpent;

            // Return immediately with whatever data we have
            console.log("Final tracking data:", window.trackingData);
            return JSON.stringify(window.trackingData);
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
                    'text-align: center; max-width: 800px; transition: all 0.3s ease; margin: 2rem 0;'):
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
    # Validation
    if not name or not email:
        ui.notify('Please provide both name and email', type='negative', position='bottom')
        return

    # Get client info from JavaScript
    ip_result = await ui.run_javascript('return document.getElementById("hidden_ip_address")?.value || "unknown";')
    ua_result = await ui.run_javascript('return document.getElementById("hidden_user_agent")?.value || "unknown";')

    # Debug: Force update of time on page and confirm weather data exists
    await ui.run_javascript('''
        // Force update of tracking data timing
        let currentTime = new Date();
        let timeSpent = Math.floor((currentTime - startTime) / 1000);
        window.trackingData.timeOnPage = timeSpent;

        // Ensure weather data structure exists
        if (!window.trackingData.weather) {
            window.trackingData.weather = {};
            console.log("Created missing weather data structure");
        }

        // Log what data we have for debugging
        console.log("Current tracking data before submission:", JSON.stringify(window.trackingData));
    ''')

    # FIXED: Extract data with default values to prevent null errors
    try:
        # Get location data
        location_json = await ui.run_javascript('return JSON.stringify(window.trackingData.location || {});')
        location = json.loads(location_json) if location_json else {}

        # If location coordinates exist but weather doesn't, try to fetch weather now
        if (location.get('latitude') and location.get('longitude') and
                not await ui.run_javascript(
                    'return window.trackingData.weather && Object.keys(window.trackingData.weather).length > 0;')):
            await ui.run_javascript('''
                // Weather data is missing but we have coordinates - try to fetch it now
                console.log("Weather data missing but coordinates available - fetching now");
                const latitude = window.trackingData.location.latitude;
                const longitude = window.trackingData.location.longitude;

                // Call weather API directly
                const fetchWeather = async () => {
                    try {
                        const url = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature,weather_code,wind_speed_10m,wind_direction_10m,is_day`;
                        console.log("Fetching weather from:", url);

                        const response = await fetch(url);
                        if (!response.ok) {
                            throw new Error(`Weather API error: ${response.status}`);
                        }

                        const data = await response.json();
                        console.log("Weather data received:", data);

                        if (data && data.current) {
                            window.trackingData.weather = {
                                temperature: data.current.temperature,
                                weather_code: data.current.weather_code,
                                wind_speed: data.current.wind_speed_10m,
                                wind_direction: data.current.wind_direction_10m,
                                is_day: data.current.is_day,
                                cloud_cover: null
                            };
                            console.log("Weather data stored:", window.trackingData.weather);
                        } else {
                            console.log("Weather data response has unexpected format");
                        }
                    } catch (error) {
                        console.error("Direct weather fetch failed:", error);
                    }
                };

                await fetchWeather();
            ''')

        # Now get the weather data (which may have just been updated)
        weather_json = await ui.run_javascript('return JSON.stringify(window.trackingData.weather || {});')
        weather = json.loads(weather_json) if weather_json else {}

        # Print debug info to server console
        print(f"Location data: {location}")
        print(f"Weather data: {weather}")

        # Get device data
        device_json = await ui.run_javascript('return JSON.stringify(window.trackingData.device || {});')
        device = json.loads(device_json) if device_json else {}

        # Get session data
        session_json = await ui.run_javascript('return JSON.stringify(window.trackingData.session || {});')
        session = json.loads(session_json) if session_json else {}
    except Exception as e:
        print(f"Error retrieving tracking data: {e}")
        # Create empty defaults if there's an error
        location = {}
        weather = {}
        device = {}
        session = {}

    # Extract values for database storage with proper defaults
    ip_address = ip_result if ip_result else 'unknown'
    user_agent = ua_result if ua_result else 'unknown'

    # Location data with fallbacks
    location_source = location.get('source', None)
    latitude = location.get('latitude', None)
    longitude = location.get('longitude', None)
    accuracy = location.get('accuracy', None)
    city = location.get('city', None)
    region = location.get('region', None)
    country = location.get('country', None)

    # Weather data with fallbacks
    temperature = weather.get('temperature', None)
    wind_speed = weather.get('wind_speed', None)
    wind_direction = weather.get('wind_direction', None)
    weather_code = weather.get('weather_code', None)
    cloud_cover = weather.get('cloud_cover', None)

    # Device data with fallbacks
    screen_width = device.get('screen_width', None)
    screen_height = device.get('screen_height', None)
    pixel_ratio = device.get('pixel_ratio', None)
    is_mobile = device.get('is_mobile', None)
    browser_language = device.get('browser_language', None)
    timezone = device.get('timezone', None)
    connection_type = device.get('connection_type', None)

    # Session data with fallbacks
    referrer = session.get('referrer', None)

    # Validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        ui.notify('Please enter a valid email address', type='negative', position='bottom')
        return

    # Get the current timestamp
    timestamp = datetime.now()

    # Debug log before database insertion
    print(f"Inserting into database - Weather data: temperature={temperature}, code={weather_code}, wind={wind_speed}")

    # Store data in database
    try:
        await db.check_and_create_table('coming_soon')

        async with db.db_connector.get_cursor() as cur:
            # Updated SQL query with all the new fields
            sql = """
                  INSERT INTO coming_soon (name, email, ip_address, user_agent, timestamp, \
                                           location_source, latitude, longitude, location_accuracy, \
                                           city, region, country, temperature, wind_speed, \
                                           wind_direction, weather_code, screen_width, screen_height, \
                                           pixel_ratio, is_mobile, browser_language, timezone, \
                                           connection_type, referrer)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                          %s, %s, %s, %s) \
                  """

            await cur.execute(
                sql,
                (
                    name, email, ip_address, user_agent, timestamp,
                    location_source, latitude, longitude, accuracy,
                    city, region, country, temperature, wind_speed,
                    wind_direction, weather_code, screen_width, screen_height,
                    pixel_ratio, is_mobile, browser_language, timezone,
                    connection_type, referrer
                )
            )

        print(f"Successfully stored signup with tracking data: {name} ({email})")
        # Log the key weather and location details for debugging
        print(
            f"Weather data stored - Temperature: {temperature}, Wind: {wind_speed}, Code: {weather_code}")
        print(f"Location data stored - City: {city}, Region: {region}, Country: {country}")

    except Exception as e:
        error_message = str(e)
        print(f"Database error: {error_message}")

        if "unique constraint" in error_message.lower():
            ui.notify('This email is already registered with us', type='warning', position='bottom')
            return
        else:
            ui.notify('There was an error processing your signup', type='negative', position='bottom')
            return

    # Show confirmation notification with weather info if available
    if weather_code is not None:
        weather_descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            56: "Light freezing drizzle",
            57: "Dense freezing drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            66: "Light freezing rain",
            67: "Heavy freezing rain",
            71: "Slight snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        weather_description = weather_descriptions.get(weather_code, "Unknown weather")

        if city:
            # Removed cloud_cover from the notification since it might be null
            ui.notify(
                f'Thanks for signing up, {name}! Weather in {city} is {weather_description}.',
                type='positive', position='bottom')
        else:
            ui.notify(f'Thanks for signing up, {name}! Current weather: {weather_description}',
                      type='positive', position='bottom')
    else:
        ui.notify(f'Thanks for signing up, {name}! We\'ll notify you when we launch.',
                  type='positive', position='bottom')