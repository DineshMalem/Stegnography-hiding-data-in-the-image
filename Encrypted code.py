import cv2
import os

# Load image
img = cv2.imread("C:/Users/dines/Downloads/flower.jpg")

# Get user inputs
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Character-to-byte mapping
d = {chr(i): i for i in range(255)}

n, m, z = 0, 0, 0

# Encrypt message into image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Message encrypted successfully in 'encryptedImage.jpg'.")

# Open the encrypted image (Windows)
os.system("start encryptedImage.jpg")
