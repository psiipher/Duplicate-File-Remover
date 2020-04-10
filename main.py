import os
import sys
import checksum
import schedule
import time


def duplicate_removal(path):
    if not os.path.isdir(path):
        print("\n\nEnter a valid path!!\n\n")
        sys.exit()
    data = {}
    for Folder, Subfolder, Files in os.walk(path):
        for name in Files:
            name = os.path.join(Folder, name)
            
            chksum = checksum.hashfile(name)

            if chksum in data:
                data[chksum].append(name)
            else:
                data[chksum] = [name]

    newdata = []
    newdata = list(filter(lambda x: len(x) > 1, data.values()))

    count = 0
    dcnt = 0
    for outer in newdata:
        icnt = 0
        for inner in outer:
            icnt += 1
            if icnt >= 2:
                count += 1
                print("\n\t\tDuplicate File found!!!\n\nPath:\t", inner)
                y = input("Do you want to delete the file ? [y/n]:\t")
                if y.lower() == "y":
                    try:
                        os.remove(inner)
                        dcnt += 1
                        print("File deleted successfully")
                    except:
                        print("\nError deleting file!!\n")

    print("\n\nTotal duplicate files found:\t", count)
    print("Total files deleted:\t", dcnt)


def main():
    if len(sys.argv) != 2:
        print("\nInvalid number of arguments. Try running with -h for help and -u for usage\n")
        sys.exit()

    if sys.argv[1] == '-h':
        print("\nDuplicate File removal with scheduling facility.\n")
        sys.exit()
    elif sys.argv[1] == '-u':
        print("\nUsage: python3 main.py absolute_path_of_directory\n")
        sys.exit()

    line = "-" * 50
    print(f"\n\n{line}Duplicate file removal{line}\n\n")
    s = input("\nDo you want to schedule this process periodically ? [y/n]:\t")
    if s.lower() == "y":
        t = int(input("Enter time interval in minutes (Eg. 1):\t"))
        schedule.every(t).minute.do(duplicate_removal, path=sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)
    elif s.lower() == 'n':
        duplicate_removal(sys.argv[1])
    else:
        print("\nNot a valid input\n")
        sys.exit()


if __name__ == "__main__":
    main()



















