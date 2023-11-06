import cv2
import pandas as pd
import random
import numpy as np
import sys
import math
import matplotlib.pyplot as plt


# used for making a histogram to display where cozmo thinks he is
def makeHistogram():
    df = pd.read_csv("/Users/Veysel Guney Yilmaz/Desktop/Cozmo/Former Group/data.csv")
    pano = cv2.imread("/Users/Veysel Guney Yilmaz/Desktop/Cozmo/Former Group/Panorama.jpeg")
    dimensions = pano.shape
    width = dimensions[1]
    a = df['X']

    fig = plt.hist(a, range=[0, width], bins=width)
    plt.title('Robot')
    plt.savefig("hist.png")


#makeHistogram()