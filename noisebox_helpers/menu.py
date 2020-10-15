from noisebox_helpers.config import Config

main_menu_items = ['CONNECT TO SERVER',
                   'LEVEL METER',
                   'P2P SESSION',
                   'SETTINGS -->']

settings_items = [{"name": "INPUT", "value": "1"},
                  "IP ADDRESS",
                  "JACKTRIP",
                  "UPDATE",
                  "<-- BACK"]

advanced_settings_items = [{"name": "CHANNELS", "value": "1"}, {"name": "BUFFER", "value": "6"}, "<-- BACK"]

input_values = ["1", "2"]
channels_values = ["1", "2"]
buffer_values = ["2", "4", "6", "8"]

def get_main_menu_items():
    return main_menu_items

def get_settings_items():
    # need to implement loading stored config values
    config = Config()
    settings_items[0]["value"] = config.get_config()["jacktrip-default"]["input-channels"]
    return settings_items

def get_settings_items():
    # need to implement loading stored config values
    return advanced_settings_items

def next_input_value(current_value):
    return next_value(input_values, current_value)

def next_buffer_value(current_value):
    return next_value(buffer_values, current_value)

def next_channels_value(current_value):
    return next_value(channels_values, current_value)

def next_value(values, current_value):
    index = values.index(current_value)
    next_index = index + 1
    next_index = 0 if next_index == len(values) else next_index
    return values[next_index]
