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
    time.sleep(2)
    button.click()
    print("Đã bấm nút submit!")

def fill_saplich_info(driver, customer_name, pet_name, veterinarian_name, diagnosis, treatment, stayrequired):
    """Tự động chọn đăng ký khám."""
    driver.get("http://localhost:8000/ghi-nhan-kham.html")
    time.sleep(2)

    driver.find_element(By.NAME, "customer").send_keys(customer_name)
    driver.find_element(By.NAME, "pet").send_keys(pet_name)
    driver.find_element(By.NAME, "veterinarian").send_keys(veterinarian_name)
    driver.find_element(By.NAME, "diagnosis").send_keys(diagnosis)
    driver.find_element(By.NAME, "treatment").send_keys(treatment)

    try:
       checkbox = driver.find_element(By.NAME, "stay_required")
       driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)  
       time.sleep(2)
       if stayrequired.lower() == "có":
         if not checkbox.is_selected():
            driver.execute_script("arguments[0].click();", checkbox)  
       else:  
        if checkbox.is_selected():
            driver.execute_script("arguments[0].click();", checkbox)  
    except Exception as e:
     print(f"Lỗi khi chọn 'Lưu Chuồng': {e}")

    submit_form(driver)  

driver = setup_driver()
try:
    driver.get("http://localhost:8000/")
    fill_saplich_info(driver, "Đỗ Tiến Đạt", "ChiChi", "Lưu Nhất Huy", "Nóng", "Uống thuốc", "có")
    fill_saplich_info(driver, "Đỗ Tiến Đạt", "Lulu", "Lưu Nhất Huy", "Sốt", "Uống thuốc", "không")
    driver.get("http://localhost:8000/lich-su-kham.html")
    input("Nhấn Enter để thoát và đóng trình duyệt...")
finally:
    driver.quit()
