from os import name


class Varoshaza:
    enabled = True

    def __init__(self, level, fa, marvany, ido, maxlakossag):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Akademia:
    enabled = True

    def __init__(self, level, fa, kristaly, ido, tudosok):
        self.level = level
        self.fa = fa
        self.kristaly = kristaly
        self.ido = ido
        self.tudosok = tudosok


class Raktar:
    enabled = True

    def __init__(self, level, fa, marvany, ido, kapacitas):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.kapacitas = kapacitas


class Fogado:
    enabled = False

    def __init__(self, level, fa, marvany, ido, maxbor, elegedettseg, borelegedettseg):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.maxbor = maxbor
        self.elegedettseg = elegedettseg
        self.borelegedettseg = borelegedettseg


class Palota:
    enabled = False

    def __init__(self, level, fa, bor, marvany, kristaly, ken, ido):
        self.level = level
        self.fa = fa
        self.bor = bor
        self.marvany = marvany
        self.kristaly = kristaly
        self.ken = ken
        self.ido = ido


class Muzeum:
    enabled = False
    alapelegedettseg = 0
    bonuszelegedettseg = 0

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.alapelegedettseg += 20
        self.bonuszelegedettseg += 50


class Kikoto:
    enabled = True
    toltesi_sebesseg = 0

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.toltesi_sebesseg += 30


class Hajogyar:
    enabled = False

    def __init__(self, level, fa, marvany, ido, enged=None):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.enged = enged


class Barakk:
    enabled = True

    def __init__(self, level, fa, marvany, ido, enged):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.enged = enged


class Varosfal:
    enabled = True

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido

    def getLevel(self):
        return self.level


class Nagykovetseg:
    enabled = True
    diplomacia_pont = 2

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.diplomacia_pont += 1


class Piac:
    enabled = False

    def __init__(self, level, fa, marvany, ido, kapacitas):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido
        self.kapacitas = kapacitas


class Muhely:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Rejtekhely:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Erdeszhaz:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Uvegfuvo:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Alkimistatorony:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Bortermelo:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Komuves:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Acsmester:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Optikus:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Tuzszeresz:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Szolopres:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Epitesz:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Templom:
    enabled = False

    def __init__(self, level, fa, marvany, ido, pap):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


class Kalozerod:
    enabled = False

    def __init__(self, level, fa, marvany, ido):
        self.level = level
        self.fa = fa
        self.marvany = marvany
        self.ido = ido


level1Kalozerod = Kalozerod(1, 450, 250, 1)
level2Kalozerod = Kalozerod(2, 906, 505, 7)
level3Kalozerod = Kalozerod(3, 1389, 783, 13)
level4Kalozerod = Kalozerod(4, 1935, 1112, 20)
level5Kalozerod = Kalozerod(5, 2593, 1534, 28)
level6Kalozerod = Kalozerod(6, 3427, 2103, 37)
level7Kalozerod = Kalozerod(7, 4516, 2883, 46)
level8Kalozerod = Kalozerod(8, 5950, 3949, 56)
level9Kalozerod = Kalozerod(9, 7834, 5388, 66)
level10Kalozerod = Kalozerod(10, 10284, 7296, 78)
level11Kalozerod = Kalozerod(11, 13430, 9782, 150)
level12Kalozerod = Kalozerod(12, 17415, 12964, 174)
level13Kalozerod = Kalozerod(13, 22394, 16970, 200)

level1Templom = Templom(1, 216, 173, 39, 12)
level2Templom = Templom(2, 228, 190, 43, 23)
level3Templom = Templom(3, 333, 290, 48, 37)
level4Templom = Templom(4, 465, 423, 52, 54)
level5Templom = Templom(5, 598, 567, 58, 73)
level6Templom = Templom(6, 760, 752, 63, 94)
level7Templom = Templom(7, 959, 989, 70, 117)
level8Templom = Templom(8, 1197, 1290, 77, 142)
level9Templom = Templom(9, 1432, 1610, 84, 168)
level10Templom = Templom(10, 1773, 2080, 93, 196)

