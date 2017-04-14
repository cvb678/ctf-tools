#Least significant bit decryption
#Gets image and ascii from last bits of bmp file

in_img_f = open("littleschoolbus.bmp", "rb")
out_txt = open("bits.txt", "wb")
out_img = open("asd.bmp", "wb")

in_img = in_img_f.read()
#Get the header
out_img.write(in_img[0:54])

#Get lsbs and create image and txt with binary
for rgb in in_img[54:]:
    lsb = ord(rgb)&1
    out_txt.write(str(lsb))
    out_img.write(chr(0000000+lsb))

in_img_f.close()
out_img.close()
out_txt.close()


#decode all binary possibilites
in_txt = open("bits.txt", "rb")
#shift by i-bytes
for i in range(0,7):
    in_txt.seek(i, 0)
    buffer = []
    try:
        byte = in_txt.read(8)
        while byte != "":
            ascii = int(byte, 2)
            #filter out non-ascii characters
            if(ascii >= 48 and ascii <= 126):
                buffer.append(''.join(chr(ascii)))
            byte = in_txt.read(8)
    finally:
        ascii_out = open("ascii/"+str(i)+".txt", "wb")
    	ascii_out.write(''.join(buffer))
    	ascii_out.close()

in_txt.close()
