import pygame
import csv


class TxtGestion:

    def __init__(self, program):
        self.program = program
        self.min_height = 1000
        self.max_height = 0



    def Read(self, file):
        f = open(file, "r")
        data = f.read()
        f.close()
        data = data.split("\n")
        game_map = []
        for row in data:
           game_map.append(list(row))
        return game_map


    def Write(self, line, type = "single", file="data/pixels.txt"):
        # get the current data in the actual file to not overwrite
        self.data = self.Read(file)

        # calculate the changes
        if type == "single":
            for numbers in line:
                self.data[numbers[1]][numbers[0]] = "1"
        elif type == 'multiple':
            for numbers in line:
                for number in numbers:
                    self.data[number[1]][number[0]] = "1"


        # open the txt file as writeble
        f = open(file, "w+")

        # apply the changes and close txt file
        lenght = len(self.data)
        count = 0

        for lines in self.data:
            for number in lines:
                f.write(str(number))
            if count == lenght - 1:
                pass
            else:
                f.write("\n")
            count += 1

        f.close()

        # clear the data to not satturate the computer
        self.data = []


    def calculate(self, x1, y1, x2, y2):
        if self.program.image_type == 2:
            if self.program.homepage.currently[0] == 1:
                #get the max height
                if y1 < y2 and y1 < self.program.homepage.images[0].min_height:
                    self.program.homepage.images[0].min_height = y1
                elif y2 < y1 and y2 < self.program.homepage.images[0].max_height:
                    self.program.homepage.images[0].min_height = y2

                #get the min height
                if y1 > y2 and y1 > self.program.homepage.images[0].min_height:
                    self.program.homepage.images[0].max_height = y1
                elif y2 > y1 and y2 > self.program.homepage.images[0].max_height:
                    self.program.homepage.images[0].max_height = y2
            else:########################################################
                # get the max height
                if y1 < y2 and y1 < self.program.homepage.images[1].min_height:
                    self.program.homepage.images[1].min_height = y1
                elif y2 < y1 and y2 < self.program.homepage.images[1].max_height:
                    self.program.homepage.images[1].min_height = y2

                # get the min height
                if y1 > y2 and y1 > self.program.homepage.images[1].min_height:
                    self.program.homepage.images[1].max_height = y1
                elif y2 > y1 and y2 > self.program.homepage.images[1].max_height:
                    self.program.homepage.images[1].max_height = y2
        elif self.program.image_type == 1:
            if y1 < y2 and y1 < self.min_height:
                self.min_height = y1
            elif y2 < y1 and y2 < self.max_height:
                self.min_height = y2

            # get the min height
            if y1 > y2 and y1 > self.min_height:
                self.max_height = y1
            elif y2 > y1 and y2 > self.max_height:
                self.max_height = y2
        self.point1 = [x1, y1]
        self.point2 = [x2, y2]
        case = 0  # 1: equal road

        # calculate the lenght of the x line
        if self.point1[0] > self.point2[0]:
            self.x_lenght = self.point1[0] - self.point2[0]
        else:
            self.x_lenght = self.point2[0] - self.point1[0]

        # calculate the lenght of the y line
        if self.point1[1] > self.point2[1]:
            self.y_lenght = self.point1[1] - self.point2[1]
        else:
            self.y_lenght = self.point2[1] - self.point1[1]


        if x1 > x2:
            longest_point = x1
            shortest_point = x2
        else:
            longest_point = x2
            shortest_point = x1
        if y1 > y2:
            highest_point = y1
            lowest_point = y2

        else:
            highest_point = y2
            lowest_point = y1






        if self.x_lenght > self.y_lenght:

            #print("passed by x_lenght > y_lenght")
            #define the line way parameters
            steps = self.y_lenght
            if self.y_lenght == 0:
                self.y_lenght = 1
            lenght_per_step = int(self.x_lenght / self.y_lenght)
            rest_lenght = self.x_lenght - (lenght_per_step*self.y_lenght)  #xc
            starting_pixel_x = self.point1[0]
            starting_pixel_y = self.point1[1]
            self.line = []


            ########  rest  #########
            if rest_lenght == 0:
                rest_lenght = 1
            default_num = int(steps/rest_lenght)
            counter = 0
            num = default_num
            #print(f"steps : {steps}, rest lenght : {rest_lenght}, num : {num}")
            #########################

            #make the line way according to the parameters
            for step in range(0, steps):
                self.line.append([starting_pixel_x, starting_pixel_y]) # CHANGE§§§§§§§§§§
                for i in range(0, lenght_per_step):
                    # here we add the rest calculated in the begining
                    if num-1 == step and not counter == rest_lenght:
                        if longest_point == self.point2[0]:
                            starting_pixel_x += 1
                        else:
                            starting_pixel_x -= 1
                        num += default_num
                        counter += 1
            ###here happens the basic line calculations
                    if longest_point == self.point2[0]:
                        starting_pixel_x += 1
                    else:
                        starting_pixel_x -= 1

                    #print(step, steps)
                    if steps - step == 1 and lenght_per_step - i == 1:
                        if highest_point == self.point2[1]:
                            starting_pixel_y += 1
                        else:
                            starting_pixel_y -= 1


                    self.line.append([starting_pixel_x, starting_pixel_y]) # CHANGE§§§§§§§§§§
                if highest_point == self.point2[1]:
                    starting_pixel_y += 1
                else:
                    starting_pixel_y -= 1


            #print(self.line)
            #print(rest_lenght)
            #print(self.line[0], self.line[-1])




        elif self.y_lenght > self.x_lenght:

            #print("passed by y_lenght > x_lenght")
            # define the line way parameters
            steps = self.x_lenght
            if self.x_lenght == 0:
                self.x_lenght = 1
            lenght_per_step = int(self.y_lenght / self.x_lenght)
            rest_lenght = self.y_lenght - (lenght_per_step * self.x_lenght)
            starting_pixel_x = self.point1[0]
            starting_pixel_y = self.point1[1]
            self.line = []

            ########  rest  #########
            if rest_lenght == 0:
                rest_lenght = 1
            default_num = int(steps / rest_lenght)
            counter = 0
            num = default_num
            #print(f"steps : {steps}, rest lenght : {rest_lenght}, num : {num}")
            #########################

            # make the line way according to the parameters
            for step in range(0, steps):
                self.line.append([starting_pixel_x, starting_pixel_y]) # CHANGE§§§§§§§§§§
                for i in range(0, lenght_per_step):
                    #here we add the rest calculated in the begining
                    if num-1 == step and not counter == rest_lenght:
                        if highest_point == self.point2[1]:
                            starting_pixel_y += 1
                            self.line.append([starting_pixel_x, starting_pixel_y]) # CHANGE§§§§§§§§§§
                        else:
                            starting_pixel_y -= 1
                            self.line.append([starting_pixel_x, starting_pixel_y]) # CHANGE§§§§§§§§§§
                        num += default_num
                        counter += 1
            ###here happens the basic line calculations
                    if highest_point == self.point2[1]:
                        starting_pixel_y += 1
                    else:
                        starting_pixel_y -= 1
                    # print(step, steps)
                    if steps - step == 1 and lenght_per_step - i == 1:
                        if longest_point == self.point2[0]:
                            starting_pixel_x += 1
                        else:
                            starting_pixel_x -= 1
                    self.line.append([starting_pixel_x, starting_pixel_y]) # CHANGE§§§§§§§§§§
                if longest_point == self.point2[0]:
                    starting_pixel_x += 1
                else:
                    starting_pixel_x -= 1
            #print(self.line)
            #print(rest_lenght)
            #print(self.line[0], self.line[-1])
        else:
            raise Exception("An unknown error occured")

        #with open("save.csv", "a", newline="\n") as f:
        #    write = csv.writer(f)
        #    t = []
        #    for number in self.line:
        #        t.append(number[0])
        #        t.append(number[1])
        #    t.append(self.point1[0])
         #   t.append(self.point1[1])
          #  t.append(self.point2[0])
          #  t.append(self.point2[1])
            #t = range of numbers  ; 4 last numbers are the first and last points
           # write.writerow(t)
          #  f.close()
        #with open("save.csv") as f:
        #    read = csv.reader(f)
        #    for row in read:
        #        print(row)
        #    f.close()


        # save the data for extra security

        f = open("data/save.csv", "r")
        actual_save = f.read()
        f.close()
        f = open("data/save.csv", "w+")
        f.write(actual_save + "\n" + str(self.line) + ";" + str((self.point1, self.point2)))
        f.close()

        return self.line


    def back(self, file="data/save.csv"):
        print("back!")
        f = open(file, "r")
        actual_data = f.read()
        f.close()
        actual_data = actual_data.split("\n")
        new_data = ""
        count = 1
        for i in actual_data:
            new_data += i
            if count == len(actual_data)-1:
                break
            else:
                count += 1
                new_data += "\n"
        f = open(file, "w+")
        f.write(new_data)
        f.close()
        if self.program.image_type == 2:
            if self.program.homepage.currently[0] == 1:
                del self.program.homepage.images[0].leaf_lines[-1]

                self.program.position1x = self.program.homepage.images[0].leaf_lines[-1][1]
                self.program.position1y = self.program.homepage.images[0].leaf_lines[-1][3]
            else:
                del self.program.homepage.images[1].leaf_lines[-1]

                self.program.position1x = self.program.homepage.images[1].leaf_lines[-1][1]
                self.program.position1y = self.program.homepage.images[1].leaf_lines[-1][3]
        else:
            del self.program.draw_line.leaf_lines[-1]

            self.program.position1x = self.program.draw_line.leaf_lines[-1][1]
            self.program.position1y = self.program.draw_line.leaf_lines[-1][3]




    #generate
#a = "0"
#game_map = []
#for i in range(0, 700):
#    game_map.append(a*1000)
#print(game_map)
#
#f = open("pixels.txt", "w+")
#for i in game_map:
#    f.write(i+"\n")
#f.close()
#
#f = open("pixels.txt", "r")
#data = f.read()
#f.close()
#data = data.split("\n")
#game_map = []
#for row in data:
#    game_map.append(list(row))
#
#print(game_map)