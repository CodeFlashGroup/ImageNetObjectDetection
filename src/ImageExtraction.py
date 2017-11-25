import cv2
import difflib

class ImgExtraction:

#|-----------------------------------------------------------------------------|
# extractImgData
#|-----------------------------------------------------------------------------|
    def extractImgData(self,imgFilePath,objectStoragePath, elementDict):
        """
        
        """
        # parsing xml in tree
        img = cv2.imread(imgFilePath)
        key=difflib.get_close_matches('object',elementDict,n=100)
        i=0
        for object in key:
            obj=elementDict[object]
            xmin=int(obj['xmin'])
            ymin=int(obj['ymin'])
            xmax=int(obj['xmax'])
            ymax=int(obj['ymax'])
            #print(xmin)
            out = img[ymin:ymax,xmin:xmax]
            strimg="../img/Cropped"+str(i)+".jpeg"
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
        #debug
        print ('key = {} '.format(key))
        #debug -ends
        firstName = elementDict['object0']['name']
        #debug
        print ('firstName = {} '.format(firstName))
        #debug -ends
        for object in key:
            obj = elementDict[object]
            objName = obj['name']
            xmin = int(obj['xmin'])
            ymin = int(obj['ymin'])
            xmax = int(obj['xmax'])
            ymax = int(obj['ymax'])
            #debug
            print ('objName = {} '.format(objName))
            #debug -ends
            # print(xmin)
#             if firstName==objName:
            img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
#             else:
#                 img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 1)
#             print(img)

        # for i -ends
        cv2.imshow("imgWithBox", img)

        cv2.imwrite("../img/imgWithBox.jpeg", img)
        cv2.waitKey(0)
        print ("object has been found")
        return True

