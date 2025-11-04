colors=input("Enter color name separated by comas:")
color_list=colors.split(",")
color_list=[color.strip() for color in color_list]
print("first color:",color_list[0])
print("first color:",color_list[-1])
