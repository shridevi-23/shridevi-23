file_path="balajis.txt"
try:
    with open(file_path,"r")as file:
        content=file.read()
        print(content)
except FilenotFoundError:
    print("File not found!")
except Exception as e:
    print("