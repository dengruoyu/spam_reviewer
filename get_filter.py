import csv
from datetime import date

csvfile1 = file('labeled.csv', 'r+')
reader1 = csv.reader(csvfile1)

shops = {}
user_label = {} 
'''
user =  {}
for line in reader1:
    if (line[1] == '[ 0.]'):
        if(user.has_key(line[0])):
            user[line[0]].append(line[3])
        else:
            user[line[3]] = 1

print len(user)
review = 0
for i in user:
    review += user[i]
print review
'''
for line in reader1:
    if (line[1] == '[ 0.]'):
        user_label[line[0]] = 0
    if (line[1] == '[ 1.]'):
        user_label[line[0]] = 1
    if(shops.has_key(line[3])):
        shops[line[3]].append([line[0],line[2]])
    else:
        shops[line[3]] = [[line[0],line[2]]]
#print len(shops)
del_shops = []
for i in shops:
    if(len(shops[i]) <= 2):
        del_shops.append(i)

for i in del_shops:
    del shops[i]

#print len(shops)

users = {}
def delta_time(a,b):
    year_a = int(a[0:4])
    month_a = int(a[4:6])
    day_a = int(a[6:8])
    year_b = int(b[0:4])
    month_b = int(b[4:6])
    day_b = int(b[6:8])
    datea = date(year_a,month_a,day_a)
    dateb = date(year_b,month_b,day_b)
    return abs((datea-dateb).days)

time_inter = 5
common = 2
for i in shops:
    #print i
    tmp = shops[i]
    for j in range(len(tmp)-1):
        for k in range(j+1,len(tmp)):
            key_name1 = tmp[j][0] +" "+ tmp[k][0]
            key_name2 = tmp[k][0] +" "+ tmp[j][0]
            if (delta_time(tmp[k][1],tmp[j][1]) < time_inter):
                if(users.has_key(key_name1)):
                    users[key_name1] += 1
                else:
                    if(users.has_key(key_name2)):
                        users[key_name2] += 1
                    else:
                        users[key_name1] = 1


for i in user_label:
    tt = i.split(" ")
    pattern = 0
    print i,",",user_label[i]
    if(user_label[i] == 0):
        if(users[i] >= common):
            if (user_label[tt[0]] == 0 and user_label[tt[1]] == 0):
                print tt[0],",",tt[1],",",users[i],",",0,",",0,",",1
            
            if (user_label[tt[0]] == 0 and user_label[tt[1]] == 1):
                print tt[0],",",tt[1],",",users[i],",",0,",",1,",",2
            if (user_label[tt[0]] == 1 and user_label[tt[1]] == 0):
                print tt[0],",",tt[1],",",users[i],",",1,",",0,",",3
            
            if (user_label[tt[0]] == 1 and user_label[tt[1]] == 1):
                print tt[0],",",tt[1],",",users[i],",",1,",",1
        





