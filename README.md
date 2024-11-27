# Discord Rich Presence Script

This script leverages the [pypresence](https://pypi.org/project/pypresence/) library to create a custom Rich Presence for Discord. It updates your activity status with custom details, state, images, and clickable buttons.

## Features

- Displays a large image with a tooltip on hover.
- Includes custom text for the "details" and "state" fields.
- Adds two clickable buttons that can direct users to URLs of your choice.
- Automatically refreshes every 60 seconds.

## Requirements

- Python 3.6+
- [pypresence](https://pypi.org/project/pypresence/) library installed.

## Setup

1. Clone this repository or copy the script to your local machine.
2. Install the `pypresence` library:
   ```bash
   pip install pypresence

Obtain your client ID from your Discord application:

Go to the Discord Developer Portal.
Create a new application or select an existing one.
Copy the Client ID from the application settings.
Add your assets (images) in the "Rich Presence" section of your Discord application settings:

Provide the image name as your_image in the script.
Add a descriptive tooltip text for large_text.
Replace the placeholder values in the script:

your_clientID with your application's client ID.
your_image with the name of the uploaded image asset.
your_text with the desired tooltip text for the image.
your_Details and your_State with custom strings to display.
Link1 and Link2 with your desired URLs.
URL_NAME1 and URL_NAME2 with the button text for each link.