level1Epitesz = Epitesz(1, 185, 106, 16)
level2Epitesz = Epitesz(2, 291, 160, 20)
level3Epitesz = Epitesz(3, 413, 222, 23)
level4Epitesz = Epitesz(4, 255, 295, 27)
level5Epitesz = Epitesz(5, 720, 379, 32)
level6Epitesz = Epitesz(6, 911, 475, 36)
level7Epitesz = Epitesz(7, 1133, 587, 36)
level8Epitesz = Epitesz(8, 1390, 716, 46)
level9Epitesz = Epitesz(9, 1689, 865, 52)
level10Epitesz = Epitesz(10, 2035, 1036, 58)
level11Epitesz = Epitesz(11, 2437, 1233, 63)
level12Epitesz = Epitesz(12, 2902, 1460, 70)

level1Szolopres = Szolopres(1, 339, 123, 22)
level2Szolopres = Szolopres(2, 423, 198, 26)
level3Szolopres = Szolopres(3, 520, 285, 30)
level4Szolopres = Szolopres(4, 631, 387, 34)
level5Szolopres = Szolopres(5, 758, 504, 38)
level6Szolopres = Szolopres(6, 905, 640, 43)
level7Szolopres = Szolopres(7, 1074, 798, 48)
level8Szolopres = Szolopres(8, 1269, 981, 53)
level9Szolopres = Szolopres(9, 1492, 1194, 58)
level10Szolopres = Szolopres(10, 1749, 1440, 64)
level11Szolopres = Szolopres(11, 2045, 1726, 70)
level12Szolopres = Szolopres(12, 2384, 2058, 76)

level1Tuzszeresz = Tuzszeresz(1, 273, 135, 16)
level2Tuzszeresz = Tuzszeresz(2, 353, 212, 19)
level3Tuzszeresz = Tuzszeresz(3, 353, 212, 23)
level4Tuzszeresz = Tuzszeresz(4, 445, 302, 28)
level5Tuzszeresz = Tuzszeresz(5, 673, 526, 32)
level6Tuzszeresz = Tuzszeresz(6, 813, 665, 37)
level7Tuzszeresz = Tuzszeresz(7, 974, 827, 42)
level8Tuzszeresz = Tuzszeresz(8, 1159, 1015, 46)
level9Tuzszeresz = Tuzszeresz(9, 1373, 1233, 52)
level10Tuzszeresz = Tuzszeresz(10, 1618, 1486, 57)
level11Tuzszeresz = Tuzszeresz(11, 1899, 1779, 63)
level12Tuzszeresz = Tuzszeresz(12, 2223, 2120, 70)
level13Tuzszeresz = Tuzszeresz(13, 2596, 2514, 76)
level14Tuzszeresz = Tuzszeresz(14, 3025, 2972, 84)


level1Optikus = Optikus(1, 119, 0, 14)
level2Optikus = Optikus(2, 188, 35, 17)
level3Optikus = Optikus(3, 269, 96, 21)
level4Optikus = Optikus(4, 362, 167, 25)
level5Optikus = Optikus(5, 471, 249, 30)
level6Optikus = Optikus(6, 597, 345, 34)
level7Optikus = Optikus(7, 742, 455, 39)
level8Optikus = Optikus(8, 912, 584, 44)
level9Optikus = Optikus(9, 1108, 733, 49)
level10Optikus = Optikus(10, 1335, 905, 55)
level11Optikus = Optikus(11, 1600, 1106, 61)
level12Optikus = Optikus(12, 1906, 1338, 67)

