d_query = ["dementia","Dementia","DEMENTIA"]
a_query = ["alzheimer","Alzheimer","amyloid","Alzheimer's disease","apoE","Early-onset","Familial Alzheimer's disease","Late-onset","Tau"]

def generateFiles(inFile):
    i_file = open(inFile,"r")
    temp = []
    files = []
    content = []

    for line in i_file:
        line = line.split("&&&")
        #print line
        #print "\n"
        filePath = line[1][1:-1]
        #print filePath
        path = "/Users/kristen/Development/nlp_project/forums/caregivers/"+ filePath + ".txt"

        #print path
        out = open(path,"w")
        out.write(line[2])

    return "done"



    '''
    for line in i_file:
        if line[0:5] == "post_":
            #print line
            line = line.replace("\n","")
            files.append(line)
        else:
            content.append(line)
        print "f: " + str(len(files))
        print "c: " + str(len(content))
        if len(content) > len(files):
            print "ERRROOORRR"
            print line
    '''


    #print files

    #print len(files)

    #print len(content)

'''
    for i in range(0,len(files)-1):
        #print files[i].replace("'","")
        path = "/Users/kristen/Development/nlp_project/forums/alz/"+ files[i] + ".txt"
        #print path
        out = open(path,"w")
        out.write(content[i])
'''

#generateFiles("/Users/kristen/Development/nlp_project/forums/memory_loss/MLH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/dementia/DH_text.txt")


#generateFiles("/Users/kristen/Development/nlp_project/forums/genetics/GH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/alz/ADH_text.txt")
generateFiles("/Users/kristen/Development/nlp_project/forums/caregivers/CH_text.txt")
