import os


def exception_handling(folder):
    try:
        files = os.listdir(folder)
        print(f"Folder {folder} found")
        print(f" The files in the folder {folder} are:")
        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"ERROR: The entered folder {folder} not found")
    except PermissionError:
        print(f"ERROR: You do'nt have access to this folder : {folder}")

def main():
    print("FILES DISPLAYING PROGRAM")
    print("------------------------")
    folders = input("Enter the folder names with spaces :").split()
    for folder in folders:
        print("----------------------------------------")
        exception_handling(folder)



if __name__ == "__main__":
    main()


