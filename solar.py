import cv2

img= cv2.imread('solar-system.jpg')
solar=img[120:360,380:480]
#img[120:360,500:600]=solar
text='Sun'
cv2.putText(img,text,(20,300),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Mercury'
cv2.putText(img,text,(120,300),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='venus'
cv2.putText(img,text,(160,180),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Earth'
cv2.putText(img,text,(275,250),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Mars'
cv2.putText(img,text,(370,280),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Jupiter'
cv2.putText(img,text,(490,360),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Saturn'
cv2.putText(img,text,(720,350),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Uranus'
cv2.putText(img,text,(950,280),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
text='Septune'
cv2.putText(img,text,(1070,280),fontScale=1,color=(255,255,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
#print(img)
cv2.imshow('output',img)
cv2.waitKey(0)