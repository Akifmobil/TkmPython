# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 21:32:56 2025

@author: Izoly
"""

import random

def oyun():
    secenekler = ["taş", "kağıt", "makas"]
    bilgisayar_secimi = random.choice(secenekler)

    kullanici_secimi = input("taş, kağıt veya makas seçin: ").lower()

    if kullanici_secimi not in secenekler:
        print("Geçersiz seçim. Lütfen taş, kağıt veya makas seçin.")
        return

    print("Bilgisayarın seçimi:", bilgisayar_secimi)

    if kullanici_secimi == bilgisayar_secimi:
        print("Berabere!")
    elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
         (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
         (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")

oyun()