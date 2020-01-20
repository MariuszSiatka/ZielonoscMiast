import cv2
import os
from matplotlib import pyplot as plt
import pandas as pd
os.environ["PROJ_LIB"] = r'D:\Anaconda_Python\Library\share'
from mpl_toolkits.basemap import Basemap
import numpy as np

os.chdir('D:\KK\OneDrive\Wroclaw w Liczbach\Gotowe projekty\\20191219 zielone miasta')
print(os.getcwd())

os.listdir(os.getcwd() + '\\mapy satelity')

#Wczytanie pliku
wawa = cv2.imread(os.getcwd() + '\\mapy satelity\\Warszawa.png')

#wywietlenie mapy
#%matplotlib inline
plt.figure(figsize = (20,20))
plt.imshow(wawa)

#Zmiana formatu zdjęć na RGB a póćniej HSV
wawa2 = cv2.cvtColor(wawa, cv2.COLOR_BGR2RGB)
plt.imshow(wawa2)
#cv2.imwrite(os.getcwd() + '\\Warszawa2.jpg', wawa2) 

wawa_hsv = cv2.cvtColor(wawa2, cv2.COLOR_RGB2HSV)
#cv2.imwrite(os.getcwd() + '\\Warszawa_hsv.jpg', wawa_hsv) 
#plt.imshow(wawa2)

#wybranie jedynie pierwszego kanału mówiącego o kolorze
#wawa_hsv[:,:,0]

#Histogram jakie są kolory
#plt.hist(wawa_hsv[:,:,0], bins = [0,20,40,60,80,100, 120, 140, 160])

#Wybranie jedynie zielonych
mask = cv2.inRange(wawa_hsv, (40, 0, 0), (80, 255,255))
print(np.sum(mask))
#zmianna na True - False
mask_TF = mask>0
print(np.sum(mask_TF))

#jaki procent w miecie to zieleń
np.sum(mask_TF) / (mask_TF.shape[0] * mask_TF.shape[1])

#zmiana koloru na czarny w tym gdzie nie było zielone
wawa3 = np.copy(wawa2)
wawa3[~mask_TF] = 0
#plt.imshow(wawa3)
#cv2.imwrite(os.getcwd() + '\\Warszawa3.jpg', wawa3) 

#cv2.imwrite(os.getcwd() + '\\testy opening\\Warszawa.jpg', wawa3) 

n = 1

for n in range(10):
    #wygładzenie - opening
    kernel = np.ones((n,n),np.uint8)
    mask1 = mask
    opening = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    #plt.imshow(opening)
    
    opening = opening > 0 
    wawa4 = np.copy(wawa2)
    wawa4[~opening] = 0
    #plt.figure(figsize = (20,20))
    #plt.title(str(n) + ": " + str(np.sum(opening) / (opening.shape[0] * opening.shape[1])))
    #plt.imshow(wawa4)
    
    print(str(n) + ": " + str(np.sum(opening) / (opening.shape[0] * opening.shape[1])))
    cv2.imwrite(os.getcwd() + '\\testy opening\\Warszawa 0' + str(n) + '.jpg', wawa4) 
    
n = 100    
for n in range(10):
    #wygładzenie - opening
    kernel = np.ones((n,n), np.uint8)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #plt.imshow(closing)
    
    closing = closing > 0 
    wawa5 = np.copy(wawa2)
    wawa5[~closing] = 0
    print(str(n) + ": closing - " + str(np.sum(closing)) +" | suma pikseli - " + str(np.sum(wawa5)))


    #cv2.imwrite(os.getcwd() + '\\Warszawa2.jpg', wawa2) 
    #cv2.imwrite(os.getcwd() + '\\Warszawa5.jpg', wawa5) 
    

    
    #print(np.sum(wawa5) / np.sum(wawa2))
    #plt.figure(figsize = (20,20))
    #plt.imshow(wawa4)
    
    #print(str(n) + ": " + str(np.sum(closing) / (closing.shape[0] * closing.shape[1])))
    
    cv2.imwrite(os.getcwd() + '\\testy closing\\Warszawa 0' + str(n) + '.jpg', wawa5) 
    
    
    ##########################
