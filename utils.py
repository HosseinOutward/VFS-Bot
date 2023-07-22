import cv2
import re
import pytesseract
import telegram
from telegram.ext import Handler
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


class WebError(Exception):
    pass


class Offline(Exception):
    pass


class AdminHandler(Handler):
    def __init__(self, admin_ids):
        super().__init__(self.cb)
        self.admin_ids = admin_ids

    def cb(self, update: telegram.Update, context):
        if not self.check_update(update):
            update.message.reply_text('unauthorized access!')

    def check_update(self, update: telegram.update.Update):
        if update.message is None or update.message.from_user.id not in self.admin_ids:
            return True

        return False


def break_captcha():
    img = cv2.imread("captcha.png")
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = cv2.copyMakeBorder(image, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=[250])
    show_image(image)

    image = cv2.filter2D(image, -1, np.ones((4, 4), np.float32) / 16)
    show_image(image)

    image = cv2.divide(image,
                       cv2.morphologyEx(image, cv2.MORPH_DILATE,
                                        cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))),
                       scale=255)
    show_image(image)

    image = cv2.filter2D(image, -1, np.ones((3, 3), np.float32) / 9)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]
    image = cv2.filter2D(image, -1, np.ones((4, 4), np.float32) / 16)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=[255])
    show_image(image)

    captcha = pytesseract.image_to_string(image, config='--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNPQRSTUVWYZ')
    denoised_captcha = re.sub('[\W_]+', '', captcha).strip()
    return denoised_captcha


def show_image(img):
    return 
    import matplotlib.pyplot as plt
    plt.imshow(img, cmap='gray')
    plt.show()


class Message:
    def __init__(self, update, context, channel_id):
        self.update = update
        self.context = context
        self.channel_id = channel_id

    def send(self, text):
        print(text)
        self.update.message.reply_text(text)

    def broadcast(self, text):
        self.send(text)
        self.context.bot.send_message(chat_id=self.channel_id, text=text)
