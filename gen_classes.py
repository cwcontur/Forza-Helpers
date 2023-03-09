# Height - 42, Width - 18/20
from PIL import Image, ImageColor,ImageDraw, ImageFont
import cv2
# import matplotlib.pyplot as plt

width = 42
height = 20
# X, Y - Offset; X, Y width/height
shape = [(39, 2), (18, 17)] # Inner rectangular white box


b_w, b_h = 4200, 2000
b_shape = [(4110, 80), (1500, 1900)]
# Amsi Pro AKS Condensed Bold

d_class = "#3dbaea"
c_class = "#f6bf31"
b_class = "#ff6533"
a_class = "#fc355a"
s1_class = "#bd5ee4"
s2_class = "#1567d6"

colors = []
colors.extend((d_class, c_class, b_class, a_class, s1_class, s2_class))
print(colors)


badges = ["D-Class", "C-Class", "B-Class", "A-Class", "S1-Class", "S2-Class"]

# myFont = ImageFont.truetype("AmsiProAKSCondensed-Bold.ttf", 165)    
# A_Class = Image.open("Source_Badges/A-Class.png")
# B_Class = Image.open("Source_Badges/B-Class.png")
# C_Class = Image.open("Source_Badges/C-Class.png")
# D_Class = Image.open("Source_Badges/D-Class.png")
# S1_Class = Image.open("Source_Badges/S1-Class.png")
# S2_Class = Image.open("Source_Badges/S2-Class.png")
# width = 420
# height = 200
# letter_x, letter_y = 35, 15

# s_rating_letter_x = 2

# rating_without_1_x, rating_without_1_y = 165, 12
# rating_with_1_x, rating_with_1_y = 183, 12


# letter_x, letter_y = 35, 15
# # A_Re = A_Class.resize((width, height),resample=Image.Resampling.LANCZOS)

# # img = Image.new(mode="RGB", color=(ImageColor.getrgb(colors[3])), size=(b_w, b_h))
# img_re = S2_Class.resize((width, height),resample=Image.Resampling.LANCZOS)
# illest = ImageDraw.Draw(img_re)
# illest.rectangle(b_shape, fill=(ImageColor.getrgb("#ffffff")))

# num_y = 20

# num_x = 167
# num_with1_1X = 180
# num_with2_1X = 190

# letter_y = 20

# single_letterX = 35
# s1_letterX = 15
# s2_letterX = 4


# illest.text((single_letterX, 20), "A", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
# illest.text((190, 20), "811", font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number# pos = 0
# img_re.show()
# pos = 0
# # img_re.show()
# for badge in badges:
#     img = Image.new(mode="RGB", color=(ImageColor.getrgb(colors[pos])), size=(b_w, b_h))
#     illest = ImageDraw.Draw(img)
#     illest.rectangle(b_shape, fill=(ImageColor.getrgb("#ffffff")))
#     save_name = badge + ".png"
#     img.save(save_name)
#     pos += 1
    # img.show()

    # letter_x, letter_y = 35, 15

    # s_rating_letter_x = 2

    # rating_without_1_x, rating_without_1_y = 165, 12
    # rating_with_1_x, rating_with_1_y = 183, 12


    # letter_x, letter_y = 35, 15

    # temp_img = A_Re.copy()
    # texting = ImageDraw.Draw(temp_img)
    # texting.text((13, letter_y), "S1", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
    # texting.text((rating_with_1_x, rating_with_1_y), "998", font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number


    # # bill.text((35, 15), "A", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
    # # bill.text((165, 12), "872", font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number

    # temp_img.show()
