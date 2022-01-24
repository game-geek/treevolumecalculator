from math import pi

class Volume:

    def __init__(self, program):
        self.program = program




    def Leaf_volume(self, precision):
        self.height = self.program.draw_line.txt_gestion.max_height - self.program.draw_line.txt_gestion.min_height
        self.part = int(self.height/precision)
        #print(self.program.draw_line.txt_gestion.min_height, self.program.draw_line.txt_gestion.max_height)
        #(self.part)
        #get all the coordinates of the points between each part

        #get the points

        f = open("data/pixels.txt", "r")
        data = f.read()
        f.close()
        data = data.split("\n")
        self.data = []
        for row in data:
            self.data.append(list(row))


        #select the points

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
            #calculate the row
            if inp:
                self.total_points.append((pixels[0], pixels[-1], count_row))
                inp = False

            pixels = []
            count_row += 1
            count = 0

        #print(self.total_points)
        #print(len(self.total_points))

        lol = []
        for row in self.total_points:
            lol.append(row[2])

        lol.sort()
        minimum = lol[0]
        maximun = max(lol)
        difference = maximun-minimum
        self.part = difference / precision
        #print(f"part :::::{self.part}")

        self.levels = []
        lol = []
        for level in range(0, precision):
            for row in self.total_points:
                if row[2] >= minimum + (level*self.part) and row[2] <= minimum + (self.part*(level+1)):
                    lol.append(row)
            self.levels.append(lol)
            lol = []

        #print("\n\n\n")
        #for row in self.levels:
            #print(row)


        ############################################
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
            self.total_points_volume.append((left_x_mean, right_x_mean, top_y_mean, bottom_y_mean)) # <x, x>, top y, botomm y

        #print(self.total_points_volume)
        
        self.data = []

    def Precise_volume(self):
        #lenght1 = lenght
        #lenght2 = hight
        #convert the inputs in reasonable ones:
        positions = self.program.homepage.position_list

        if positions[0][0] > positions[1][0]:
            lenght1_pixels = positions[0][0] - positions[1][0]
        else:
            lenght1_pixels = positions[1][0] - positions[0][0]

        if positions[2][1] > positions[3][1]:
            lenght2_pixels = positions[2][1] - positions[3][1]
        else:
            lenght2_pixels = positions[3][1] - positions[2][1]


        #print(f"lenght1 pixels : {lenght1_pixels}      lenght2 pixels : {lenght2_pixels}")
        lenght1_meters = float(self.program.homepage.phrase1)
        lenght2_meters = float(self.program.homepage.phrase2)
    #  print(f"lenght1 meters : {lenght1_meters}      lenght2 meters : {lenght2_meters}")

        #convert 1 meters to a number of pixels
        lenght1_per_meter = lenght1_pixels/lenght1_meters
        lenght2_per_meter = lenght2_pixels/lenght2_meters

     #   print(f"lenght1 per meter : {lenght1_per_meter}      lenght2 per meters : {lenght2_per_meter}")
#




        height = self.height/ len(self.total_points_volume)
      #  print(f"height :::::: {self.height}")
        self.Pvolume = []

        for i in self.total_points_volume:
            #get the min and max in pixels
            min_x = i[0]
            max_x = i[1]
            #convert the min and max in meters
            if lenght1_per_meter == 0:
                lenght1_per_meter = 1
            min_x_meter = min_x/lenght1_per_meter
            max_x_meter = max_x/lenght1_per_meter
            #calculate the rayon
            #print(min_x, max_x)
            #print(min_x_meter, max_x_meter)
            rayon = (max_x_meter-min_x_meter)/2
            #convert the height in meters
            height_meter = self.part/lenght2_per_meter
            #print(f"rayon : {rayon}  hight : {height_meter}")
            self.Pvolume.append(pi*(rayon**2)*height_meter)
        self.Ptotal_volume = 0

        for i in self.Pvolume:
            self.Ptotal_volume += i

        self.Ptotal_volume_round = round(self.Ptotal_volume)


















