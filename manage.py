#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


"""
manage.py はサイトの管理に役立つスクリプトである．
(projectの作成) : django-admin startproject mysite .
python manage.py runserver : webサーバの起動
python manage.py startapp blog : 新しいアプリケーションの作成（この場合だとbqlogディレクトリを作成）
python manage.py makemigrations blog : 移行ファイル（マイグレーションファイル）の作成（モデルに変更があったことをDjangに知らせる）
python manage.py migrate blog : モデルをデータベースに反映させる（Djangoが作ってくれた移行ファイル(migrationfile)を私たちがデータベースに追加）
python manage.py createsuperuser : admin画面の最初のユーザーネーム，パスワードを決める．
"""
