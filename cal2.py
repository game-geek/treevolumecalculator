import  pygame


class Cal:

    def __init__(self):
        self.points = []
        self.calculate(30, 25, 30, 300)

    def imp(self, screen):
        pix = pygame.PixelArray(screen)
        for i in self.points:

            pix[i[0]][i[1]] = (0, 0, 225)
            print(i[0],i[1])

        print(self.points)

    def calculate(self, Ax, Ay, Bx, By):
        change = None
        print('ha')
        self.points.clear()
        self.default_Ax = Ax
        self.default_Bx = Bx
        self.default_Ay = Ay
        self.default_By = By







        # Were is a and b


        if Ax > Bx:
            longest_point = Ax
            shortest_point = Bx
        else:
            longest_point = Bx
            shortest_point = Ax
        if Ay > By:
            highest_point = Ay
            lowest_point = By

        else:
           highest_point = By
           lowest_point = Ay

        #print(highest_point)
        #print(lowest_point)
        #print(longest_point)
        #print(shortest_point)




        #Calculate general coeff and coeff

        if longest_point-shortest_point > highest_point-lowest_point:
            general_coeff = 'Hight'
            coeff = int(highest_point-lowest_point)
            coeff2 = (longest_point-shortest_point)/coeff
        else:
            general_coeff = 'Lenght'
            coeff = int(longest_point-shortest_point)
            coeff2 = (highest_point-lowest_point) / coeff



        # Detect if coeff2 = 1.9 to 2
        #print(coeff2)
        print(coeff2)
        if coeff2 > int(coeff2):
            if coeff2 > int(coeff2)+0.9:
                coeff2 = int(coeff2)+1
                change = None
            elif coeff2 >= int(coeff2)+0.8 :
                print(coeff2)
                change = 8
            elif coeff2 >= int(coeff2)+0.7 :
                print(coeff2)
                change = 7
            elif coeff2 >= int(coeff2)+0.6 :
                print(coeff2)
                change = 6
            elif coeff2 >= int(coeff2)+0.5 :
                print(coeff2)
                change = 5
            elif coeff2 >= int(coeff2)+0.4 :
                print(coeff2)
                change = 4
            elif coeff2 >= int(coeff2)+0.3 :
                print(coeff2)
                change = 3
            elif coeff2 >= int(coeff2)+0.2 :
                print(coeff2)
                change = 2
            elif coeff2 >= int(coeff2)+0.1 :
                print(coeff2)
                change = 1
            else:
                change = None
        print(coeff2)
        coeff2 = int(coeff2)
        print(coeff2)

        #if not detect if coeff2 = 1.1 to 1.9


        # set Ax and Ay

        pixelx = Ax
        pixely = Ay
        basic_coeff2 = coeff2
        up = coeff2 + 1

        number = 1


        if change != None:
            coeff2 = up


        #proirity

        for i in range (0, coeff):


            for a in range (0, coeff2):
                self.points.append((pixelx, pixely))






                #add a pixel
                if general_coeff == 'Hight':
                    if longest_point == Ax:
                        pixelx -= 1
                    else: #longest point = Bx
                        pixelx += 1
                else:
                    if longest_point == Ax:
                        pixely -= 1
                    else: #longest point = Bx
                        pixely += 1

            #Change
            if change != None:
               if number <= change:
                   coeff2 = up
                   number+=1
               elif number == 10:
                   number = 1
               else:
                   coeff2 = basic_coeff2


                   number+=1

               print(coeff2)



            #move up a pixel step
            if general_coeff == 'Hight':
                if highest_point == Ay:
                    pixely -= 1
                else: # highest_point = By
                    pixely += 1
            else:
                if highest_point == Ay:
                    pixelx -= 1
                else:  # highest_point = By
                    pixelx += 1

        if By == lowest_point:
            if pixely > By:
                while pixely > By:
                    self.points.append((pixelx, pixely))
                    pixely-=1
        elif By == highest_point:
            if pixely < By:
                while pixely < By:
                    self.points.append((pixelx, pixely))
                    pixely+=1


        if Bx == shortest_point:
            if pixelx > Bx:
                while pixelx > Bx:
                    self.points.append((pixelx, pixely))
                    pixelx-=1
        elif Bx == longest_point:
            if pixelx < Bx:
                while pixelx < Bx:
                    self.points.append((pixelx, pixely))
                    pixelx+=1







