# Import thư viện
import cv2 
import pytesseract
import re

def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

# Lấy file hình
# img = cv2.imread("/var/www/html/thien.tran/img/vin-commerce.jpg")
# img = cv2.imread("/var/www/html/thien.tran/img/vin-commerce.jpg")
# img = cv2.imread("/var/www/html/thien.tran/img/vin-commerce.jpg")
# img = cv2.imread("/var/www/html/thien.tran/img/vin-commerce.jpg")
# img = cv2.imread("/var/www/html/thien.tran/img/circle-k.jpg")
img = cv2.imread("/var/www/html/thien.tran/img/vin-commerce.jpg")

# Xử lí hình ảnh

# # Chuyển hình trắng đen
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# # Tăng hiệu suất trắng đen
# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 

# # Cấu hình kích thước hình đọc
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (500,500))

# # Làm rõ các kí tự hơn
# dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# # Finding contours 
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# # Tạo bản sao hình ảnh
im2 = img.copy()

# # File export
file = open("vin-commerce.txt", "w+")
file.write("")
file.close()

# Write file
# for cnt in contours: 
    # x, y, w, h = cv2.boundingRect(cnt) 

# Open the file in append mode 
file = open("vin-commerce.txt", "a") 

# Apply OCR on the cropped image 
tmpText = pytesseract.image_to_string(im2, lang='vie') 

text = no_accent_vietnamese(tmpText)

# Appending the text into file 
file.write(text) 
# file.write("\n")

# Close the file 
file.close 

print("Mario")