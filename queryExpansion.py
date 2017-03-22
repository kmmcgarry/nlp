d_query = ["dementia","Dementia","DEMENTIA"]
a_query = ["alzheimer","Alzheimer","amyloid","Alzheimer's disease","apoE","Early-onset","Familial Alzheimer's disease","Late-onset","Tau"]

def generateFiles(inFile):
    i_file = open(inFile,"r")
    temp = []
    for i in i_file:
        temp.append(i)
    print (temp)
    count = 0
    boo = True
    files = []
    content = []
    while (boo == True):
        print count
        if count == (len(temp)-1):
            boo = False
        files.append(temp[count])
        content.append(temp[count+1])
        count += 1


    '''
    for line in i_file:
        if line[0:5] == "post_":
            #print line
            line = line.replace("\n","")
            files.append(line)
        else:
            line = line.replace("\n","")
            content.append(line)
    '''

    print files

    print len(files)

    print len(content)

'''
    for i in range(0,len(files)-1):
        #print files[i].replace("'","")
        path = "/Users/kristen/Development/nlp_project/forums/dementia/"+ files[i] + ".txt"
        #print path
        out = open(path,"w")
        out.write(content[i])
'''

#generateFiles("/Users/kristen/Development/nlp_project/forums/memory_loss/MLH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/dementia/DH_text.txt")


generateFiles("/Users/kristen/Development/nlp_project/forums/genetics/GH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/alz/ADH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/caregivers/CH_text.txt")
