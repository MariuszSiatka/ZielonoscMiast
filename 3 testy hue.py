import cv2
import os
from matplotlib import pyplot as plt
import pandas as pd
os.environ["PROJ_LIB"] = r'D:\Anaconda_Python\Library\share'
from mpl_toolkits.basemap import Basemap
import numpy as np

os.chdir('D:\KK\OneDrive\Wroclaw w Liczbach\Gotowe projekty\\20191219 zielone miasta')
print(os.getcwd())

# wybrane zostyało Closing 3 - opening 3



########################################
#sprawdzenie ile zajmuje rzeka

mapy = os.listdir(os.getcwd() + '\\mapy' )


mapy = 'Poznan.png'


Kroki = True

miasta = []
zielonosc = []
ilosc_pikseli_zielonych = []
x = []
y = []
ilosc_pikseli_rzeki = []
zielonosc_po_closing = []
zielonosc_po_opening = []




print(mapy)
miasto = mapy[0:-4]

mapa = cv2.imread(os.getcwd() + '\\mapy\\' + mapy)


mapa_RGB = cv2.cvtColor(mapa, cv2.COLOR_BGR2RGB)


R = 170
G = 218
B = 255

#Wybranie jedynie rzeki
rzeka = cv2.inRange(mapa_RGB, (R - 1, G - 1, B - 1), (R + 1, G + 1, B + 1))

#zmianna na True - False
rzeka_TF = rzeka>0

#zmiana koloru na czarny w tym gdzie jest rzeka
mapa_final = np.copy(mapa)
mapa_final[rzeka_TF] = 0

#wxzytanie saletlity
satelita = cv2.imread(os.getcwd() + '\\mapy satelity\\'  + mapy)

satelita_RGB = cv2.cvtColor(satelita, cv2.COLOR_BGR2RGB)

satelita_hsv = cv2.cvtColor(satelita_RGB, cv2.COLOR_RGB2HSV)

#usunięcie rzeki
satelita_hsv[rzeka_TF] = 0
satelita_RGB_1 = np.copy(satelita_RGB)
satelita_RGB_1[rzeka_TF] = 0
#plt.imshow(satelita_hsv)


for i in range(30,51,5):
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki testy\\h - ' + str(i) + " - " +  miasto + ' 08 satelita bez rzeki.jpg', satelita_RGB_1) 

    #Wybranie jedynie zielonych
    mask = cv2.inRange(satelita_hsv, (i, 0, 0), (80, 255,255))

    
    #zmianna na True - False
    mask_TF = mask>0
    #print(np.sum(mask_TF))

    
    #zmiana koloru na czarny w tym gdzie nie było zielone
    satelita_RGB_2 = np.copy(satelita_RGB)
    satelita_RGB_2[~mask_TF] = 0
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki testy\\h - ' + str(i) + " - " +  miasto + ' 09 satelita zielone.jpg' , satelita_RGB_2) 
    #plt.imshow(satelita_RGB_2)
    
    
    
    #wygładzenie - closing
    n = 3
    kernel_closing = np.ones((n,n),np.uint8)
    mask_closing = np.copy(mask)
    closing = cv2.morphologyEx(mask_closing, cv2.MORPH_CLOSE, kernel_closing)
    
    closing_TF = closing > 0 
    satelita_RGB_3 = np.copy(satelita_RGB_1)
    satelita_RGB_3[~closing_TF] = 0
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki testy\\h - ' + str(i) + " - " +  miasto + ' 10 closing.jpg', satelita_RGB_3) 
    #plt.imshow(satelita_RGB_3)
    
    
    m = 3
    kernel_opening = np.ones((m,m), np.uint8)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel_opening)
    
    
    opening_TF = opening > 0 
    satelita_RGB_4 = np.copy(satelita_RGB_1)
    satelita_RGB_4[~opening_TF] = 0
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki testy\\h - ' + str(i) + " - " +  miasto + ' 11 po operacjach morfologicznych.jpg', satelita_RGB_4) 
    #plt.imshow(satelita_RGB_3)
    
    #tmp = satelita_RGB_4 == satelita_RGB_2
    #tmp.all()


    #cv2.imwrite(os.getcwd() +'\\final\\' +  miasto + '.jpg' , satelita_RGB_3) 

    #jaki procent w miecie to zieleń w miecie bez rzeki i inne dane 
    miasta.append(miasto)
    ilosc_pikseli_zielonych.append(np.sum(opening_TF))
    x.append(opening.shape[0])
    y.append(opening.shape[1])
    ilosc_pikseli_rzeki.append(np.sum(rzeka_TF))
    zielonosc_po_closing.append(np.sum(closing_TF))
    zielonosc_po_opening.append(np.sum(opening_TF))
    
    zielonosc.append(np.sum(opening_TF) / (opening.shape[0] * opening.shape[1] - np.sum(rzeka_TF)))
    #print(str(i) + " " + zielonosc[i])

 