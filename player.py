import pygame


class Player:


    def __init__(self, nummer, eingelochte_kugeln=0, turn=False):
        self._nummer = nummer
        self._turn = turn
        self._eingelochte_kugeln = eingelochte_kugeln
        self._achtfreigabe = False

    def get_achtfreigabe(self):
        return self._achtfreigabe

    def get_nummer(self):
        return self._nummer

    def get_turn(self):
        return self._turn

    def get_eingelochte_kugeln(self):
        return self._eingelochte_kugeln

    def set_achtfreigabe(self, bool):
        self._achtfreigabe = bool

    def set_nummer(self, nummer):
        self._nummer = nummer

    def set_turn(self, turn):
        self._turn = turn

    def set_eingelochte_kugeln(self, eingelochte_kugeln):
        self._eingelochte_kugeln_ofballtype = eingelochte_kugeln

