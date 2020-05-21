import os

INPUT_FILE="D:\My\Data\Test\Blondie - Rapture.mp3"

def readInputFile():
    in_file = open(INPUT_FILE, "rb") # opening for [r]eading as [b]inary
    data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    in_file.close()
    return data

#print(data)


def injectTag(data, id3Tag, value):
    id3Ascii = toAsciiArray(id3Tag)
    valueAscii = toAsciiArray(value)
    data[11:11] = id3Ascii
    return data

def toAsciiArray(value):
    #return the ascii representation of the value
    return [ord(c) for c in value]


fileContent = readInputFile()
print(fileContent[0])

updatedContent = injectTag(fileContent, "TIT2", "Eric")
print(updatedContent[:15])




#injectTag(data, "TIT2", "Eric Title")

#out_file = open("out-file", "wb") # open for [w]riting as [b]inary
#out_file.write(data)
#out_file.close()