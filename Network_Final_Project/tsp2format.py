from sys import argv
import numpy as np
if len(argv) != 2:
    print("Provide a dataset with euc_2d ")
    exit(1)

inputf=open(argv[1])
lines=inputf.readlines()
inputf.close()

outputf=open(argv[1]+".out",'w')
# output= []
outputf.write(str(len(lines)))
outputf.write('\n')
for current in lines:
    n1, x1,y1= current.split(' ')
    n1, x1, y1=int(n1),float(x1),float(y1)
    # output.append( [] )
    # print()
    # break
    for node in lines:
        n2,x2,y2=node.split(' ')
        n2, x2, y2=int(n2),float(x2),float(y2)

        # print( "values:",n1,x1,y1,n2,x2,y2 )
        outputf.write(str(int(np.sqrt( (x2-x1)**2+(y2-y1)**2 )) )+' ' )
        pass
    outputf.write('\n')
    pass

# print(output)

# for i in output:
#     for j in i:
#         outputf.write( str(j)+' ' )
#         # print(j, end=' ')
#     outputf.write('\n')
#     # print()
# outputf.close()