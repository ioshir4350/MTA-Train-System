#Isfar Oshir
#Lecture: XLC1
#iao233
#In accordance with the code of conduct, I have not plagiarized any portion of this assignment

def create_file_into_list(file_name, lst):  #puts given MTA data into a list
    trainfile = open(file_name, "r")
    for line in trainfile:
        lst1 = line.split(",")
        lst1[-1] = lst1[-1].strip("\n")
        lst.append(lst1)
    lst.pop(0)
    return lst

def create_dict_of_trains_and_stations(lst):    #creates a dictionary with the train lines as keys
    train_dict = {"A": [],"C": [],"E": [],"B": [],"D": [],"F": [],"M": [],
                  "G": [],"L": [],"J": [],"Z": [],"N": [],"Q": [],"R": [],
                  "W": [],"1": [],"2": [],"3": [],"4": [],"5": [],"6": [],
                  "7": [],"S": [],}
    for element in lst:
        stop_id = element[0]
        if element[2] not in train_dict[stop_id[0]]:
            train_dict[stop_id[0]].append(element[2])
    return train_dict

def create_dict_of_stations_and_trains(lst):
    station_dict = {}
    for element in lst:
        stop_name = element[2]
        if stop_name not in station_dict:
            station_dict[stop_name] = []
    for element in lst:
        stop_name1 = element[2]
        stop_id = element[0]
        train_line = stop_id[0]
        if train_line not in station_dict[stop_name1]:
            station_dict[stop_name1].append(train_line)
    return station_dict

def train_input(train_dict):    #deals with the user interface
    string = input("Please enter a train line, or 'done' to stop: ")
    while string != "done":
        station_string = ','.join(train_dict[string])
        print(string, "line:", station_string)
        print()
        string = input("Please enter a train line, or 'done' to stop: ")

def destination(current, final, lst):   #only one transfer is available right now
    station_dict = create_dict_of_stations_and_trains(lst)
    trains_available = station_dict[current]
    ultimate_train = station_dict[final]
    for train in trains_available:
        if train in ultimate_train:
            return train
        else:
            for station in station_dict:
                for train_line in trains_available:
                    for ultimate_line in ultimate_train:
                        if train_line in station_dict[station] and ultimate_line in station_dict[station]:
                            string = 'Go to '+str(station)+' using the '+str(train_line)+' then transfer to '+str(ultimate_line)+' to go to '+ final
                            return string
            
    
    
def main():
    lst = []
    create_file_into_list("hw9 - mta train stop data.csv", lst)
    train_dict = create_dict_of_trains_and_stations(lst)
   # station_dict = create_dict_of_stations_and_trains(lst)
    print(destination('215 St', 'Old Town', lst))
    train_input(train_dict)

main()
