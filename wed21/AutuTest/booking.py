from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    """Khởi tạo và trả về driver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def submit_form(driver):
    """Bấm nút Tạo Tài Khoản hoặc Lưu Thông Tin."""
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()
    print("Đã bấm nút submit!")

def fill_booking_info(driver, customer_name, pet_name, veterinarian_name, appointment_date_value, fee_value):
    """Tự động chọn đăng ký khám."""
    driver.get("http://localhost:8000/dang-ky-kham.html")
    time.sleep(2)
    driver.find_element(By.NAME, "customer").send_keys(customer_name)
    driver.find_element(By.NAME, "pet").send_keys(pet_name)
    driver.find_element(By.NAME, "veterinarian").send_keys(veterinarian_name)
    script = f"document.getElementsByName('appointment_date')[0].value = '{appointment_date_value}';"
    driver.execute_script(script)
    driver.find_element(By.NAME, "fee").send_keys(fee_value)
    print(f"Đã đăng ký khám thành công: {customer_name}.")
    submit_form(driver)

driver = setup_driver()
try:
    driver.get("http://localhost:8000/")
    fill_booking_info(driver, "Đỗ Tiến Đạt", "Chichi", "Lưu Nhất Huy", "2024-04-13T13:55", "0")
    driver.get("http://localhost:8000/quan-ly-booking.html")
    input("Nhấn Enter để thoát và đóng trình duyệt...")
finally:
    driver.quit()
