import os    


filenames=os.listdir("./")  
#获取输出文件的路径 
file=open('Na_K_PDS.bed','w')  
   
for filename in filenames[1:]:  
    filepath='./'+filename    
    for line in open(filepath):  
        file.writelines(line)  
    file.write('\n')  
 
