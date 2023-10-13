# 금융 사기 용의자 및 피해자의 데이터 확인
## 목차
- [금융 사기 용의자 및 피해자의 데이터 확인](#금융-사기-용의자-및-피해자의-데이터-확인)
  - [목차](#목차)
  - [1. 개요](#1-개요)
  - [2. 기능](#2-기능)
  - [3. 프로젝트 문제 해결](#3-프로젝트-문제-해결)
  - [4. 예상 되는 문제](#4-예상-되는-문제)

## 1. 개요

  - ## 1) 기획 의도
    - 디지털 시대에서 금융사기가 많아지는 것을 예상할 수 있는데, 이를 데이터를 통해 방식과 발생 시기를 확인 할 수 있다.
    - 용의자 데이터와 피해자의 데이터를 통해 발생 빈도, 발생 시기를 확인해 사전에 예방할 수 있도록 해보자.
    > ![image](https://github.com/wonjun12/Financial-Fraud-App-Dashboard/assets/108748094/27c76d3e-39f4-4418-b1cb-6c7ebcd3b5dd)


  - ## 2) 사용 기술
  ![aws ec2](https://img.shields.io/badge/Amazon_Web_Server-EC2-red) ![Anaconda](https://img.shields.io/badge/Python-Anaconda-blue) ![Streamlit](https://img.shields.io/badge/Python-Streamlit-blue) ![streamlit_option_menu](https://img.shields.io/badge/Python-streamlit_option_menu-blue) ![Numpy](https://img.shields.io/badge/Python-Numpy-blue)
 ![Pandas](https://img.shields.io/badge/Python-Pandas-blue)
 ![Joblib](https://img.shields.io/badge/Python-Joblib-blue)
 ![Plotly](https://img.shields.io/badge/Python-Plotly.express-blue) 

  - ## 3) 링크
    - 사이트 : [ec2-52-78-84-125.ap-northeast-2.compute.amazonaws.com:10001/](http://ec2-52-78-84-125.ap-northeast-2.compute.amazonaws.com:10001/)
    - 다운로드 : [금융 사기 데이터](https://www.bigdata-policing.kr/product/list?vendor_code=all&product_category=&product_type=all&datepicker_type=all&datepicker_from=&datepicker_to=&price_yn=all&orderby=&dateGroup=all&feeGroup=all&dataGruop=all&keyword=%EA%B8%88%EC%9C%B5%EC%82%AC%EA%B8%B0)


## 2. 기능
  - **Github의 Actions를 통한 CI/CD 자동 배포 설정**
  - **About**
    - 다운로드 출처를 확인 할 수 있습니다.
    - 간략한 목차를 확인 할 수 있습니다.
  - **통신사 데이터**
    - 용의자의 통신사 데이터를 보실 수 있습니다.
    - 가장 많이 사용된 데이터의 신뢰를 바탕으로 사용이 많이 안된 통신사를 확인할 수 있습니다.
      - 생각지도 못한 통신사를 확인 한다면 사전에 어느정도 예방이 가능하다.
  - **지역 데이터**
    - 용의자 및 피해자의 지역에 대한 데이터를 알려줍니다.
    - 시도, 시군구 기준으로 가장 많이 사는 기준으로 보여줍니다.
  - **피해 데이터**
    - 가장 많이 사기를 당한 순위대로 보여줍니다.
    - 주말, 평일 기준으로 보여주며, 요일 기준으로도 보여줍니다.
    - ### **세부 종류**
      - **전체**
        - 피해 발생 수
          - 사기 발생 빈도에 따른 순위를 보여줍니다.
        - 사용된 물품
          - 금융 사기에 사용된 물품을 가장 많이 사용된 순위로 보여줍니다.
        - 사용된 은행/증권
          - 금융 사기에 사용된 은행/증권에 대해 많이 사용된 순위로 보여줍니다.
      - **성별**
        - 성별 돈
          - 성별에 따라 가장 많이 사기를 당한 금액을 보여줍니다.
        - 성별 물품
          - 성별에 따라 가장 많이 사기를 당한 물품을 보여줍니다.
      - **나이**
        - 나이 사이트
          - 나이에 따라 가장 많이 사기를 당한 사이트를 보여줍니다.
        - 나이 물품
          - 나이에 따라 가장 많이 사기를 당한 물품을 보여줍니다.
        - 나이 돈
          - 나이에 따라 가장 많이 사기를 당한 금액을 보여줍니다.
![image](https://github.com/wonjun12/Financial-Fraud-App-Dashboard/assets/108748094/195b80c8-eae0-4950-85ba-902d44e8701f)
![image](https://github.com/wonjun12/Financial-Fraud-App-Dashboard/assets/108748094/484c1ed0-6ace-4048-afcf-a2cb6d304c78)




## 3. 프로젝트 문제 해결
  1. **중복되는 코드 함수화 및 파일화**
      - 만드는 과정에서 중복되는 코드(차트 그리기, 날짜 입력/받기, 화면 갯수 입력)들이 주기적으로 많이 등장하다보니 해당 코드들을 함수화 시키면 사용하기 편해질것 이라는 판단에 함수화 시켜서 파일로  만들어서 사용했다.
  2. **파일의 데이터가 너무 많아 서버가 다운되는 경우가 발생했다.**
      - 파일이 엄청 많다보니 함치기만 해서 200MB가 넘어가는 경우가 많았고, 파일을 그룹핑 하는 과정에서 너무 많은 데이터를 처리하다보니 메모리를 크게 잡아 먹는 경우가 생겼다.
      - 해결하기 위해 그룹핑하는 과정에 대해서 **주피터**환경으로 돌아와 미리 그룹핑하고 해당 결과를 컬럼에 추가하여 데이터의 크기를 10MB정도로 낮춰서 저장했다.
      - 데이터 크기를 낮췄는데도 서버가 다운되는 경우가 있었는데, 이는 EC2 프론티어 서버의 한계점이라 생각했고 SWAP을 이용해 가상 메모리를 생성해 서버가 다운되는 경우를 막았다.

##  4. 예상 되는 문제
  1. **몇몇의 파일이 누락되는 경우가 있다.** 중복되는 파일도 많고 데이터가 엄청 많다보니 원하는 부분에 대해 열람하기 힘들고, 다른 방향으로 보여주기 위해서 파일의 크기가 증가 할텐데 현재는 할 수 없는게 아쉽다.
  2. 금융 사기의 종류가 점점 증가하며, 이전의 데이터가 필요없어질 수도 있는게 단점이다. 계속 데이터를 넣더라도 의미가 없어질 가능성이 없잖아 있을수 있다.
