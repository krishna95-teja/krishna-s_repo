def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if((food_type=="N" or food_type=="V")and quantity_ordered>=1 and distance_in_kms>0):
        if(food_type=="V"):
            if(distance_in_kms<=3):
                bill_amount=120*quantity_ordered+0
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=120*quantity_ordered+((distance_in_kms-3)*3)
            else:
                bill_amount=120*quantity_ordered+((distance_in_kms-6)*6)+9                          #why add 9 at the end?
        else:
            if(distance_in_kms<=3):
                bill_amount=150*quantity_ordered+0
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=150*quantity_ordered+((distance_in_kms-3)*3)
            else:
                bill_amount=150*quantity_ordered+((distance_in_kms-6)*6)+9                           #why add 9 at the end?
    else:
        bill_amount=(-1)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,3)
print(bill_amount)