level1Acsmester = Acsmester(1, 63, 0, 13)
level2Acsmester = Acsmester(2, 122, 0, 16)
level3Acsmester = Acsmester(3, 192, 0, 20)
level4Acsmester = Acsmester(4, 274, 0, 24)
level5Acsmester = Acsmester(5, 372, 0, 29)
level6Acsmester = Acsmester(6, 486, 0, 34)
level7Acsmester = Acsmester(7, 620, 0, 38)
level8Acsmester = Acsmester(8, 777, 359, 43)
level9Acsmester = Acsmester(9, 962, 444, 49)
level10Acsmester = Acsmester(10, 1178, 546, 55)
level11Acsmester = Acsmester(11, 1432, 669, 60)
level12Acsmester = Acsmester(12, 1730, 816, 67)
level13Acsmester = Acsmester(13, 2078, 993, 73)
level14Acsmester = Acsmester(14, 2486, 1205, 81)

level1Komuves = Komuves(1, 274, 0, 18)
level2Komuves = Komuves(2, 467, 116, 30)
level3Komuves = Komuves(3, 718, 255, 43)
level4Komuves = Komuves(4, 1045, 436, 57)
level5Komuves = Komuves(5, 1469, 671, 73)
level6Komuves = Komuves(6, 2021, 977, 91)
level7Komuves = Komuves(7, 2738, 1375, 110)
level8Komuves = Komuves(8, 3671, 1892, 131)
level9Komuves = Komuves(9, 4883, 2574, 155)
level10Komuves = Komuves(10, 6459, 3437, 180)
level11Komuves = Komuves(11, 8508, 4572, 210)


level1Bortermelo = Bortermelo(1, 274, 0, 18)
level2Bortermelo = Bortermelo(2, 467, 116, 30)
level3Bortermelo = Bortermelo(3, 718, 255, 43)
level4Bortermelo = Bortermelo(4, 1045, 436, 57)
level5Bortermelo = Bortermelo(5, 1469, 671, 73)
level6Bortermelo = Bortermelo(6, 2021, 977, 91)
level7Bortermelo = Bortermelo(7, 2738, 1375, 110)
level8Bortermelo = Bortermelo(8, 3671, 1892, 131)
level9Bortermelo = Bortermelo(9, 4883, 2574, 155)
level10Bortermelo = Bortermelo(10, 6459, 3437, 180)
level11Bortermelo = Bortermelo(11, 8508, 4572, 210)


level1Alkimistatorony = Alkimistatorony(1, 274, 0, 18)
level2Alkimistatorony = Alkimistatorony(2, 467, 116, 30)
level3Alkimistatorony = Alkimistatorony(3, 718, 255, 43)
level4Alkimistatorony = Alkimistatorony(4, 1045, 436, 57)
level5Alkimistatorony = Alkimistatorony(5, 1469, 671, 73)
level6Alkimistatorony = Alkimistatorony(6, 2021, 977, 110)
level7Alkimistatorony = Alkimistatorony(7, 2738, 1375, 131)
level8Alkimistatorony = Alkimistatorony(8, 3671, 1892, 131)
level9Alkimistatorony = Alkimistatorony(9, 4883, 2564, 155)
level10Alkimistatorony = Alkimistatorony(10, 6459, 3437, 240)
level11Alkimistatorony = Alkimistatorony(11, 8508, 4572, 210)
level12Alkimistatorony = Alkimistatorony(12, 11172, 6049, 262)
level13Alkimistatorony = Alkimistatorony(13, 1463, 7968, 274)

level1Uvegfuvo = Uvegfuvo(1, 274, 0, 18)
level2Uvegfuvo = Uvegfuvo(2, 467, 116, 30)
level3Uvegfuvo = Uvegfuvo(3, 718, 255, 43)
level4Uvegfuvo = Uvegfuvo(4, 1045, 436, 57)
level5Uvegfuvo = Uvegfuvo(5, 1469, 671, 73)
level6Uvegfuvo = Uvegfuvo(6, 2021, 977, 91)
level7Uvegfuvo = Uvegfuvo(7, 2738, 1375, 110)
level8Uvegfuvo = Uvegfuvo(8, 3671, 1892, 131)

