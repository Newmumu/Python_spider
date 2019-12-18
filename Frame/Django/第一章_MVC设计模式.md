让我们来研究一个简单的例子，通过该实例，你可以分辨出，通过Web框架来实现的功能与之前的方式有何不
同。 下面就是通过使用Django来完成简单的web应用的例子： 首先，我们分成4个Python的文件，(models.py ,
views.py , urls.py ) 和html模板文件 (latest_books.html )
```python
# models.py (the database tables)
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()

# views.py (the business logic)
from django.shortcuts import render_to_response
from models import Book
def latest_books(request):
    book_list = Book.objects.order_by('‐pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})

# urls.py (the URL configuration)
from django.conf.urls.defaults import *
import views
urlpatterns = patterns('',
    (r'^latest/$', views.latest_books),
)

# latest_books.html (the template)
<html>
    <head>
        <title>Books</title>
    </head>
    <body>
        <h1>Books</h1>
        <ul>
            {% for book in book_list %}
            <li>{{ book.name }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```
