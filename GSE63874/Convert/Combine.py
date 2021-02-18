import os    


filenames=os.listdir("./")  
#获取输出文件的路径 
file=open('a.bed','w')  
   
for filename in filenames:  
    filepath='./'+filename    
    for line in open(filepath):  
        file.writelines(line)  
    file.write('\n')  
 
