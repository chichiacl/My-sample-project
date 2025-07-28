file = input("File name: ")
index = file.rfind(".")
type = file[index:]
if index != -1 :
    match type.strip().lower():
        case ".gif" :
            print("image/gif")
        case ".jpg"|".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")



