import os
def rename_files ():
    #(1) get file names from folder
    file_list = os.listdir(r"C:\Users\v.venkatakrishnan\Desktop\Workspace\Python\prank")
    #print (file_list)
    #(2) rename files
    os.chdir(r"C:\Users\v.venkatakrishnan\Desktop\Workspace\Python\TestData\prank")
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))

rename_files()



