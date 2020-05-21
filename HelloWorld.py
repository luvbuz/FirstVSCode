import os

def main():
    print("start")

    tracks = []

    for root, dir, files, in os.walk("D:\\My\\Music\\Mix 2020"):
        for name in files:
            if name.endswith(".mp3"):
                print(name)
main()
