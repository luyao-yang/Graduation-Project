import os    

filenames=os.listdir("./")  

file=open('PA.bed','w')  
   
filepath='./GSE129281_PA_K_hits.bed'    

for line in open(filepath):
    line_feature = line.split()
    new_line = line_feature[:-3]
    new_line = "\t".join(new_line)
    new_line = new_line + '\n'
    file.writelines(new_line)  
file.write('\n')  