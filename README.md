# Python Miniconda environment construction

- author: laplaciannin102
- date: 2021/04/05
- version: 0.0.2

---

## Table of Contents

- [Python Miniconda environment construction](#python-miniconda-environment-construction)
  - [Table of Contents](#table-of-contents)
  - [背景](#背景)
  - [概要](#概要)
  - [本記事で触れない内容](#本記事で触れない内容)
  - [対象読者](#対象読者)
  - [作業環境](#作業環境)
  - [対応するGitHubリポジトリとQiita記事](#対応するgithubリポジトリとqiita記事)
  - [作業手順](#作業手順)
    - [batファイルのダウンロード](#batファイルのダウンロード)
    - [Anaconda環境から引越す準備](#anaconda環境から引越す準備)
    - [Anacondaのアンインストール](#anacondaのアンインストール)
    - [Miniconda+conda-forge環境構築](#minicondaconda-forge環境構築)
  - [Appendix](#appendix)
    - [batファイルの中身概要](#batファイルの中身概要)
  - [参考](#参考)
    - [Anaconda有償化関連](#anaconda有償化関連)
    - [Anaconda全般](#anaconda全般)

---

## 背景

- 従業員数200名以上の営利企業でのAnaconda利用が有償化された.


## 概要

- Anacondaの有償化を受けて, これまでAnaconda環境を使用していた方がAnacondaのパッケージを引き継ぎ**Miniconda+conda-forge**環境に移行するための手順.
- Pythonパッケージ一覧を**出力**するbatファイルを作成した.
- Pythonパッケージ一覧を**一括でインストール**するbatファイルを作成した.
  - pip版とconda版あり.


## 本記事で触れない内容

- 仮想環境関連
  - **env(venv, pyenv, pipenv)
  - docker


## 対象読者

- 新規にPythonをインストールする方
(以下, **新規Pythonユーザ**).
- すでにAnacondaを使用してPythonをインストールしている方
(以下, **既存Anacondaユーザ**).
  - かつ, AnacondaをアンインストールしてMiniconda環境に移行する方.


---

## 作業環境

| No. | 項目 | 想定      | 
| :-: | :--: | :-------: | 
| 1   | OS   | Windows10 | 

---

## 対応するGitHubリポジトリとQiita記事

- **GitHubリポジトリ:**
  - リポジトリ名: [py_miniconda_env_construction](https://github.com/laplaciannin102/py_miniconda_env_construction)

  - URL: [https://github.com/laplaciannin102/py_miniconda_env_construction](https://github.com/laplaciannin102/py_miniconda_env_construction)

- **Qiita記事:**
  - [(Qiita)Anaconda有償化に伴いMiniconda+conda-forgeに引越しをした](https://qiita.com/AnnnPsinan414/private/7782a753347ff8ba448d)

---

## 作業手順

### batファイルのダウンロード

1. [py_miniconda_env_constructionリポジトリ](https://github.com/laplaciannin102/py_miniconda_env_construction)へアクセスする.
   - URL: [https://github.com/laplaciannin102/py_miniconda_env_construction](https://github.com/laplaciannin102/py_miniconda_env_construction)

2. **git clone** または **zipのダウンロード** を行い, batファイルを取得する.
   - git cloneできない方:
     1. 右上の「Code」を押下する.
     2. 「Download ZIP」を押下する.
     3. 任意の場所に保存する.
     4. zipファイルの解凍を行う.
   - **git clone command:**

     ```bash
     git clone https://github.com/laplaciannin102/py_miniconda_env_construction.git
     ```

- batファイルの一覧(3種類)

| No. | batファイル名                      | 説明                                                                                          | 
| :-- | :--------------------------------- | :-------------------------------------------------------------------------------------------- | 
| 1   | no001_backup_python_packages.bat   | - Pythonにおけるインストール済みパッケージの一覧をバックアップテキストファイルとして取得する. | 
| 2   | no002_conda_install_from_files.bat | - `conda install`を使用して, テキストファイルから一括でパッケージをインストールする.          | 
| 3   | no003_pip_install_from_files.bat   | - `pip install`を使用して, テキストファイルから一括でパッケージをインストールする.            | 

- 各batファイルで大体何をしているのかは, [batファイルの中身概要](#batファイルの中身概要)を参照.

---

### Anaconda環境から引越す準備

- 本手順は**既存Anacondaユーザ**向け手順である.
   - **新規Pythonユーザ**は[Miniconda+conda-forge環境構築](#minicondaconda-forge環境構築)を参照.

1. インストール済みパッケージバックアップ用batファイルを実行する.
   - ダブルクリック or 右クリックして「開く」 or 右クリックして「管理者として実行」
   - **実行ファイル名:**
     - **no001_backup_python_packages.bat**
   - **処理概要:**
     - インストール済みパッケージの一覧をバックアップテキストとして取得する.
     - python_pkgs_filesという名前のディレクトリを作成し, その中にテキストファイルを格納する.
     - Anacondaにプリインストールされているパッケージの一覧も同時に取得する.
       - Anaconda package lists: [https://docs.anaconda.com/anaconda/packages/pkg-docs/](https://docs.anaconda.com/anaconda/packages/pkg-docs/)
   - **出力先ディレクトリ:**
     - ./python_pkgs_files/
   - **出力ファイル一覧:**
     - いわゆる**requirements.txt**と同様のファイル群.
     - **yyyymmdd**は作業日付.

    | ファイル名                                        | 説明                                                                                                                                         | 
    | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------- | 
    | conda_pkgs_list_raw.txt                           | - condaのパッケージ一覧ファイル.<br>- `conda list --export`で取得.                                                                           | 
    | conda_pkgs_list_eq_**yyyymmdd**.txt               | - condaのパッケージ一覧のversionを **[package]==x.x.x** で設定したファイル.                                                                  | 
    | conda_pkgs_list_geq_**yyyymmdd**.txt              | - condaのパッケージ一覧のversionを **[package]>=x.x.x** で設定したファイル.                                                                  | 
    | pip_pkgs_list_raw.txt                             | - pipのパッケージ一覧ファイル.<br>- `pip list --format freeze`で取得.<br>- `pip freeze`だとversion部分がURLになってしまう場合がある.         | 
    | pip_pkgs_list_eq_**yyyymmdd**.txt                 | - pipのパッケージ一覧のversionを **[package]==x.x.x** で設定したファイル.                                                                    | 
    | pip_pkgs_list_geq_**yyyymmdd**.txt                | - pipのパッケージ一覧のversionを **[package]>=x.x.x** で設定したファイル.                                                                    | 
    | anaconda_preinstall_pkgs_list_eq_**yyyymmdd**.txt | - Anacondaにプリインストールされているパッケージの一覧ファイル.<br>- これを使用することで, Anaconda環境と同様のパッケージをインストール可能. | 
    | anaconda_preinstall_pkgs_list_eq_**sample**.txt   | - sampleファイル.<br>- anaconda_preinstall_pkgs_list_eq_**yyyymmdd**.txtと同様の内容.                                                        | 

---

### Anacondaのアンインストール

- 本手順は**既存Anacondaユーザ**向け手順である.
   - **新規Pythonユーザ**は[Miniconda+conda-forge環境構築](#minicondaconda-forge環境構築)を参照.

1. Anaconda Promptを起動する.
2. 次のコマンドを入力し, **anaconda-clean**というパッケージをインストールする.

    ```bat
    conda install anaconda-clean
    ```

3. 次のコマンドを入力し, Anaconda関連のファイルやディレクトリを削除する.
   - 各項目について確認しながら削除を行う場合:

    ```bat
    anaconda-clean
    ```
   - 各項目について確認せず一括で削除を行う場合:

    ```bat
    anaconda-clean --yes
    ```

4. Windowsの場合, コントロールパネルを起動する.
5. プログラムと機能 > プログラムのアンインストール を開く.
6. Anacondaを選択し, アンインストールする.

- Anacondaの[公式ドキュメント(Uninstalling Anaconda)](https://docs.anaconda.com/anaconda/install/uninstall/)も参照のこと.

---

### Miniconda+conda-forge環境構築

1. Minicondaのインストーラを下記URLからダウンロードする.
   - Miniconda: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

2. インストーラを実行し, Minicondaをインストールする.
   1. 「Miniconda3~.exe」を実行する. セットアップウィザードが表示される.
   2. 最初の画面で, 「Next」を押下する.
   3. 「I Agree」を押下する.
   4. Install forはJust Meのまま「Next」を押下する.
   5. インストール先の指定では任意の場所を指定して, 「Next」を押下する.
      - 好みが無い方は初期設定のままでok.
   6. 「Add Miniconda3 to my PATH environment variable」にチェックを入れる.
   7. 「Install」を押下する.
   8. インストールされるので待機する.

3. (インストール済みMinicondaの)Anaconda Promptを立ち上げる.
   - Windows10の場合, 左下の虫眼鏡アイコンから検索に「anaconda prompt」と入力すれば表示される.
   - **Anaconda Prompt(Miniconda3)** というソフト名.
   - 他cmdなどのコマンドラインでも可能.

4. 次のコマンドを入力し, condaのチャネルの設定に**conda-forge**チャネルを追加する.

    ```bat
    conda config --add channels conda-forge
    ```

5. 次のコマンドを入力し, condaのチャネル一覧を確認する.

    ```bat
    conda config --show channels
    ```
   - `conda config --get channels`でも可能.

6. 次のコマンドを入力し, condaのチャネルの設定から**defaults**チャネルを削除する.

    ```bat
    conda config --remove channels defaults
    ```

7. 次のコマンドを入力し, condaのチャネル一覧を確認する. チャネル一覧からdefaultsが消えていることを確認する.

    ```bat
    conda config --show channels
    ```
   - `conda config --get channels`でも可能.

8. 次のコマンドを入力し, conda自体を最新版にUpdateする.

    ```bat
    conda update conda
    ```

8. 次のコマンドを入力し, インストール済みパッケージを全て最新版にUpdateする.
   - ※Miniconda使用のため, 不要.

    ```bat
    conda update --all
    ```

9.  パッケージインストール用batファイルを実行する.
   - ダブルクリック or 右クリックして「開く」 or 右クリックして「管理者として実行」
   - 使用するパッケージ管理ツール毎に実行するbatファイルが異なる.
     - condaの場合:
       - **no002_conda_install_from_files.bat**
     - pipの場合:
       - **no003_pip_install_from_files.bat**
   - 「>>○○」という行は, 裏でどのようなコマンドが実行されてるか参考までに表示しているもの.

11. コマンドライン(黒い画面)が立ち上がる. 次の**sample**の様に, 「list of files in python_pkgs_files」の下にインストール対象となるパッケージ一覧が記載されたテキストファイルが一覧表示されていることを確認する.
   - **新規Pythonユーザ**は「anaconda_preinstall_pkgs_list_eq_sample.txt」しか表示されない.
     - anaconda_preinstall_pkgs_list_eq_**yyyymmdd**.txt
       - Anacondaにプリインストールされているパッケージの一覧ファイル.
       - これを使用することで, Anaconda環境と同様のパッケージをインストール可能.」
   - **sample**

      ```cmd
      list of files in python_pkgs_files

      >>call dir /b python_pkgs_files
      ========================================
      anaconda_preinstall_pkgs_list_eq_20210330.txt
      anaconda_preinstall_pkgs_list_eq_sample.txt
      conda_pkgs_list_eq_20210330.txt
      conda_pkgs_list_geq_20210330.txt
      conda_pkgs_list_raw.txt
      pip_pkgs_list_eq_20210330.txt
      pip_pkgs_list_geq_20210330.txt
      pip_pkgs_list_raw.txt
      ========================================

      select a packages file name : 
      ```

11. 「select a packages file name : 」の右側に, インストールしたいテキストファイル名を入力し, Enterを押下する.
    - 入力はコピペでOK!!
    - **[推奨]** Anacondaで元々プリインストールされていたパッケージを全てインストールする場合は, 「anaconda_preinstall_pkgs_list_eq_**yyyymmdd**.txt」または「anaconda_preinstall_pkgs_list_eq_sample.txt」を選択する.
    - 次の**sample**は「pip_pkgs_list_geq_20210330.txt」を選択した例.
    - **sample**

      ```cmd
      list of files in python_pkgs_files

      >>call dir /b python_pkgs_files
      ========================================
      anaconda_preinstall_pkgs_list_eq_20210330.txt
      anaconda_preinstall_pkgs_list_eq_sample.txt
      conda_pkgs_list_eq_20210330.txt
      conda_pkgs_list_geq_20210330.txt
      conda_pkgs_list_raw.txt
      pip_pkgs_list_eq_20210330.txt
      pip_pkgs_list_geq_20210330.txt
      pip_pkgs_list_raw.txt
      ========================================

      select a packages file name : pip_pkgs_list_geq_20210330.txt
      ```

12. pipの場合, 「Do you want to install it as a user??」と**ユーザインストール**を行うか聞かれるので, ユーザインストールする場合は「**y**」(Yesの意味), そうでない場合は「**n**」(Noの意味)を入力し, Enterを押下する.
    - 「**y**」を選択すると, `pip install --user [package]`を行う.
    - ユーザインストールが分からない方:
      - 「管理者権限がある」かつ「どのユーザもパッケージを使用したい」: **n**
      - それ以外: **y**
      - 迷った場合, 「**y**」を推奨.

13. パッケージの一括インストールが開始される.
    - 複数のパッケージ管理ツールを使用する場合, 複数のテキストファイルからパッケージをインストールする場合は10の手順を複数回実行する.
    - **[注意事項]** condaを使用して大量のインストールを行うと何時間もかかる場合があるので, 放置しておく.


[終わり]

---

## Appendix

### batファイルの中身概要

- 詳しくはGitHubリポジトリからbatファイルを直接見てください.

- **no001_backup_python_packages.bat**

  ```bat
  set py_pkgs_files_dpath=python_pkgs_files

  rem ディレクトリを作成する.
  echo make directory for packages files
  call mkdir %py_pkgs_files_dpath%

  rem エラー対策のアップデート
  echo command1 to avoid conda errors
  echo y|call conda install anaconda

  rem エラー対策のアップデート
  echo command2 to avoid conda errors
  echo y|call conda update --all

  set conda_list_file0=%py_pkgs_files_dpath%/conda_pkgs_list_raw.txt

  rem condaのパッケージ一覧を出力する.
  echo output conda packages file
  call conda list --export > %conda_list_file0%

  set pip_list_file0=%py_pkgs_files_dpath%/pip_pkgs_list_raw.txt

  rem pipのパッケージ一覧を出力する.
  echo output pip packages file
  call pip list --format freeze > %pip_list_file0%
  ```

- **no002_conda_install_from_files.bat**

  ```bat
  rem ファイルから1行ずつ読み込んでconda installを行う.
  rem yesかnoか聞かれる場合があるので, 全てyes(y)で答える.
  rem input_pkgs_fpathにはファイルパスをセット.
  for /f %%l in (%input_pkgs_fpath%) do (
      echo y|call conda install "%%l"
  )
  ```

- **no003_pip_install_from_files.bat**

  ```bat
  rem ファイルから1行ずつ読み込んでpip installを行う.
  rem input_pkgs_fpathにはファイルパスをセット.
  for /f %%l in (%input_pkgs_fpath%) do (
      call pip install "%%l"
  )
  ```


---

## 参考

### Anaconda有償化関連

- [(Qiita)Anacondaが有償化されて困っている人に贈る、Pythonのパッケージ管理](https://qiita.com/c60evaporator/items/ba41cef4b37465c39948)


- [(Qiita)Anaconda パッケージリポジトリが「大規模な」商用利用では有償になっていた](https://qiita.com/tfukumori/items/f8fc2c53077b234384fc)


- [(reddit)Anaconda is not free for commercial use (anymore) - alternatives ?](https://www.reddit.com/r/Python/comments/iqsk3y/anaconda_is_not_free_for_commercial_use_anymore/gqdqrk9/?context=3)


- [Anacondaの有償化に伴いminiconda+conda-forgeでの運用を考えてみた](https://qiita.com/kimisyo/items/986802ea52974b92df27)


### Anaconda全般

- [Anaconda package lists](https://docs.anaconda.com/anaconda/packages/pkg-docs/)

- [conda install documentation](https://docs.conda.io/projects/conda/en/latest/commands/install.html)

- [Installing conda packages Anaconda  documentation](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/)

- [Uninstalling Anaconda](https://docs.anaconda.com/anaconda/install/uninstall/)

- [(Qiita)conda updateで「Solving environment: failed」となった時の解決法](https://qiita.com/jordi/items/cd974b668e7ecf312543)
