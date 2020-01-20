# https://scentellegher.github.io/visualization/2018/10/10/beautiful-bar-plots-matplotlib.html

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
import pandas as pd
import os
import cv2


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

zielonosc_PL_sort = zielonosc_PL.sort_values('zielonosc', ascending=True)
df = zielonosc_PL_sort.iloc[: , 0:2]
df = df.set_index('miasto')





plt.style.use('classic')

plt.rcParams.update(plt.rcParamsDefault)

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'

# create some fake data



# we first need a numeric placeholder for the y axis
my_range=list(range(1,len(df.index)+1))

fig, ax = plt.subplots(figsize=(5,3.5))

# create for each expense type an horizontal line that starts at x = 0 with the length 
# represented by the specific expense percentage value.

Inne    = (254 / 255 , 153 / 255 , 41 / 255) 
Wroclaw = (217 / 255 , 95 / 255 , 14 / 255)
colors  = [Inne, Inne, Wroclaw, Inne, Inne, Inne, Inne, Inne, Inne]
plt.hlines(y=my_range, xmin=0, xmax=df['zielonosc'], color=colors, alpha=0.5, linewidth=5)

# create for each expense type a dot at the level of the expense percentage value
plt.plot(df['zielonosc'], my_range, "o", markersize=5, color='#993404', alpha = 0.8)

# set labels
ax.set_xlabel('Procent zajmowanej przez zieleń powierzchni miasta', 
              fontsize=12, color = '#333F4B')
ax.set_ylabel('')

# add an horizonal label for the y axis 
fig.text(0, 0.96, 'Zieloność Polskich miast', fontsize=15, fontweight='black', color = '#333F4B')

# set axis
ax.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(my_range, df.index)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)

plt.gca().xaxis.set_major_formatter(PercentFormatter(1))

# set the spines position
ax.spines['bottom'].set_position(('axes', -0.04))
ax.spines['left'].set_position(('axes', 0.015))

plt.savefig('wykresy liniowy.png', dpi=300, bbox_inches='tight')