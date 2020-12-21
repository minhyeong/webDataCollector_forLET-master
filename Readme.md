
# Web アプリケーション
- 作成者
    - 土井 優太
    - 今村 光男

## 環境
- Ubuntu Linux 20.04 LTS
    - インストールは[ここ参照](https://qiita.com/Aruneko/items/c79810b0b015bebf30bb)
    - Windows で運用する場合は不要
        - psql の認証方法とかは psql.exe で設定できる
- [Docker for windows (Edge)](https://www.docker.com/products/docker-desktop)
    - Egde でちゃんと wsl2 対応してるものをインストールすること

## 手順
1. wsl2 の導入
1. Docker の導入
1. PostgreSQL の導入
1. WebApp の起動

## wsl2 の導入
1. windows のバージョンを確認
    - 設定 > バージョン情報(一番下)
        - OS ビルド : 18362.1082
            - 18362 or 18363 かつ 1049 以上 であれば導入可能<br>
            バージョンが古い場合 windows update を行うこと

1. powershellを管理者権限で起動

1. Linux ディストリビューションのバージョンを確認
    ```
    > wsl --list --verbose

      NAME            STATE           VERSION
    * Ubuntu-20.04    Stopped         1
    ```
    - version が 2 ならこの工程は無視して大丈夫です

1. [Linux カーネル更新プログラムパッケージ](https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-kernel)からコンポーネントを更新する

1. wsl2 をデフォルト設定に変更後、再起動
    ```
    wsl --set-default-version 2
    net stop LxssManager
    net start LxssManager
    ```
    - 後は　AppStore から好きなバージョンの ubuntu をダウンロード

1. 既存のものに適用する場合
    - ``※変換時にファイルがいろいろ削除されることがあるのでバックアップ取っておいてください``
    ```
    > wsl --set-version Ubuntu-20.04 // ちゃんとバージョン調べること

    変換中です。この処理には数分かかることがあります...
    WSL 2 との主な違いについては、https://aka.ms/wsl2 を参照してください
    変換が完了しました。

    > wsl --list --verbose

      NAME            STATE           VERSION
    * Ubuntu-20.04    Stopped         2
    ```


## Docker の導入
1. パッケージインデックスの更新
    - 入れたばかりでも一応更新しておくと良いかも
    - 端末右クリック > プロパティ > Ctrl+Shift+C/V にチェック入れるとコピペが楽になります
        ```
        sudo apt-get update
        ```
    - ``dpkgが中断されました`` とかエラーが出たら多分エラーをクリアするとなんとかなると思います.
        ```
        cd /var/lib/dpkg/updates
        sudo rm *
        sudo apt-get update

        // これでもダメな場合以下も削除
        sudo rm /var/lib/apt/lists/lock
        sudo rm /var/cache/apt/archives/lock
        sudo apt-get update
        ```
    - ``E: Unable to locate package softwareproperties-common``とかエラー出た場合
        - 原因はパッケージを探すリポジトリが古いから名前がない
        ```
        sudo apt-get install apt-file
        sudo apt-file update        
        ```

1. 前提ソフトのインストール
    ```
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    ```
    
1. GPG 公開鍵のインストール
    - docker のパッケージを復号化するのに使います.
        ```
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        ```
        - 失敗する場合、gpg を再インストール
            ```
            sudo apt remove gpg
            sudo apt install gnupg1
            ```
        - 公開鍵のフィンガープリント
            - public key が、目的のものであるか確認するために用います.
            ```
            $ sudo apt-key fingerprint 0EBFCD88

            pub   4096R/0EBFCD88 2017-02-22
            フィンガー・プリント = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
            uid                  Docker Release (CE deb) <docker@docker.com>
            sub   4096R/F273FCD8 2017-02-22
            ```

1. aptリポジトリの設定
    - apt-get で取得する先のリポジトリを登録
    ```
    sudo apt-get install software-properties-common
    sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
    ```

1. Docker-ce のインストール
    - 結構時間かかります
    ```
    sudo apt-get update
    sudo apt-get install docker-ce
    ```
    
1. 一般ユーザでの実行
    - root でなく一般ユーザで docker を実行する場合には docker グループに所属している必要があります.
    - 念のため、実行後 wsl を再起動することを勧めます.
    ```
    sudo usermod -aG docker <アカウント名>
    ```

1. バージョン確認
    ```
    $ sudo service docker start
    $ docker version

    Client: Docker Engine - Community
        (略)

    Server: Docker Engine - Community
        (略)
    ```

1. docker-compose のインストール
    - [ここでバージョンを確認すること](https://github.com/docker/compose/releases)
        - 2020/09/01 現在だと 1.26.2 が最新
    ```
    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

1. docker-compose に実行権限追加
    ```
    sudo chmod +x /usr/local/bin/docker-compose
    ```
1. 正常にインストールされたか確認
    ```
    $ docker-compose --version

    docker-compose version 1.26.2, build eefe0d31
    ```

## PostgreSQLの導入

1. PostgreSQL の導入
    - 時間かかります
    ```
    sudo apt-get update
    sudo apt-get install postgresql
    ```

1. たまに不正常なまま起動しているので再起動しておきます
    ```
    $ sudo /etc/init.d/postgresql restart

    * Restarting PostgreSQL 12 database server                                                                      [ OK ]
    ```

1. 認証方法の変更とログイン
    - このままだとログインできないので認証方法を変更する
    ```
    $ sudo vi /etc/postgresql/12/main/pg_hba.conf

    // 下にある peer を md5 に変更して保存
    # "local" is for Unix domain socket connections only
    local   all             all                                     md5 #peer
    ```
    - 認証変更したらログインしてパスワード設定
        - ここではパスを postgres としています
    ```
    $ sudo su postgres -c 'psql --username=postgres' // postgres=# ってでたらOK
    # ALTER USER postgres with encrypted password 'postgres'; // ";" つけないと入力まち続ける
    
    ALTER ROLE
    
    # \q // ログアウト
    ```
    - 次は postgres の認証方法を変更
    ```
    $ sudo vi /etc/postgresql/12/main/pg_hba.conf

    // 今度は `postgres` の認証を変更 ※パスワード変える前にやらないこと
    # Database administrative login by Unix domain socket
    local   all             postgres                                md5 #peer
    ```
    - サーバ再起動させる
    ```
    sudo /etc/init.d/postgresql restart
    ```
    - ログインできるか確認
    ```
    $ psql -U postgres

    postgres=# // これがでたら完了
    ```

1. データベース作成
    ```
    $ psql -U postgres

    # create database データベース名; // ここでは "db" としています
    CREATE DATABASE

    # \l

    // 作ったデータベース名が表示されれば完了
      Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
    -----------+----------+----------+-------------+-------------+-----------------------
    db        | postgres | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 |
    postgres  | postgres | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 |
    template0 | postgres | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | =c/postgres          +
              |          |          |             |             | postgres=CTc/postgres
    template1 | postgres | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | =c/postgres          +
              |          |          |             |             | postgres=CTc/postgres
    (4 rows)
    ```

1. データベースユーザの作成
    - データベースに接続するユーザの作成を行う<br>
    ここではユーザ名を'db_test', パスワードを'password'としている<br>
    CREATE ROLE と出ない場合、 ";" が抜けているか、綴りが間違っている
        ```
        create user db_test with password 'postgres';
        ```
    - 次に、タイムゾーンや Django の推奨設定を行う
        ```
        ALTER ROLE db_test SET client_encoding TO 'utf8';
        ALTER ROLE db_test SET default_transaction_isolation TO 'read committed';
        ALTER ROLE db_test SET timezone TO 'Asia/Tokyo';
        ```
    - 最後にユーザに対しテーブルへの接続権利を与えてセッションを終える
        ```
        GRANT ALL PRIVILEGES ON DATABASE db TO db_test;
        ```

## WebApp
1. Docker 動いてるか確認しておく
    ```
    $ sudo service docker status
    * Docker is not running

    // not running とか言ってたら起動させる
    $ sudo service docker start
    ```

1. pyenv のインストール
    - 必要なライブラリのインストール
        ```
        sudo apt update
        sudo apt-get install git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev
        ```
    - git から pyenv のインストールとパスを通す
        ```
        git clone https://github.com/pyenv/pyenv.git ~/.pyenv

        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
        echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

        source ~/.bash_profile
        ```
    - バージョン確認
        ```
        $ pyenv -v

        pyenv 1.2.20-5-g1ec3c6f1
        ```
    - python 3.6.10 をインストール
        ```
        pyenv install 3.6.10
        ```
    - python のバージョン一覧
        ```
        $ pyenv versions

        * system (set by /home/imamura/.pyenv/version)
          3.6.10
        ```

1. webDataCollector_forLET-master の導入
    - git からとってくる
        ```
        git clone https://github.com/minhyeong/webDataCollector_forLET-master.git
        cd webDataCollector_forLET-master
        pyenv local 3.6.10 // python のバージョンを指定
        ```
    - django/data_collector/setting.py の DATABASEの中身を書き換える
        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres', // psqlで設定したデータベース名
                'USER': 'postgres', // psqlで設定したユーザ名
                'PASSWORD': 'password', // psqlで設定したユーザのパスワード
                'HOST': 'db', // 開発環境では localhost, コンテナ作成するときは db
                'PORT': 5432, // 余計な事してなければ 5432 になるはず
            }
        }
        ```
    - マウント先を指定
        ```
        sudo mkdir /sys/fs/cgroup/systemd
        sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd
        ```
    - コンテナを作成する
        ```
        $ docker-compose up --build // 一回ビルドしたら次からは --build はいらないです

        django_1  | [2020-11-20 03:43:58 +0000] [1] [INFO] Starting gunicorn 19.7.1
        django_1  | [2020-11-20 03:43:58 +0000] [1] [INFO] Listening at: http://0.0.0.0:3031 (1)
        django_1  | [2020-11-20 03:43:58 +0000] [1] [INFO] Using worker: sync
        django_1  | [2020-11-20 03:43:58 +0000] [14] [INFO] Booting worker with pid: 14
        ```
    - 接続してみる
        1. 好きなブラウザで localhost に接続
    
    ![アンケートサイト](material/site.png)

----

## 参考文献
1. [WSL2 を Windows バージョン 1909 で使用する](https://kawadev.net/wsl2/)

1. [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

1. [WSLで docker を install するときにハマった話](https://qiita.com/obukoh/items/416c4cb1b88261bf3357)

1. [Docker のインストールの意味を完全に理解してみる](https://qiita.com/TsuyoshiUshio@github/items/2a81a55bceed5fa11c4f)

1. [Ubuntu に docker をインストールする](https://qiita.com/tkyonezu/items/0f6da57eb2d823d2611d)

1. [Ubuntu に docker と docker-compose を入れる](https://qiita.com/mochizukikotaro/items/ae7ae1461ea4bf495bd0)

1. [Docker で Django を動かしてみた](https://note.com/tico0602/n/nb2ea4f0b51f8)
