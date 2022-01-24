

class Generate:

    def __init__(self):
        pass

    def Generate_pixels(self, file):
        a = "0"
        game_map = []
        for i in range(0, 700):
            game_map.append(a * 1300)

        f = open(file + ".txt", "w+")
        for i in game_map:
            f.write(i + "\n")
        f.close()

    def Clear(self, file, type):
        f = open(file+"."+type, "w+")
        f.write("")
        f.close()



