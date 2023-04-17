



def leap_year(l):

    l1 = []
    l2 = []

    # Write your logic here
    for i in l:
        if i%400 == 0:
            l1.append(i)
            return l1
        elif i%100 == 0:
            l2.append(i)
            return l2
        elif i%4 == 0:
            l1.append(i)
            return l1
    
    
    return {'leap': l1, 'not leap': l2}


years = [1800, 1900, 2100, 2400, 2500]
leap_year(years)

print(leap_year(years))