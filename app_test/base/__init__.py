from appium.webdriver.webdriver import By

"""
1.应用的包名和启动名
"""
app_package = 'com.android.settings'
app_activity = ".Settings"

"""
2.搜索
"""
search_button = (By.XPATH, "//*[@content-desc='搜索']")
search_edit_text = (By.CLASS_NAME, "android.widget.EditText")
back_button = (By.CLASS_NAME, "android.widget.ImageButton")





