# WebDataCollector_forLET(延命治療の意思決定支援のためのデータ収集用サイト)
LET : 延命治療の意思決定支援

## 概要


## ローカル開発用
```
$ git clone http://ubuntu.b3.is.tokushima-u.ac.jp:8080/gitbucket/git/doi-yuta/WebDataCollector_forLET.git
$ cd WebDataCollector_forLET/django
$ virtualenv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python manage.py migrate
(venv)$ python manage.py migrate
```

## デプロイ先
```
$ git clone http://ubuntu.b3.is.tokushima-u.ac.jp:8080/gitbucket/git/doi-yuta/WebDataCollector_forLET.git
$ cd WebDataCollector_forLET
$ docker-compose up -d
```

## 注意
- SELinuxの設定はしておく
- バックアップする際は，以下のディレクトリを作成
  ```
  $ mkdir /tmp/weblet_backup
  ```
#   w e b D a t a C o l l e c t o r _ f o r L E T - m a s t e r  
 