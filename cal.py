import  pygame


class Cal:

    def __init__(self):
        self.points = []
        self.calculate(200, 100, 100, 50)

    def imp(self, screen):
        pix = pygame.PixelArray(screen)
        for i in self.points:

            pix[i[0]][i[1]] = (0, 0, 225)

    def calculate(self, Ax, Bx, Ay, By):
        self.points.clear()
        self.default_Ax = Ax
        self.default_Bx = Bx
        self.default_Ay = Ay
        self.default_By = By
        if Ax > Bx and Ay > By:
            # case1

            for i in range (0, 10000):
                if Ax - Bx > Ay - By:
                    if Ax == self.default_Bx + 1:
                        pass
                    else:
                        print('case1')
                        Ax -= 1
                        self.points.append((Ax, Ay))
                else:
                    if Ay == self.default_By+1:
                        pass
                    else:
                        print('case1b')
                        Ay -= 1
                        self.points.append((Ax, Ay))

                print(Ax)
                #if  Ax == self.default_Bx+1 or Ay == self.default_By+1:
                #    print('break')
                #    break

            print(self.points)


        #    else:
#
        #elif Ax > Bx and By > Ay:
        #    # case2
        #    self.points.clear()
        #    if Ax - Bx > By - Ay:
        #        print('case2')
        #        default_Bx = Bx
        #        steps = By - Ay
        #        self.steps2 = int(steps) + 1
        #        total_line_lenght = Ax - Bx
        #        line_lenght = total_line_lenght / steps
        #        for i in range(0, self.steps2):
        #            for a in range(0, int(line_lenght)):
        #                print(default_Bx, Bx)
        #                if Ax == default_Bx - 1:
        #                    print('break')
        #                    break
        #                Ax -= 1
        #                self.points.append((Ax, Ay))
        #            Ay += 1
        #        print(self.points)
        #    else:
        #        print('case2b')
        #        default_Bx = Bx
        #        steps = Ax - Bx
        #        self.steps2 = int(steps) + 1
        #        total_line_lenght = By - Ay
        #        line_lenght = total_line_lenght / steps
        #        for i in range(0, self.steps2):
        #            for a in range(0, int(line_lenght)):
        #                print(default_Bx, Bx)
        #                if Ax == default_Bx - 1:
        #                    print('break')
        #                    break
        #                Ay += 1
        #                self.points.append((Ax, Ay))
        #            Ax -= 1
        #        print(self.points)
        #elif Bx > Ax and By > Ay:
        #    # case3
        #    if Bx - Ax > By - Ay:
        #        print('case3')
        #        default_Bx = Bx
        #        steps = By - Ay
        #        self.steps2 = int(steps) + 1
        #        total_line_lenght = Bx - Ax
        #        line_lenght = total_line_lenght / steps
        #        for i in range(0, self.steps2):
        #            for a in range(0, int(line_lenght)):
        #                print(default_Bx, Bx)
        #                if Ax == default_Bx - 1:
        #                    print('break')
        #                    break
        #                Ax += 1
        #                self.points.append((Ax, Ay))
        #            Ay += 1
        #        print(self.points)
        #    else:
        #        print('case3b')
        #        default_Bx = Bx
        #        steps = Bx - Ax
        #        self.steps2 = int(steps) + 1
        #        total_line_lenght = By - Ay
        #        line_lenght = total_line_lenght / steps
        #        for i in range(0, self.steps2):
        #            for a in range(0, int(line_lenght)):
        #                print(default_Bx, Bx)
        #                if Ax == default_Bx - 1:
        #                    print('break')
        #                    break
        #                Ay += 1
        #                self.points.append((Ax, Ay))
        #            Ax += 1
        #        print(self.points)
        #elif Bx > Ax and Ay > By:
        #    # case4
        #    if Bx - Ax > Ay - By:
        #        print('case4')
        #        steps = Ay - By
        #        self.steps2 = int(steps) + 1
        #        total_line_lenght = Bx - Ax
        #        default_Bx = Bx
        #        line_lenght = total_line_lenght / steps
        #        for i in range(0, self.steps2):
        #            for a in range(0, int(line_lenght)):
        #                print(default_Bx, Bx)
        #                if Ax == default_Bx - 1:
        #                    print('break')
        #                    break
        #                Ax += 1
        #                self.points.append((Ax, Ay))
        #            Ay -= 1
        #        print(self.points)
        #    else:
        #        print('case4b')
        #        steps = Bx - Ax
        #        default_Bx = Bx
        #        self.steps2 = int(steps) + 1
        #        total_line_lenght = By - Ay
        #        line_lenght = total_line_lenght / steps
        #        for i in range(0, self.steps2):
        #            for a in range(0, int(line_lenght)):
        #                print(default_Bx, Bx)
        #                if Ax == default_Bx - 1:
        #                    print('break')
        #                    break
        #                Ay -= 1
        #                self.points.append((Ax, Ay))
        #            Ax += 1
        #        print(self.points)
        ## [coordonnes]
#Ax - Bx > Ay - By
#Ax, Bx, Ay, By
#cal = Cal(20, 10, 10, 5)