from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    """Khởi tạo và trả về driver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def enter_employee_info(driver, name, phone, address, email, birthday, password):
    """Nhập thông tin nhân viên hoặc bác sĩ."""
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "phone_number").send_keys(phone)
    driver.find_element(By.NAME, "address").send_keys(address)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "birthday").send_keys(birthday)
    driver.find_element(By.NAME, "password").send_keys(password)
    print(f"Đã nhập thông tin cho: {name}")

def submit_form(driver):
    """Bấm nút Tạo Tài Khoản hoặc Lưu Thông Tin."""
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()
    print("Đã bấm nút submit!")

def create_employee_account(driver):
    """Tạo tài khoản nhân viên."""
    driver.get("http://localhost:8000/tao-tai-khoan-nhan-vien.html")
    time.sleep(2)
    enter_employee_info(
        driver, "Trần Huỳnh Đức Ninh", "0387972840", 
        "ấp 7a, xã mỹ yên, huyện bến lức, tỉnh long an", 
        "tranninh456@gmail.com", "09/09/2005", "1234"
    )
    submit_form(driver)

def create_doctor_account(driver):
    """Tạo tài khoản bác sĩ."""
    driver.get("http://localhost:8000/tao-tai-khoan-bac-si.html")
    time.sleep(2)
    enter_employee_info(
        driver, "Lưu Nhất Huy", "0387972840", 
        "ấp 7a, xã mỹ yên, huyện bến lức, tỉnh long an", 
        "nhathuynhathuy456@gmail.com", "09/09/2005", "1234"
    )
    submit_form(driver)

def create_customer_account(driver):
    """Tạo tài khoản khách hàng."""
    driver.get("http://localhost:8000/tao-tai-khoan-khach-hang.html")
    time.sleep(2)
    enter_employee_info(
        driver, "Đỗ Tiến Đạt", "0387972840", 
        "ấp 7a, xã mỹ yên, huyện bến lức, tỉnh long an", 
        "dodatsdf282@gmail.com", "10/11/2005", "1234"
    )
    submit_form(driver)

def fill_pet_info(driver, customer_name, pet_name, species, age, medical_history):
    """Nhập thông tin pet."""
    driver.get("http://localhost:8000/checkin-thu-cung.html")
    time.sleep(2)
    driver.find_element(By.NAME, "customer").send_keys(customer_name)
    driver.find_element(By.NAME, "name").send_keys(pet_name)
    driver.find_element(By.NAME, "species").send_keys(species)
    driver.find_element(By.NAME, "age").send_keys(age)
    driver.find_element(By.NAME, "medical_history").send_keys(medical_history)
    print(f"Đã nhập thông tin pet: {pet_name}.")
    submit_form(driver)

def fill_kennel_info(driver, kennel_name):
    """Nhập thông tin chuồng thú cưng."""
    driver.get("http://localhost:8000/quan-ly-chuong.html")
    time.sleep(2)
    driver.find_element(By.NAME, "name").send_keys(kennel_name)
    print(f"Đã thêm chuồng: {kennel_name}.")
    submit_form(driver)

def fill_Dk_info(driver, date_value, start, end):
    """Nhập thông tin chuồng thú cưng."""
    driver.get("http://localhost:8000/thoi-gian-kham/58/")
    time.sleep(2)
    driver.find_element(By.NAME, "date").send_keys(date_value)
    script = f"document.getElementsByName('start_time')[0].value = '{start}';"
    driver.execute_script(script)
    script = f"document.getElementsByName('end_time')[0].value = '{end}';"
    driver.execute_script(script)
    print(f"Da dang ky thanh cong: {date_value}.")
    submit_form(driver)

# Khởi tạo driver
driver = setup_driver()
try:
    driver.get("http://localhost:8000/")
    time.sleep(2)
    create_employee_account(driver)
    time.sleep(2)
    create_doctor_account(driver)
    time.sleep(2)
    create_customer_account(driver)
    time.sleep(2)
    fill_pet_info(driver, "Đỗ Tiến Đạt", "Chichi", "Chó", "1", "không")
    fill_pet_info(driver, "Đỗ Tiến Đạt", "Lulu", "Mèo", "1", "không")
    fill_kennel_info(driver, "số 1")
    fill_kennel_info(driver, "số 2")
    fill_kennel_info(driver, "số 3")
    fill_Dk_info(driver, "15/02/2025", "07:30", "18:00")
    
    input("Nhấn Enter để thoát và đóng trình duyệt...")
finally:
    driver.quit()
