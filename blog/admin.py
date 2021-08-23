from django.contrib import admin
from .models import Post, Category
#models.py で作成したPostClassをimportしている

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
#admin.site.register(Tag)
"""
admin.py : 管理者ページでデータを表示する際の設定を記述する
models.py : データモデルを記述する
"""