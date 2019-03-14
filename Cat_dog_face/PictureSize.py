import PIL
from PIL import Image

sayi = 1


def Olcek():

    for i in range(1, 263):
        resim_dosya_adi = "C:/Users/asd/Desktop/Pitbull/p/" + str(i) + ".jpg"

        resim = Image.open(resim_dosya_adi)

        # Yeniden Boyutlandir
        resim = resim.resize((150, 150), PIL.Image.ANTIALIAS)

        # Yeniden Boyutlandirilmis Resmi Kaydet
        resim.save("C:/Users/asd/Desktop/Pitbull/p/" + str(i) + ".jpg")


Olcek()
