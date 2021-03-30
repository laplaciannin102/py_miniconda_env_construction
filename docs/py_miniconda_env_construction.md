# Python Miniconda environment construction

- author: laplaciannin102
- date: 2021/03/31
- version: 0.0.1

---

## Table of Contents

- [Python Miniconda environment construction](#python-miniconda-environment-construction)
  - [Table of Contents](#table-of-contents)
  - [背景](#背景)
  - [概要](#概要)
  - [対象読者](#対象読者)
  - [作業環境](#作業環境)
  - [対応するGitHubリポジトリとQiita記事](#対応するgithubリポジトリとqiita記事)
  - [作業手順](#作業手順)
    - [batファイルのダウンロード](#batファイルのダウンロード)
    - [Anaconda環境から引越す準備](#anaconda環境から引越す準備)
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
- Pythonパッケージ一覧を出力するbatファイルを作成した.
- Pythonパッケージ一覧を一括でインストールするbatファイルを作成した.


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

---

### Anaconda環境から引越す準備

- 本手順は**既存Anacondaユーザ**向け手順である.
   - **新規Pythonユーザ**は[minicondaによる環境構築](#minicondaによる環境構築)を参照.

1. **no001_backup_python_packages.bat** を実行し, インストール済みパッケージの一覧をバックアップテキストとして取得する. 
その際, python_pkgs_filesという名前のディレクトリを作成しその中にテキストファイルが格納される.

   - **出力先ディレクトリ:**
     - ./python_pkgs_files/

   - **出力ファイル:**

     - conda_pkgs_list_raw.txt
       - condaのパッケージ一覧ファイル.
       - `conda list --export`で取得.

     - conda_pkgs_list_eq_**yyyymmdd**.txt
       - condaのパッケージ一覧のversionを **[package]==x.x.x** で設定したファイル.

     - conda_pkgs_list_geq_**yyyymmdd**.txt
       - condaのパッケージ一覧のversionを **[package]>=x.x.x** で設定したファイル.

     - pip_pkgs_list_raw.txt
       - pipのパッケージ一覧ファイル.
       - `pip list --format freeze`で取得.
       - `pip freeze`だとversion部分がURLになってしまう場合がある.

     - pip_pkgs_list_eq_**yyyymmdd**.txt
       - pipのパッケージ一覧のversionを **[package]==x.x.x** で設定したファイル.

     - pip_pkgs_list_geq_**yyyymmdd**.txt
       - pipのパッケージ一覧のversionを **[package]>=x.x.x** で設定したファイル.

     - anaconda_preinstall_pkgs_list_eq_**yyyymmdd**.txt
       - Anacondaにプリインストールされているパッケージの一覧ファイル.
       - これを使用することで, Anaconda環境と同様のパッケージをインストール可能.

   - Anacondaにプリインストールされているパッケージの一覧も同時に取得する.
     - Anaconda package lists: [https://docs.anaconda.com/anaconda/packages/pkg-docs/](https://docs.anaconda.com/anaconda/packages/pkg-docs/)

2. Anacondaをアンインストールする.
   1. Windowsの場合, コントロールパネルを起動する.
   2. プログラムと機能 > プログラムのアンインストール
   3. Anacondaを選択し, アンインストールする.

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

4. 次のコマンドを入力し, condaのチャネルの設定に**conda-forge**チャネルを削除する.

    ```bat
    conda config --add channels conda-forge
    ```

5. 次のコマンドを入力し, condaのチャネル一覧を確認する.

    ```bat
    conda config --show channels
    ```

    or

    ```bat
    conda config --get channels
    ```

6. 次のコマンドを入力し, condaのチャネルの設定から**defaults**チャネルを削除する.

    ```bat
    conda config --remove channels defaults
    ```

7. 次のコマンドを入力し, condaのチャネル一覧を確認する. チャネル一覧からdefaultsが消えていることを確認する.

    ```bat
    conda config --show channels
    ```

    or

    ```bat
    conda config --get channels
    ```

8. パッケージインストール用batファイルを実行する.
   - ダブルクリック or 右クリックして「開く」 or 右クリックして「管理者として実行」

   - 使用するパッケージ管理ツール毎に実行するbatファイルが異なる.

     - condaの場合:
       - **no002_conda_install_from_files.bat**

     - pipの場合:
       - **no003_pip_install_from_files.bat**

   - 「>>○○」という行は, 裏でどのようなコマンドが実行されてるか参考までに表示しているもの.

9. コマンドライン(黒い画面)が立ち上がる. 次の**sample**の様に, 「list of files in python_pkgs_files」の下にインストール対象となるパッケージ一覧が記載されたテキストファイルが一覧表示されていることを確認する.

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

10. 「select a packages file name : 」の右側に, インストールしたいテキストファイル名を入力し, Enterを押下する. 次の**sample**は「pip_pkgs_list_geq_20210330.txt」を選択した例.

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

11. パッケージの一括インストールが開始される.
    - 複数のパッケージ管理ツールを使用する場合, 複数のテキストファイルからパッケージをインストールする場合は10の手順を複数回実行する.


[終わり]

---

## Appendix

### batファイルの中身概要

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

- [(Qiita)conda updateで「Solving environment: failed」となった時の解決法](https://qiita.com/jordi/items/cd974b668e7ecf312543)
