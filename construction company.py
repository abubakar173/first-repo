l1 = "Welcome to ABC construction company"
l2 = "*****************************************************************"
l3 = "Press A for  3 rooms . 1 kitchen and 2 washroom"
l4 = "Press B for 3 rooms , 1 kichen , 1 washroom and tv launch"
l5 = "Press C 2 rooms , 1 kitchen , tv launch, car parking and washroom"
l6 = "******************************************************************"
print(l1.center(80))
print(l2.center(80))
print(l3.center(80))
print(l4.center(80))
print(l5.center(80))
print(l6.center(80))
opt = input("Please select any of the above option")
opt = opt.upper()
def construction(opt):


    ps=900
    if (opt == 'A'):
        r1=200
        r2=200
        r3=200
        w1=100
        w2=100
        k=100
        ps=k+w1+w1+r1+r2+r3
        print("Option A has been selected for plot size ",ps,'sqmt')
        print("3 Rooms each of 200 sq feet")
        print("2 washroom each of 100 sq feet")
        print("1 Kitchen an area of 100 sq feet")
    elif (opt == 'B'):
        print("Option B has been selected")
        print("3 Rooms each of 150 sq feet")
        print("1 washroom each of 100 sq feet")
        print("1 Kitchen an area of 100 sq feet")
        print("1 TV lounge of 250 sq feet")
    elif (opt == 'C'):
        print("Option C has been selected")
        print("2 Rooms each of 150 sq feet")
        print("1 washroom each of 50 sq feet")
        print("1 Kitchen an area of 50 sq feet")
        print("1 TV lounge of 200 sq feet")
        print("1 Car parking of 300 sq feet")

construction(opt)

