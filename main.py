import os

# path of image folder
path = r'.\pic'

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


if __name__ == '__main__':
    s = []
    # defining prefix
    prefix = input("Enter Prefix: ")
    for file in os.listdir():
        suffix = file.split('.')[1]
        s.append(suffix)
        middle_counter = counter_create(counter)
        new_name = prefix + "{}".format(middle_counter) + "." + suffix
        os.rename(file, new_name)
        counter = counter + 1
    print("File extensions are :")
    print(s)
    print("#############################################################")
    print("Total file renamed --->" + str(counter))
    print("#############################################################")
