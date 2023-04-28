#to print python books available in the store
print("Python books available......")
print("1.Introduction to python programming : Rs 499.00")
print("2.Python Libraries Cookbook : Rs.855.00")
print("3.Data science in python : Rs.645.00")
a=int(input("Enter no.of 1st book : "))
b=int(input("Enter no.of 2nd book : "))
c=int(input("Enter no.of 3rd book : "))
total_amount=(a*499.00)+(b*855.00)+(645.00*c)
gst=(12/100)*total_amount
print("GST amount : ",gst)
print("Delivery charges : 250.00")
bill=total_amount+gst+250.00
print("Total bill : ",bill)


#*************************************************************************************************************
#2nd code
a=input("Enter string : ").casefold()
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=[]
c.append(a[0])
for i in a:
    if i not in c:
        if i in b:
            c.append(i)
d=','.join(c)
print(d)

