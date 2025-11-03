# 📜 Automated Certificate Generator & Email Sender

**This Python script can save your life by automatically generating and sending certificates to any number of people via email!**

No more manually editing certificates one by one or sending hundreds of emails individually. Just prepare your participant list, and let this script do all the heavy lifting. 🚀

---

## ✨ Features

- 🎨 **Automatic Name Placement** - Dynamically places participant names on certificate templates
- 📧 **Bulk Email Sending** - Sends personalized emails with certificate attachments to unlimited recipients
- 🔄 **Batch Processing** - Process hundreds or thousands of certificates in minutes
- 💾 **PDF Generation** - Converts certificates to professional PDF format
- 🎯 **Smart Font Scaling** - Automatically adjusts font size for long names to prevent overflow
- ⚡ **Time Saver** - What takes hours manually can be done in minutes

---

## 📋 Prerequisites

Before running the script, make sure you have:

- Python 3.7 or higher installed
- Gmail account with App Password enabled (for sending emails)
- Certificate template image (PNG format)
- Font file (TTF format)
- Excel file with participant data

---

## 🛠️ Installation

1. **Clone or download this repository**
2. **Install required Python packages:**

```bash
pip install pillow pandas yagmail openpyxl
```

---

## 📁 Project Structure

```
cert_project/
│
├── generate.py              # Main script
├── certificate.png          # Your certificate template
├── participants.xlsx        # Excel file with participant data
├── fonts/
│   └── AlexBrush-Regular.ttf  # Font for names (or your chosen font)
└── certificates/            # Generated certificates (auto-created)
```

---

## 📝 Setup Instructions

### 1. Prepare Your Certificate Template

- Create a certificate design with a blank space for the participant's name
- Save it as `certificate.png` in the project root
- Note the approximate coordinates where you want the name to appear

### 2. Prepare Participant Data

Create an Excel file named `participants.xlsx` with the following columns:

| Name               | Email                   |
| ------------------ | ----------------------- |
| Sadman Abid        | myself@sadmanabid.me    |
| Nirjon Kumar Kundu | nirjonkundu@gmail.com   |
| Mahdi Bin Zaman    | mahdibinzaman@gmail.com |

### 3. Configure Email Settings

1. Go to your Google Account settings
2. Enable 2-Factor Authentication
3. Generate an App Password:
   - Go to Security → 2-Step Verification → App Passwords
   - Generate a password for "Mail"
4. Update the script with your credentials:

```python
sender_email = "your-email@gmail.com"
app_password = "your-app-password-here"
```

### 4. Adjust Certificate Positioning

Edit these values in `generate.py` to position the name correctly:

```python
x = (img_width - text_width) // 2  # Horizontal position (centered)
y = 310  # Vertical position (adjust as needed)
```

---

## 🚀 Usage

Simply run the script:

```bash
python generate.py
```

The script will:

1. ✅ Read all participants from the Excel file
2. ✅ Generate a personalized certificate for each person
3. ✅ Save certificates as PDFs in the `certificates/` folder
4. ✅ Send each certificate via email automatically
5. ✅ Print progress for each sent email

---

## ⚙️ Customization

### Change Font Style or Size

```python
FONT_PATH = "fonts/YourFont.ttf"
FONT_SIZE = 120  # Adjust size as needed
```

### Modify Text Color

```python
draw.text((x, y), text, font=font, fill=(98, 0, 234))  # RGB color
```

### Update Email Template

**You can easily customize the email message by editing the `generate.py` file.**

Simply locate the `subject` and `body` variables in the script and modify them to your needs:

```python
subject = "Your Certificate Title"
body = f"""Your custom message here...
Include {name} for personalization.

Add your greeting, message, and signature.
The {name} variable will be replaced with each participant's name."""
```

**No coding knowledge required** - just edit the text between the triple quotes `"""` to change what recipients will see in their email!

### Adjust Position

- **Move name DOWN**: Increase `y` value (e.g., 350, 400)
- **Move name UP**: Decrease `y` value (e.g., 280, 250)
- **Move name RIGHT**: Add to x (e.g., `x + 50`)
- **Move name LEFT**: Subtract from x (e.g., `x - 50`)

---

## 🎯 Use Cases

Perfect for:

- 🎓 **Hackathons & Competitions** - Send certificates to hundreds of participants
- 🏆 **Workshops & Webinars** - Recognize attendees instantly
- 📚 **Online Courses** - Automated course completion certificates
- 🎉 **Events & Conferences** - Bulk certificate distribution
- 🏅 **Awards Ceremonies** - Professional certificate generation

---

## 🔒 Security Notes

- ⚠️ **Never commit your App Password to GitHub** - Add it to `.gitignore`
- 🔐 Use Gmail App Passwords, not your actual Gmail password
- 📧 Test with a few emails before sending to everyone
- 💾 Keep backups of your participant data

---

## 🐛 Troubleshooting

### Name appears in wrong position

- Adjust the `y` value (line with `y = 310`)
- Try values between 250-400 to find the right spot

### Name is cut off or overflows

- Reduce `FONT_SIZE` value
- Implement dynamic font scaling (see advanced customization)

### Email not sending

- Verify App Password is correct
- Check if 2-Factor Authentication is enabled
- Ensure email/password have no extra spaces

### Font not found error

- Check font file path is correct
- Use absolute path if relative path doesn't work

---

## 📊 Performance

- ⚡ Processes ~10-20 certificates per minute (depends on email server)
- 💪 Can handle thousands of participants
- 📈 Much faster than manual processing!

---

## 🤝 Contributing

Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Share improvements

## 👨‍💻 Author

**Sadman Abid**
General Secretary, Josephite IT Club
Portfolio: [https://sadmanabid.me](https://sadmanabid.me)

---

## 💡 Tips

1. **Test First**: Run with 2-3 test emails before processing everyone
2. **Backup Data**: Keep original participant data safe
3. **Check Spam**: First emails might go to spam folders
4. **Preview Certificates**: Generate one certificate manually to verify positioning
5. **Track Progress**: The script prints each successful send - monitor the console

---

**Save hours of manual work. Generate and send certificates automatically! 🎉**

For questions or support, feel free to reach out!
