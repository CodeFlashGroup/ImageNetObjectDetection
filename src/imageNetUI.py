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

        xmlFilePath="../xmlData/lady.xml"
        elementDict = xmlExtraction.extractXMLData(xmlFilePath = xmlFilePath)
        
        #debug
        print ('elementDict = {} '.format(elementDict))
        #debug -ends
        imgpath="../img/lady.jpeg"
        imgExtraction=ImgExtraction()
        flag2=imgExtraction.displayImageObject(imgpath, elementDict)
        flag=imgExtraction.extractImgData(imgpath,elementDict)
        print (flag, flag2)
#|------------------------imagenetObjectDetection -ends------------------------|















if __name__ == '__main__':
    filePath = "I:\ILSVRC"
    imageNetUI = ImageNetUI()
    imageNetUI.imagenetObjectDetection(filePath)
    