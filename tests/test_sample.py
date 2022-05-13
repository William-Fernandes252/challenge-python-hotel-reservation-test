from unittest import TestCase
from context import src
from src import my_module


class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, my_module.get_cheapest_hotel(
            "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, my_module.get_cheapest_hotel(
            "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, my_module.get_cheapest_hotel(
            "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test4(self):
        result = "Lakewood"
        self.assertEqual(result, my_module.get_cheapest_hotel(
            "Rewards: 11May2009(wed), 27Mar2009(thur), 28Mar2009(fri)"))

    def test5(self):
        result = "Lakewood"
        self.assertEqual(result, my_module.get_cheapest_hotel(
            "Rewards: 11May2009(tues), 27Mar2009(wed), 28Mar2009(thurs)"))
