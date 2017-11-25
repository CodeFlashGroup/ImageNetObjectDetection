import cv2
import difflib

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
    def displayImageObject(self, imgFilePath,elementDict):
        # parsing xml in tree
        img = cv2.imread(imgFilePath)
        key = difflib.get_close_matches('object', elementDict, n=100)
        i = 0

        firstName = elementDict['object0']['name']
        print (firstName)
        for i in range(len(key)):
            obj = elementDict['object' + str(i)]
            objName = obj['name']
            xmin = int(obj['xmin'])
            ymin = int(obj['ymin'])
            xmax = int(obj['xmax'])
            ymax = int(obj['ymax'])
            # print(xmin)
            if firstName==objName:
                img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
            else:
                img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 1)
            print(img)

        # for i -ends
        cv2.imshow("imgWithBox", img)

        cv2.imwrite("imgWithBox.jpeg", img)
        cv2.waitKey(0)
        print ("object has been found")
        return True

