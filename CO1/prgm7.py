list1=list(map(int,input("Enter integers for first list(space separated): ").split()))
list2=list(map(int,input("Enter integers for second list(space separated): ").split()))
same_length=len(list1)==len(list2)
print("Both list are of the SAME length:",same_length)
    
same_sum=sum(list1)==sum(list2)
print("Both list are of the SAME sums:",same_sum)

common_value=set(list1)&set(list2)
if common_values:
    print(f"(c)common values in both lists:",common_values)
else:
    print("check completed.")
       
