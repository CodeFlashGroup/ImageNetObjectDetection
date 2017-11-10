import cv2

class ImgExtraction:

#|-----------------------------------------------------------------------------|
# extractImgData
#|-----------------------------------------------------------------------------|
    def extractImgData(self,imgFilePath,elementDict):
        """
        
        """
        # parsing xml in tree
        img = cv2.imread(imgFilePath)
        key=difflib.get_close_matches('object',elementDict,n=100)
        i=0
        for i in range(len(key)):
            obj=elementDict['object'+str(i)]
            xmin=int(obj['xmin'])
            ymin=int(obj['ymin'])
            xmax=int(obj['xmax'])
            ymax=int(obj['ymax'])
            #print(xmin)
            out = img[ymin:ymax,xmin:xmax]
            strimg="Cropped"+str(i)+".jpeg"
            print(strimg)
            cv2.imwrite(strimg, out)
            cv2.waitKey(0)
        #for i -ends
        return True
#|------------------------extractImgData -ends----------------------------------|    
