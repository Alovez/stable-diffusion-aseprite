import os
import sys

if __name__ == "__main__":
    if sys.argv[1] == "remote":
        print("remote")
        os.system("rm ../settings.txt && cp ../settings_remote.txt ../settings.txt")
    else:
        print("local")
        os.system("rm ../settings.txt && cp ../settings_local.txt ../settings.txt")