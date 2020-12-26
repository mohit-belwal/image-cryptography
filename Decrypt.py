from PIL import Image


def decryptRSA(output, n, d):
    message = ''

    for i in output:
        message+= chr(pow(int(i, 2), d)%n)              # converting to string 

    return message                                      # returning decrypted message

def decode(image):
    p = list(image.getdata())                           # getting pixel values of encoded image as list
    output = []                                         # to store binary values of decoded numbers

    for i in range(len(p)):
        a = False                                       # end of message is False

        temp = ''                                       # to store a binary number

        for j in range(9):
            t = p[(i*9+j)//3][j%3]
            
            if j == 8 and t%2 == 0:
                a = True   
                break                                   # end of message

            elif j!=8:
                if t%2:
                    temp += '1'
                else:
                    temp += '0'

        output.append(temp)

        if a:
            break

    return output                                       # returning list of binary numbers


def main():
    s = input("Enter png image name(with extension) to be decoded: ")
    image = Image.open(s)

    output = decode(image)                              # decoding from image (Steganography)

    n, d = map(int, input("Enter your private key: ").split())
    message = decryptRSA(output, n, d)                  # decrypting with RSA

    print("Encrypted message is: " + message)

if __name__ == '__main__':
    main()
