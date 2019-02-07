django

1. 폴더생성

   mkdir

2. -django설치

   ​	pip install django

   -startproject

   ​	django-admin startproject [플젝이름] .

   -startapp

   ​	python manage.py startapp [앱이름]

python manage.py runserver $IP:$PORT

python manage.py startapp pages

pyenv local intro-venv

pyenv virtualenv 3.6.7 intro-venv  

pip install django  



//

pip install Pillow





pip install pilkit

pip install django-imagekit pilkit





REST의 구성

​	자원(Resource)-URL

​	행위(Verb)-HTTP Method

​	표현(Representations)



REST API 디자인 가이드

1. URI는 정보의 자원을 표현해야한다.
2. 자원에 대한 행위는 HTTP Method(GET,PUT,DELETE)로 표현한다.



예시

```DJANGO
GET/ movies/show/1  (x)
GET/ movies/1		(o)

GET/ movies/create  (x)-get method는 자원생성에 부적합.
POST/ movies        (o)

GET/ movies/2/update (x)
PUT/ movies/2        (o)

GET/ moives/2/edit   - 수정 페이지 보여줌
POST/ movies/2/edit  - 수정 작업을 수행함
```

