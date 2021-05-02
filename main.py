from src.console import Red, Blue, Yellow, Off
import src.console as console

import src.event as event
import src.embed as embed

import datetime
import requests
import binascii
import base64
import time
import sys

var_name = "CHIAKI_BASE64_TOKEN"  # The name of the environment variable containing the token
url = None  # The base64 encrypted webhook link to make the request to

# Implement some error handling
try:
    # Get the env var and decrypt it
    url = base64.b64decode(os.getenv(var_name)).decode("utf-8")

except TypeError:
    # The getenv method returned None AKA env var was not found
    console.out(Red, "[ERROR]", Off, " The environment variable with the Webhook link wasn't found...")
    console.out(Blue, "[*]", Off, f" Make sure that the {var_name} environment variable is set to the Webhook's link")
    exit(1)

except binascii.Error:
    # Invalid base64 input
    console.out(Red, "[ERROR]", Off, " Invalid base64 encrypted Webhook link/token...")
    console.out(Blue, "[*]", Off, " Check that your token is properly encoded in base64")
    exit(2)

while True:
    now = datetime.datetime.now()

    time_tomorrow = datetime.time(event.timetable[event.Tomorrow()][0], event.timetable[event.Tomorrow()][1])
    date_tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)
    datetime_tomorrow = datetime.datetime.combine(date_tomorrow, time_tomorrow)

    delta = datetime_tomorrow - now     # Get the time delta between our next timestamp and now

    payload = embed.Embed()

    time.sleep(delta.seconds)       # And basically vibe til' then

    response = requests.post(url, json=payload)   # Make our request and store response for error handling

    # Implement error handling for some error codes.
    # If new ones were to emerge, I'd strongly recommend to add them here
    if not response.ok:
        if response.status_code == 401:
            console.out(f"{Red}[ERROR]{Off} Unauthorized client! Check logs for details...")
            console.log(f"{sys.path[0]}/assets/logs/error.log", f"Unauthorized due to invalid webhook token. "
                        "Post request return code: 401 Unauthorized.",
                        f"Response body: {response.json()}")

        elif response.status_code == 404:
            console.out(f"{Red}[ERROR]{Off} Webhook was not found! Check logs for details...")
            console.log(f"{sys.path[0]}/assets/logs/error.log",
                        f"Unknown webhook. Post request return code: 404 Not Found.",
                        f"Response body: {response.json()}")

        else:
            console.out(f"{Red}[ERROR]{Off} An unkown error has occured! Check logs for details...")
            console.log(f"{sys.path[0]}/assets/logs/error.log",
                        f"Unkown error. Post request return code: {response.status_code}",
                        f"Response body: {response.json()}",
                        f"{Yellow}NOTE: Please consider adding a handling function to this error code if possible{Off}")
    exit(0)
    """
        Note: Consider future optimization of this Error Handling.
        This one is kind of a temporary solution to get this out already.
        A good idea would be to create a dedicated source file using a dictionary
        along with a try to handle unkown errors in order to avoid all these ifs.
        
        Something like:
        
        def Handle_401():
            pass
            
        def Handle 404():
            pass
        
        error_codes = {
            401: Handle_401,
            404: Handle_404
        }
        
        try:
            error_codes[status_code]()
        
        except KeyError:
            # handle an unknown
        
        All this actually makes it easier to add new exceptions
    """
