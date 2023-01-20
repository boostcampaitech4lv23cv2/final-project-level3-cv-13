# How To prepare Sashimi Data

## window에서 가상환경 만들기

<br/>

### venv를 이용하여 가상환경을 만들 것이므로 venv 실행

<br/>

```bash
python3 -m venv /path/to/new/virtual/environment
```

### 가상환경 이름을 지정해주기 (scraping)
<br/>

```bash
python -m venv scraping
```

### 가상환경 실행을 위해 Scripts에 접근
<br/>

```bash
cd scraping\Scripts
```

### 가상환경을 실행시킴
```bash
activate
```
<br/>

### 가상환경에 라이브러리 설치를 하기위해 <br/>Scripts 에 requirements.txt를 복붙하고 아래의 코드를 실행 <br/>

```bash
pip install - r requirements.txt
```

<br/>

## Before Running Data_Scraping.py
<br/>


### 1. 먼저 본인의 크롬 브라우저의 버전을 확인한다

<br/>

```text
크롬창 우측 상단 더보기 -> 도움말 -> Chrome 정보
본인 :버전 108.0.5359.126(공식 빌드) (64비트)
```

<br/>

### 2. 본인의 버전에 맞는 chromeDriver를 설치
<br/>

```text
https://chromedriver.chromium.org/downloads 에 들어가서
자신에게 맞는 OS를 선택 (맨뒤의 126 등은 무시 가능) 
ex) 본인 :버전 108.0.5359.126 -> 버전 108.0.5359
```
<br/>

### 3. 본인의 Chromedriver를 저장해주자
<br/>

```text
압축을 풀고 Sashimi안에 있는 chromedriver.exe를 덮어쓰기 해준다
(main과 같은 경로에 있어야 한다)
```

<br/>

### 4. Data_Scraping.py의 세팅부분을 건드려 주자
<br/>

#### 4-1. User_agent : 다음링크에 들어가서 User_agent확인 

https://www.whatismybrowser.com/detect/what-is-my-user-agent/

```text
User_agent : 일종의 '인증키'라 생각 
= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' 
```


#### 4-2. 나머지 부분을 세팅해주자 

**search_url : 구글이미지 url (고정추천)**

(예시) "https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl"<br/><br/>


**search_keywords** : 검색할 키워드


(예시) ["광어회", "방어회" ,"참치회"] <br/><br/>

**max_img_num** : 최대 다운 이미지 개수 

(예시) 1500 <br/><br/>

**Max_scroll_count** : 최대 스크롤 수 (1 스크롤 => 약 50장)

(예시) 30<br/><br/>

**save_path** : 결과물 저장 경로

(예시) "C:\\Users\\tmdwh\\Desktop\\Sashimi\\scraping\\output"<br/><br/>

**DELAY** : 각 행동 당 대기시간

(예시) 1.8<br/>
(빠른버전) 0.8<br/><br/>

**SCROLL_PAUSE_TIME** : 한 스크롤 당 대기시간

(예시) 2<br/>
(빠른버전) 0.5<br/><br/>

+) **Max_scroll_count**는 1번에 약 50장이지만 중간에 다운로드가 되지 않아 <br/>

패스되는 이미지들 개수도 고려해야 합니다

+) **DELAY, SCROLL_PAUSE_TIME**은 만약 너무 빠르다면 작업이 도중에 멈출 수 있습니다<br/>

<br/>

### 5. 다음과 같은 세팅을 마친 후
<br/>

```text
Data_Scraping.py를 실행 시켜준다
```

### 6. out폴더를 확인한다
<br/>

```text
size_csv : 각 크롤링된 파일에 대한 크기 정보를 담은 csv

keyword 파일 : 각 키워드에 따른 이미지들 모음
```