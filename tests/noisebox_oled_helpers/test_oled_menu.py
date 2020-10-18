from noisebox_oled_helpers.menu import Menu
from unittest.mock import Mock

menu_items = ['CONNECT TO SERVER',
              'LEVEL METER',
              'P2P SESSION',
              'SETTINGS -->']

advanced_settings_items = [{"name": "CHANNELS", "value": "1"}, {"name": "QUEUE", "value": "6"}, {"name": "IP", "value": "123.123.123.123"}, "CHANGE IP","<-- BACK"]


def test_get_menu_item_string():

    results = [
        "CHANNELS: 1",
        "QUEUE: 6",
        "IP: 123.123.123.123",
        "CHANGE IP",
        "<-- BACK"
    ]

    menu = Menu(dry_run=True)
    for i in range(len(menu_items)):
        assert menu.get_menu_item_str(i) == menu_items[i]

    menu.new_menu_items(advanced_settings_items)
    for i in range(len(advanced_settings_items)):
        assert menu.get_menu_item_str(i) == results[i]

def test_new_menu_items():
    menu = Menu()
    menu.reset_menu(advanced_settings_items)
    assert menu.counter == 0
    assert menu.menuindex == 0
    assert menu.active_menu_items == advanced_settings_items
