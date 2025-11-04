filename=input("Enter a file name(with extension):")
parts=filename.split('.')
if len(parts)>1:
    print("file extension is:",parts[-1])
else:
    print("no extension found in the file name.")
