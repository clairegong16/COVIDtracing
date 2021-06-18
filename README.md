# COVIDtracing
This project focuses on given a list of lists and a target person, return a list of people who were in contact with the target person from the lists. For instance, the list:somelist = [['James', 'Robert', 'Patricia', 'Mary', 'David', 'Sarah', 'Karen', 'Charles', 'Matthew'], #15 total people
            ['David', 'Sarah', 'Lisa', 'Matthew'], 
            ['Lisa', 'Betty', 'Daniel' ], 
            ['Christopher', 'Anthony'], 
            ['Betty',  'William', 'Sarah']]    
The first person in the list contacts all of the people in the following list. For instance Betty was in contact William and Sarah. It doesn't mean that WIlliam and Sarah were in contact with each other. 
I included two approaches in this code. 
1. Iterative, use a 2D array to mark who has been in contact with each other. 1 means they have, 0 means they haven't. Then, use a second method to go through the 2D array with a given patient to create the list. 
2. Recursive, go through the list of lists with a recursive method. 

Here are the results of this input (they alternate iterative first, then recursive).
the target the_patient is  James  and here are the list of the contacted:  ['James', 'Robert', 'Patricia', 'Mary', 'David', 'Sarah', 'Karen', 'Charles', 'Matthew', 'Lisa', 'Betty', 'Daniel', 'William']
recursive:  ['James', 'Robert', 'Patricia', 'Mary', 'David', 'Sarah', 'Karen', 'Charles', 'Matthew', 'Lisa', 'Betty', 'Daniel', 'William']
the target the_patient is  Robert  and here are the list of the contacted:  ['Robert']
recursive:  ['Robert']
the target the_patient is  Patricia  and here are the list of the contacted:  ['Patricia']
recursive:  ['Patricia']
the target the_patient is  Mary  and here are the list of the contacted:  ['Mary']
recursive:  ['Mary']
the target the_patient is  David  and here are the list of the contacted:  ['David', 'Sarah', 'Matthew', 'Lisa', 'Betty', 'Daniel', 'William']
recursive:  ['David', 'Sarah', 'Matthew', 'Lisa', 'Betty', 'Daniel', 'William']
the target the_patient is  Sarah  and here are the list of the contacted:  ['Sarah']
recursive:  ['Sarah']
the target the_patient is  Karen  and here are the list of the contacted:  ['Karen']
recursive:  ['Karen']
the target the_patient is  Charles  and here are the list of the contacted:  ['Charles']
recursive:  ['Charles']
the target the_patient is  Matthew  and here are the list of the contacted:  ['Matthew']
recursive:  ['Matthew']
the target the_patient is  Lisa  and here are the list of the contacted:  ['Lisa', 'Betty', 'Daniel', 'Sarah', 'William']
recursive:  ['Lisa', 'Betty', 'Daniel', 'Sarah', 'William']
the target the_patient is  Betty  and here are the list of the contacted:  ['Betty', 'Sarah', 'William']
recursive:  ['Betty', 'Sarah', 'William']
the target the_patient is  Daniel  and here are the list of the contacted:  ['Daniel']
recursive:  ['Daniel']
the target the_patient is  Christopher  and here are the list of the contacted:  ['Christopher', 'Anthony']
recursive:  ['Christopher', 'Anthony']
the target the_patient is  Anthony  and here are the list of the contacted:  ['Anthony']
recursive:  ['Anthony']
the target the_patient is  William  and here are the list of the contacted:  ['William']
recursive:  ['William']
