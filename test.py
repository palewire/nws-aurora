#! /usr/bin/env python
import unittest

from nws_aurora import get_forecast, get_grid, get_images, get_latest_image


class NwsAuroraTest(unittest.TestCase):
    def test_images(self):
        get_images("north")
        get_images("south")

    def test_latest_image(self):
        get_latest_image("north")
        get_latest_image("south")

    def test_grid(self):
        get_grid()

    def test_forecast(self):
        get_forecast()


if __name__ == "__main__":
    unittest.main()
