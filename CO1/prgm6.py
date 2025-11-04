names=input("Enter first names separated by space:").split()
count=sum(name.lower().count('a')for name in names)
print("list of names:",names)
print("total occurrences of 'a':",count)
