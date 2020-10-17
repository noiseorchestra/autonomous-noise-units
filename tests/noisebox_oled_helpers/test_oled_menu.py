from noisebox_oled_helpers.menu import Menu


menu_items = ['CONNECT TO SERVER',
              'LEVEL METER',
              'P2P SESSION',
              'SETTINGS -->']

settings_menu = ["MONO INPUT",
                 "IP ADDRESS",
                 "JACKTRIP",
                 "UPDATE",
                 "<-- BACK"]

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
