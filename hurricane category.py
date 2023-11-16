windfall = input("What are the mph?\n") 
mph = int(windfall)

if 74 <= mph <= 95:
    print("Category 1 which can be as high as 4-5 feet with minimal damage at landfall")
elif 96 <= mph <= 110:
    print("Category 2 which can be as high as 6-8 feet with moderate damage at landfall")
elif 111 <= mph <= 130:
    print("Category 3 which can be as high as 9-12 feet with extensive damage at landfall")
elif 131 <= mph <= 155:
    print("Category 4 which can be as high as 13-18 feet with extreme damage at landfall")
elif mph >= 155:
    print("Category 5 which can be as high as 19+ feet with catastrophic damage at landfall")