import qrcode as qr # Import the qrcode library to generate QR codes
from PIL import Image # Import the Image module from the PIL (Python Imaging Library) library to manipulate images and save them in different formats
qr = qr.QRCode(
    version=1, # Set the version of the QR code (1 is the smallest) meaning it can store up to 25 alphanumeric characters
    error_correction=qr.constants.ERROR_CORRECT_H, # Set the error correction level (H is the highest) meaning it can recover up to 30% of the data if the QR code is damaged or obscured
    box_size=10,border=4) # Set the size of each box in the QR code  
img = qr.make("https://linkedin.com/in/Vipul-chib-80440b2b6") # Generate a QR code for the specified LinkedIn profile URL
qr.add_data("https://linkedin.com/in/Vipul-chib-80440b2b6") # Add the LinkedIn profile URL to the QR code meaning it will store the data in the QR code so that when scanned, it will redirect to the specified LinkedIn profile URL
qr.make(fit=True) # Fit the QR code to the data meaning it will adjust the size of the QR code to fit the data provided by the user by adjusting the version and error correction level accordingly
img=qr.make_image(fill_color="Red", back_color="White")# Generate the QR code image with a red fill color and a white background color

img.save("linkedin_qr.png") # Save the generated QR code as an image file
# add_data and make methods are used to add data to the QR code and generate the QR code image respectively.And there is no such difference between them. The add_data method is used to add data to the QR code, while the make method is used to generate the QR code image based on the data added. The make method can also be used to fit the QR code to the data by adjusting the version and error correction level accordingly.
# method used to create qr code for add_data is called make(fit=True) which means it will adjust the size of the QR code to fit the data provided by the user by adjusting the version and error correction level accordingly. The make method can also be used to generate the QR code image with a specified fill color and background color. In this case, the fill color is set to red and the background color is set to white.
