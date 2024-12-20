def convert_cel_to_far(C: float):
    F = C*1.8+32
    return F

def convert_far_to_cel(F: float):
    C = (F-32)*5/9
    return C



print(convert_cel_to_far(15))
print(convert_far_to_cel(59))
    
    