import difflib
import xml.etree.ElementTree as ET
import cv2
#from fuzzywuzzy import fuzz

class XmlExtraction:
    # |-----------------------------------------------------------------------------|
    # extractXMLData
    # |-----------------------------------------------------------------------------|
    def extractXMLData(self, xmlFilePath):
        """
        given function reads xml file, and return its values in the dictionary
        """
        # parsing xml in tree
        tree = ET.parse('../xmlData/lady.xml')
        # getting root element of tree
        root = tree.getroot()
        # creating elementDict
        elementDict = {}
        counter = 0

        # reading elementDict file details
        elementDict['folder'] = root.find('folder').text
        elementDict['fileName'] = root.find('filename').text
        elementDict['dbName'] = root.find('source/database').text
        elementDict['height'] = root.find('size/height').text
        elementDict['width'] = root.find('size/width').text
        # looping over object to get object details
        for obj in root.iter('object'):
            objDict = {}
            objDict['name'] = obj.find('name').text
            objDict['xmin'] = obj.find('bndbox/xmin').text
            objDict['xmax'] = obj.find('bndbox/xmax').text
            objDict['ymin'] = obj.find('bndbox/ymin').text
            objDict['ymax'] = obj.find('bndbox/ymax').text
            elementDict['object' + str(counter)] = objDict
            counter += 1

        return elementDict
# |------------------------extractXMLData -ends---------------------------------|
class ImgExtraction:
    # |-----------------------------------------------------------------------------|
    # extractImgData
    # |-----------------------------------------------------------------------------|
    def extractImgData(self,imgFilePath,elementDict):
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
        return True

if __name__ == '__main__':
    xmlpath="../xmlData/lady.xml"
    xmlExtraction = XmlExtraction()
    elementDict = xmlExtraction.extractXMLData(xmlpath)
    # debug
    print('elementDict = {} '.format(elementDict))

    imgpath="../img/lady.jpeg"
    imgExtraction=ImgExtraction()
    flag=imgExtraction.extractImgData(imgpath,elementDict)
    if(flag):
        print("Extraction has been done")