level1Erdeszhaz = Erdeszhaz(1, 250, 0, 18)
level2Erdeszhaz = Erdeszhaz(2, 430, 104, 30)
level3Erdeszhaz = Erdeszhaz(3, 664, 237, 43)
level4Erdeszhaz = Erdeszhaz(4, 930, 410, 58)
level5Erdeszhaz = Erdeszhaz(5, 1364, 635, 73)
level6Erdeszhaz = Erdeszhaz(6, 1878, 928, 91)
level7Erdeszhaz = Erdeszhaz(7, 2545, 1309, 110)
level8Erdeszhaz = Erdeszhaz(8, 3415, 180, 130)
level9Erdeszhaz = Erdeszhaz(9, 4544, 2446, 175)

level1Rejtekhely = Rejtekhely(1, 113, 0, 24)
level2Rejtekhely = Rejtekhely(2, 248, 0, 36)
level3Rejtekhely = Rejtekhely(3, 402, 0, 49)
level4Rejtekhely = Rejtekhely(4, 578, 0, 61)
level5Rejtekhely = Rejtekhely(5, 779, 129, 75)
level6Rejtekhely = Rejtekhely(6, 1007, 276, 90)
level7Rejtekhely = Rejtekhely(7, 1267, 366, 105)
level8Rejtekhely = Rejtekhely(8, 1564, 471, 121)
level9Rejtekhely = Rejtekhely(9, 1903, 593, 140)
level10Rejtekhely = Rejtekhely(10, 2288, 735, 160)
level11Rejtekhely = Rejtekhely(11, 2728, 900, 174)
level12Rejtekhely = Rejtekhely(12, 3230, 1090, 194)

level1Muhely = Muhely(1, 220, 95, 42)
level2Muhely = Muhely(2, 383, 167, 54)
level3Muhely = Muhely(3, 569, 251, 66)
level4Muhely = Muhely(4, 781, 349, 80)
level5Muhely = Muhely(5, 1023, 461, 93)
level6Muhely = Muhely(6, 1300, 592, 108)
level7Muhely = Muhely(7, 1613, 744, 123)
level8Muhely = Muhely(8, 1972, 920, 140)
level9Muhely = Muhely(9, 2380, 1125, 160)
level10Muhely = Muhely(10, 2846, 1362, 180)

level1Piac = Piac(1, 48, 0, 24, 400)
level2Piac = Piac(2, 173, 0, 42, 1600)
level3Piac = Piac(3, 346, 0, 61, 3600)
level4Piac = Piac(4, 581, 0, 83, 6400)
level5Piac = Piac(5, 896, 540, 107, 10000)
level6Piac = Piac(6, 1314, 792, 133, 14400)
level7Piac = Piac(7, 1800, 1123, 162, 19600)
level8Piac = Piac(8, 2580, 1555, 184, 25600)
level9Piac = Piac(9, 3509, 2115, 220, 32400)
level10Piac = Piac(10, 4706, 2837, 270, 40000)
level11Piac = Piac(11, 6200, 3762, 310, 48400)
level12Piac = Piac(12, 8203, 4945, 360, 57600)
level13Piac = Piac(13, 10699, 6450, 408, 67600)

level1Nagykovetseg = Nagykovetseg(1, 242, 155, 72)
level2Nagykovetseg = Nagykovetseg(2, 415, 342, 84)
level3Nagykovetseg = Nagykovetseg(3, 623, 571, 100)
level4Nagykovetseg = Nagykovetseg(4, 873, 850, 110)
level5Nagykovetseg = Nagykovetseg(5, 1173, 1190, 123)
level6Nagykovetseg = Nagykovetseg(6, 1532, 1606, 140)
level7Nagykovetseg = Nagykovetseg(7, 1964, 2112, 158)
level8Nagykovetseg = Nagykovetseg(8, 2482, 2730, 170)
level9Nagykovetseg = Nagykovetseg(9, 3103, 3484, 186)

