from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Khởi tạo ChromeDriver
driver = webdriver.Chrome()

try:
    # Truy cập trang đăng nhập
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    
    # Tìm phần tử input username và nhập giá trị
    inputUserName = driver.find_element(By.NAME, "username")
    print("Tìm thấy input tên người dùng:", inputUserName)
    inputUserName.send_keys("admin")
    time.sleep(2)

    # Tìm phần tử input password và nhập giá trị
    password = driver.find_element(By.NAME, "password")
    print("Tìm thấy input mật khẩu:", password)
    password.send_keys("1234")
    time.sleep(2)

    # Nhấn Enter để đăng nhập
    password.send_keys(Keys.RETURN)
    time.sleep(2)

    # Kiểm tra tiêu đề sau khi đăng nhập
    if "Site administration" in driver.title:
        print("[PASSED] Đăng nhập thành công!")
    else:
        print("[FAILED] Đăng nhập thất bại!")

finally:
    driver.quit(20)
