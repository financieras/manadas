#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:00:00 2020
@author: financieras
"""
import random

class Juez:
    def __init__(self):
        self.tablero = [[0]*50 for _ in range(50)]
        self.manada_a = Manada("A")
        self.manada_b = Manada("B")
        self.generar_comida()
    
    def generar_comida(self):
        for i in range(16):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            self.tablero[x][y] += 1
        for i in range(8):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            self.tablero[x][y] += 2
        for i in range(4):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            self.tablero[x][y] += 3
    
    def jugar(self):
        while True:
            self.manada_a.jugar(self.tablero)
            if self.tablero_vacio():
                self.declarar_ganador()
                break
            self.manada_b.jugar(self.tablero)
            if self.tablero_vacio():
                self.declarar_ganador()
                break
    
    def tablero_vacio(self):
        for i in range(50):
            for j in range(50):
                if self.tablero[i][j] > 0:
                    return False
        return True
    
    def declarar_ganador(self):
        if self.manada_a.miembros > self.manada_b.miembros:
            print("La Manada A ha ganado!")
        elif self.manada_b.miembros > self.manada_a.miembros:
            print("La Manada B ha ganado!")
        else:
            print("El juego ha terminado en empate.")
