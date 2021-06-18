#declaring two dictionaries
dict1={"English":91,"Tamil":95,"Computer":98}
print("dict1: ",dict1)
dict2={"Physics":90,"Chemistry":99,"Maths":93}
print("dict2: ",dict2)

#Merging two dictionaries
dict1.update(dict2)
print("After merging two dictionaries, dict1: ",dict1)

#to remove a key from a dictionary
del dict2["Physics"]
print("After removing physics in dict2: ",dict2)

#mapping two list into a dictionary
list1=["English","Tamil","Computer"]
print("list1: ",list1)
list2=[91,95,98]
print("list2: ",list2)
newdict= dict(zip(list1,list2))
print("After mapping two list into a dictionary: ",newdict)


list3=["Physics","Chemistry","Computer"]
print("list3",list3)
list4=[90,99,93]
print("list4",list4)
newdict1={list3[i]:list4[i] for i in range(len(list2))}
print("After mapping another two list into a dictionary: ",newdict1)

#To find length of a set
set1={"English","Tamil","Computer","Physics","Chemistry","Maths"}
print("set1 :",set1)
print("The length of set1: ",len(set1))

#To remove the intersection of a 2nd set from the 1st set
set2={1,2,3,4,5}
print("set2 :",set2)
set3={3,4,5,6,7}
print("set3 :",set3)
s=set2.intersection(set3)
print("After removing the intersection of set2 from set3: ",set3-s)


