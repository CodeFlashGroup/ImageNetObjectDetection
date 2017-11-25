from ImageExtraction import ImgExtraction
from xmlExtraction import XmlExtraction

class ImageNetUI:
    
#|-----------------------------------------------------------------------------|
# imagenetObjectDetection
#|-----------------------------------------------------------------------------|
    def imagenetObjectDetection(self, filePath):
        """
        1. for all files, find xml details and make its dict
        2. based on these xml, detect objects
        3. train data
        
        """
        xmlExtraction=XmlExtraction()
        catFilePath = "I:/ILSVRC/ImageSets/DET/train_1.txt"
        categoryList = xmlExtraction.readCategory(catFilePath)

#         #debug
#         print ('categoryList = {} '.format(categoryList))
#         #debug -ends

        xmlFilePath="I:/ILSVRC/Annotations/DET/train/"        
        imgpath="I:/ILSVRC/Data/DET/train/"
        
        objStoragePath = "I:/ILSVRC/objects"
        
        self.getObjectImg(xmlDirPath = xmlFilePath, imgDirPath = imgpath,\
                                            objectStoragePath = objStoragePath,\
                                                     catList = categoryList)
        imgExtraction=ImgExtraction()
#|------------------------imagenetObjectDetection -ends------------------------|

#|-----------------------------------------------------------------------------|
# getObjectImg
#|-----------------------------------------------------------------------------|
    def getObjectImg(self, xmlDirPath, imgDirPath, objectStoragePath, catList):
        """
        given function read catList path, append that path in xmlPath or imgPath,
        read xml as well as image, and store objects based on its category
        """
        xmlExtraction=XmlExtraction()
        imgExtraction=ImgExtraction()

        for i in range(5):
            xmlFilePath = xmlDirPath+catList[i]+".xml"
            imgFilePath = imgDirPath+catList[i]+".jpeg"
            
            #debug
            print ('xmlFilePath = {} '.format(xmlFilePath))
            print ('imgFilePath = {} '.format(imgFilePath))
            #debug -ends
            
            elementDict = xmlExtraction.extractXMLData(xmlFilePath = xmlFilePath)
            #debug
            print ('elementDict = {} '.format(elementDict))
            #debug -ends  
            flag2=imgExtraction.displayImageObject(imgFilePath, elementDict)
            flag=imgExtraction.extractImgData(imgFilePath, objectStoragePath ,elementDict)          
            
#|------------------------getObjectImg -ends----------------------------------|    













if __name__ == '__main__':
    filePath = "I:\ILSVRC"
    imageNetUI = ImageNetUI()
    imageNetUI.imagenetObjectDetection(filePath)
    