level1Varosfal = Varosfal(1, 114, 0, 1)
level2Varosfal = Varosfal(2, 361, 203, 51)
level3Varosfal = Varosfal(3, 657, 516, 62)
level4Varosfal = Varosfal(4, 1012, 892, 73)
level5Varosfal = Varosfal(5, 1439, 1344, 90)
level6Varosfal = Varosfal(6, 1951, 1885, 100)
level7Varosfal = Varosfal(7, 2565, 2535, 120)
level8Varosfal = Varosfal(8, 3302, 3315, 133)
level9Varosfal = Varosfal(9, 4102, 4251, 151)
level10Varosfal = Varosfal(10, 5247, 5374, 170)
level11Varosfal = Varosfal(11, 6251, 6721, 195)
level12Varosfal = Varosfal(12, 8000, 8000, 217)

level1Barakk = Barakk(1, 49, 0, 1, "dardas")
level2Barakk = Barakk(2, 114, 0, 17, "parittyas")
level3Barakk = Barakk(3, 195, 0, 22, "faltoro")
level4Barakk = Barakk(4, 296, 0, 27, "hoplita")
level5Barakk = Barakk(5, 420, 0, 32, "sef")
level6Barakk = Barakk(6, 574, 0, 39, "kardforgato")
level7Barakk = Barakk(7, 766, 0, 46, "Ijasz")
level8Barakk = Barakk(8, 1003, 0, 53, "Katapult")
level9Barakk = Barakk(9, 1297, 178, 61, "felcser")
level10Barakk = Barakk(10, 1662, 421, 70, "gyrokopter")
level11Barakk = Barakk(11, 2115, 745, 80, "ballonos")
level12Barakk = Barakk(12, 2676, 1134, 92, "gozorias")
level13Barakk = Barakk(13, 3371, 1616, 103, "karabelyos")
level14Barakk = Barakk(14, 4234, 2214, 120, "agyu")

level1Hajogyar = Hajogyar(1, 105, 0, 43, "toro")
level2Hajogyar = Hajogyar(2, 202, 0, 51, "baliszta")
level3Hajogyar = Hajogyar(3, 324, 0, 60, "katapult")
level4Hajogyar = Hajogyar(4, 477, 0, 68, "lang")
level5Hajogyar = Hajogyar(5, 671, 0, 78)
level6Hajogyar = Hajogyar(6, 914, 778, 90)
level7Hajogyar = Hajogyar(7, 1222, 1052, 100, "leghajo")
level8Hajogyar = Hajogyar(8, 1609, 1400, 109)
level9Hajogyar = Hajogyar(9, 2096, 1832, 153, "uszobazis")
level10Hajogyar = Hajogyar(10, 2710, 2381, 130)

level1Kikoto = Kikoto(1, 60, 0, 2)
level2Kikoto = Kikoto(2, 150, 0, 23)
level3Kikoto = Kikoto(3, 274, 0, 30)
level4Kikoto = Kikoto(4, 429, 0, 38)
level5Kikoto = Kikoto(5, 637, 0, 48)
level6Kikoto = Kikoto(6, 894, 175, 59)
level7Kikoto = Kikoto(7, 1207, 326, 72)
level8Kikoto = Kikoto(8, 1645, 540, 90)
level9Kikoto = Kikoto(9, 2106, 791, 108)
level10Kikoto = Kikoto(10, 2735, 1139, 122)
level11Kikoto = Kikoto(11, 3537, 1598, 144)
level12Kikoto = Kikoto(12, 4492, 2176, 170)

