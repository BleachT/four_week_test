def trapezoid_area(base_up,base_down,height):
    print ( (base_down + base_up) * height * 0.5)

trapezoid_area(1,2,3)
# 参数1,2,3 分别对应base_up, base_down, height,
# positional argument 位置参数

trapezoid_area(base_down=2,height=3,base_up=1)
# keyword argument 关键词参数，顺序不影响

# trapezoid_area(height=3,base_down=,2,1)
#Wrong

trapezoid_area(base_up=3,base_down=2,height=1)

def flshlight(battery1,battery2):
    return "Light !"
nanfu1 = 600
nanfu2 = 700
print(flshlight(nanfu1,nanfu2))

print("   *","  *","***", "  |   ")
print("   *","  ***","*******", "   |   ",sep="\n")

def trapezoid_area(base_up,base_down,height=3):
    print ( (base_down + base_up) * height * 0.5)
# 默认参数高设置成3

trapezoid_area(1,2)
trapezoid_area(1,2,height=6)