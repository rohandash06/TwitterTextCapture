
import operator


def Total_Users():
    INPUTFILE = input(" Enter the path of the input file located : ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    t = input(" Enter a number : ")
    o = int(t)
    OUTFILE = r'C:\Users\rdas3\Desktop\Docs\Total_Users'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        tweet=myFile.readlines()
    f = {}
    for data in tweet:
       
        file_Temp = data.split()
        if file_Temp[0] in f:
            f[file_Temp[0]] +=1
        else:
            f[file_Temp[0]] = 1
    f = sorted(f.items(), key = operator.itemgetter(1), reverse = True)
 
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    output_File.write(" The top "+ t +" users who have tweeted most in the time frame : \n")
    for i in range (0,o):
        output_File.write(" User Name " + f[i][0] + "\n\n")
        
    output_File.close
Total_Users()

def Active_users_PerHour():
    INPUTFILE = input(" Enter the path of the input file located : ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    val = input(" Enter a number : ")
  
    OUT_FILE = r'C:\Users\rdas3\Desktop\Docs\Active_users_PerHour'
    OUTPUT_FILE_PATH = OUT_FILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as my_File:
        dataS=my_File.readlines()

    f = {}
    for data in dataS:
        file_Temp = data.split()
        file_Temp2 = file_Temp[1].split(":")
        tweet_Temp = file_Temp[0] + " " + file_Temp2[1]
        if tweet_Temp in f:
            f[tweet_Temp]+=1
        else:
            f[tweet_Temp]=1
    f = sorted(f.items(), key = operator.itemgetter(1), reverse = True)

    f2={}
    total_Users_In = 0
    for data in f:
        total_Users_In+=1
        if(data[0].split()[1]) in f2:
            f2[data[0].split()[1]]+=1
        else:
            f2[data[0].split()[1]]=1
    f2 = sorted(f2.items(), key = operator.itemgetter(1))

    
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
   
    outputFile.write(" The top "+ val +" users who have tweeted the most number of times in an hour: " + "\n\n")
    for z in range (0,len(f2)):
   
        m_Search = 10
        
       
        for data in f:
            if m_Search == 0:
                break
            if data[0].split()[1] == f2[z][0]:
                outputFile.write(" Username: " + data[0].split()[0] + "\n\n")
                
                m_Search-=1
    outputFile.close
Active_users_PerHour()

def Maximum_Followers():
    INPUTFILE = input(" Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    t = input(" Enter a number: ")
    val = int(t)
    OUTFILE = r'C:\Users\rdas3\Desktop\Docs\Maximum_Followers'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as my_File:
        tweet=my_File.readlines()

    f = {}
    for data in tweet:
        file_Temp = data.split()
        if file_Temp[0] not in f:
            f[file_Temp[0]] = file_Temp[-2]

    f = sorted(f.items(), key = operator.itemgetter(1), reverse = True)
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    output_File.write(" The top "+ t + " users who have the maximum number of followers : " + "\n\n")

    for i in range (0, val):
        output_File.write(" Username: " + f[i][0] + "\n\n")
    output_File.close
Maximum_Followers()

def Count_of_retweets():
    INPUTFILE = input(" Enter the path of the input file located : ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    val = input(" Enter a number : ")
    n = int(val)
    OUT_FILE = r'C:\Users\rdas3\Desktop\Docs\Count_of_retweets'
    OUTPUT_FILE_PATH = OUT_FILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as my_File:
        tweet=my_File.readlines()

    f = {}
    for data in tweet:
  
        file_Temp = data.split()
        y = len(file_Temp)-2
        tweets = "\""
        for x in range (4, y):
            tweets += file_Temp[x] + " "
        tweets += " ::::;:::: " + file_Temp[0]
  
        if tweets not in f:
            f[tweets] = int(file_Temp[-1])

    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    f = sorted(f.items(), key = operator.itemgetter(1), reverse = True)
    output_File.write(" The top "+  val + " tweets that had the max number of retweets : " + "\n\n")

    for x in range (0, n):
        output_File.write("\n Tweet : " +
                      f[x][0].split(":::;:::")[0]  + "\n\n")
    output_File.close
Count_of_retweets()






    