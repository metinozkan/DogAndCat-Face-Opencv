import cv2


img=cv2.imread('picture.jpg')#picture path


yuz_cascade=cv2.CascadeClassifier('dog_face.xml')#used haarcascade Classifier
kedi_cascade=cv2.CascadeClassifier('haarcascade_frontalcatface.xml path')#used haarcascade Classifier



griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#Picture conversion gray tone with haarcascade
it = yuz_cascade.detectMultiScale(griton,1.1,4)#search for the object you want in photos
kedi=kedi_cascade.detectMultiScale(griton,1.1,4)
kopeksay=0#increases the number of found objects
kedisay=0

#objects in the rectangle
for (x, y, w, h) in it:
    cv2.rectangle(img, (x, y), (x + w,y + h), (0, 255, 0), 3)
    kopeksay=kopeksay+1
for (x, y, w, h) in kedi:
    cv2.rectangle(img, (x, y), (x + w,y + h), (0, 10, 0), 3)
    kedisay=kedisay+1


print("kopek->",kopeksay)#number of found objects
print("kedi-->",kedisay)
cv2.imshow('yuzler', img)

cv2.waitKey(0)
cv2.destroyAllWindows()