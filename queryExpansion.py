
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


def queryExpansion(path):
    caregiver_files =["post_4109051.txt","post_5538310.txt","post_6581813.txt","post_7936623.txt","post_4129097.txt","post_5567258.txt","post_6592060.txt","post_7942578.txt","post_2571276.txt","post_4397231.txt","post_5567273.txt","post_6712675.txt","post_7973278.txt","post_2575681.txt","post_4406748.txt","post_5567661.txt","post_6720410.txt","post_8021034.txt","post_2579872.txt","post_4427982.txt","post_5625635.txt","post_6777016.txt","post_8028825.txt",
    "post_2613750.txt","post_4431725.txt","post_5637918.txt","post_6928010.txt","post_8036041.txt","post_2615304.txt","post_4451228.txt","post_5639429.txt","post_7010908.txt","post_8070151.txt",
    "post_2618158.txt","post_4481892.txt","post_5662928.txt","post_7124466.txt","post_8073381.txt",
    "post_2669760.txt","post_4491650.txt","post_5667582.txt","post_7127526.txt","post_8084129.txt",
    "post_2709593.txt","post_4522929.txt","post_5667871.txt","post_7179830.txt","post_8103651.txt",
    "post_2746323.txt","post_4587454.txt","post_5694587.txt","post_7181445.txt","post_8108202.txt",
    "post_2746679.txt","post_4599474.txt","post_5789094.txt","post_7191442.txt","post_8118858.txt",
    "post_2761594.txt","post_4665174.txt","post_5792594.txt","post_7198209.txt","post_8119211.txt",
    "post_2779564.txt","post_4775901.txt","post_5823700.txt","post_7232851.txt","post_8120783.txt",
    "post_2835128.txt","post_4797801.txt","post_5847402.txt","post_7277978.txt","post_8120953.txt",
    "post_2876083.txt","post_4818888.txt","post_5889887.txt","post_7277982.txt","post_8121524.txt",
    "post_2886995.txt","post_4821929.txt","post_5890491.txt","post_7296989.txt","post_8124845.txt",
    "post_3007061.txt","post_4999039.txt","post_5996431.txt","post_7322648.txt","post_8125152.txt",
    "post_3007436.txt","post_5057669.txt","post_5998002.txt","post_7394700.txt","post_8131676.txt",
    "post_3118159.txt","post_5124663.txt","post_6001473.txt","post_7426002.txt","post_8140713.txt",
    "post_3175252.txt","post_5176971.txt","post_6013188.txt","post_7489234.txt","post_8178926.txt",
    "post_3187128.txt","post_5179744.txt","post_6028216.txt","post_7493273.txt","post_8243129.txt",
    "post_3225097.txt","post_5202902.txt","post_6081429.txt","post_7556189.txt","post_8286671.txt",
    "post_3240087.txt","post_5202968.txt","post_6102641.txt","post_7654042.txt","post_8286675.txt",
    "post_3308786.txt","post_5206830.txt","post_6118159.txt","post_7665970.txt","post_8288599.txt",
    "post_3363905.txt","post_5245775.txt","post_6166835.txt","post_7672130.txt","post_8289159.txt",
    "post_3735502.txt","post_5245783.txt","post_6200763.txt","post_7737656.txt","post_8293843.txt",
    "post_3739274.txt","post_5252235.txt","post_6241319.txt","post_7750061.txt","post_8297169.txt",
    "post_3755327.txt","post_5299378.txt","post_6255798.txt","post_7755361.txt","post_8323650.txt",
    "post_3790996.txt","post_5338056.txt","post_6259053.txt","post_7775540.txt","post_8355695.txt",
    "post_3940331.txt","post_5397435.txt","post_6261824.txt","post_7783546.txt","post_8379415.txt",
    "post_3948486.txt","post_5416551.txt","post_6272747.txt","post_7800004.txt","post_8384189.txt",
    "post_3965710.txt","post_5419370.txt","post_6295444.txt","post_7804377.txt","post_8409923.txt",
    "post_3970676.txt","post_5442472.txt","post_6401174.txt","post_7845987.txt","post_8431877.txt",
    "post_3995349.txt","post_5445318.txt","post_6436163.txt","post_7858610.txt","post_8503725.txt",
    "post_3999987.txt","post_5463721.txt","post_6436792.txt","post_7918628.txt","post_8508415.txt",
    "post_4012960.txt","post_5476480.txt","post_6475443.txt","post_7922443.txt","post_8519938.txt",
    "post_4039396.txt","post_5498696.txt","post_6488222.txt","post_7923847.txt","post_8638643.txt",
    "post_4045538.txt","post_5508177.txt","post_6537528.txt","post_7928527.txt","post_8658930.txt",
    "post_4049482.txt","post_5516310.txt","post_6551745.txt","post_7929120.txt","post_8695880.txt",
    "post_4099013.txt","post_5530660.txt","post_6579535.txt","post_7936341.txt","post_8738549.txt"]


    d_query = ["dementia","Dementia","DEMENTIA"]
    a_query = ["alzheimer","amyloid","alzheimer's disease","apoe","familial alzheimer's disease","tau","amyloid beta-peptides","FAC1 protein"]

    dementia_files = []
    alz_files = []

    for files in caregiver_files:
        forum = path+files
        #print forum
        i_file = open(forum,"r")

        # what if both words are present? look at frequencies and choose which ever one is more frequent

        for line in i_file:
            for term in d_query:
                if term in line:
                    dementia_files.append(forum[-16:])
            for term in a_query:
                if term in line:
                    alz_files.append(forum[-16:])
    print dementia_files
    print len(dementia_files)
    print alz_files
    print len(alz_files)
    return "done"






queryExpansion("/Users/kristen/Development/nlp_project/forums/caregivers/")




#generateFiles("/Users/kristen/Development/nlp_project/forums/memory_loss/MLH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/dementia/DH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/genetics/GH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/alz/ADH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/caregivers/CH_text.txt")