#testy test - opening - closing
n =1    
for n in range(10):
    #wygładzenie - opening
    kernel = np.ones((n,n),np.uint8)
    mask1 = np.copy(mask)
    opening = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    #plt.imshow(opening)
    
    #opening = opening > 0 
    #wawa4 = np.copy(wawa2)
    #wawa4[~opening] = 0
    #plt.figure(figsize = (20,20))
    #plt.title(str(n) + ": " + str(np.sum(opening) / (opening.shape[0] * opening.shape[1])))
    #plt.imshow(wawa4)
    
    #print(str(n) + ": " + str(np.sum(opening) / (opening.shape[0] * opening.shape[1])))
    #cv2.imwrite(os.getcwd() + '\\testy opening\\Warszawa ' + str(n) + '.jpg', wawa4) 
    
    for m in range(10):
        #wygładzenie - opening
        kernel = np.ones((m,m), np.uint8)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        
        closing = closing > 0 
        wawa5 = np.copy(wawa2)
        wawa5[~closing] = 0
        cv2.imwrite(os.getcwd() + 
                    '\\test - opening - closing v2\\Warszawa - ' + 
                    'opening 0' + str(n) + 
                    '- closing 0' + str(m) + 
                    '.jpg', wawa5) 
        print(str(n) + "-" + str(m) + ": " + str(np.sum(closing) / (closing.shape[0] * closing.shape[1])))




    ##########################
#testy test  - closing - opening
n =1    
for n in range(10):
    #wygładzenie - opening
    kernel = np.ones((n,n),np.uint8)
    mask1 = np.copy(mask)
    closing = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)


    for m in range(10):
        #wygładzenie - opening
        kernel = np.ones((m,m), np.uint8)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
        
        opening = opening > 0 
        wawa5 = np.copy(wawa2)
        wawa5[~opening] = 0
        cv2.imwrite(os.getcwd() + 
                    '\\test - closing - opening v2\\Warszawa - ' + 
                    'closing 0' + str(n) + 
                    '- opening 0' + str(m) + 
                    '.jpg', wawa5) 
        print(str(n) + "-" + str(m) + ": " + str(np.sum(opening) / (opening.shape[0] * opening.shape[1])))





#################################################################
        # zmiana ilosci kolorów na obrazku
import numpy as np
import cv2

m = 5
n = 5

img = cv2.imread(os.getcwd() + '\\test - opening - closing\\Warszawa - ' + 'opening 0'   + str(m) + '- closing 0' + str(n) +'.jpg')

img = cv2.imread(os.getcwd() + '\\mapy satelity\\Warszawa.png')
Z = img.reshape((-1,3))
#Z.head()

for n in range(1, 21):
    # convert to np.float32
    Z = np.float32(Z)
    
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    K = n
    print(K)
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    
    #cv2.imshow('res2',res2)
    cv2.imwrite(os.getcwd() + '\\k means\\Warszawa ' + str(n) + ' k-means.jpg', res2) 

cv2.waitKey(0)
cv2.destroyAllWindows()

############################3
#sredni kolor miasta RGB
mapy = os.listdir(os.getcwd() + '\\mapy satelity' )

i = 1
for i in range(len(mapy)):
    print(mapy[i])
    
    mapa = cv2.imread(os.getcwd() + '\\mapy satelity\\' + mapy[i])
    Z = mapa.reshape((-1,3))
    Z = np.float32(Z)
    
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    K = 1
    
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    
    #cv2.imshow('res2',res2)
    cv2.imwrite(os.getcwd() + '\\sredni kolor miasta\\' + mapy[i] + '.jpg', res2) 



############################3
#sredni kolor miasta HSV _ kanał H
mapy = os.listdir(os.getcwd() + '\\mapy satelity' )

i = 1
for i in range(len(mapy)):
    print(mapy[i])
    
    mapa = cv2.imread(os.getcwd() + '\\mapy satelity\\' + mapy[i])
    mapa_hsv = cv2.cvtColor(mapa, cv2.COLOR_RGB2HSV)
    
    sr_hsv = mapa_hsv[:,:,0].reshape((1,mapa_hsv.shape[0]  * mapa_hsv.shape[1] ))
    sr_hsv.shape
    
    sr_hsv = np.float32(sr_hsv[0])
    sr_hsv_l = sum(sr_hsv) / len(sr_hsv)
    
    mapa_hsv[:,:,0] = sr_hsv_l
    
    #cv2.imshow('res2',res2)
    cv2.imwrite(os.getcwd() + '\\sredni kolor miasta\\' + mapy[i] + '_HSV.jpg', mapa_hsv) 



