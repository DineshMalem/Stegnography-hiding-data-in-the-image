import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.jpg")

# Character-to-byte reverse mapping
c = {i: chr(i) for i in range(255)}

# Get decryption password
password = input("Enter the passcode for decryption: ")

# Original password used for encryption (Assuming the same is used)
original_password = input("Re-enter the passcode used in encryption: ")

# Check password
if password == original_password:
    message = ""
    n, m, z = 0, 0, 0

    while True:
        try:
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        except:
            break  # Stop if we reach the end of the encrypted data

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
