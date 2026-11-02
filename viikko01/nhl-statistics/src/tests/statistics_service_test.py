import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaaja_loytyy(self):
        pelaaja = self.stats.search("Gretzky")
        self.assertEqual(pelaaja.name, "Gretzky")

    def test_pelaajaa_ei_loydy(self):
        self.assertIsNone(self.stats.search("Nobody"))

    def test_joukkueen_pelaajat(self):
        pelaajat = self.stats.team("EDM")
        nimet = [pelaaja.name for pelaaja in pelaajat]
        self.assertEqual(nimet, ["Semenko", "Kurri", "Gretzky"])

    def test_parhaat_pelaajat(self):
        pelaajat = self.stats.top(2)
        nimet = [pelaaja.name for pelaaja in pelaajat]
        self.assertEqual(nimet, ["Gretzky", "Lemieux", "Yzerman"])

