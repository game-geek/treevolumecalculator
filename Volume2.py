from math import pi
#  NOTE THAT THE PROGRAM IS JUNKY :)

class Volume2:

    def __init__(self, program):
        self.program = program


    def calculate(self, precision, min_height, max_height, file="data/pixels2.txt"):

        ########################################################################################################
        #############THIS FUNCTION CUTS THE TREE IN SEVERAL PARTS AND RETURNS ALL THE INFO######################
        ########################################################################################################

        self.height = max_height - min_height #get the height of the tree
        self.part = int(self.height / precision)  #devise the tree in different parts

        #read the data of the txt file
        f = open(file, "r")
        data = f.read()
        f.close()
        data = data.split("\n")
        self.data = []
        for row in data:
            self.data.append(list(row))



        #here we loop tru each line and get the furthest left point and the furthest right point
        count = 1
        count_row = 1
        pixels = []
        self.total_points = []
        inp = False
        for row in self.data:
            for pixel in row:
                if pixel == "1":
                    inp = True
                    pixels.append(count)
                count += 1

            # calculate the row
            if inp:
                self.total_points.append((pixels[0], pixels[-1], count_row))  #here we get the "total" of the row
                inp = False

            #update for a new row
            pixels = []
            count_row += 1
            count = 0

        #total_points  contains all the rows with the min and max point

        #here I get all the coordinates of the lines of the tree
        lol = [] #lol is just a random variable :)
        for row in self.total_points:
            lol.append(row[2])

        minimum = lol[0]
        maximun = max(lol)
        difference = maximun - minimum
        self.part = difference / precision # here we get the parts of the tree


        #loop tru the total_points to know exactly wich lines go with each part
        self.levels = []
        lol = []
        for level in range(0, precision):
            for row in self.total_points:
                if row[2] >= minimum + (level * self.part) and row[2] <= minimum + (self.part * (level + 1)):
                    lol.append(row)
            self.levels.append(lol)
            lol = []


        ######################################################################
        #levels contains all the lines for each part
        # total_points  contains all the rows with the min and max point
        #####################################################################


        #here we generelize all the points before calculating the volume in total_points_volume
        self.total_points_volume = []

        for row in self.levels:
            right_points = []
            right_points_total = 0
            left_points = []
            left_points_total = 0
            height = []
            for numbers in row:
                height.append(numbers[2])
                right_points.append(numbers[1])
                right_points_total += numbers[1]
                left_points.append(numbers[0])
                left_points_total += numbers[0]

            right_x_mean = round(right_points_total / len(right_points))
            left_x_mean = round(left_points_total / len(left_points))
            bottom_y_mean = round(min(height))
            top_y_mean = round(max(height))
            self.total_points_volume.append(
                (left_x_mean, right_x_mean, top_y_mean, bottom_y_mean))  # <x, x>, top y, botomm y



        self.data = []  #clear data
        return self.total_points_volume    #return the info of each line





    def fuse(self, point1, points2, scale, scale2, phrase1, phrase2):

        ############################################################################################################################
        #############THIS FUNCTION PUTS TOGETHER ALL THE POINTS OF THE TWO IMAGES AND RETURNS THE TOTAL VOLUME######################
        ############################################################################################################################


        #DISCLAIMER !!!!!!!
        #IF THE IMAGES DON'T PERFECTLY HAVE A IDENTIC HEIGHT
        #THE VOLUME WILL BE WRONG
        #WE ARE TRIYNG TO FIND A WAY ......


        #here is just mathematical algorithms
        length_x1 = []
        length_x2 = []
        lenght_y = self.part
        disk_volume = 0

        for i in point1:
            length_x1.append(i[1]-i[0])

        for i in points2:
            length_x2.append(i[1]-i[0])
        for i in range(0, 10):
            disk_volume += ((pi*length_x1[i]*length_x2[i])/4)*lenght_y


        positions = scale
        positions2 = scale2

        if positions[0][0] > positions[1][0]:
            lenght1_pixels = positions[0][0] - positions[1][0]
        else:
            lenght1_pixels = positions[1][0] - positions[0][0]

        if positions[2][1] > positions[3][1]:
            lenght2_pixels = positions[2][1] - positions[3][1]
        else:
            lenght2_pixels = positions[3][1] - positions[2][1]
########################################################################
        if positions2[0][0] > positions2[1][0]:
            lenght1_pixels2 = positions2[0][0] - positions2[1][0]
        else:
            lenght1_pixels2 = positions2[1][0] - positions2[0][0]

        if positions2[2][1] > positions2[3][1]:
            lenght2_pixels2 = positions2[2][1] - positions2[3][1]
        else:
            lenght2_pixels2 = positions2[3][1] - positions2[2][1]

        lenght_pixel_per_meter = lenght1_pixels/float(phrase1[0])
        height_pixel_per_meter = lenght2_pixels/float(phrase1[1])

        lenght2_pixel_per_meter = lenght1_pixels2 / float(phrase2[0])
        disk_volume = 0
        for i in range(0, 10):
            disk_volume += ((pi*(length_x1[i]/lenght_pixel_per_meter)*(length_x2[i]/lenght2_pixel_per_meter))/4)*(lenght_y/height_pixel_per_meter)

        #return the final volume
        return disk_volume
