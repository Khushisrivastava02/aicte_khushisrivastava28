# 🕵️‍♂️ Image Steganography with Python

### 🔐 Hide and Reveal Secret Messages Inside Images using OpenCV

This project lets you hide (encrypt) a secret message inside an image and later reveal (decrypt) it using a password. It’s a basic terminal-based implementation for learning purposes.

## Project Structure

steganography/  
├── stego.py              # Main Python script  
├── mypic.png             # Input image used to hide the message  
├── encryptedImage.jpg    # Output image after encryption (auto-generated)  
└── README.md             # Project documentation

## Technologies Used

- Python: Programming language  
- OpenCV (cv2): Image processing  
- os module: File launching

## How to Run This Project

Step 1: Prerequisites  
Make sure Python is installed. Then open terminal and install OpenCV:  
`pip install opencv-python`

Step 2: Set Up  
1. Save an image file named `mypic.png` in the same folder as `stego.py`  
2. Open the terminal in that folder  
3. Run the script:  
`python stego.py`

## What Happens Next

You’ll be prompted to:  
- Enter your secret message  
- Enter a password to protect the message  

The message will be hidden in `mypic.png`, and a new image `encryptedImage.jpg` will be created.  
Then you’ll be asked to re-enter the password to decrypt and reveal the message.

## Sample Interaction

Enter secret message: Hello AICTE!  
Enter a passcode: 2802  
(An image viewer opens showing the encrypted image)  
Enter passcode for Decryption: 2802  
✅ Decryption message: Hello AICTE!

❌ If the passcode is incorrect:  
YOU ARE NOT auth

## Notes

- The input image should be large enough to encode the message  
- One character = one pixel channel  
- Works with .png, .jpg, etc.  
- For educational/demo purposes only — not secure encryption

## Project Highlights

- Minimal and easy-to-understand logic  
- No third-party steganography libraries used  
- Simple pixel-channel manipulation  
- Basic password protection

## Possible Improvements

- GUI with Tkinter or Streamlit  
- AES encryption before hiding  
- Better LSB-based encoding  
- Support for longer messages

## Developed By

Khushi Srivastava  

💡 Feel free to fork or enhance this project for your own learning or academic use!
