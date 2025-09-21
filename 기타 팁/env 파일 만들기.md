# 가상환경 만들기

1. 해당 터미널의 해당 디렉터리로 이동한다
2. 파일을 생성한다 : python3 -m venv .venv
3. 가상환경에 접속했는지 확인한다 : which python. 
/.venv/bin/python 이 출력되면 성공
4. 원하는 라이브러리, 프레임워크를 설치한다.
5. pip3 list : 설치된 라이브러리를 확인한다.
6. pip3 freeze > requirements.txt: requirements.txt파일을 만들어 설치된 프레임 워크를 확인한다.  
(프레임워크를 다른 가상환경에서 편하게 설치하기 위해서)