# product_classification



## Project Name
상품 이미지 데이터를 활용한 상품 분류 모델 개발

#### -- Project Status: Continue


## Project Objective
* 상품 분류 모델 개발
* 다양한 백본 모델간 성능 비교 
* (옵션) 논문 리뷰

### Methods Used
* CNN (ResNet18, MobileNetV2, InceptionV3, EfficientNet)
* etc. 

### Dependencies
* 


## Process
1. Data Preparation 
  - 데이터 다운로드 ([link](https://aihub.or.kr/aidata/34145/download))
  - 디렉토리 구조 설정
  - 디렉토리명 변환
2. Training (ResNet18, MobileNetV2, InceptionV3, EfficientNet)
3. Validation : 백본 모델 성능 비교


## Usage

#### 1. 데이터 준비 

   ##### 1.1 데이터 다운로드 ([link](https://aihub.or.kr/aidata/34145/download))
   
   ##### 1.2 디렉토리 구조 설정 
    
    # 데이터셋 디렉토리 구조 
    products_classification
        ├── data
            ├── convert
            |   ├── train
            |   ├── val

            ├── dataset  
            |   ├── train
            |   ├── val
   
    
   ##### 1.3 디렉토리명 변환
   1.3.1 다운받은 상품 이미지 데이터의 변환하고자 하는 폴더를 다음 경로로 이동
     - "./상품 이미지 데이터/Training/" 경로 하위 폴더 -> "./products_classification/data/convert/train/" 경로로 이동
     - "./상품 이미지 데이터/Validation/" 경로 하위 폴더 -> "./products_classification/data/convert/val/" 경로로 이동
   
   1.3.2 디렉토리명 변환 (아래 명령어 실행)
    
    # cd utils
    
    python convert_dirname.py

   1.3.3 데이터 로드를 위해, 변환된 폴더를 다음 경로로 이동 (아래 명령어 실행)
    
    # cd utils
    
    python move_dir.py  
    
 



#### 2. 모델 학습

    python train.py






