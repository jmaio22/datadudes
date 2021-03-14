import csv

with open('C:\\Users\\DasGautam(SchoolSA)\\Documents\\data.csv') as f:
    reader = csv.reader(f)
    next(reader)
    year = 1970
    csv_columns = ["Country", "year", "Power Industry", "Buildings", "Transport", "Other industrial combustion", "Other sectors" , "Total"]
    countries = []
    years = []
    ROWS = []
    for row in reader:
        ROWS.append(row)
        if row[1] not in countries:
            countries.append(row[1])
        if row[3] not in years:
            years.append(row[3])
    

    def Sort(sub_li): 

        sub_li.sort(key = lambda x: x[2]) 
        return sub_li 

    
    with open("C:\\Users\\DasGautam(SchoolSA)\\Documents\\datasolved.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        
    for country in countries:
        l = []
        L = []
        for R in ROWS:
            if R[1] == country:
                l.append(R)
    
        chunks = [l[x:x+5] for x in range(0, len(l), 5)]
        
        D = {}
        LIST =[]
        
        for y in range(len(years)):
            
            for s in range(5):
                T=0    
                D["Country"] = country
                D["year"] = 1970 +y
                try:
                    D[chunks[y][s][2]] = chunks[y][s][4]
                except:
                    pass
                try:
                    T = T+ float(chunks[y][s][4])
                except:
                    pass
            D["Total"] = T
            
            LIST.append(D)

            with open("C:\\Users\\DasGautam(SchoolSA)\\Documents\\datasolved.csv", "a") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
                
                writer.writerow(D)
            

        


