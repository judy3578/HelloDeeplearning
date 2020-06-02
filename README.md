# HelloDeeplearning
20181204 개설
123



### 리눅스 명령어 
<모듈 설치>

~/.venv/py367tf/bin/python -m pip install jupyter

~/.venv/py367tf/bin/python -m pip install matplotlib

~/.venv/py367tf/bin/pip install scikit-image

​

<activate 방법>

source ~/.venv/py367tf/bin/activate    내가 무슨 파이썬을 실행하고 있는지를 알고 써야한다. 여러 버전의 파이썬이 깔려있을 수 있기에 내가 지금 하는 프로젝트에서 쓸 버전을 activate해준다.

가상환경이 없다면 만들어주도록 한다. 내가 잘쓰는 폴더에 .venv 폴더를 만들고 cmd를 켜서 이 안에 python을 설치한다. 그리고 앞으로 새로운 모듈을 설치할 때만다 이 경로로 설치해야 좋다. ~./venv/py369/bin/pip install librosa

​

<리눅스에서 폴더 삭제할때>

rm -rf folderName           ---> 디렉토리와 하위 파일까지 삭제 됨. 주의

r : 파일 디렉토리 함께 삭제하기

f : 파일 유무와 상관없이 삭제하기

v : 어떻게 완료되었는지 설명하기

​

<GPU 및 돌아가고 있는지 확인>

nvidia-smi           

netstat -ntlp

jupyter-notebook list

​

<돌아가는 GPU 중단>

kill -9 PID번호

​

<사용되는 메모리 확인>

df -h  --> 쓰고 있는 메모리 확인

df -i

​

<HISTORY>

!숫자 ---> history 입력한 후  !숫자 치면 그 번호의 명령어가 실행된다.

​

<UI로 서버 폴더들 보고 싶을때>

gnome-commander &

​

<압축 푸는 법>

unzip 파일명.zip

​

<파일 전송>

지금 서버 --> 다른 서버로 파일전송시

rsync -avz --exclude '@*' --exclude '*.db' --exclude '.*' --exclude '__pycache__' --exclude 'Thumbs.db' --delete /home/경로/ 사용자아이디@IP주소:/경로/

​

rsync -avz --exclude '@*' --exclude '*.db' --exclude '.*' --exclude 'Thumbs.db' --exclude '__pycache__'--delete hyejoo@IP주소:/home/hyejoo/work/repos/어쩌구/ /home/hyejoo/work/repos/어쩌구

​

​

<vi 편집기>

vi 편집기는 텍스트 에디터로 리눅스 등의 텍스트 기반 터미널에서 사용된다.

:q! ----> 는 저장하지 않고 종료하는 명령어

​

https://m.blog.naver.com/occidere/220844431751


 
6. Vi 에디터 명령어 및 사용법 (2017-07-10 수정)
오랜만에 써보는 리눅스 관련 포스팅이다.(사실 몇일 전 테스트 한다고 이것저것 해보다가 리눅스를 통째로...

m.blog.naver.com

​

<screen 쓰는 방법>

내가 사용할 파일이 있는 폴더까지 cd + 폴더이름으로 들어간다(tab치면 자동완성됨)

screen -S project 라고 치면 스크린이 시작되고

학습 돌려놓고 ctrl+A 누르고 D누르면 스크린에서 빠져나온다

다시 들어가고 싶을땐 screen -r 번호 치면 내가 열어놓은 스크린중 친 번호의 스크린이 다시 켜진다.

스크린이 좋은 점은 내가 실수로 화면 덮어버려도 다시 스크린만 열면 된다는 것이다.

​

​

​

<쉘이란>

쉘이란 

https://dohk.tistory.com/186  ----> 쉘, 터미널 등등..

쉘(shell)에 대하여
쉘의 개념, bashrc의 개념: https://dohk.tistory.com/191 1. 커널 컴퓨터 과학에서 커널(kernel)은 운영 체제의 핵심 부분으로서, 운영 체제의 다른 부분 및 응용 프로그램 수행에 필요한 여러 가지 서비스를 제..

dohk.tistory.com

<문제 해결>

1. 서버를 바꿨는데 코드가 돌아가지 않을 때

pip list를 쳐서 설치된 모듈 중 텐서플로와 케라스의 버전확인

주피터에서 

import tensorflow as tf  

print(tf.__version__)

import keras

print(keras.__version__)

해서 버전 확인. 둘 중 하나라도 이전서버에서 쓰던 버전과 다르다면 코드가 안돌아갈 수 있다.

​

2. 코드를 돌리는데 중간에 커널이 자꾸 죽는다

돌리고 있던 코드가 gpu를 전부 사용중인데 새로운 코드를 돌리려고 해서 그럴 수 있다.

사용안하는 gpu로 새로운 코드를 돌리던지, 돌아가던 코드가 다 돌고나서 nvidia-smi로 gpu사용량 확인하고 새로운 코드 돌릴 것.

​

3. 모듈이 없어서 install을 했는데 에러가 뜨면서 설치가 안될 때

나는 memory_profiler라는 모듈이 없었고 이 모듈 설치를 위해서는 psutil이 설치되어야 했는데 어마무시한 에러가 뜨고 설치가 안됐다.

https://github.com/giampaolo/psutil/issues/1143


 
psutil fails to install on python3.6 and Ubuntu16.04 · Issue #1143 · giampaolo/psutil
install psutil with pip on python3.6 gives this error I've tried installing different versions of psutil with the same error Command "/usr/bin/python3.6 -u -c "import setuptools, toke...

github.com

이 사이트를 참고하니 sudo apt-get install python3.5-dev를 하라고 해서 해보려고 했지만 나는 sudo 권한이 없어서 부여받은 다음 시도했다.

dpkg -l 을 하면 설치된 모든 패키지를 볼 수 있다길래 해봤더니 나는 python 3.6으로 되어있길래 나는 sudo apt-get install python3.6-dev를 해주고 그 뒤에 psutil을 설치했더니 문제 없이 설치됐다. 정말 힘들었다..

​

4. gpu 메모리가 이상

cuda version 이 잘못되어 있었음.

nvcc --version 을 통해  cuda 버젼 확인가능


https://datamasters.co.kr/33?category=783262


Keras, Tensorflow에서 GPU 똑똑하게 사용하기 - 1부
이번 포스팅에서는 Keras와 Tensorflow에서 GPU를 더 똑똑하게 사용하는 방법에 대해 알아보자. 케라스 (와 당연히 텐서플로우)를 사용한다면, GPU도 높은 확률로 사용 중일 것 이다. 근데 이놈의 텐서플로우는 d..

datamasters.co.kr

​
