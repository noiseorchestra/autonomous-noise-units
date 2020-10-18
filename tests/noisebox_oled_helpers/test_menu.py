from noisebox_helpers import Config
from noisebox_oled_helpers import MenuItems

main_menu_items = ['CONNECT TO SERVER',
                   'LEVEL METER',
                   'P2P SESSION',
                   'SETTINGS -->']

settings_items = [{"name": "INPUT", "value": "2"},
                  "IP ADDRESS",
                  "JACKTRIP",
                  "UPDATE",
                  "<-- BACK"]

advanced_settings_items = [{"name": "CHANNELS", "value": "2"}, {"name": "QUEUE", "value": "6"}, {"name": "IP", "value": "111.111.111.111"},"<-- BACK"]

input_values = ["1", "2"]
queue_values = ["2", "4", "6", "8"]

menu = MenuItems(dry_run=True)

def test_active_menu_items():
    assert menu.active_menu_items == main_menu_items

def test_get_settings_items():
    assert menu.settings_items == settings_items

def test_get_advanced_settings_items():
    assert menu.advanced_settings_items == advanced_settings_items

def test_next_input_value():
    assert menu.next_value(input_values, "1") == "2"
    assert menu.next_value(input_values, "2") == "1"

def test_next_queue_value():
    assert menu.next_value(queue_values, "2") == "4"
    assert menu.next_value(queue_values, "6") == "8"
    assert menu.next_value(queue_values, "8") == "2"
