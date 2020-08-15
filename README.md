# Special-Character-Recognition
> 특수문자 인식 Application

- JavaFX를 이용하여 App의 Layout 및 Logic 제작
- Scene Builder로 디자인
- CherryPy를 이용하여 Server 구축
- Sklearn.MLP 모델을 이용하여 특수문자 유사도 모델 제작

## ✍️  Introduction

최근 문서작업은 직장인부터 학생까지 다양한 연령층이 사용할 정도로 필수적인 작업입니다. 특히 대표적인 문서작업인 '보고서'는 작성 시 정해진 형식에 맞춰야합니다. 그러나 우리는 종종 평소 사용하는 형식이 아닌 다른 형식을 사용해야할 때가 존재하고 필요한 특수문자들을 찾는데 꽤 오랜 시간을 소비합니다. 

이를 위해 특수문자를 그리면 인식하여 실시간적으로 해당 특수문자를 제공하는 어플리케이션을 제작하게 되었습니다.

현 워드프로세서 상 특수문자를 찾기 위해 존재하는 과정을 단축시킴으로써 문서 작업의 효율성 증대 및 이용의 편리성을 기대합니다.

## 📁 Directory structure

```
  |#Client           
  |  |-IMG                   #인식 가능한 10개의 대표이미지 데이터
  |  |-SCR.exe               #App 실행 파일   
  |  |-SCR.jar               #App의 로직
  |  |-SCR.xml              
  |  |-sam_path.json         #이미지 path
  |  |-uni_path.json         #인식결과에 해당되는 유니코드를 찾기 위한 json 파일
  |
  |#Server & Model        
  |  |-test_MLP.py            #이미지 인식 모델
  |  |-IMG_MLP.pkl            #train된 모델 파일 
  |  |-test.py                #서버 파일      
  |
  |#etc
  |  |-IMG                    #tain data : 문자 당 51개의 데이터
  |  |-json_mk.py (server)    #test_Path.json, uni_path.json 생성 파일                   
  |  |-test_Path.json         #train data의 PATH 파일
  |  |-uni_path.json          #server측에서 search를 위한 key:value 쌍의 json파일
  |
  |-README.md                               
```

## 💻 dependency

- Java 8([https://www.java.com/ko/download/windows-64bit.jsp](https://www.java.com/ko/download/windows-64bit.jsp))

## 💡App 제작 과정
![KakaoTalk_20200815_034032756](https://user-images.githubusercontent.com/69345896/90305104-d7fb1200-def9-11ea-91ee-54f95ffffce5.png)

## 📒 App 실행 과정
![KakaoTalk_20200815_034808967](https://user-images.githubusercontent.com/69345896/90305110-e3e6d400-def9-11ea-8c08-dd6aaa1db00c.png)

## 📑 테스트 실행 방법

- v1.0 release 다운로드 후, SCR.exe 실행


## 🧪기능

### 1) 세부 설명

- 그림판 : client가 입력한 데이터를 받아들이는 매체
- Result : 가장 비슷한 특수문자부터 최대 4개의 인식 결과 대표사진을 보여주는 공간으로 사진 click시, 클립보드에 저장됨
- Recently Used : client가 최근에 사용한 특수문자를 보여주는 공간으로 사진 click시, 클립보드에 저장됨
- Reset : 그림판에 그려져있는 모든 것을 지우는 기능
- Remove : 지우개 기능( 아직 구현 중 )
- Okay : 400*400 size인 그림판을 capture한 후, 그림이 그려진 부분만 crop하여 전처리된 데이터를 Server에 전달하는 기능
- Open : client가 입력한 IP,Port에 해당되는 서버로 연결하는 기능( 현재 구현 중 )

### 2) 현재 인식 가능한 특수문자( 10개 )

![Untitled (1)](https://user-images.githubusercontent.com/69345896/90305124-109aeb80-defa-11ea-9d29-a9b1ea9c4f90.png)

### 3) 실제 실행 모습

- 실행 영상([https://www.youtube.com/watch?v=ggJGCJegkf8](https://www.youtube.com/watch?v=ggJGCJegkf8))
