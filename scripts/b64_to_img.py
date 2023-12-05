import base64

with open('temp2/temp.b64', 'r') as f:
    b64 = f.read()
    index = 1
    for s in b64[10:].split(','):
        imgdata = base64.decodebytes(bytes(s[1:-1], "utf-8"))
        with open("temp/temp" + f"{index}_d.png", 'wb') as outf:
            outf.write(imgdata)
        index += 1
