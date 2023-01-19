from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os


#setting part
search_url = "https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl"#구글이미지
User_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
search_keywords = ["네이버 부스트캠프 ai tech 4기 합격후기"]
max_img_num = 3
save_path = "C:\\Users\\tmdwh\\Desktop\\Sashimi\\scraping\\output"


#디렉토리 만들어주기
try:
    if not os.path.exists(save_path):
        os.makedirs(save_path)
except OSError:
    print("Error: Failed to create the directory.")

#user_agent
header =urllib.request.build_opener()
header.addheaders=[('User-Agent',User_agent)]
urllib.request.install_opener(header)


#driver setting
options = webdriver.ChromeOptions() #다운 받은 chrome 드라이버를 불러옴
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options = options)

for keyword in search_keywords:
    save_path = save_path + "\\" + keyword
    #디렉토리 만들어주기
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    except OSError:
        print("Error: Failed to create the directory.")

    ###################### Setting #########################
    output_name = 1
    count = 0
    ########################################################
    driver.get(search_url) #드라이버를 통해 이동

    #html 검색창으로 접근 name = "q" 이므로
    elem = driver.find_element(By.NAME, "q")

    # 원하는 값을 입력
    elem.send_keys(keyword)

    #enter key를 의미
    elem.send_keys(Keys.RETURN)

    #스크롤 내려주는 코드
    SCROLL_PAUSE_TIME = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    #브라우저의 높이를 찾아서 값을 저장

    while True: #페이지당 50장
        # Scroll down to bottom -> 브라우저 끝까지 스크롤 내림
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page -> 로딩 때문에
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height: #더 내릴게 없다면
            try:
                #더보기 버튼을 눌러봄
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height


    #class를 이용하여 작은 이미지를 클릭하는 코드를 작성
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    #find_elements_by_css_selector(".rg_i.Q4LuWd")[0]의 의미는 가장 첫번째 애를 누르겠다



    for image in images:
        if count == max_img_num:
            break
        try:
            count += 1
            image.click()
            #만약 실행이 잘 안되면 이미지 로드 문제 일수도 있어서 지연을 조금주자
            time.sleep(2)

            #큰 이미지를 누르는 코드 
            img_url = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
            #img_url = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
            
            #이제 src 링크를 가져오는 코드를 짜자
            urllib.request.urlretrieve(img_url, save_path + "\\" + str(output_name) +".jpg")
            output_name += 1
        except:
            print("can't load image")
            pass

    driver.close()