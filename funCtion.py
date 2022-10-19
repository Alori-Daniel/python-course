#funtion with postional arguments
#def wise(weight, height):
 #   bmi = (height ** 2)/weight
  #  #print(bmi)
   # return bmi


#w= int(input())
#h= int(input())
#wise(w,h)

#my_bmi = wise(w, h)
#print(my_bmi)






#funtion with keyword arguments
def BMI(weight=73, height=15):
    return(height ** 2)/weight

var2 = BMI(60,17)
print(var2)

#funtion with variable length arguments