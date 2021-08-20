from selenium import webdriver

def test_setup():
	global driver
	print("sample test case started")  
	driver = webdriver.Chrome(executable_path=r"C:\tools\chromedriver.exe")
	driver.maximize_window()

def test_form_entry():
	driver.get("http://localhost/form.php")
	driver.find_element_by_name("nip").send_keys("33260126012606930001")
	driver.find_element_by_name("nama").send_keys("iwan prayitno")
	driver.find_element_by_name("nik").send_keys("15093613")
	driver.find_element_by_name("alamat").send_keys("Pochinki")
	driver.find_element_by_name("perusahaan").send_keys("PT. SAT, Tbk")
	driver.find_element_by_name("tanggal").send_keys("26 Juni 1993")
	driver.find_element_by_name("divisi").send_keys("IT")
	driver.find_element_by_name("posisi").send_keys("Data Mining Programming Analyst")
	driver.find_element_by_name("gaji").send_keys("100 JT, Aamiin")
	driver.find_element_by_name("atasan").send_keys("Sih Eko")
	driver.find_element_by_name("submit").click()

def test_cleanup():
	driver.close()
	driver.quit()