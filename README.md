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

## Obtain your client ID from your Discord application:

1. Go to the Discord Developer Portal.
2. Create a new application or select an existing one.
3. Copy the Client ID from the application settings.
4. Add your assets (images) in the "Rich Presence" section of your Discord application settings:

## Provide the image name as your_image in the script.
1.Add a descriptive tooltip text for large_text.

2.Replace the placeholder values in the script.


## Usage
1. Run the script:
```bash
python script_name.py
