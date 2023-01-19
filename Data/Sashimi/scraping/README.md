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

### 5. 다음과 같은 세팅을 마친 후
<br/>

```text
Data_Scraping.py를 실행 시켜준다 (경로 등을 설정)
```
