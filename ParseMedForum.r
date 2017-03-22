MFQ <- read.table('questions.txt',sep = '\t',header=FALSE,na.strings = "NA",fill=TRUE,quote = "")
View(MFQ)
MFC <- read.table('comments.txt',sep = '\t',header=FALSE,na.strings = "NA",fill=TRUE,quote = "")
View(MFC)

summary(MFQ)
summary(MFC)

# split tables into respective categories: 170, 1465, 146, 1428, 221
# For now, focus only on MFQ

library(dplyr)
library(tidyr)
count(MFQ,V4)

# group by data frame id
splitMFQ <- split(MFQ, MFQ$V4)
View(splitMFQ)
MLH <- splitMFQ[[1]]
GH <- splitMFQ[[2]]
DH <- splitMFQ[[3]]
ADH <- splitMFQ[[4]]
CH <- splitMFQ[[5]]


# checking to make sure all questions were correctly captured 
count(MLH) #31
count(GH) #1191
count(DH) #53
count(ADH) #373
count(CH) #210

# output seperated questions tables into files that can be itereated through python
#write.table(MLH, file = "MLH.txt", sep = "\t")
#write.table(GH, file = "GH.txt", sep = "\t")
#write.table(DH, file = "DH.txt", sep = "\t")
#write.table(ADH, file = "ADH.txt", sep = "\t")
#write.table(CH, file = "CH.txt", sep = "\t")

# split v1 (title.txt) and v7 (question)



#MLH_text <- data.frame(MLH$V1,MLH$V7)
#GH_text <- data.frame(GH$V1,GH$V7)
#DH_text <- data.frame(DH$V1,DH$V7)
#ADH_text <- data.frame(ADH$V1,ADH$V7)
#CH_text <- data.frame(CH$V1,CH$V7)


#write.table(MLH_text, file = "MLH_text.txt", sep = "\n")
#write.table(GH_text, file = "GH_text.txt", sep = "\n")
#write.table(DH_text, file = "DH_text.txt", sep = "\n")
#write.table(ADH_text, file = "ADH_text.txt", sep = "\n")
#write.table(CH_text, file = "CH_text.txt", sep = "\n")