level1Muzeum = Muzeum(1, 560, 280, 96)
level2Muzeum = Muzeum(2, 1435, 1200, 130)
level3Muzeum = Muzeum(3, 2748, 2573, 180)
level4Muzeum = Muzeum(4, 4716, 4676, 200)
level5Muzeum = Muzeum(5, 7677, 7871, 249)
level6Muzeum = Muzeum(6, 12099, 12729, 299)
level7Muzeum = Muzeum(7, 18744, 20121, 350)
level8Muzeum = Muzeum(8, 28333, 31335, 440)
level9Muzeum = Muzeum(9, 43661, 48333, 480)
level10Muzeum = Muzeum(10, 66000, 74323, 542)
level11Muzeum = Muzeum(11, 99724, 113736, 600)

level1Palota = Palota(1, 712, 0, 0, 0, 0, 268)
level2Palota = Palota(2, 5824, 0, 1434, 0, 0, 376)
level3Palota = Palota(3, 16048, 0, 4546, 0, 3089, 540)
level4Palota = Palota(4, 36400, 10894, 10770, 0, 10301, 720)
level5Palota = Palota(5, 77392, 22110, 23218, 21188, 24725, 1020)
level6Palota = Palota(6, 159184, 44534, 48232, 42400, 53573, 1440)
level6Palota = Palota(7, 322344, 89382, 97906, 84824, 111265, 2000)

level1Fogado = Fogado(1, 101, 0, 17, 4, 12, 60)
level2Fogado = Fogado(2, 222, 0, 28, 8, 24, 120)
level3Fogado = Fogado(3, 367, 0, 40, 13, 36, 180)
level4Fogado = Fogado(4, 541, 94, 53, 24, 48, 240)
level5Fogado = Fogado(5, 750, 122, 66, 24, 60, 300)
level6Fogado = Fogado(6, 1001, 158, 81, 24, 72, 360)
level7Fogado = Fogado(7, 1302, 206, 96, 30, 84, 420)
level8Fogado = Fogado(8, 1663, 267, 112, 44, 96, 480)
level9Fogado = Fogado(9, 2097, 348, 130, 51, 108, 540)
level10Fogado = Fogado(10, 2617, 452, 148, 60, 120, 600)
level11Fogado = Fogado(11, 3241, 587, 167, 68, 132, 660)
level12Fogado = Fogado(12, 3990, 764, 188, 78, 144, 720)
level13Fogado = Fogado(13, 4888, 993, 210, 88, 156, 780)
level14Fogado = Fogado(14, 5967, 1290, 240, 99, 168, 840)

level1Raktar = Raktar(1, 160, 0, 1, 8000)
level2Raktar = Raktar(2, 288, 0, 7, 16000)
level3Raktar = Raktar(3, 442, 0, 35, 24000)
level4Raktar = Raktar(4, 626, 96, 45, 32000)
level5Raktar = Raktar(5, 847, 211, 56, 40000)
level6Raktar = Raktar(6, 1113, 349, 1, 48000)
level7Raktar = Raktar(7, 1430, 515, 69, 56000)
level8Raktar = Raktar(8, 1813, 714, 84, 64000)
level9Raktar = Raktar(9, 2272, 953, 100, 72000)
level10Raktar = Raktar(10, 2822, 1240, 126, 80000)
level11Raktar = Raktar(11, 3483, 1584, 166, 88000)
level12Raktar = Raktar(12, 4275, 1997, 195, 96000)
level13Raktar = Raktar(13, 5200, 2492, 227, 104000)
level14Raktar = Raktar(14, 6000, 3000, 264, 112000)

level1Akediamia = Akademia(1, 64, 0, 0.5, 8)
level2Akediamia = Akademia(2, 68, 0, 22., 12)
level3Akediamia = Akademia(3, 115, 0, 37, 16)
level4Akediamia = Akademia(4, 263, 0, 47, 22)
level5Akediamia = Akademia(5, 382, 225, 59, 28)
level6Akediamia = Akademia(6, 626, 428, 74, 35)
level7Akediamia = Akademia(7, 982, 744, 85, 43)
level8Akediamia = Akademia(8, 1330, 1089, 101, 51)
level9Akediamia = Akademia(9, 2004, 1748, 136, 60)
level10Akediamia = Akademia(10, 2665, 2454, 166, 69)
level11Akediamia = Akademia(11, 3916, 3786, 201, 79)
level12Akediamia = Akademia(12, 5156, 5216, 244, 89)
level13Akediamia = Akademia(13, 7446, 7862, 300, 100)
level14Akediamia = Akademia(14, 9753, 10729, 350, 111)

