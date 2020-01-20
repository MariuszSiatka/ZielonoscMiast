import cv2
import os
from matplotlib import pyplot as plt
import pandas as pd
os.environ["PROJ_LIB"] = r'D:\Anaconda_Python\Library\share'
from mpl_toolkits.basemap import Basemap
import numpy as np

os.chdir('D:\KK\OneDrive\Wroclaw w Liczbach\Gotowe projekty\\20191219 zielone miasta')
print(os.getcwd())



Kroki = True

miasta = []
zielonosc = []
ilosc_pikseli_zielonych = []
x = []
y = []
ilosc_pikseli_rzeki = []
zielonosc_po_closing = []
zielonosc_po_opening = []

Hue_limit_dolny = 30
Hue_limit_gorny = 80
Saturation_limit_dolny = 50
Saturation_limit_gorny = 255
Value_limit_dolny = 50
Value_limit_gorny = 255

#zmienne
R = 0
G = 0
B = 0

n = 4 #opening
m = 4 #closing

Prefix_plikow = ""


#wxzytanie saletlity
mapa = cv2.imread(os.getcwd() + '\Wroclaw - plac spoleczny.jpg')
if Kroki:
    cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\' + Prefix_plikow  + ' 04 satelita.jpg' , mapa) 

satelita_RGB = cv2.cvtColor(mapa, cv2.COLOR_BGR2RGB)
#plt.imshow(satelita_RGB)
if Kroki:
    cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\' + Prefix_plikow  + ' 05 satelita RGB.jpg' , satelita_RGB) 


#### Wczytanie ile pikseli ma plac spoleczny
#Wybranie jedynie rzeki
pl_spoleczny = cv2.inRange(satelita_RGB, (R - 1, G - 1, B - 1), (R + 1, G + 1, B + 1))

#print(np.sum(rzeka))
#zmianna na True - False
pl_spoleczny_TF = pl_spoleczny>0
print(np.sum(pl_spoleczny_TF))
#ile pikseli plac spoleczny
wielkosc_pl_spolecznego = (pl_spoleczny_TF.shape[0] * pl_spoleczny_TF.shape[1]) - np.sum(pl_spoleczny_TF)  





#### Sprawdzenie ile już jest zielonosci
satelita_hsv = cv2.cvtColor(satelita_RGB, cv2.COLOR_RGB2HSV)
if Kroki:
    cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\' + Prefix_plikow + ' 06 satelita hsv.jpg' , satelita_hsv) 

#Wybranie jedynie zielonych
mask = cv2.inRange(satelita_hsv, (Hue_limit_dolny, Saturation_limit_dolny, Value_limit_dolny), (Hue_limit_gorny, Saturation_limit_gorny, Value_limit_gorny))


#zmianna na True - False
mask_TF = mask>0
#print(np.sum(mask_TF))


#zmiana koloru na czarny w tym gdzie nie było zielone
satelita_RGB_2 = np.copy(satelita_RGB)
satelita_RGB_2[~mask_TF] = 0
if Kroki:
    cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\' + Prefix_plikow + ' 09 satelita zielone.jpg' , satelita_RGB_2) 
#plt.imshow(satelita_RGB_2)



#wygładzenie - closing
kernel_closing = np.ones((n,n),np.uint8)
mask_closing = np.copy(mask)
closing = cv2.morphologyEx(mask_closing, cv2.MORPH_CLOSE, kernel_closing)

closing_TF = closing > 0 
satelita_RGB_3 = np.copy(satelita_RGB)
satelita_RGB_3[~closing_TF] = 0
if Kroki:
    cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\' + Prefix_plikow + ' 10 closing.jpg', satelita_RGB_3) 
#plt.imshow(satelita_RGB_3)


kernel_opening = np.ones((m,m), np.uint8)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel_opening)


opening_TF = opening > 0 
satelita_RGB_4 = np.copy(satelita_RGB)
satelita_RGB_4[~opening_TF] = 0
if Kroki:
    cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\' + Prefix_plikow + ' 11 po operacjach morfologicznych.jpg', satelita_RGB_4) 
#plt.imshow(satelita_RGB_3)

#tmp = satelita_RGB_4 == satelita_RGB_2
#tmp.all()


cv2.imwrite(os.getcwd() +'\\PL Spoleczny\\'  + '12 final.jpg' , satelita_RGB_3) 

#jaki procent w miecie to zieleń w miecie bez rzeki i inne dane 
ilosc_pikseli_zielonych = np.sum(opening_TF)
ilosc_pikseli_drogowych = wielkosc_pl_spolecznego - ilosc_pikseli_zielonych

Surplus_parku_spolecznego = ilosc_pikseli_drogowych / (pl_spoleczny_TF.shape[0] * pl_spoleczny_TF.shape[1]) 
