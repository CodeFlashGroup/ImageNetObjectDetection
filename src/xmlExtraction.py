import xml.etree.ElementTree as ET
import numpy as np

class XmlExtraction:
   
#|-----------------------------------------------------------------------------|
# extractXMLData
#|-----------------------------------------------------------------------------|
    def extractXMLData(self, xmlFilePath):
        """
        given function reads xml file, and return its values in the dictionary
        """
        #parsing xml in tree
        tree = ET.parse('../xmlData/lady.xml')
        #getting root element of tree
        root = tree.getroot()
        #creating elementDict
        elementDict = {}
        counter=0
        
        #reading elementDict file details
        elementDict['folder']=root.find('folder').text
        elementDict['fileName'] = root.find('filename').text
        elementDict['dbName'] = root.find('source/database').text
        elementDict['height']=root.find('size/height').text
        elementDict['width']=root.find('size/width').text
        #looping over object to get object details 
        for obj in root.iter('object'):
            objDict = {}
            objDict['name']=obj.find('name').text
            objDict['xmin']=obj.find('bndbox/xmin').text
            objDict['xmax']=obj.find('bndbox/xmax').text
            objDict['ymin']=obj.find('bndbox/ymin').text
            objDict['ymax']=obj.find('bndbox/ymax').text
            elementDict['object'+str(counter)]=objDict
            counter+=1
        
        return elementDict    
#|------------------------extractXMLData -ends---------------------------------|
#|-----------------------------------------------------------------------------|
# readCategory
#|-----------------------------------------------------------------------------|
    def readCategory(self, catFilePath):
        """
        Input: filePath string
        output: list containing file path
        given function reads a particular category file and store its file path
        into a list
        
        NOTE: skipping folders which has ILSVRC2013_train_extra ... key word as
        their ennotations are not provided
        """
        #reading file
        with open(catFilePath) as textFile:
            lines = [line.split() for line in textFile]
        #file read -ends
        
        #closing text file
        textFile.close()
        
        #removing 2nd column with number
        fileList =  (np.array(lines)[:,0])
        
        parsedFileList = self.removeExtraDir(fileList)
        return parsedFileList
#|------------------------readCategory -ends----------------------------------| 
#|-----------------------------------------------------------------------------|
# removeExtraDir
#|-----------------------------------------------------------------------------|
    def removeExtraDir(self, fileList):
        """
        here, images in ILSVRC2013_train_extra ... does not have annotations.
        So we are skipping these extra directories
        """
        parsedFileList = []
        for myStr in fileList:
            if not (myStr.startswith("ILSVRC2013_train_extra")):
                parsedFileList.append(myStr)
            #if -ends
        #for -ends
        return parsedFileList
    
#|------------------------removeExtraDir -ends----------------------------------|    
 
if __name__ == '__main__':
    filePath = '../xmlData/lady.xml'
     
    xmlExtraction = XmlExtraction()
    elementDict = xmlExtraction.extractXMLData(filePath)
     
    #debug
    print ('elementDict = {} '.format(elementDict))
    #debug -ends
    
