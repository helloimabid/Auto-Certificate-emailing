from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import yagmail
import os

df = pd.read_excel("participants.xlsx")

TEMPLATE = "certificate.png"
OUT_DIR = "certificates"
FONT_PATH = "fonts/AlexBrush-Regular.ttf"
FONT_SIZE = 120 

os.makedirs(OUT_DIR, exist_ok=True)


sender_email = "example@gmail.com"
app_password = "your_app_password_here"  
yag = yagmail.SMTP(sender_email, app_password)

for idx, row in df.iterrows():
    name = row['Name']
    email = row['Email']

    img = Image.open(TEMPLATE)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

   
    text = name
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    img_width, img_height = img.size

    x = (img_width - text_width)-(img_width - text_width) // 2
    
    y = 700  

    draw.text((x, y), text, font=font, fill=(98, 0, 234))

    output_file = f"certificates/{name}'s_certificate.pdf"
    img.save(output_file, "PDF", resolution=100.0)

    subject = " 🎉 Your Certificate of Participation - Technovation'25"
    body = f"""Assalamualikum {name},

Thank you for participating in the Technovation'25, the national tech fest of Josephite IT Club presented by Eastern Bank LTD. Your creativity, collaboration, and coding spirit made the event a vibrant celebration of youth innovation and technology. 🚀

Please find attached your Certificate of Participation.

We hope this experience inspires you to keep exploring, building, and innovating. Looking forward to your participation in future editions of Technovation. 💡

Best regards,
Sadman Abid
General Secretary
Josephite IT Club
Portfolio: https://sadmanabid.me"""

    yag.send(email, subject, body, attachments=output_file)
    print(f"Sent to {name} -> {email}")

print("Certificates created & emailed successfully!")
