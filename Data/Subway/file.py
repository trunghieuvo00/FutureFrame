import os  
  
# importing shutil module  
import shutil  
  
# path  
path = '/home/abnormal_detection/VuNgocTu/dataset/subway/testing_total/frames/01/'
  
# List files and directories  
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'  
#print("Before moving file:")  
#print(os.listdir(path))  
  
  
# Source path  
#arr_=[]
#for i in sorted(os.listdir(path)):
  #arr_.append(int(i[:-4]))
#print(arr_)
for i in sorted(os.listdir(path)):
  #if int(i[:-4])<=20000:
  #  continue
  if int(i[:-4])<=50000:
    continue
    #break
    
    
  source = os.path.join(path,i)
  
# Destination path  
  destination = '/home/abnormal_detection/VuNgocTu/dataset/subway/testing/frames/02/'
  
# Move the content of  
# source to destination  
  dest = shutil.move(source, destination)  
  
