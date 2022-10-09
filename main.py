from tokenize import String
import matplotlib.pyplot as plt
import cv2
import easyocr
from Cohereinpython import identify
from DataPreprocessing import DataPProcess
import os



reader = easyocr.Reader(['en'])

def main(img):
    output_list = reader.readtext(img)
    output_text = ""
    for i in output_list:
        output_text = output_text +" "+ i[1]
    text = DataPProcess(output_text)
    result_lable,result_confidence = identify(text)
    os.system('cls')
    print(f"Content: {text}")
    print(f"Category: {result_lable}")


main("test01.png")
