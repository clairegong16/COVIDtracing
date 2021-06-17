#the input lists for example [a,b,c] means that a has been in contact with b and c. it does not mean that b an c have been in contact with each other. 
#making the dictionary which should have have the indexes for each person on the spreadchart 

##################INPUT THE LISTS OF PEOPLE CONTACT #################################
somelist = [['James', 'Robert', 'Patricia', 'Mary', 'David', 'Sarah', 'Karen', 'Charles', 'Matthew'], #15 total people
            ['David', 'Sarah', 'Lisa', 'Matthew'], 
            ['Lisa', 'Betty', 'Daniel' ], 
            ['Christopher', 'Anthony'], 
            ['Betty',  'William', 'Sarah']]    


def makedictionary(alllists): #all of the lists in a 2D array 
    thedictionindex = 0 
    thediction = {}
    for alist in alllists: 
        for val in alist: 
            yep = False #checks to see if the person is already accounted for in thediction
            for key in thediction: 
                if val == key: 
                    yep = True
            if yep == False: #if there isn't a key, it adds the person to the thediction with its corresponding index as value. 
                thediction[val] = thedictionindex
                thedictionindex = thedictionindex + 1
    return thediction

#MAKE SURE TO STORE THEDICTION INTO A GLOBAL VARIABLE 






thediction = makedictionary(somelist)
print("thediction = ", thediction)






#using the lists to create a 2d array of the contacted people. if it is 1, the two people have been in contact with each other. if 0, they haven't 
rows, cols = (len(thediction), len(thediction))

spreadchart = [[ 0 for i in range(rows)] for j in range(cols)]
print("spreadchart = ", spreadchart)

def thespreadchart(alllists, spreadchart):
    i = 0 #index for rows 
    for row in alllists: #row is list. [a,b,c,d]
        j = 0 #index for cols 
        for col in row: #col is string, person 'a' or 'b', etc. 
            if j == 0: 
                first = col #this is a person not the index, for instance in [a,b,c,d] it is a. only the first person in each list can be first 
            if first != col: 
                index1 = thediction[first] 
                index2 = thediction[col] 
                spreadchart[index1][index2] = 1
                #spreadchart[index2][index1] = 1
            j = j + 1 
        i = i + 1
    return spreadchart 

spreadchart = thespreadchart(somelist, spreadchart)
print(spreadchart)
#using the 2D array (spreadchart) to make the final list of all of the patients that the given patient has contacted

def findcontacted(patient, spreadchart): 
    thedictionval = list(thediction.values())
    thedictionkey = list(thediction.keys())
    #get all of the first contacts
    i = 0 
    #need to see if the patient equals at least one of the first values a list 
    heh = False
    for a in range(len(somelist)): #index goes through each row 
        if patient == somelist[a][0]:
            heh = True
    if heh == True: 
        for contacttracker in spreadchart[thediction[patient]]: #found the row, with the given patient. Now it needs to go through the col of the row to add the contacts. 
            #to check if they have been in contacted, needs to equal 0 
            position = thedictionval.index(i)
            person = thedictionkey[position]
            if contacttracker == 1:
                #check to see if it is already in the finallist 
                yep = person in finallist 
                if yep == False:
                    finallist.append(person)
            i = i + 1
        



#printing and getting the finallist 
def thefinallist(patient, spreadchart):
    for theperson in finallist: 
            findcontacted(theperson,spreadchart)
    print("the target patient is ", patient, " and here are the list of the contacted: ", finallist)
        

###########################INPUT THE SPECIFIC PATIENT##########################
#in this case I used a for loop to have all of the people in the list be the targeted patient. 
thedictionkey = list(thediction.keys())
for patient in thedictionkey:
    finallist = [patient]
    thefinallist(patient, spreadchart)
