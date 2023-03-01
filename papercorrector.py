# The program evaluate an answer and rewards percentage points depending on the number of required keywords mentioned in the answer.
# If an answer is wrong, partially or totally, it also displays the associated concept where the student is weak at.

Key = [["1586", "Maharana Pratap", "Man Singh"], 
     ["1945", "Hiroshima", "Nagasaki"]] # keywords

S = ["Fought in 1586 between Maharana Pratap and Babur.", 
     "WW2 ended in 1945 after Hiroshima Nagasaki bombings."] # student solutions

# User Input
# for i in range(2):
#     s = input()
#     S.append(s)  

C = ["Battle of Haldighati", "End of World War 2"] # associated concepts
  
    
for j in range(len(Key)):
    c = 0;
    print("In Question ", (j+1), "\n")
    for k in Key[j]:
        if k in S[j]:
            c += 1
        else:
            print("\tThe keyword missing was: ", k)
            print("\tAssociated concept: ", C[j])
    print("\tPercentage points: ", (c*100)/len(Key[j]), "\n")
