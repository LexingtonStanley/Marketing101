from nicegui import ui, app
import json


async def test_weather_api():
    status_label = ui.label('Testing weather API...').classes('text-lg font-bold text-blue-600')
    results_container = ui.element('div')

    # Fixed test coordinates for London
    lat = 51.5072178
    lon = -0.1275862

    # Test 1: Basic API call with minimal parameters
    with results_container:
        ui.label('Test 1: Basic API call').classes('text-xl font-bold mt-4')

    test1_result = await ui.run_javascript(f'''
    return new Promise((resolve, reject) => {{
        const url = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature";
        console.log("Test 1 URL:", url);

        fetch(url)
        .then(response => {{
            const status = response.status;
            const statusText = response.statusText;
            console.log("Response status:", status, statusText);

            return response.json().then(data => {{
                return {{
                    status: status,
                    statusText: statusText,
                    data: data
                }};
            }}).catch(error => {{
                return {{
                    status: status,
                    statusText: statusText,
                    error: "JSON parse error: " + error.toString()
                }};
            }});
        }})
        .then(result => {{
            console.log("Test 1 result:", result);
            resolve(result);
        }})
        .catch(error => {{
            console.error("Test 1 error:", error);
            resolve({{
                status: 'error',
                error: error.toString()
            }});
        }});
    }});
    ''')

    with results_container:
        ui.label(f"Status: {test1_result.get('status')}").classes('font-bold')
        ui.label(json.dumps(test1_result, indent=2)).classes('font-mono whitespace-pre bg-gray-100 p-2 rounded')

    # Test 2: Alternative formatting of coordinates
    with results_container:
        ui.label('Test 2: Alternative formatting').classes('text-xl font-bold mt-4')

    test2_result = await ui.run_javascript(f'''
    return new Promise((resolve, reject) => {{
        // Using toString to ensure proper formatting of floating point numbers
        const url = "https://api.open-meteo.com/v1/forecast?latitude=" + {lat}.toString() + "&longitude=" + {lon}.toString() + "&current=temperature";
        console.log("Test 2 URL:", url);

        fetch(url)
        .then(response => {{
            const status = response.status;
            const statusText = response.statusText;
            console.log("Response status:", status, statusText);

            return response.json().then(data => {{
                return {{
                    status: status,
                    statusText: statusText,
                    data: data
                }};
            }}).catch(error => {{
                return {{
                    status: status,
                    statusText: statusText,
                    error: "JSON parse error: " + error.toString()
                }};
            }});
        }})
        .then(result => {{
            console.log("Test 2 result:", result);
            resolve(result);
        }})
        .catch(error => {{
            console.error("Test 2 error:", error);
            resolve({{
                status: 'error',
                error: error.toString()
            }});
        }});
    }});
    ''')

    with results_container:
        ui.label(f"Status: {test2_result.get('status')}").classes('font-bold')
        ui.label(json.dumps(test2_result, indent=2)).classes('font-mono whitespace-pre bg-gray-100 p-2 rounded')

    # Test 3: All parameters - check which one might be causing issues
    with results_container:
        ui.label('Test 3: Testing all parameters individually').classes('text-xl font-bold mt-4')

    params = [
        "temperature",
        "relative_humidity",
        "apparent_temperature",
        "is_day",
        "precipitation",
        "rain",
        "weather_code",
        "cloud_cover",
        "pressure_msl",
        "surface_pressure",
        "wind_speed_10m",
        "wind_direction_10m",
        "wind_gusts_10m"
    ]

    for param in params:
        param_result = await ui.run_javascript(f'''
        return new Promise((resolve, reject) => {{
            const url = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current={param}";
            console.log("Testing parameter: {param}, URL:", url);

            fetch(url)
            .then(response => {{
                return {{
                    parameter: "{param}",
                    status: response.status,
                    ok: response.ok
                }};
            }})
            .then(result => {{
                console.log("Parameter test result:", result);
                resolve(result);
            }})
            .catch(error => {{
                console.error("Parameter test error:", error);
                resolve({{
                    parameter: "{param}",
                    status: 'error',
                    error: error.toString()
                }});
            }});
        }});
        ''')

        with results_container:
            status_color = "text-green-600" if param_result.get('ok') else "text-red-600"
            ui.label(f"Parameter '{param}': {param_result.get('status')}").classes(f'font-bold {status_color}')

    # Test 4: Working API solution
    with results_container:
        ui.label('Test 4: Working API solution').classes('text-xl font-bold mt-4')

    final_solution = await ui.run_javascript(f'''
    return new Promise((resolve, reject) => {{
        const url = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature,weather_code,wind_speed_10m,wind_direction_10m";
        console.log("Final solution URL:", url);

        fetch(url)
        .then(response => {{
            if (!response.ok) {{
                throw new Error(`Network response was not ok: ${{response.status}}`);
            }}
            return response.json();
        }})
        .then(data => {{
            console.log("Final solution success:", data);
            resolve({{
                status: 'success',
                data: data
            }});
        }})
        .catch(error => {{
            console.error("Final solution error:", error);
            resolve({{
                status: 'error',
                error: error.toString()
            }});
        }});
    }});
    ''')

    with results_container:
        if final_solution.get('status') == 'success':
            ui.label(f"✅ Found working solution!").classes('text-xl font-bold text-green-600')
            ui.label(json.dumps(final_solution.get('data'), indent=2)).classes(
                'font-mono whitespace-pre bg-gray-100 p-2 rounded')

            # Generate the fixed code
            fixed_code = f'''
// FIXED WEATHER API CODE:
function getWeatherData(latitude, longitude) {{
    // Use simplified parameters that are guaranteed to work
    return fetch(`https://api.open-meteo.com/v1/forecast?latitude=${{latitude}}&longitude=${{longitude}}&current=temperature,weather_code,wind_speed_10m,wind_direction_10m,is_day`)
        .then(response => {{
            if (!response.ok) {{
                throw new Error(`Network response was not ok: ${{response.status}}`);
            }}
            return response.json();
        }})
        .then(data => {{
            if (data && data.current) {{
                return {{
                    temperature: data.current.temperature,
                    weather_code: data.current.weather_code,
                    wind_speed: data.current.wind_speed_10m,
                    wind_direction: data.current.wind_direction_10m,
                    is_day: data.current.is_day
                }};
            }}
            return {{}};
        }})
        .catch(error => {{
            console.log("Weather API call failed:", error);
            return {{}};
        }});
}}
'''

            with results_container:
                ui.label("Copy this fixed code to your application:").classes('text-xl font-bold mt-4')
                ui.code(fixed_code).classes('text-sm')
        else:
            ui.label(f"❌ Failed to find working solution").classes('text-xl font-bold text-red-600')
            ui.label(json.dumps(final_solution, indent=2)).classes('font-mono whitespace-pre bg-gray-100 p-2 rounded')

    status_label.text = '✅ API testing complete'


