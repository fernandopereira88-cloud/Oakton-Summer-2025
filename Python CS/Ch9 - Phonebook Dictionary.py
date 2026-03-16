#phonebook = {'Chris':'555','Katie':'666','Joanne':'777'}

#for fernando in phonebook:
#    print(fernando)

#Q1
#result = d['answer']
#Q2
#us_cabinet['Justice Department']='Randolph'
#Q3
#iso_3166['Timor-Leste'] = iso_3166['East Timor'] 
#del iso_3166['East Timor']
#Q4
#
#inverted={}

#for index in range(1,n+1):
#    inverted[index]=1/index

#Q5
#dct = {}
#
#tuple_1 = (1,2,3)
#tuple_2 = (4,5,6)

#for index in range(0,len(tuple_1)):
#    dct[tuple_1[index]] = tuple_2[index]

#dct


# digits = {int(s) for s in data if s.isdigit()}

#data.remove(min(data))
#data.remove(max(data))

#try:
#    avg = sum(data)/len(data)

#except:
#    avg = None


###############
#Project 2
###############

#def count_vowels(string):
#    list_string =[]
#    count_a = 0
#    count_e = 0
#    count_i = 0
#    count_o = 0
#    count_u = 0
#    list_string = list(string)

#    for index in range(0,len(list_string)):
#        if list_string[index] == 'a' or  list_string[index] == 'A' :
#            count_a +=1

#        if list_string[index] == 'e' or  list_string[index] == 'E' :
#            count_e +=1

#        if list_string[index] == 'i' or  list_string[index] == 'I' :
#            count_i +=1

#        if list_string[index] == 'o' or  list_string[index] == 'O' :
#            count_o +=1

#        if list_string[index] == 'u' or  list_string[index] == 'U' :
#            count_u +=1

#    vowel_dictionary ={'a':count_a,'e':count_e,'i':count_i,'o':count_o,'u':count_u}

#    return vowel_dictionary



####################################
#Project 1

def common_word_count(string1,string2):
    list_string1 = []
    list_string2 = []
    count_set_string1 = 0
    count_set_string2 = 0
    intersect_dct ={}
    #1 Identify Common Words
     #Split both string arguments into lists of words.

    list_string1 = string1.split()
    list_string2 = string2.split()
    
     #Convert the lists to sets.
    set_string1 = set(list_string1)
    set_string2 = set(list_string2)    

     #Find the intersection of these two sets to identify the common words.
    set_intersection = set_string1.intersection(set_string2)
    
    #2 Count Word Occurrences:
     #Iterate through each string argument, counting the occurrences of each common word.
    for element in set_intersection:
        for index1 in range(0,len(list_string1)):
         if  list_string1[index1] == element:
             count_set_string1 += 1
                         
        for index2 in range(0,len(list_string2)):
         if list_string2[index2] == element:             
             count_set_string2 += 1
             
        count_strings = count_set_string1 + count_set_string2
        
        intersect_dct[element] =count_strings
        count_set_string1 = 0
        count_set_string2 = 0
        count_strings     = 0

    return intersect_dct         


common_word_count(string1 = 'Helo my name is Fernando fox fox bright bright',string2 = 'Another weeked Helo bright fox working on content')





















    




    
