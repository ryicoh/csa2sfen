csa2sfen
========

将棋のCSA形式の棋譜をSFENに変換するツールです。

インストール
------------

::

   git clone https://github.com/ryicoh/csa2sfen
   pip install pipenv
   pipenv install

使用例
------

ファイルから読み込み

::

   pipenv run csa2sfen ./u57z4dp0x32t.csa

URLから読み込み

::

   pipenv run csa2sfen https://jisn7d4exc.execute-api.ap-northeast-1.amazonaws.com/prod/quest/games/u57z4dp0x32t.csa
