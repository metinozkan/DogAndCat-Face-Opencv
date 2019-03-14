import urllib.request,cv2,os,time
def n_resim():

	negatif_resimlerin_linki= 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02472987'
	negatif_resim_linki= urllib.request.urlopen(negatif_resimlerin_linki).read().decode()
	if not os.path.exists('n'):
		os.makedirs('n')
	resimNo = 410
	for i in negatif_resim_linki.split('\n'):
		try:
			print(i)
			urllib.request.urlretrieve(i, "n/"+str(resimNo)+'.jpg')
			resim = cv2.imread("n/"+str(resimNo)+'.jpg', cv2.IMREAD_GRAYSCALE)
			yenidenBoyutlandır = cv2.resize(resim,(100,100))
			cv2.imwrite("n/"+str(resimNo)+'.jpg',yenidenBoyutlandır)
			resimNo +=1
		except Exception as e:
			print(str(e))

n_resim()
