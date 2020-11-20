import os

# path of image folder
path = '.\\pic'
# name of 1st img with extension
first_image_name = "Img 00001.jpg"  # change the value as your name
# defining path for checking file extension
path_img = ".\\pic\\" + first_image_name
# read path of images
os.chdir(path)
# defining counter
counter = 1


# creating sequence number
def counter_create(num: int):
    if 10 > num >= 1:
        ctr = "00000" + str(num)
    elif 100 > num >= 10:
        ctr = "0000" + str(num)
    elif 1000 > num >= 100:
        ctr = "000" + str(num)
    elif 10000 > num >= 1000:
        ctr = "00" + str(num)
    else:
        ctr = str(num)
    return ctr

# defining file extension
def file_ext():
    filename, file_extension = os.path.splitext(path_img)
    return file_extension


# defining prefix
prefix = "DSC" + " "

if __name__ == '__main__':
    for file in os.listdir():
        suffix = file_ext()
        middle_counter = counter_create(counter)
        new_name = prefix + "{}".format(middle_counter) + suffix
        os.rename(file, new_name)
        counter = counter + 1

    print("#############################################################")
    print("Total file renamed --->" + str(counter))
    print("#############################################################")