@ui.page('/')
def test_page():
    # Add some basic styling
    ui.add_head_html('''
    <style>
        body {
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        .content {
            max-width: 800px;
            margin: 0 auto;
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        pre {
            overflow-x: auto;
        }
    </style>
    ''')

    with ui.element('div').classes('content'):
        ui.label('Weather API Debug Tool').classes('text-2xl font-bold mb-4')
        ui.label('This tool will identify which weather API parameters are causing the 400 error.').classes('mb-4')

        # Add a button to run the test
        ui.button('Run API Tests', on_click=test_weather_api).classes('mb-4 bg-blue-500 text-white')

        # Add browser console viewer
        ui.label('Browser Console Output (for debugging):').classes('text-xl font-bold mt-8')

        console_output = ui.element('div').classes(
            'bg-black text-green-400 p-4 rounded font-mono text-sm h-40 overflow-auto')

        ui.add_body_html('''
        <script>
            // Capture console output
            (function(){
                const consoleDiv = document.querySelector('.text-green-400');
                if (!consoleDiv) return;

                const oldLog = console.log;
                const oldError = console.error;
                const oldWarn = console.warn;

                console.log = function() {
                    const args = Array.from(arguments);
                    oldLog.apply(console, args);

                    const msg = args.map(arg => {
                        if (typeof arg === 'object') return JSON.stringify(arg);
                        return arg;
                    }).join(' ');

                    const logLine = document.createElement('div');
                    logLine.textContent = '▶ ' + msg;
                    consoleDiv.appendChild(logLine);
                    consoleDiv.scrollTop = consoleDiv.scrollHeight;
                };

                console.error = function() {
                    const args = Array.from(arguments);
                    oldError.apply(console, args);

                    const msg = args.map(arg => {
                        if (typeof arg === 'object') return JSON.stringify(arg);
                        return arg;
                    }).join(' ');

                    const logLine = document.createElement('div');
                    logLine.textContent = '⚠️ ' + msg;
                    logLine.style.color = '#f56565';
                    consoleDiv.appendChild(logLine);
                    consoleDiv.scrollTop = consoleDiv.scrollHeight;
                };

                console.warn = function() {
                    const args = Array.from(arguments);
                    oldWarn.apply(console, args);

                    const msg = args.map(arg => {
                        if (typeof arg === 'object') return JSON.stringify(arg);
                        return arg;
                    }).join(' ');

                    const logLine = document.createElement('div');
                    logLine.textContent = '⚠ ' + msg;
                    logLine.style.color = '#ecc94b';
                    consoleDiv.appendChild(logLine);
                    consoleDiv.scrollTop = consoleDiv.scrollHeight;
                };

                console.log('Console logger initialized');
            })();
        </script>
        ''')


# Run the app
ui.run(title="Weather API Debug Tool", port=8080)