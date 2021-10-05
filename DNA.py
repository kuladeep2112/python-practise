import csv
from sys import argv
if len(argv)!=3:
    print("usage:no of argument")
else:

    with open(argv[1], 'r') as file:
        #to open csv file as a list
        reader = csv.reader(file)
        #list of list
        List=list(reader)
        # list containing all the different STR in a given CSV file
        STR=list(List[0][1:])

        with open(argv[2],'r') as file:
            for line in file:
                sequence=str(line)
            numpy=[]
            t=len(sequence)
            for k in range(len(STR)):

                z=t-len(STR[k])
                nums=[]
                for i in range(t):
                    j=i+len(STR[k])
                    count=0
                    while sequence[i:j]==STR[k] or i==z-1:
                        count=count+1
                        i=i+len(STR[k])
                        j=i+len(STR[k])
                    nums.append(count)

                count=max(nums)
                numpy.append(count)