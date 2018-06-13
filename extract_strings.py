# -*- coding: utf-8 -*-
import subprocess, os, base64, zlib


def Decode_Script(data):

	data = data.split("-e")[1]
	data = base64.b64decode(data)
	data = data.split("'")[1]
	print "[*] Base64 Decoded Data Is Compressed."
	#print data
	print "[*] Decompressing..."
	data = base64.b64decode(data)
	data = zlib.decompress(data, -15)
	print "[*] Data Decompressed: "
	print data
	print "[*] File Deobfuscation Complete. Exiting."
	return
	
	

def Form(output_file):
	
	print "[*] Gathering Function Names..."
	
	Function_Names = []
	f1 = open(output_file, "r")
	data = f1.readlines()
	f1.close()
	
	for lines in data:
		if "Function" in lines and "=" not in lines:
			string = ""
			string = lines[9:]
			Function_Names.append(string[:-3])
		else:
			continue
			
	print "[*] Located All Function Names."
	print "[*] Creating Python Extraction Script."
	
	f1 = open(output_file + ".py", "w")
	
	for lines in data:
		if "VBA" not in lines and "Function" not in lines:
			f1.write(lines)
		else:
			continue
			
	f1.write("f = open('newfile.txt', 'w')")
	for functions in Function_Names:
		f1.write("\nf.write(" + functions + ")")
		
	f1.write("\nf.close")
	f1.close()
			
	
	print "[*] Forming Base64 String From Data..."
	
	subprocess.call(['python', output_file + ".py"])
	
	os.remove(output_file)
	os.remove(output_file + ".py")
	
	f2 = open("newfile.txt", "r")
	data = f2.read()
	f2.close()
	
	#print data
	
	os.remove("newfile.txt")
	print "[*] Decrypting Base64 String."
	
	Decode_Script(data)
	
	return

def main():

	input_file = raw_input("[*] Filename containing strings: ")
	output_file = "Output_File"
	
	f = open(input_file, "r")
	f1 = open(output_file, "w")
	data = f.readlines()
	f.close()
	for lines in data:
	
		if "CStr" not in lines and "End" not in lines and "Error" not in lines and "Function_" not in lines:
			f1.write(lines)
		else:
			continue
	f1.close()
	print "[*] Removed Junk Code From File!"
	
	Form(output_file)
	
	
		
	return

if __name__ == "__main__":
	main()