def make_badges():
    myFont = ImageFont.truetype("AmsiProAKSCondensed-Bold.ttf", 165)    
    A_Class = Image.open("Source_Badges/A-Class.png")
    B_Class = Image.open("Source_Badges/B-Class.png")
    C_Class = Image.open("Source_Badges/C-Class.png")
    D_Class = Image.open("Source_Badges/D-Class.png")
    S1_Class = Image.open("Source_Badges/S1-Class.png")
    S2_Class = Image.open("Source_Badges/S2-Class.png")
    width = 420
    height = 200

    A_Re = A_Class.resize((width, height),resample=Image.Resampling.LANCZOS)
    B_Re = B_Class.resize((width, height),resample=Image.Resampling.LANCZOS)
    C_Re = C_Class.resize((width, height),resample=Image.Resampling.LANCZOS)
    D_Re = D_Class.resize((width, height),resample=Image.Resampling.LANCZOS)
    S1_Re = S1_Class.resize((width, height),resample=Image.Resampling.LANCZOS)
    S2_Re = S2_Class.resize((width, height),resample=Image.Resampling.LANCZOS)

    num_y = 20

    num_x = 172
    num_with1_1X = 180
    num_with2_1X = 190

    letter_y = 20

    single_letterX = 35
    s1_letterX = 15
    s2_letterX = 4

    try:
        file = open("ratings.txt", "r")
    except:
        print("Failed to load information list!")
        exit(1)



    ratings = []
    pos = 0
    for rate in file:
        # ratings.append(rate)
        temp = int(rate)
        if temp <= 500:
            items = str(temp) 
            ones = 0 
            for num in items:
                if num == "1":
                    ones += 1
                    
            if ones == 1:
                temp_img = D_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "D", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with1_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            elif ones == 2:
                temp_img = D_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "D", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with2_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            else:
                temp_img = D_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "D", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((172, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
        elif (temp <=600) and (temp > 500):   
            items = str(temp) 
            ones = 0 
            for num in items:
                if num == "1":
                    ones += 1
                    
            if ones == 1:
                temp_img = C_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "C", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with1_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            elif ones == 2:
                temp_img = C_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "C", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with2_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            else:
                temp_img = C_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "C", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_x, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)    
        elif (temp <=700) and (temp > 600):   
            items = str(temp) 
            ones = 0 
            for num in items:
                if num == "1":
                    ones += 1
                    
            if ones == 1:
                temp_img = B_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "B", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with1_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            elif ones == 2:
                temp_img = B_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "B", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with2_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            else:
                temp_img = B_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "B", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_x, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
        elif (temp <=800) and (temp > 700): 
            items = str(temp) 
            ones = 0 
            for num in items:
                if num == "1":
                    ones += 1
                    
            if ones == 1:
                temp_img = A_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "A", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with1_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            elif ones == 2:
                temp_img = A_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "A", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with2_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            else:
                temp_img = A_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((single_letterX, letter_y), "A", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_x, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            items = str(temp)  
        elif (temp <=900) and (temp > 800):   
            items = str(temp) 
            ones = 0 
            for num in items:
                if num == "1":
                    ones += 1
                    
            if ones == 1:
                temp_img = S1_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((s1_letterX, letter_y), "S1", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with1_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            elif ones == 2:
                temp_img = S1_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((s1_letterX, letter_y), "S1", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with2_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            else:
                temp_img = S1_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((s1_letterX, letter_y), "S1", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_x, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
        elif (temp <=998) and (temp > 900):   
            items = str(temp) 
            ones = 0 
            for num in items:
                if num == "1":
                    ones += 1
                    
            if ones == 1:
                temp_img = S2_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((s2_letterX, letter_y), "S2", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with1_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            elif ones == 2:
                temp_img = S2_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((s2_letterX, letter_y), "S2", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((num_with2_1X, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            else:
                temp_img = S2_Re.copy()
                texting = ImageDraw.Draw(temp_img)
                texting.text((s2_letterX, letter_y), "S2", font=myFont, fill=(ImageColor.getrgb("#ffffff"))) # Class Letter
                texting.text((175, num_y), items, font=myFont, fill=(ImageColor.getrgb("#000000"))) # Rating number
                save_file = "Car_Class_Badges/" + str(pos) + ".png"
                temp_img.save(save_file)
            
        pos += 1




make_badges()
    
