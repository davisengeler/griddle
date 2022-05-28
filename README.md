# Griddle

[Griddle](https://griddle.app) is a simple python app made for Docker that helps you save money on your energy bill. It
watches the live price of electricity in your billing zone and makes clever adjustments to your thermostat. In this version, Griddle uses IFTTT to talk to your thermostat and adjust your home's comfort range *just enough* to shift your power consumption closer to the low 'average price' of wholesale providers. 

Griddle is only beneficial if you use a variable rate wholesale rate energy provider. These providers can average well below the rates of typical plans as long as you can shape your consumption against the volatile live market price. Griddle takes a lot of the hassle away from avoiding the spikes. 

It's a little bit wonky to set up in this version. That said, during certain peaks it's saved me several dollars per minute on my energy bill. I have plans to improve it sooner rather than later, but feel free to set it up now if you don't mind the dependencies. 

## Get Started

Griddle uses Docker and IFTTT. To get started, let's set up IFTTT.

### Prepare IFTTT

If you don't already have an account, sign up for IFTTT and connect your thermostat.
[Create three new triggers](https://ifttt.com/create), one at a time, each being an *If Webhook*:

1. **If** Webhook (Event Name: `g_heat`)

    **Then** `your thermostat for **heat** setting`

    **Temp** = `{{Value1}}`

1. **If** Webhook (Event Name: `g_cool`)

    **Then** `your thermostat for **cool** setting`

    **Temp** = `{{Value1}}`

1. **If** Webhook (Event Name: `g_notification`)

    **Then** `Notification`

    **Message** = `{{Value1}}`


Find and copy your key from IFTTT by clicking the **Documentation** on [this page](https://ifttt.com/maker_webhooks/).

### Prepare Griddle

1. If you don't already have [Docker](https://www.docker.com/products/docker-desktop), install and start it.
1. Clone this repository and `cd` into the project directory.
1. Create a `config.env` file and populate it with:
    ```
    LOAD_ZONE=YOUR_LOAD_ZONE_ID
    IFTTT_KEY=YOUR_IFTTT_KEY_GOES_HERE
    ```
1. Create a `settings/fav_heat.txt` and `settings/fav_cool.txt` containing your default heat/cool settings.
1. Build the image with `docker build -t griddle .`
1. Create a container (replace the all-caps with the full path to the settings directory)

    ```
    docker run \
        --name griddle \
        --env-file config.env \
        -v PATH/TO/SETTINGS:/griddle/settings \
        griddle
    ```

Assuming all was set up correctly and you have IFTTT notifications enabled on your phone,
you should receive a greeting from Griddle. In the next section, we set up a cron job to
instruct Docker to start a Griddle check every minute so you never get caught up in a random price spike.

### Automating Griddle

1. Run `crontab -e`, press `i` to insert, then add the following (replace all-caps with the full path to your docker
executable; run `which docker` to find out):

    ```
    */1 * * * * PATH/TO/DOCKER start griddle
    ```

1. Press the escape key several times, then type `:wq` and press return.

You're ready to go! Assuming all was set up correctly and you have IFTTT notifications enabled on your phone,
you should receive a greeting from Griddle.
