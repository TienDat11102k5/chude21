from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    """Khởi tạo và trả về driver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def submit_form(driver):
    """Bấm nút Submit."""
    try:
        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        button.click()
        print("Đã bấm nút submit!")
        time.sleep(2)
    except Exception as e:
        print(f"Lỗi khi bấm Submit: {e}")

def fill_nhapvien_info(driver, pet_name, kennel):
    """Nhập thông tin nhập viện."""
    driver.get("http://localhost:8000/sap-lich-nhap-vien.html")
    time.sleep(2)
    
    driver.find_element(By.NAME, "pet").send_keys(pet_name)
    driver.find_element(By.NAME, "kennel").send_keys(kennel)
    
    submit_form(driver)

def click_update_button(driver):
    """Nhấn vào nút 'Cập nhật'."""
    driver.get("http://localhost:8000/danh-sach-cham-soc.html")
    time.sleep(4)

    try:
        update_button = driver.find_element(By.XPATH, "//a[contains(text(),'Cập nhật')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", update_button)
        time.sleep(3)
        update_button.click()
        print("Đã nhấn vào nút 'Cập nhật'!")
        time.sleep(3)
    except Exception as e:
        print(f"Lỗi khi nhấn vào nút 'Cập nhật': {e}")

def fill_ghichu_info(driver, notes):
    """Nhập ghi chú sau khi nhấn 'Cập nhật'."""
    try:
        notes_input = driver.find_element(By.NAME, "notes")
        notes_input.clear()
        notes_input.send_keys(notes)
        print(f"Đã nhập ghi chú: {notes}")
        submit_form(driver)
    except Exception as e:
        print(f"Lỗi khi nhập ghi chú: {e}")
driver = setup_driver()
try:
    driver.get("http://localhost:8000/")
    fill_nhapvien_info(driver, "Chichi", "1")
    click_update_button(driver)
    fill_ghichu_info(driver, "Die")
    driver.get("http://localhost:8000/theo-doi-nhap-vien.html")
    time.sleep(5)
    driver.get("http://localhost:8000/danh-sach-cham-soc.html")
    time.sleep(5)

    input("Nhấn Enter để thoát và đóng trình duyệt...")
finally:
    driver.quit()