level1Varoshaza = Varoshaza(1, 0, 0, 0, 60)
level2Varoshaza = Varoshaza(2, 158, 0, 59, 96)
level3Varoshaza = Varoshaza(3, 335, 0, 66, 142)
level4Varoshaza = Varoshaza(4, 623, 0, 74, 200)
level5Varoshaza = Varoshaza(5, 923, 285, 83, 262)
level6Varoshaza = Varoshaza(6, 1390, 551, 94, 332)
level7Varoshaza = Varoshaza(7, 2015, 936, 108, 410)
level8Varoshaza = Varoshaza(8, 2706, 1411, 123, 492)
level9Varoshaza = Varoshaza(9, 2706, 2000, 141, 580)
level10Varoshaza = Varoshaza(10, 4776, 3000, 162, 672)
level11Varoshaza = Varoshaza(11, 6173, 4000, 186, 768)
level12Varoshaza = Varoshaza(12, 8074, 5600, 210, 870)
level13Varoshaza = Varoshaza(13, 10281, 7600, 248, 976)
level14Varoshaza = Varoshaza(14, 13023, 10214, 290, 1086)
kalozerod = [level1Kalozerod, level2Kalozerod, level3Kalozerod, level4Kalozerod, level5Kalozerod, level6Kalozerod,
             level7Kalozerod, level8Kalozerod, level9Kalozerod, level10Kalozerod, level11Kalozerod, level12Kalozerod, level13Kalozerod]
templom = [level1Templom, level2Templom, level3Templom, level4Templom, level5Templom,
           level6Templom, level7Templom, level8Templom, level9Templom, level10Templom]
epitesz = [level1Epitesz, level2Epitesz, level3Epitesz, level4Epitesz, level5Epitesz, level6Epitesz,
           level7Epitesz, level8Epitesz, level9Epitesz, level10Epitesz, level11Epitesz, level12Epitesz]
szolopres = [level1Szolopres, level2Szolopres, level3Szolopres, level4Szolopres, level5Szolopres, level6Szolopres,
             level7Szolopres, level8Szolopres, level9Szolopres, level10Szolopres, level11Szolopres, level12Szolopres]
tuzszeresz = [level1Tuzszeresz, level2Tuzszeresz, level3Tuzszeresz, level4Tuzszeresz, level5Tuzszeresz, level6Tuzszeresz, level7Tuzszeresz,
              level8Tuzszeresz, level9Tuzszeresz, level10Tuzszeresz, level11Tuzszeresz, level12Tuzszeresz, level13Tuzszeresz, level14Tuzszeresz]
optikus = [level1Optikus, level2Optikus, level3Optikus, level4Optikus, level5Optikus, level6Optikus,
           level7Optikus, level8Optikus, level9Optikus, level10Optikus, level11Optikus, level12Optikus]
acsmester = [level1Acsmester, level2Acsmester, level3Acsmester, level4Acsmester, level5Acsmester, level6Acsmester, level7Acsmester,
             level8Acsmester, level9Acsmester, level10Acsmester, level11Acsmester, level12Acsmester, level13Acsmester, level14Acsmester]

komuves = [level1Komuves, level2Komuves, level3Komuves, level4Komuves, level5Komuves,
           level6Komuves, level7Komuves, level8Komuves, level9Komuves, level10Komuves, level11Komuves]
bortemelo = [level1Bortermelo, level2Bortermelo, level3Bortermelo, level4Bortermelo, level5Bortermelo,
             level6Bortermelo, level7Bortermelo, level8Bortermelo, level9Bortermelo, level10Bortermelo, level11Bortermelo]
