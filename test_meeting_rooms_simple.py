#L'idea qui è di salvare tutti i valori prenotati in una lista e poi, per ogni elemento nel 
#range tra il numero più piccolo e più grande, contare quante volte si osserva quel numero.
def findrooms(prenotation_vector):
    num_of_rooms = 0
    num_of_prenotation = len(prenotation_vector)
    print(f"Num of prenotation is : {num_of_prenotation}") #Debug
    temp_list_times = []
    for i_prenotation in range(num_of_prenotation):
        i_prenotation_vector = prenotation_vector[i_prenotation]
        start_i = i_prenotation_vector[0]
        end_i = i_prenotation_vector[1]+1
        to_add = list(range(start_i,end_i))
        print(f"Prenotation {i_prenotation+1} is : {i_prenotation_vector}") #Debug
        #print(f"To add is : {to_add}") #Debug
        temp_list_times = temp_list_times + to_add
        
        
    print(f"Total slot prenoted are {temp_list_times}") #Debug
    max_count = 0
    for i_check in range(min(temp_list_times),max(temp_list_times)+1):
        #print(i_check) #Debug
        max_i = temp_list_times.count(i_check)
        if max_i>max_count:
            max_count = max_i
            
    print(f"Number of needed rooms is {max_count}")
    
    num_of_rooms = max_count
    
    return num_of_rooms
    

#Assert check for my functions 
assert findrooms([[0, 30],[5, 10],[15, 20]]) == 2
assert findrooms([[0, 30], [5, 10], [6, 20]]) == 3

#findrooms([[0, 30],[5, 10],[15, 20]])
