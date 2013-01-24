import time, PE6

f = open('pe_main_results.txt', 'a')

#currently the PE_solutions.txt file has solutions for problems 1-20 in order
solutions = open('PE_solutions.txt','r')
solution_list =[]

while True:
    line = solutions.readline()
    if len(line)==0:
        break
    else:
        solution_list.append(int(line))

s = time.time()

correct_results = 0
total_results = 0
incorrect_results = []

run_time = []

exercises = [6]

for ii in exercises:
    #getattr() call is used to programatically call the main() method for each
    #PEX.py where X is both imported and in the exercises array
    #
    #one improvement would be to automatically generate the exercises array
    #this could probably be done using the globals() function
    if getattr(globals()['PE'+str(ii)],'main')() == solution_list[ii-1]:
        f.write('PE6: Success!\n')
        run_time.append(time.time()-s)
        f.write('Time: ' + str(run_time[-1])+'\n')
        f.write('\n')
        f.write('Test'+'\n')
        correct_results+=1
        total_results+=1
    else:
        total_results+=1
        incorrect_results.append(6)



print 'Execution complete!'
f.write('Execution complete:'+'\n')
f.write('Exercises attempted: '+str(total_results)+'\n')
f.write('Exercises correct: '+str(correct_results)+'\n')
f.write('\n')
f.write('Percent complete: '+str(100.0*correct_results/total_results)+'%'+'\n')

if len(incorrect_results)>0:
    f.write('Incorrect exercies:'+'\n')
    f.write(str(incorrect_results))

f.close()