alkimistatorony = [level1Alkimistatorony, level2Alkimistatorony, level3Alkimistatorony, level4Alkimistatorony, level5Alkimistatorony, level6Alkimistatorony,
                   level7Alkimistatorony, level8Alkimistatorony, level9Alkimistatorony, level10Alkimistatorony, level11Alkimistatorony, level12Alkimistatorony, level13Alkimistatorony]
erdeszhaz = [level1Erdeszhaz, level2Erdeszhaz, level3Erdeszhaz, level4Erdeszhaz,
             level5Erdeszhaz, level6Erdeszhaz, level7Erdeszhaz, level8Erdeszhaz, level9Erdeszhaz]
rejtekhely = [level1Rejtekhely, level2Rejtekhely, level3Rejtekhely, level3Rejtekhely, level4Rejtekhely, level5Rejtekhely,
              level6Rejtekhely, level7Rejtekhely, level8Rejtekhely, level9Rejtekhely, level10Rejtekhely, level11Rejtekhely, level12Rejtekhely]
muhely = [level1Muhely, level2Muhely, level3Muhely, level4Muhely, level5Muhely,
          level6Muhely, level7Muhely, level8Muhely, level9Muhely, level10Muhely]
piac = [level1Piac, level2Piac, level3Piac, level4Piac, level5Piac, level6Piac,
        level7Piac, level8Piac, level9Piac, level10Piac, level11Piac, level12Piac, level13Piac]
varosfal = [level1Varosfal, level2Varosfal, level3Varosfal, level4Varosfal, level5Varosfal, level6Varosfal, level7Varosfal,
            level8Varosfal, level9Varosfal, level10Varosfal, level11Varosfal, level12Varosfal, level13Varoshaza, level14Varoshaza]
barakk = [level1Barakk, level2Barakk, level3Barakk, level4Barakk, level5Barakk, level6Barakk, level7Barakk,
          level8Barakk, level9Barakk, level10Barakk, level11Barakk, level12Barakk, level13Barakk, level14Barakk]
kikoto = [level1Kikoto, level2Kikoto, level3Kikoto, level4Kikoto, level5Kikoto, level6Kikoto,
          level7Kikoto, level8Kikoto, level9Kikoto, level10Kikoto, level11Kikoto, level12Kikoto]
muzeum = [level1Muzeum, level2Muzeum, level3Muzeum, level4Muzeum, level5Muzeum,
          level6Muzeum, level7Muzeum, level8Muzeum, level9Muzeum, level10Muzeum, level11Muzeum]
palota = [level1Palota, level2Palota, level3Palota,
          level4Palota, level5Palota, level6Palota]
fogado = [level1Fogado, level2Fogado, level3Fogado, level4Fogado, level5Fogado, level6Fogado,
          level7Fogado, level8Fogado, level9Fogado, level10Fogado, level11Fogado, level12Fogado, level13Fogado]
raktar = [level1Raktar, level2Raktar, level3Raktar, level4Raktar, level5Raktar, level6Raktar, level7Raktar,
          level8Raktar, level9Raktar, level10Raktar, level11Raktar, level12Raktar, level13Raktar, level14Raktar]
akademia = [level1Akediamia, level2Akediamia, level3Akediamia, level4Akediamia, level5Akediamia, level6Akediamia, level7Akediamia,
            level8Akediamia, level9Akediamia, level10Akediamia, level11Akediamia, level12Akediamia, level13Akediamia, level14Akediamia]
varoshaza = [level1Varoshaza, level2Varoshaza, level3Varoshaza, level4Varoshaza, level5Varoshaza, level6Varoshaza, level7Varoshaza,
             level8Varoshaza, level9Varoshaza, level10Varoshaza, level11Varoshaza, level12Varoshaza, level13Varoshaza, level14Varoshaza]


