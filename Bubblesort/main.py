def bubbleSort(sorted_list):
    for passnum in range(len(sorted_list)-1,0,-1):
        for i in range(passnum):
            if sorted_list[i]>sorted_list[i+1]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i+1]
                sorted_list[i+1] = temp

numeric_list = [14,46,57,21,70,2,101,55,27,223]
sorted_numeric_list = [2,14,21,27,46,55,57,70,101,223]
reversed_numeric_list = [223,101,70,57,55,46,27,21,14,2]
string_list = ['Głowa Kasandry','Metro 2033','451° Fahrenheita','Ojciec chrzestny','Zew Cthulhu','Buszujący w zbożu','Hobbit','Solaris','Sokół maltański','Ja, robot']
sorted_string_list = ['451° Fahrenheita','Buszujący w zbożu','Głowa Kasandry','Hobbit','Ja, robot','Metro 2033','Ojciec chrzestny','Sokół maltański','Solaris','Zew Cthulhu']
reversed_string_list = ['Zew Cthulhu','Solaris','Sokół maltański','Ojciec chrzestny','Metro 2033','Ja, robot','Hobbit','Głowa Kasandry','Buszujący w zbożu','451° Fahrenheita']
print("Lista nieposortowana: ", string_list)
bubbleSort(string_list)
print("Lista posortowana: ", string_list)
