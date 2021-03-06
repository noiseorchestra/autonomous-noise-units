import time
from luma.core.virtual import hotspot
import noisebox_oled_helpers.fonts as fonts

def vertical_bar(draw, name, x1, y1, x2, y2, yh):
    """Draw meter bar and frame"""

    draw.rectangle((x1, y1) + (x2, y2), "black", "white")
    draw.rectangle((x1, y1) + (x2, yh), "white", "white")
    draw.text((x1, y1 + 2), name, font=fonts.generate_font(14), fill="white")


def render(draw, name, width, height, meter):
    """Calculate measurements and render"""

    top_margin = 3
    bottom_margin = 3

    bar_height = height - 15 - top_margin - bottom_margin
    width_meter = width
    bar_width = 0.5 * width_meter
    bar_margin = (width_meter - bar_width) / 2

    fraction = (52 + meter.get_current_value()) / 52
    level = (bar_height - (bar_height * (fraction * fraction))) - top_margin
    vertical_bar(draw, name, bar_margin, bar_height,
                 bar_margin + bar_width, top_margin, level)


class Meter(hotspot):
    """Object for drawing level meter"""

    def __init__(self, name, width, height, meter, interval):
        super(Meter, self).__init__(width, height)
        self._interval = interval
        self._last_updated = 0
        self.meter = meter
        self.name = name

    def should_redraw(self):
        return time.time() - self._last_updated > self._interval

    def update(self, draw):
        render(draw, self.name, self.width, self.height, self.meter)
        self._last_updated = time.time()
