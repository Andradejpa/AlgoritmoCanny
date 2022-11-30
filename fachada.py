import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Importando a Imagem
imagem = cv.imread('IMG_0455.jpg',0)

#Executando Algoritmo Canny com precisão de (100,200)
edges = cv.Canny(imagem,100,200)

plt.subplot(121),plt.imshow(imagem,cmap = 'gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])

cv.imwrite('imagem_original_0455.jpg',imagem)
plt.subplot(122),plt.imshow(edges,cmap = 'gray')

plt.title('Detecção de Borda Canny'), plt.xticks([]), plt.yticks([])
cv.imwrite('imagem_comCannyEdge_0455.jpg',edges)
