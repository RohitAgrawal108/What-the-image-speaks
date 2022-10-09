from tokenize import String
import matplotlib.pyplot as plt
import cv2
import easyocr

from DataPreprocessing import DataPProcess
# from pylab import rcParams
# from IPython.display import Image

reader = easyocr.Reader(['en'])

def main(img):
    output_list = reader.readtext(img)
    output_text = ""
    for i in output_list:
        output_text = output_text +" "+ i[1]
    text = DataPProcess(output_text)
    print(text)


main("test01.png")
