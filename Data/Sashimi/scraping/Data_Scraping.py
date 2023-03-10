from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from tqdm import tqdm

#setting part
search_url = "https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl"#구글이미지
User_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
search_keywords = ["참돔회"]
max_img_num = 1500
Max_scroll_count = 40
save_path = "C:\\Users\\user\\Desktop\\final_proj\\myenv\\output"
DELAY = 1
SCROLL_PAUSE_TIME = 1.5


count_list = {"normal" : 0, "link" : 0, "cant" : 0}


print("###########################")
print("## 환경세팅을 시작합니다 ##")
print("########################### \n")

#디렉토리 만들어주기
csv_save_path = save_path + "\\size_csv"
try:
    if not os.path.exists(csv_save_path):
        os.makedirs(csv_save_path)
except OSError:
    print("Error: Failed to create the directory.")

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
options = webdriver.ChromeOptions() # 다운 받은 chrome 드라이버를 불러옴
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options = options)

print("\n 환경세팅을 성공적으로 마쳤습니다 \n")

for keyword in search_keywords:
    size_lst = []
    print("###################################################")
    print("## [",keyword,"] 에 대한 크롤링을 시작합니다 (최대 이미지 개수 : ",max_img_num,")")

    tmp_save_path = save_path + "\\" + keyword

    #디렉토리 만들어주기
    try:
        if not os.path.exists(tmp_save_path):
            os.makedirs(tmp_save_path)
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


    # 4k 버튼 눌러주기
    equipment_xpath = "/html/body/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div" #통과
    view_box_xpath = "/html/body/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[1]/div/div[1]"
    #큰 사진
    big_xpath = "/html/body/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[2]/div"
    #중간 사진
    mid_xpath = "/html/body/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[3]/div"

    driver.find_element_by_xpath(equipment_xpath).click()
    driver.find_element_by_xpath(view_box_xpath).click()
    driver.find_element_by_xpath(big_xpath).click()
    #driver.find_element_by_xpath(mid_xpath).click()


    #스크롤 내려주는 코드
    
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    #브라우저의 높이를 찾아서 값을 저장


    scroll_count = 0
    print("## 스크롤링을 시작합니다 (최대 Scroll 횟수 : ", Max_scroll_count,")")
    while True: #페이지당 50장
        print("## 스크롤 ",scroll_count,"번 진행 완료")
        if scroll_count >= Max_scroll_count:
            break

        scroll_count += 1

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
    time.sleep(DELAY)

    link_url = []

    print("## 스크롤링을 성공적으로 마쳤습니다")
    print("## [",keyword,"] 에 대한 이미지 다운로드 시작합니다 (최대 이미지 개수 : ",max_img_num,")\n")
    print("## 크롤링된 이미지 개수 : ",len(images),"\n")
    with tqdm(total=len(images)) as pbar:
        for image in images:
            if count == max_img_num:
                break
            try:
                image.click()
                #만약 실행이 잘 안되면 이미지 로드 문제 일수도 있어서 지연을 조금주자
                time.sleep(DELAY)
                
                #큰 이미지를 누르는 코드 
                img_url = driver.find_element_by_css_selector(".n3VNCb.KAlRDb").get_attribute("src")
                #img_url = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")

                #print(img_url)
                driver.execute_script('window.open("'+img_url+'");')  #구글 창 새 탭으로 열기
                time.sleep(DELAY)

                #이 부분에서 다운로드가 받아지고 탭이 안열리는 현상이 발생
                if len(driver.window_handles) <= 1: # 탭이 안 열림
                    print("## 탭이 닫혔습니다")
                    driver.switch_to.window(driver.window_handles[-1]) # 마지막 탭으로 이동
                    time.sleep(DELAY)
                    count += 1
                    count_list["link"]+=1
                    pbar.update(1)
                    continue #다음 loop로

                else:

                    driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
                    time.sleep(DELAY)
                    #이제 src 링크를 가져오는 코드를 짜자
                    urllib.request.urlretrieve(img_url, tmp_save_path + "\\" + str(output_name).zfill(4) +".jpg")
                    size_lst.append(driver.title.split()[-1][1:-1])
                    driver.close()  #링크 이동 후 탭 닫기

                    driver.switch_to.window(driver.window_handles[0])  #다시 이전 창(탭)으로 이동
                    time.sleep(DELAY)
                    count += 1
                    count_list["normal"]+=1
                    print("\n## ",max_img_num,"(",len(images),")","개의 이미지 중 ",output_name,"번째 이미지 저장완료")
                    pbar.update(1)
                    output_name += 1
            except:

                print("\n## [Error] 사진을 저장하지 못했습니다 (can't load image)")
                count_list["cant"]+=1
                pbar.update(1)
            print(len(driver.window_handles))
            if len(driver.window_handles) != 1:
                time.sleep(DELAY)
                driver.close()  #링크 이동 후 탭 닫기
                driver.switch_to.window(driver.window_handles[0])  #다시 이전 창(탭)으로 이동
                time.sleep(DELAY)



    print("###################################################################")
    print("## 사진 크기 정보 csv 만들기")
    print("###################################################################")
    with open(csv_save_path + "\\"+ keyword +"_size.csv",'w', newline='') as f:
        writer =csv.writer(f)
        for idx in range (len(size_lst)):
            writer.writerow(size_lst[idx].split("×"))


    print("## csv가 성공적으로 만들어 졌습니다")
    print('## csv 저장 경로 : ', csv_save_path + "\\"+ keyword +"_size.csv 를 확인하세요")

    print("###################################################################")
    print("## 예외 url 정보 csv 만들기")
    print("###################################################################")

    # with open(csv_save_path + "\\"+"[Error]" +keyword +"_link.csv",'w', newline='') as f:
    #     writer =csv.writer(f)
    #     for idx in range (len(link_url)):
    #         writer.writerow(link_url[idx].split(""))
            
    print(count_list)


    print("## csv가 성공적으로 만들어 졌습니다")
    print('## csv 저장 경로 : ', csv_save_path + "\\"+ keyword +"_size.csv 를 확인하세요")



#    print("###################################################################")
    print("## 스크랩핑이 성공적으로 마무리 되었습니다 다음의 경로를 확인하세요")
    print("## 저장 경로 : ",tmp_save_path)
    print("###################################################################\n\n\n")

driver.close()