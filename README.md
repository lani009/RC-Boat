# RC-Boat
## 1. 목적
>집에서 할거 없어서 만듦   
>gps로 컨트롤 범위 외에서도 자동으로 주행 및 귀환할 수 있음.

## 2. Dependency
### 2.1. PC
>pip3 install keyboard

### 2.2. RPI
>sudo apt-get install python-rpi.gpio  
>pip3 install spidev
#### 2.2.1. SPI 사용 설정
>pi@raspberrypi ~ $ sudo raspi-config  
>→ 8. Advanced Options → A6 SPI → Yes and OK

## 3. 통신 방법
### 3.1. pc -> boat
-----
#### 3.1.1. 속도 제어
  - 0: zeroSpeed    00000
  - 1: 1(25%)       00100
  - 2: 2(50%)       01000
  - 3: 3(75%)       01100
  - 4: FullSpeed    10000
  - 5가지 -> 3비트

#### 3.1.2. 방향 제어
  - 0: 왼           00000
  - 1: 우           00001
  - 2: 중           00010
  - 3가지 -> 2비트

#### 3.1.3. 신호 전달 방식
신호 주파수: 10Hz  
속도 신호와 방향 신호를 OR 비트연산하여 총 5비트로 전송  
>data = speed | direction

### 3.2. boat -> pc
-----
#### 3.2.1. 배터리 잔량
  - 6비트 -> 64가지
  - 최소 표현단위 1.5625

## 4. 조작법
### 4.1. PC
#### 4.1.1. 속도
  - z:      속도   0%
  - x:      속도  25%
  - c:      속도  50%
  - v:      속도  75%
  - space:  속도 100%
  - w: 속도 25% 증가
  - s: 속도 25% 감소

#### 4.1.2. 방향
  - 화살표 왼쪽: 좌현으로 선회
  - 화살표 오른쪽: 우현으로 선회

#### 4.1.3. 부가 기능
  - ctrl+q: 종료

## 5. 보트 구성
  - 라즈베리파이
  - 와이파이 동글
  - 전압 측정 센서
  - 리튭폴리머 배터리
  - ADC
  - 서보모터
  - 브러쉬리스 모터
  - 우리의 운

## 6. 실행 방법
  - 라즈베리파이에서 ./Boat/pycode/rpiServer.py 실행
  - 컴퓨터에서 index.py 실행