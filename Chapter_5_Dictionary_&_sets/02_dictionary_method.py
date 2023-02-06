myDict ={
    "fast": "is a quick manner",
    "harry": "a coder",
    "marks": [1,2,3,4],
    "anotherdict":{'harry':'player'}
}


# print(list(myDict.keys())) #--->can convert it to any data type
# print(list(myDict.values()))
# print(myDict.items())  #print the (key,value) for all the contents in dictionary




# #updating the dictionary
# updatedict={
#     'enemy' : "no one",
#     "harry": "a fucker" #---> wil replace it on the main dictionary
# }
# myDict.update(updatedict)  #-----> will update the dicitonary (add the latest item)



print(myDict["harry"]) #--->it will throw error if the suspected item not found
print(myDict.get("harry2"))  #----> it will not throw any error if the suspected item not found


