# 📰 네이버 뉴스 요약 프로젝트 📝

### 목적 : 
### 스마트폰의 보급이 활발하게 되면서 실시간으로 다양한 뉴스들을 확인할 수 있지만, 수 많은 뉴스기사를 하나 하나 읽을 시간이 없습니다.
### 특히 요즘은 유튜브에서 동영상을 시청하는시간이 많이 늘어나다 보니, 글을 읽을 때 집중이 잘 되지 문제가 발생하고 있습니다.
### 그리고 뉴스기사의 문제점중 하나는 출퇴근 또는 이동시간에 스마트폰으로 뉴스를 보려고 하면 광고들이 많아서 의도치 않게 광고를 클릭하게 되고,
### 어떨 땐 이상한 바로가기 앱이 만들어지기도 합니다. 뉴스를 읽으려던 의지는 어느새 불편함으로 연결되죠.
### 하지만, 이러한 불편함을 감수하더라도 뉴스의 필요성은 누구나 알고 있을 것 같아요.
### 그래서 이런 문제를 해결하기 위해서 정보는 많고, 시간이 없는 현대인을 위해서 중요한 뉴스만 요약해서 보내주고
### 네이버 뉴스를 분야별로 요약해서 카카오 메시지로 받아 시간을 절약해보는 프로젝트를 완성하는게 저희팀의 목적입니다.

### ----------

### 의의 :
### 시간 절약: 바쁜 현대인들이 중요한 뉴스를 빠르게 파악할 수 있도록 도와줍니다.
### 광고 없는 환경: 광고로 인한 불편함 없이 순수한 뉴스 정보를 제공합니다.
### 집중력 향상: 요약된 뉴스 제공으로 글을 읽을 때의 집중력 저하 문제를 해결합니다.
### 맞춤형 정보 제공: 분야별로 요약된 뉴스를 제공하여 사용자가 관심 있는 정보를 더욱 쉽게 접근할 수 있게 합니다.
### 편리한 접근성: 카카오 메시지를 통해 간편하게 뉴스를 받아볼 수 있어 이동 중에도 편리하게 이용할 수 있습니다.

### ----------

## 뉴스 크롤링 방법 과정

#### 전체 구현 과정

![구현순서](https://github.com/seunggyo9/open_source/blob/master/image/%EA%B5%AC%ED%98%84%EC%88%9C%EC%84%9C.png)

출처 : <https://ai-creator.tistory.com/36>

### 사용방법

1. 먼저 자신이 읽고 싶은 뉴스기사를 https://news.naver.com/ 네이버 뉴스에서 검색하고 url을 복사합니다.

![네이버뉴스](https://github.com/seunggyo9/open_source/blob/master/image/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%89%B4%EC%8A%A4.png)

2. 뉴스크롤링.ipynb 파일을 실행합니다.
3. pip 파일들을 먼저 실행해서 라이브러리를 설치해줍니다.
4. 주석으로 최종이라고 쓰여져있는 코드부분을 실행합니다.
5. 사용자의 카카오톡으로 요약본을 받기 위하여 토큰을 받아야 하므로 카카오 개발자 페이지를 이용하여 토큰을 발급받습니다.
6. 자신의 토큰 비번을 입력하고 토큰 코드 부분 코드를 실행하면 카톡으로 요약본을 받아 볼 수 있습니다.

