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


#mapy = ['Wroclaw.png','Krakow.png','Warszawa.png']


i = 28
i = 0


Kroki = True

miasta = []
zielonosc = []
ilosc_pikseli_zielonych = []
x = []
y = []
ilosc_pikseli_rzeki = []
zielonosc_po_closing = []
zielonosc_po_opening = []


#zmienne
R = 170
G = 218
B = 255

Hue_limit_dolny = 30
Hue_limit_gorny = 80
Saturation_limit_dolny = 50
Saturation_limit_gorny = 255
Value_limit_dolny = 50
Value_limit_gorny = 255


n = 4 #opening
m = 4 #closing

Prefix_plikow = ""

for i in range(len(mapy)):
    print(mapy[i])
    miasto = mapy[i][0:-4]
    
    mapa = cv2.imread(os.getcwd() + '\\mapy\\' + mapy[i])
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 01 BGR.jpg' , mapa) 
    #plt.imshow(mapa)
    
    mapa_RGB = cv2.cvtColor(mapa, cv2.COLOR_BGR2RGB)
    #plt.imshow(mapa_RGB)
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 02 RGB.jpg', mapa_RGB) 
    

    
    #Wybranie jedynie rzeki
    rzeka = cv2.inRange(mapa_RGB, (R - 1, G - 1, B - 1), (R + 1, G + 1, B + 1))
    
    #print(np.sum(rzeka))
    #zmianna na True - False
    rzeka_TF = rzeka>0
    #print(np.sum(rzeka_TF))
    #jaki procent w miecie to ryeka
    #np.sum(rzeka_TF) / (rzeka.shape[0] * rzeka.shape[1])

    #zmiana koloru na czarny w tym gdzie jest rzeka
    mapa_final = np.copy(mapa)
    mapa_final[rzeka_TF] = 0
    #plt.imshow(mapa_final)
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 03 bez rzeki.jpg' , mapa_final) 

    #wxzytanie saletlity
    satelita = cv2.imread(os.getcwd() + '\\mapy satelity\\'  + mapy[i])
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 04 satelita.jpg' , satelita) 
    
    satelita_RGB = cv2.cvtColor(satelita, cv2.COLOR_BGR2RGB)
    #plt.imshow(satelita_RGB)
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 05 satelita RGB.jpg' , satelita_RGB) 
    
    satelita_hsv = cv2.cvtColor(satelita_RGB, cv2.COLOR_RGB2HSV)
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 06 satelita hsv.jpg' , satelita_hsv) 
    
    #usunięcie rzeki
    satelita_hsv[rzeka_TF] = 0
    satelita_RGB_1 = np.copy(satelita_RGB)
    satelita_RGB_1[rzeka_TF] = 0
    #plt.imshow(satelita_hsv)
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 07 satelita bez rzeki.jpg', satelita_hsv) 
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 08 satelita bez rzeki.jpg', satelita_RGB_1) 
    
    #Wybranie jedynie zielonych
    mask = cv2.inRange(satelita_hsv, (Hue_limit_dolny, Saturation_limit_dolny, Value_limit_dolny), (Hue_limit_gorny, Saturation_limit_gorny, Value_limit_gorny))

    
    #zmianna na True - False
    mask_TF = mask>0
    #print(np.sum(mask_TF))

    
    #zmiana koloru na czarny w tym gdzie nie było zielone
    satelita_RGB_2 = np.copy(satelita_RGB)
    satelita_RGB_2[~mask_TF] = 0
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 09 satelita zielone.jpg' , satelita_RGB_2) 
    #plt.imshow(satelita_RGB_2)
    
    
    
    #wygładzenie - closing
    kernel_closing = np.ones((n,n),np.uint8)
    mask_closing = np.copy(mask)
    closing = cv2.morphologyEx(mask_closing, cv2.MORPH_CLOSE, kernel_closing)
    
    closing_TF = closing > 0 
    satelita_RGB_3 = np.copy(satelita_RGB_1)
    satelita_RGB_3[~closing_TF] = 0
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 10 closing.jpg', satelita_RGB_3) 
    #plt.imshow(satelita_RGB_3)
    
    
    kernel_opening = np.ones((m,m), np.uint8)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel_opening)
    
    
    opening_TF = opening > 0 
    satelita_RGB_4 = np.copy(satelita_RGB_1)
    satelita_RGB_4[~opening_TF] = 0
    if Kroki:
        cv2.imwrite(os.getcwd() +'\\kroki\\' + Prefix_plikow +  miasto + ' 11 po operacjach morfologicznych.jpg', satelita_RGB_4) 
    #plt.imshow(satelita_RGB_3)
    
    #tmp = satelita_RGB_4 == satelita_RGB_2
    #tmp.all()


    cv2.imwrite(os.getcwd() +'\\final\\' +  miasto + '.jpg' , satelita_RGB_3) 

    #jaki procent w miecie to zieleń w miecie bez rzeki i inne dane 
    miasta.append(miasto)
    ilosc_pikseli_zielonych.append(np.sum(opening_TF))
    x.append(opening.shape[0])
    y.append(opening.shape[1])
    ilosc_pikseli_rzeki.append(np.sum(rzeka_TF))
    zielonosc_po_closing.append(np.sum(closing_TF))
    zielonosc_po_opening.append(np.sum(opening_TF))
    
    zielonosc.append(np.sum(opening_TF) / (opening.shape[0] * opening.shape[1] - np.sum(rzeka_TF)))
    print(zielonosc[i])
    
    #    print(str(n) + "-" + str(m) + ": " + str(np.sum(opening) / (opening.shape[0] * opening.shape[1])))

end = pd.DataFrame(list(zip(miasta, zielonosc, ilosc_pikseli_zielonych, x, y, ilosc_pikseli_rzeki, zielonosc_po_closing, zielonosc_po_opening)), 
               columns = ['miasto', 'zielonosc', 'ilosc_pikseli_zielonych', 'x', 'y', 'ilosc_pikseli_rzeki', 'zielonosc_po_closing', 'zielonosc_po_opening'])
print(end)   

end.to_csv(os.getcwd() + '\\'  + Prefix_plikow + 'wynik.csv')