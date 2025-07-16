import cv2
import os

# Load the image
img = cv2.imread("mypic.png")

# Check if the image loaded properly
if img is None:
    print("❌ Error: Image not found. Make sure 'mypic.jpg' is in the same folder.")
    exit()

# Get the dimensions of the image
rows, cols, _ = img.shape
capacity = rows * cols * 3

# Get the message and password from user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Check if the message fits in the image
if len(msg) > capacity:
    print("❌ Message too long for this image. Use a bigger image or shorter message.")
    exit()

# Create dictionaries for encoding/decoding characters
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Encode the message
index = 0
for char in msg:
    row = index // cols
    col = index % cols
    channel = index % 3
    img[row, col, channel] = d[char]
    index += 1

# Save and show the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")

# Decryption process
pas = input("Enter passcode for decryption: ")

if pas == password:
    decoded = ""
    index = 0
    for _ in range(len(msg)):
        row = index // cols
        col = index % cols
        channel = index % 3
        decoded += c[img[row, col, channel]]
        index += 1
    print("✅ Decrypted Message:", decoded)
else:
    print("❌ Incorrect password. Access denied.")
