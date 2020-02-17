# Griddle

[Griddle](https://griddle.app) is a simple python app made for Docker that helps you save money on your energy bill by
watching the live price of electricity in your billing zone. Griddle is only beneficial if you use a variable rate /
wholesale rate energy provider like [Griddy](http://ssqt.co/mefxez0). These providers can average well below the rates
of typical plans as long as you can shape your consumption against the volatile live market price. Griddle takes the
hassle away!

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

    **Temp** = `{{Value1}}`


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
        --name gridsheriff \
        --env-file config.env \
        -v PATH/TO/SETTINGS:/griddle/settings \
        griddle
    ```