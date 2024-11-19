import datetime 

file = open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\GitPortf\Portfolio\wout\Py-TaskScheduler\task.txt','a')

file.write(f'{datetime.datetime.now()} - The script ran \n')