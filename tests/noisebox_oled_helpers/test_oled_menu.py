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
    menu = Menu()
    for i in range(len(menu_items)):
        assert menu.get_menu_item_str(menu_items, i) == menu_items[i]

    for i in range(len(advanced_settings_items)):
        assert menu.get_menu_item_str(advanced_settings_items, i) == results[i]

def test_new_menu_items():
    menu = Menu()
    new_menu_items = Mock()
    menu.new_menu_items = new_menu_items
    menu.reset_menu(advanced_settings_items)
    assert menu.counter == 0
    assert menu.menuindex == 0
    menu.new_menu_items.assert_called_with(advanced_settings_items)
