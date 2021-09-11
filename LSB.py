from PIL import Image

# encrypt img2 into img1
def encrypt(img1,img2):
    map1 = img1.load()
    map2 = img2.load()
    img3 = Image.new(img1.mode, img1.size)
    map3 = img3.load()
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r,g,b = map1[i, j]
            r1,g1,b1 = ('{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b))
            r,g,b = map2[i,j]
            r2,g2,b2 = ('{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b))
            r3,g3,b3 = (r1[:4] + r2[:4],g1[:4] + g2[:4],b1[:4] + b2[:4])
            map3[i, j] = (int(r3,2),int(g3,2),int(b3,2))
    return img3

# decrypt
def decrypt(img3):
    map3 = img3.load()
    img4 = Image.new(img3.mode, img3.size)
    map4 = img4.load()
    for i in range(img3.size[0]):
        for j in range(img3.size[1]):
            r,g,b = map3[i, j]
            r3,g3,b3 = ('{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b))
            r4,g4,b4 = (r3[4:] + '0000',g3[4:] + '0000',b3[4:] + '0000')
            map4[i, j] = (int(r4,2),int(g4,2),int(b4,2))
    return img4
'''
# test
img1 = Image.open('../input/3.jpg')
img2 = Image.open('../input/4.jpg')
img3 = encrypt(img1,img2)
img3.show()
img4 = decrypt(img3)
img4.show()
'''
