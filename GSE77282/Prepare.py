import os    

filenames=os.listdir("./")  
#获取输出文件的路径 
file=open('test.bed','w')  
   
for filename in filenames[1:]:  
    filepath='./GSE77282_K_hits.bed'    
    for line in open(filepath):
        line_feature = line.split()
        new_line = line_feature[:-6]
        new_line = '\t'.join(new_line)
        new_line = new_line + '\n'
        file.writelines(new_line)  
    file.write('\n')  