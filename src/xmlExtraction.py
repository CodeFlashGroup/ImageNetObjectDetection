import xml.etree.ElementTree as ET

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

if __name__ == '__main__':
    filePath = '../xmlData/lady.xml'
    
    xmlExtraction = XmlExtraction()
    elementDict = xmlExtraction.extractXMLData(filePath)
    
    #debug
    print ('elementDict = {} '.format(elementDict))
    #debug -ends