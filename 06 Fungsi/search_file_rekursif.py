import os

def search_file(nama, path=None):
    for dir in os.listdir(path):
        if path == None:
            path = os.getcwd() 
        full_path = path+"/"+dir
        if os.path.isdir(full_path):
            # print("DIR ",full_path)
            search_file(nama,full_path)
        else: 
            if nama.lower() in full_path.lower():
                print("FILE ",full_path)
search_file("fungsi")