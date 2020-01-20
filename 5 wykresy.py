import pandas as pd
import os
import cv2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

from matplotlib.ticker import PercentFormatter


os.chdir('D:\KK\OneDrive\Wroclaw w Liczbach\Gotowe projekty\\20191219 zielone miasta')
os.getcwd()

zielonosc = pd.read_csv(os.getcwd() + '\\wynik.csv').iloc[:, 1:9]

zielonosc_PL = zielonosc.loc[zielonosc['miasto'].isin([
        'Wroclaw','Bialystok','Gdansk','Gdynia','Krakow','Lodz','Poznan','Warszawa','Szczecin'])]

Polskie_nazwy = {'Wroclaw'  : 'Wrocław',
                 'Bialystok': 'Białystok',
                 'Gdansk'   : 'Gdańsk',
                 'Gdynia'   : 'Gdynia',
                 'Krakow'   : 'Kraków',
                 'Lodz'     : 'Łódź',
                 'Poznan'   : 'Poznań',
                 'Warszawa' : 'Warszawa',
                 'Szczecin' : 'Szczecin'}

Polskie_nazwy["Lodz"]

zielonosc_PL_sort = zielonosc_PL.sort_values('zielonosc', ascending=False)


################3
#wzkres 9 map

mapy_zielonosc = []

mapy = os.listdir(os.getcwd() + '\\mapy' )
for i in range(0, 10):
    print(i)    
    tmp = cv2.imread(os.getcwd() + '\\final\\' + zielonosc_PL_sort['miasto'].iloc[i] + '.png')
    mapy_zielonosc.append(tmp)
        
len(mapy_zielonosc)
    



f, axarr = plt.subplots(3,3, figsize=(6,6))
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'

# add an horizonal label for the y axis 
f.text(0, 1, 'Mapy satelitarne wybranych miast\nz zaznaczonymi obszarami zielonymi', 
         fontsize=15, fontweight='black', color = '#333F4B')

for i in range(1,4):
    for j in range(1,4):
        print('i: ' + str(i) + ' j: ' + str(j) + ' - ' + zielonosc_PL_sort['miasto'].iloc[(i * 3 - 3 + j - 1)])
        axarr[i - 1, j - 1].imshow(mapy_zielonosc[(i * 3 - 3 + j - 1)])
        axarr[i - 1, j - 1].set_axis_off()
        axarr[i - 1, j - 1].axis("tight")  # gets rid of white border
        axarr[i - 1, j - 1].axis("image") # square up the image instead of filling the "figure" space
        title = str(Polskie_nazwy[zielonosc_PL_sort['miasto'].iloc[(i * 3 - 3 + j - 1)]]) + " - " + str("{0:.0%}".format(zielonosc_PL_sort['zielonosc'].iloc[(i * 3 - 3 + j - 1)]))
        axarr[i - 1, j - 1].set_title(title)
        axarr[i - 1, j - 1].set_facecolor('b')
        

#plt.suptitle('Zieleń w miastach Polski',  fontsize=16)   #verticalalignment='bottom', 
plt.tight_layout()        
#plt.set_facecolor('b')

plt.savefig(os.getcwd() + '\\wykresy\\' +'9 map zielonosci.png')








################3
#wzkres kroki pryejscia

kroki = os.listdir(os.getcwd() + '\\Kroki')
kroki_2 = list(filter(lambda x: 'Wroclaw' in x, kroki)) 
kroki_3 = [kroki_2[i] for i in [1, 3, 7, 8, 9, 10]]



Kroki = []

for i in range(0, 7):
    print(i)
    tmp = cv2.imread(os.getcwd() + '\\kroki\\' + kroki_3[i])

    Kroki.append(tmp)
        
len(Kroki)
    

f, axarr = plt.subplots(2,3, figsize=(7.5,5))
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'

# add an horizonal label for the y axis 
f.text(0, 1, 'Kroki analizy', 
         fontsize=15, fontweight='black', color = '#333F4B')

for i in range(1,3):
    for j in range(1,4):
        print('i: ' + str(i) + ' j: ' + str(j) + ' - ' + kroki_3[i * 3 - 3 - 1 + j ])
        axarr[i - 1, j - 1].imshow(Kroki[(i * 3 - 3 + j - 1)])
        axarr[i - 1, j - 1].set_axis_off()
        axarr[i - 1, j - 1].axis("tight")  # gets rid of white border
        axarr[i - 1, j - 1].axis("image") # square up the image instead of filling the "figure" space
        #title = str(zielonosc_PL_sort['miasto'].iloc[(i * 3 - 3 + j - 1)]) + " - " + str("{0:.0%}".format(zielonosc_PL_sort['zielonosc'].iloc[(i * 3 - 3 + j - 1)]))
        #axarr[i - 1, j - 1].set_title(title)
        axarr[i - 1, j - 1].set_facecolor('b')
        

#plt.suptitle('Zieleń w miastach Polski',  fontsize=16)   #verticalalignment='bottom', 
plt.tight_layout()        
#plt.set_facecolor('b')

plt.savefig(os.getcwd() + '\\wykresy\\' +'kroki.png')


