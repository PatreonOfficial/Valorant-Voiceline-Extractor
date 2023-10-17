import json
import os
import glob
import shutil

jsonDir = "src\jsons/"
mediaDir = "src\Media/"
error = []

# Open a file
dirs = os.listdir( jsonDir )

for file in dirs:
    f = open(jsonDir + file)
    data = json.load(f)
    vo_id=[]

    count = 0

    #get file Ids
    for i in data[1]["Properties"]["MediaList"]:
        vo_id.append(i["AssetPathName"].split(".")[1])
        
        print(file.split(".")[0])
        print(vo_id)
        #print(i)

        
        #move and rename file
        oldFileName = vo_id[count] + ".wav"

        if count == 0:
            newFileName = file.split(".")[0] +".wav"
        else:
            newFileName = file.split(".")[0] +"-"+ str(count) +".wav"

        if os.path.exists(mediaDir + oldFileName):
            shutil.copy(mediaDir + oldFileName , "output/" + newFileName)
        else:
            print("Error: Source does not exist! " + vo_id[count])
            error.append(vo_id[count])
            

        count += 1
        
    f.close()
print(error)
