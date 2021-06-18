#contact list code in python
# 
# #the input lists for example [a,b,c] means that a has been in contact with b and c. it does not mean that b an c have been in contact with each other. 
#making the dictionary which should have have the indexes for each person on the spreadchart 

##################INPUT THE LISTS OF PEOPLE CONTACT ################################# this must be a 2D array 
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
#using the 2D array (spreadchart) to make the final list of all of the patients that the given the_patient has contacted

def findcontacted(the_patient, spreadchart): 
    thedictionval = list(thediction.values())
    thedictionkey = list(thediction.keys())
    #get all of the first contacts
    i = 0 
    #need to see if the the_patient equals at least one of the first values a list 
    heh = False
    for a in range(len(somelist)): #index goes through each row 
        if the_patient == somelist[a][0]:
            heh = True
    if heh == True: 
        for contacttracker in spreadchart[thediction[the_patient]]: #found the row, with the given the_patient. Now it needs to go through the col of the row to add the contacts. 
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
def thefinallist(the_patient, spreadchart):
    for theperson in finallist: 
            findcontacted(theperson,spreadchart)
    print("the target the_patient is ", the_patient, " and here are the list of the contacted: ", finallist)
        





#####
#
# function returns the list of people having contact with the patient, recursively.
# we need to deal with two cases - the special case, and the general case (like for any recursive functions)
#
def findcontact(the_patient, cohort_list, final_list):
    #case 1: if the the_patient does not appear first in one of the lists, then done 
    ishead = False #keeps track of if it is a head or not. if it is true, then it is a head 
    #print("investigate the_patient: ", the_patient)
    for a_cohort in cohort_list: #index goes through each row         
        if the_patient == a_cohort[0]:
            ishead = True 
            break
    if ishead == False:        
        return final_list # 
    #case 2: 
    else: # we've found a cohort with 'the_patient' as head
        for a_contact in a_cohort[1:]: # any person after the head [a, b, c] 
            #print(a_contact, "is a contact of ", the_patient)
            my_list = final_list + [a_contact]
            final_list = findcontact(a_contact, cohort_list, my_list) #  add the contact to final list 
        return final_list

def removeDouble(final_list):
    finalfinallist = []
    for i in final_list:
        if i not in finalfinallist: 
            finalfinallist.append(i)
    return finalfinallist


apatient = 'Lisa' #the specific patient 
# we use a loop to test all the cases we want test:
print("Cohort list = ",somelist)
print("test case:", apatient, " is the patient")
finallist = [apatient]
print ("these people have had contact with ", apatient, removeDouble(findcontact(apatient, somelist, finallist)))
print("====")




###########################INPUT THE SPECIFIC PATIENT##########################
#in this case I used a for loop to have all of the people in the list be the targeted the_patient. 
thedictionkey = list(thediction.keys())
for the_patient in thedictionkey:
    finallist = [the_patient]
    thefinallist(the_patient, spreadchart)   #iteritative with a 2D array to represent the contact relationship 
    print("recursive: ", removeDouble(findcontact(the_patient, somelist, finallist)))  #recursive, directly works off of the contact list.

#thank you for reading my code 

