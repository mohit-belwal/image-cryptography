from PIL import Image


def encryptRSA(msg, n, e):
    data = []

    for i in msg:
        data.append(format(pow(ord(i), e)%n, '08b'))    # converting from ((chr to ascii) to RSA encryption) to binary

    return(data)

def newpix(p, data):
    Pix = []

    for i in range(len(data)):
        t = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                Pix.append(tuple(t))                    # saving RGB value of previous pixel in tuple
                t=[]

            temp = p[(i*9+j) // 3][j % 3]               # value of ith pixel

            if j == 8:
                if i == len(data) - 1:                  # end of message
                    if temp % 2:                        # (temp%2==0)=stop reading further
                        if temp == 0:                   # if pixel value is 0, increase by 1
                            temp += 1
                        else:
                            temp -= 1
                else:
                    if temp % 2 ==0:
                        temp += 1

            else:                                       # if (temp%2==1), then keep reading
                if data[i][j] == '1':                   # if binary value=='1' then, (pixel value)%2==1
                    if temp % 2 == 0:
                        if temp:
                            temp -= 1
                        else:
                            temp += 1

                else:                                   # if data[i]==0, then (pixel value)%2==0
                    if temp % 2:
                        temp -= 1

            t.append(temp)

        Pix.append(tuple(t))

    return Pix

def encode(img, data):
    p = list(img.getdata())                             # pixel values of 'img' as a list

    Pix = newpix(p, data)                               # modified pixel values as list of tuples (of RGB values)
    (x, y) = (0, 0)                                     # coordinate to paste modified pixel

    for i in range(len(Pix)):
        img.paste(Pix[i], (x, y, x+1, y+1))             # putting modified pixels

        if(x == img.size[0]-1):                         # right-most to image
            x = 0                                       # getting back to left-most to image
            y += 1                                      # going one step downward
        else:
            x += 1                                      # to next pixel (forward)
        i += 2

    name = input("Enter png image name(with extension) for encoded image created: ")
    img.save(name)

def main():
    s = input("Enter png image name(with extension) to be encoded: ")
    image = Image.open(s)
    img = image.copy()                                  # to save original image from any modification

    msg = input("Enter the message to encrypt: ")
    n, e = map(int, input("Enter your public key (n, e): ").split())

    data = encryptRSA(msg, n, e)                        # encryption with RSA

    encode(img, data)                                   # encoding to image (Steganography)

if __name__ == '__main__':
    main()
