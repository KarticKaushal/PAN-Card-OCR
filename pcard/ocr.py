from django.conf import settings

try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract
import numpy as np
import cv2
import ftfy
import re
import json
import io
import os

def ocr(filename):  
    """
    This function will handle the core OCR processing of images.
    """
    i = cv2.imread(filename)
    
    # Convert to gray
    i = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    i = cv2.dilate(i, kernel, iterations=1)
    i = cv2.erode(i, kernel, iterations=1)
    
    text = pytesseract.image_to_string(i)
    #return text

    # Cleaning all the gibberish text
    text = ftfy.fix_text(text)
    text = ftfy.fix_encoding(text)
    return text
'''
    # Initializing data variable
    name = None
    fname = None
    dob = None
    pan = None
    nameline = []
    dobline = []
    panline = []
    text0 = []
    text1 = []
    text2 = []

    # Searching for PAN
    lines = text.split('\n')
    for lin in lines:
        s = lin.strip()
        s = lin.replace('\n','')
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)

    text1 = list(filter(None, text1))

    # to remove any text read from the image file which lies before the line 'Income Tax Department'

    lineno = 0  # to start from the first line of the text file.

    for wordline in text1:
        xx = wordline.split('\n')
        if ([w for w in xx if re.search('(INCOMETAXDEPARWENT @|mcommx|INCOME|TAX|GOW|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$', w)]):
            text1 = list(text1)
            lineno = text1.index(wordline)
            break

    text0 = text1[lineno+1:]
    print(text0)  # Contains all the relevant extracted text in form of a list - uncomment to check

    def findword(textlist, wordstring):
        lineno = -1
        for wordline in textlist:
            xx = wordline.split( )
            if ([w for w in xx if re.search(wordstring, w)]):
                lineno = textlist.index(wordline)
                textlist = textlist[lineno+1:]
                return textlist
        return textlist

    try:
        # Cleaning first names, better accuracy
        name = text0[0]
        name = name.rstrip()
        name = name.lstrip()
        name = name.replace("8", "B")
        name = name.replace("0", "D")
        name = name.replace("6", "G")
        name = name.replace("1", "I")
        name = re.sub('[^a-zA-Z] +', ' ', name)

        # Cleaning Father's name
        fname = text0[1]
        fname = fname.rstrip()
        fname = fname.lstrip()
        fname = fname.replace("8", "S")
        fname = fname.replace("0", "O")
        fname = fname.replace("6", "G")
        fname = fname.replace("1", "I")
        fname = fname.replace("\"", "A")
        fname = re.sub('[^a-zA-Z] +', ' ', fname)

        # Cleaning DOB
        dob = text0[2]
        dob = dob.rstrip()
        dob = dob.lstrip()
        dob = dob.replace('l', '/')
        dob = dob.replace('L', '/')
        dob = dob.replace('I', '/')
        dob = dob.replace('i', '/')
        dob = dob.replace('|', '/')
        dob = dob.replace('\"', '/1')
        dob = dob.replace(" ", "")

        # Cleaning PAN Card details
        text0 = findword(text1, '(Pormanam|Number|umber|Account|ccount|count|Permanent|ermanent|manent|wumm)$')
        panline = text0[0]
        pan = panline.rstrip()
        pan = pan.lstrip()
        pan = pan.replace(" ", "")
        pan = pan.replace("\"", "")
        pan = pan.replace(";", "")
        pan = pan.replace("%", "L")

    except:
        pass 

    # Making tuples of data
    data = {}
    data['Name'] = name
    data['Father Name'] = fname
    data['Date of Birth'] = dob
    data['PAN'] = pan

    
    # Writing data into JSON
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    # Write JSON file
    with io.open('data.json', 'w', encoding='utf-8') as outfile:
        str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('data.json', encoding = 'utf-8') as data_file:
        data_loaded = json.load(data_file)

    # print(data == data_loaded)

    # Reading data back JSON(give correct path where JSON is stored)
    with open('data.json', 'r', encoding= 'utf-8') as f:
        ndata = json.load(f)
    

    t = (f"Name: {data['Name']}\n"
     f"Father's Name: {data['Father Name']}\n"
     f"Dat of Birth: {data['Date of Birth']}\n"
     f"PAN number: {data['PAN']}\n")

    return t
'''
#print(ocr('images/ocr_example_1.png'))