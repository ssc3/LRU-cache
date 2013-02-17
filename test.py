#!/bin/python

BOUND = 4
KEY = 1
VALUE = 'a'
cache = []  # this is same as cache_list = dict()
cache_age = []
new_key = -1

NUM_CACHE_TRANS = 0

#Defining a set-associative cache

def initialize_cache():
   for index in range(0, BOUND):
       cache.append([])
       cache_age.append([])
       for jindex in range(0, 4):
           cache[index].insert(jindex,-1) 
           cache_age[index].insert(jindex, 0)

def update_ages(index, current_way):
    print "Updating ages\n"
    if (cache_age[index].count(4) != 0):
        for jindex in range(0, 4):
             if (jindex != current_way):
                 cache_age[index][jindex] += 1 
        


def cache_write(key, value):
    # Simple hash to allow any int to be a key beyond the limited value of BOUND
    new_key = ord(key) % BOUND 
    print ("Inserting Key = " + str(key) + " value = " + str(value))
    
    insert_status = False
    for i in range(0, 4):
        if (cache[new_key][i] == -1):
            cache[new_key][i] = value
            break

    update_ages(new_key, i)
   # cache_age[new_key] += 1
    print ("Cache key = " + str(new_key) + " value = " + str(cache[new_key]))

def cache_read(key, update):
   new_key = ord(key) % BOUND
   print (str(cache[new_key]))
   if (update == True):
    #   cache_age[new_key] +=1
       print "Hello\n"    
 

def print_full_cache():
   for index in range(0, BOUND):
       print("Index = " + str(index) + " Value = " + str(cache[index]) + " Age = " + str(cache_age[index]))     



initialize_cache()

opcode = -1
opcode_set = False
key_set = False

input_file = open("input00.txt", "r")
for line in input_file.readlines():
   for word in line.split():
       NUM_CACHE_TRANS+=1 
       print (word + " ")
       
       if (word == "BOUND"):
           print "Setting BOUND"	
           opcode = 0x01
           opcode_set = True
           continue

       elif (word == "SET"):
           print "Setting SET"
           opcode = 0x02
           opcode_set = True
           continue
   
       elif (word == "GET"):
           print "GET"
           opcode = 0x03
           opcode_set = True
           continue

       elif (word == "PEEK"):
           print "PEEK"
           opcode = 0x04
           opcode_set = True
           continue

       elif (word == "DUMP"):
           print "DUMP"
           opcode = 0x05
           opcode_set = True



       if (opcode_set == True):
           if (opcode == -1):
               print "Invalid op\n" 

           if (opcode == 0x01):
               print ("In bound\n") 
               BOUND = int(word)
               opcode_set = False

           if (opcode == 0x02):
               print ("In SET\n") 
               if(key_set == False):
                   if(word.isdigit() == False):
                       KEY = word
                       key_set = True       
                   else:
                       print ("ERROR: Expected alpha-numeric value for key\n")              
               else: 
                   if (word.isdigit()):
                       VALUE = int(word)
                       cache_write(KEY, VALUE) 
                       opcode_set = False
                       opcode = -1  
                       key_set = False
                   else:
                       print ("ERROR: Expected numeric value for key\n") 

           if (opcode == 0x03):
               print ("In GET\n") 
               if(word.isdigit() == False):
                   KEY = word
                   cache_read(KEY, True)
                   opcode_set = False
                   opcode = -1
               else:
                   print ("ERROR: Expected alpha-numeric value for key\n")

           if (opcode == 0x04):
               print ("In PEEK\n") 
               if(word.isdigit() == False):
                   KEY = word
                   cache_read(KEY, False)
                   opcode_set = False
                   opcode = -1
               else:
                   print ("ERROR: Expected alpha-numeric value for key\n")


           if (opcode == 0x05):
               print ("In DUMP\n") 
               print_full_cache()





