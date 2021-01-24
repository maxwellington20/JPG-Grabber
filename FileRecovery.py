import re, binascii, hashlib

with open("Project2Updated.dd", "rb") as file:
    disk = file.read()

hexdump = binascii.hexlify(disk)

jpg_matches = re.finditer("ffd8ff(.*?)ffd90000", hexdump.decode())

if jpg_matches:

    jpg_counter = 1

    
    for x in jpg_matches:

        startoffset, endoffset = x.span(0)
                
        print("Starting/Ending Offsets for JPG_File" + str(jpg_counter) + ":")
        print(str(hex(int(startoffset/2))) + "/" + str(hex(int(endoffset/2))))
        full_image = x.group(0)
        print("sha-256:" + hashlib.sha256(full_image.encode()).hexdigest())
        converted_image = binascii.a2b_hex(full_image)
        output_file_path = "JPG_File" + str(jpg_counter) + ".jpg"
        jpg_counter += 1

        with open(output_file_path, "wb") as image:
            image.write(converted_image)

        if jpg_counter == 4:
            break