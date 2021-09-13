# *********************************** Desktop Notifications **********************************888

# Importing libraries
import time
from plyer import notification

# Notes: 
"""
title (str) – Title of the notification
message (str) – Message of the notification
app_name (str) – Name of the app launching this notification
app_icon (str) – Icon to be displayed along with the message
timeout (int) – time to display the message for, defaults to 10
ticker (str) – text to display on status bar as the notification arrives
toast (bool) – simple Android message instead of full notification
"""

if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Drinking Water Notification",
            message="Human needs at least 3 to 4 liters of water every day...! So keep drinking water everyday..! Thanks for your time..!",
            app_name="Healthy Programmer",
            app_icon="C:\PycharmProjects\sachinfile.py\Image and logos\Julie-Henriksen-Kitchen-Water-Boiler-Electric-Kettle.ico",
            ticker="Drinking water notification...",
            toast=True
        )
        time.sleep(6)
        # time.sleep(60*60)
        continue

