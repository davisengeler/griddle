import os
import time
import gs_price
import gs_coms
import gs_temp

# =======================
# Configuration
# =======================

load_zone = os.environ["LOAD_ZONE"]
ifttt_key = os.environ["IFTTT_KEY"]
notification_url = f"https://maker.ifttt.com/trigger/gs_notification/with/key/{ifttt_key}"
heat_url = f"https://maker.ifttt.com/trigger/gs_heat/with/key/{ifttt_key}"
cool_url = f"https://maker.ifttt.com/trigger/gs_cool/with/key/{ifttt_key}"

# Read the favorite temperature settings
with open("settings/fav_heat.txt") as file:
    fav_heat = int(file.read())
with open("settings/fav_cool.txt") as file:
    fav_cool = int(file.read())

try:
    with open("settings/.last_heat.txt") as file:
        last_heat = int(file.read())
    with open("settings/.last_cool.txt") as file:
        last_cool = int(file.read())
except Exception as e:
    last_heat = -1
    last_cool = -1
    gs_coms.send_data(notification_url, ["Welcome to Griddle! If everything is set up right, I'll start saving "
                                         "you money by shifting your AC and Heat usage away from random spikes! "
                                         "Make sure that you're starting the container every minute for best results."])

print(f"{last_heat} {last_cool}")

# =======================
# Get the price and temp
# =======================

# Get the current price
current_price, updated_at = gs_price.get_current(load_zone)
print(f"Currently costs {round(current_price, 2)}¢ ({updated_at})")

# Calculate the new temperature settings
temp_offset = gs_temp.calculate_offset(current_price)
new_cool = fav_cool + temp_offset
new_heat = fav_heat - temp_offset

# =======================
# Update, notify, & save
# =======================

if last_cool != new_cool or last_heat != new_heat:
    # Update the heat
    gs_coms.send_data(
        heat_url,
        [new_heat]
    )
    # Update the cool
    time.sleep(2)
    gs_coms.send_data(
        cool_url,
        [new_cool]
    )
    # Send a notification about the changes
    time.sleep(2)
    gs_coms.send_data(
        notification_url,
        [f"Griddle – The price of energy is at {current_price}¢ so I'm setting your temp to {new_heat}º – {new_cool}º."]
    )
    # Update 'last' values
    with open("settings/.last_heat.txt", "w") as file:
        file.write(str(new_heat))
    with open("settings/.last_cool.txt", "w") as file:
        file.write(str(new_cool))
