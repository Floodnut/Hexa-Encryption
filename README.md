<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<div align="center">    
 
# Hexa Encrytion v1.1

<!-- [![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/NeurIPS-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/ICLR-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)   -->
<!-- 
ARXIV   
[![Paper](http://img.shields.io/badge/arxiv-math.co:1480.1111-B31B1B.svg)](https://www.nature.com/articles/nature14539) -->

<!-- ![CI testing](https://github.com/PyTorchLightning/deep-learning-project-template/workflows/CI%20testing/badge.svg?branch=master&event=push) -->


<!--  
Conference   
-->   
</div>
 
## Description   
 스도쿠 퍼즐은 9x9의 크기의 칸을 각 행, 열 그리고 3x3의 박스에 숫자를 1부터 9까지 중복되지 않게 입력하여 완성하는 퍼즐입니다.   
이 스도쿠 퍼즐을 16x16 크기로 확장한 헥사 도쿠에서 아이디어를 얻어 암호 알고리즘을 만들었습니다.


## How to run   
먼저, 의존성 패키지를 설치하세요   
```bash
# install numpy and others

python3 -m virtualenv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```   

## Encryption
```bash
python3 encryption.py
```

```bash
 ___  ___  _______      ___    ___ ________                                                     
|\  \|\  \|\  ___ \    |\  \  /  /|\   __  \                                                    
\ \  \\\  \ \   __/|   \ \  \/  / | \  \|\  \                                                   
 \ \   __  \ \  \_|/__  \ \    / / \ \   __  \                                                  
  \ \  \ \  \ \  \_|\ \  /     \/   \ \  \ \  \                                                 
   \ \__\ \__\ \_______\/  /\   \    \ \__\ \__\                                                
    \|__|\|__|\|_______/__/ /\ __\    \|__|\|__|                                                
                       |__|/ \|__|                                                              
                                                                                                
                                                                                                
 _______   ________   ________  ________      ___    ___ ________  ___  ________  ________      
|\  ___ \ |\   ___  \|\   ____\|\   __  \    |\  \  /  /|\   __  \|\  \|\   __  \|\   ___  \    
\ \   __/|\ \  \\ \  \ \  \___|\ \  \|\  \   \ \  \/  / | \  \|\  \ \  \ \  \|\  \ \  \\ \  \   
 \ \  \_|/_\ \  \\ \  \ \  \    \ \   _  _\   \ \    / / \ \   ____\ \  \ \  \\\  \ \  \\ \  \  
  \ \  \_|\ \ \  \\ \  \ \  \____\ \  \\  \|   \/  /  /   \ \  \___|\ \  \ \  \\\  \ \  \\ \  \ 
   \ \_______\ \__\\ \__\ \_______\ \__\\ _\ __/  / /      \ \__\    \ \__\ \_______\ \__\\ \__\
    \|_______|\|__| \|__|\|_______|\|__|\|__|\___/ /        \|__|     \|__|\|_______|\|__| \|__|
                                            \|___|/                                             
Hexa Encryption v1.1                                                                                        
----- 평문을 입력하세요. -----
안녕하세요!!!
----- 키를 입력하세요 -----
This is Key!
----- 암호화를 시작합니다. -----
5c8f6b36c00d567e4734858e4a37592d7da0f020293ba32fb14d71cdd933d693
----- 암호문이 완성되었습니다. -----
소요시간 : 0.8464460372924805초
```

## Decryption
```bash
python3 decryption.py
```

```bash
 ___  ___  _______      ___    ___ ________                                                    
|\  \|\  \|\  ___ \    |\  \  /  /|\   __  \                                                   
\ \  \\\  \ \   __/|   \ \  \/  / | \  \|\  \                                                  
 \ \   __  \ \  \_|/__  \ \    / / \ \   __  \                                                 
  \ \  \ \  \ \  \_|\ \  /     \/   \ \  \ \  \                                                
   \ \__\ \__\ \_______\/  /\   \    \ \__\ \__\                                               
    \|__|\|__|\|_______/__/ /\ __\    \|__|\|__|                                               
                       |__|/ \|__|                                                             
                                                                                               
                                                                                               
 ________  _______   ________  ________      ___    ___ ________  ___  ________  ________      
|\   ___ \|\  ___ \ |\   ____\|\   __  \    |\  \  /  /|\   __  \|\  \|\   __  \|\   ___  \    
\ \  \_|\ \ \   __/|\ \  \___|\ \  \|\  \   \ \  \/  / | \  \|\  \ \  \ \  \|\  \ \  \\ \  \   
 \ \  \ \\ \ \  \_|/_\ \  \    \ \   _  _\   \ \    / / \ \   ____\ \  \ \  \\\  \ \  \\ \  \  
  \ \  \_\\ \ \  \_|\ \ \  \____\ \  \\  \|   \/  /  /   \ \  \___|\ \  \ \  \\\  \ \  \\ \  \ 
   \ \_______\ \_______\ \_______\ \__\\ _\ __/  / /      \ \__\    \ \__\ \_______\ \__\\ \__\
    \|_______|\|_______|\|_______|\|__|\|__|\___/ /        \|__|     \|__|\|_______|\|__| \|__|
                                           \|___|/                                             
                                                                                               
                                                                                                                                          
Hexa Decryption v1.1                                                                                        
----- 암호문을 입력하세요. -----
5c8f6b36c00d567e4734858e4a37592d7da0f020293ba32fb14d71cdd933d693
----- 키를 입력하세요 -----
This is Key!
----- 복호화를 시작합니다. -----
안녕하세요!!!
----- 평문이 완성되었습니다. -----
소요시간 : 0.8663084506988525초
```

## 개발 환경
<table>
  <tr>
    <td align="center">스택</a></td>
    <td align="center">운영체제</td>
    <td align="center">사용 언어</td>
  </tr>
  <tr>
    <td align="center">Floodnut</a></td>
    <td align="center"><a>Ubuntu 20.04 LTS<br/>MacOS Big Sur</a></td>
   <td align="center"><a>Python 3.8.10</a></td>
  </tr>
  <tr>
    <td align="center">cobolnet</a></td>
    <td align="center"><a>Windows 10<br/>MacOS Big sur</a></td>
   <td align="center"><a>Python 3.9.</a></td>
  </tr>
  <tr>
  <td align="center">nsih</a></td>
  <td align="center"><a>Windows 10</a></td>
 <td align="center"><a>Python 3.9.</a></td>
</tr>
</table>

## 동작 환경
Python 3.8 이상이 설치된 환경


## 알고리즘 설명
헥사 암호화는 256비트 블록의 대칭키 암호화 알고리즘입니다.
지원하는 입력 평문 및 키는 UTF-8 문자입니다.

	1. 키와 평문을 입력합니다.  

	2. 키는 SHA-256으로 해시화 한 후 키는 256비트의 16x16의 테이블에 입력됩니다.

	3. 평문은 256 비트 블록 단위로 쪼개어지며 제로 패딩으로 패딩됩니다.

	4. 키를 한 행씩 읽어 16으로 나머지 연산을 수행합니다.
		나머지 연산의 결과를 4x4의 박스에 행 번호에 맞게 넣습니다.
		중복된 값은 공백으로 비워둔 후 16행을 모두 수행하면 빈 칸을 0부터 F까지 사용하지 않은 값으로 순서대로 채워넣습니다.

	5. 박스를 헥사도쿠 테이블에 넣은 후 이 박스를 통해 헥사도쿠 테이블을 완성합니다.

	6. 완성된 헥사도쿠 테이블은 전치 테이블로 사용됩니다.
		4x4의 16개의 박스가 존재하고 첫번째 박스는 전체 박스의 순서를 결정합니다.
		첫번째 박스를 포함한 전체 박스 내부의 각 칸의 값은 값을 채워넣을 순서를 결정합니다.

	7. 평문블록을 테이블에 전치한 후 키와 XOR합니다.

	8. 키는 라운드 별로 우-하향 시프트합니다.

	9. 헥사도쿠 테이블은 박스와 박스 내부 값을 짝수 라운드에 우측 시프트, 홀수 라운드에 하향 시프트 합니다.

	10. 총 16라운드를 수행하여 암호문을 완성합니다. 



## 버그 제보
버그 제보는 이슈를 통해 부탁드립니다!


## 업데이트 내역.
<table>
  <tr>
    <td align="center">버전</a></td>
    <td align="center">업데이트 내역</td>
    <td align="center">업데이트 날짜</td>
  </tr>
    <tr>
    <td align="center">1.0</a></td>
    <td align="center"><a>헥사 암호 알고리즘 1.0 완성</a></td>
   <td align="center"><a>2021.12.03</a></td>
  </tr>
    <tr>
    <td align="center">1.1</a></td>
    <td align="center"><a>전치 테이블 P_table의 박스 시프트 알고리즘 추가</a></td>
   <td align="center"><a>2021.12.06</a></td>
  </tr>
 </table>
> 전체 내역 확인 : https://github.com/students16/2021crypto

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Floodnut"><img src="https://avatars.githubusercontent.com/u/15941204?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Floodnut</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/cobolnet"><img src="https://avatars.githubusercontent.com/u/82963112?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cobolnet</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/nsih"><img src="https://avatars.githubusercontent.com/u/81147612?v=4?s=100" width="100px;" alt=""/><br /><sub><b>nsih</b></sub></a><br /></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
