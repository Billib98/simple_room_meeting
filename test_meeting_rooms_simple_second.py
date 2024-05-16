#L'idea qui è simile al primo caso ma "salvando" in una lista solo le informazioni "utili"
#Il costo da pagare è avere molti più loop, quindi più tempo di esecuzione su grandi scale
def findrooms(prenotation_vector):
    num_of_rooms = 0
    num_of_prenotation = len(prenotation_vector)
    temp_list_times = []
    print(f"Num of prenotation is : {num_of_prenotation}") #Debug
    min_slot = 0
    max_slot = 0
    for i_prenotation in range(num_of_prenotation):
        i_prenotation_vector = prenotation_vector[i_prenotation]
        start_i = i_prenotation_vector[0]
        end_i = i_prenotation_vector[1]+1
        if min_slot > start_i:
            min_slot = start_i
        if max_slot < end_i:
            max_slot = end_i

        print(f"Prenotation {i_prenotation+1} is : {i_prenotation_vector}") #Debug
    
    slot_list = list(range(min_slot,max_slot)) 
    for i_val in range(min_slot,max_slot):
        temp_list_times.append([i_val,0]) 
    
    #print(f"Total slot needed are {temp_list_times}") #Debug
    print(f"Total slot range is {slot_list}") #Debug
    
    for i_prenotation in range(num_of_prenotation):
         i_prenotation_vector = prenotation_vector[i_prenotation]
         start_i = i_prenotation_vector[0]
         end_i = i_prenotation_vector[1]+1
         for i_slot in range(start_i,end_i):
             #print(i_slot)
             prenotation_on_i_slot = temp_list_times[i_slot][1]
             temp_list_times[i_slot][1] = temp_list_times[i_slot][1] + 1
             #print(f"prenotation on {i_slot} is {prenotation_on_i_slot}") #Debug
             
             
    print(f"Total slot needed are {temp_list_times}") #Debug
    
    room_count = 0
    for i_check in range(len(slot_list)):
        if temp_list_times[i_check][1] > room_count:
            room_count = temp_list_times[i_check][1]

    print(f"Total rooms needed are {room_count}") #Debug
    
    num_of_rooms = room_count
    
    return num_of_rooms
    

#Assert check for my functions 
assert findrooms([[0, 30],[5, 10],[15, 20]]) == 2
assert findrooms([[0, 30], [5, 10], [6, 20]]) == 3

#findrooms([[0, 30],[5, 10],[15, 20]])
