import datetime 

file = open(r'C:\Users\manai\Desktop\TIG\portf\Portfolio\wout\Py-TaskScheduler\task.txt','a')

file.write(f'{datetime.datetime.now()} - The script ran \n')