### 第四章_Web表单

```bash
pip install flask-wtf
```

#### 4.1 跨站请求伪造保护

1. 为了实现CSRF 保护，Flask-WTF 需要程序设置一个密钥。Flask-WTF 使用这个密钥生成
   加密令牌，再用令牌验证请求中表单数据的真伪。设置密钥的方法如示例4-1 所示。

```python
示例4-1　hello.py：设置Flask-WTF
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

#### 4.2 表单类

```python
示例4-2 是一个简单的Web 表单，包含一个文本字段和一个提交按钮。
示例4-2　hello.py：定义表单类
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')
```

这个表单中的字段都定义为类变量，类变量的值是相应字段类型的对象。在这个示例中，
NameForm 表单中有一个名为name 的文本字段和一个名为submit 的提交按钮。

StringField类表示属性为type="text" 的<input> 元素。

SubmitField 类表示属性为type="submit" 的<input> 元素。字段构造函数的第一个参数是把表单渲染成HTML 时使用的标号。
StringField 构造函数中的可选参数validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据。验证函数Required() 确保提交的字段不为空。

Form 基类由Flask-WTF 扩展定义，所以从flask.ext.wtf 中导入。字段和验证函数却可以直接WTForms 包中导入。
WTForms 支持的HTML 标准字段如表4-1 所示。

表4-1　WTForms支持的HTML标准字段

| 字段类型            | 说　　明                             |
| ------------------- | ------------------------------------ |
| StringField         | 文本字段                             |
| TextAreaField       | 多行文本字段                         |
| PasswordField       | 密码文本字段                         |
| HiddenField         | 隐藏文本字段                         |
| DateField           | 文本字段，值为datetime.date 格式     |
| DateTimeField       | 文本字段，值为datetime.datetime 格式 |
| IntegerField        | 文本字段，值为整数                   |
| DecimalField        | 文本字段，值为decimal.Decimal        |
| FloatField          | 文本字段，值为浮点数                 |
| BooleanField        | 复选框，值为True 和False             |
| RadioField          | 一组单选框                           |
| SelectField         | 下拉列表                             |
| SelectMultipleField | 下拉列表，可选择多个值               |
| FileField           | 文件上传字段                         |
| SubmitField         | 表单提交按钮                         |
| FormField           | 把表单作为字段嵌入另一个表单         |
| FieldList           | 一组指定类型的字段                   |

WTForms 内建的验证函数如表4-2 所示。
表4-2　WTForms验证函数

| 验证函数    | 说　　明                                               |
| ----------- | ------------------------------------------------------ |
| Email       | 验证电子邮件地址                                       |
| EqualTo     | 比较两个字段的值；常用于要求输入两次密码进行确认的情况 |
| IPAddress   | 验证IPv4 网络地址                                      |
| Length      | 验证输入字符串的长度                                   |
| NumberRange | 验证输入的值在数字范围内                               |
| Optional    | 无输入值时跳过其他验证函数                             |
| Required    | 确保字段中有数据                                       |
| Regexp      | 使用正则表达式验证输入值                               |
| URL         | 验证URL                                                |
| AnyOf       | 确保输入值在可选值列表中                               |
| NoneOf      | 确保输入值不在可选值列表中                             |

#### 4.3　把表单渲染成HTML

表单字段是可调用的，在模板中调用后会渲染成HTML。假设视图函数把一个NameForm 实例通过参数form 传入模板，在模板中可以生成一个简单的表单，如下所示：

```html
<form method="POST">
{{ form.hidden_tag() }}
{{ form.name.label }} {{ form.name() }}
{{ form.submit() }}
</form>
```

当然，这个表单还很简陋。要想改进表单的外观，可以把参数传入渲染字段的函数，传入的参数会被转换成字段的HTML 属性。例如，可以为字段指定id 或class 属性，然后定义CSS 样式：

```html
<form method="POST">
{{ form.hidden_tag() }}
{{ form.name.label }} {{ form.name(id='my-text-field') }}
{{ form.submit() }}
</form>
```

即便能指定HTML 属性，但按照这种方式渲染表单的工作量还是很大，所以在条件允许的情况下最好能使用Bootstrap 中的表单样式。Flask-Bootstrap 提供了一个非常高端的辅助函数，可以使用Bootstrap 中预先定义好的表单样式渲染整个Flask-WTF 表单，而这些操作只需一次调用即可完成。使用Flask-Bootstrap，上述表单可使用下面的方式渲染：

```jinja2
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

import 指令的使用方法和普通Python 代码一样，允许导入模板中的元素并用在多个模板中。导入的bootstrap/wtf.html 文件中定义了一个使用Bootstrap 渲染Falsk-WTF 表单对象的辅助函数。

wtf.quick_form() 函数的参数为Flask-WTF 表单对象，使用Bootstrap 的默认样式渲染传入的表单。hello.py 的完整模板如示例4-3 所示。
示例4-3　templates/index.html：使用Flask-WTF 和Flask-Bootstrap 渲染表单

```jinja2
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}

{% block page_content %}
    <div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
    </div>
	{{ wtf.quick_form(form) }}
{% endblock %}
```

模板的内容区现在有两部分。第一部分是页面头部，显示欢迎消息。这里用到了一个模板条件语句Jinja2 中的条件语句格式为{% if condition %}...{% else %}...{% endif %}。如果条件的计算结果True，那么渲染if 和else 指令之间的值。如果条件的计算结果为False，则渲染else 和endif 指令之间的值。在这个例子中，如果没有定义模板变量name，则会渲染字符串“Hello, Stranger!”。内容区的第二部分使用wtf.quick_form() 函数渲染NameForm 对象。

#### 4.4　在视图函数中处理表单

在新版hello.py 中，视图函数index() 不仅要渲染表单，还要接收表单中的数据。示例4-4是更新后的index() 视图函数。

```python
示例4-4　hello.py：路由方法
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
```

app.route 修饰器中添加的methods 参数告诉Flask 在URL 映射中把这个视图函数注册为GET 和POST 请求的处理程序。如果没指定methods 参数，就只把视图函数注册为GET 请求的处理程序。把POST 加入方法列表很有必要，因为将提交表单作为POST 请求进行处理更加便利。表单也可作为GET 请求提交，不过GET 请求没有主体，提交的数据以查询字符串的形式附加到URL 中，可在浏览器的地址栏中看到。基于这个以及其他多个原因，提交表单大都作为POST 请求进行处理。

局部变量name 用来存放表单中输入的有效名字，如果没有输入，其值为None。如上述代码所示，在视图函数中创建一个NameForm 类实例用于表示表单。提交表单后，如果数据能被所有验证函数接受，那么validate_on_submit() 方法的返回值为True，否则返回False。这个函数的返回值决定是重新渲染表单还是处理表单提交的数据。

用户第一次访问程序时，服务器会收到一个没有表单数据的GET 请求，所以validate_on_submit() 将返回False。if 语句的内容将被跳过，通过渲染模板处理请求，并传入表单对象和值为None 的name 变量作为参数。用户会看到浏览器中显示了一个表单。用户提交表单后，服务器收到一个包含数据的POST 请求。validate_on_submit() 会调用name 字段上附属的Required() 验证函数。如果名字不为空，就能通过验证，validate_on_submit() 返回True。现在，用户输入的名字可通过字段的data 属性获取。在if 语句中，把名字赋值给局部变量name，然后再把data 属性设为空字符串，从而清空表单字段。最后一行调用render_template() 函数渲染模板，但这一次参数name 的值为表单中输入的名字，因此会显示一个针对该用户的欢迎消息。

图4-1 是用户首次访问网站时浏览器显示的表单。用户提交名字后，程序会生成一个针对该用户的欢迎消息。欢迎消息下方还是会显示这个表单，以便用户输入新名字。

如果用户提交表单之前没有输入名字，Required() 验证函数会捕获这个错误

注意一下扩展自动提供了多少功能。这说明像Flask-WTF 和Flask-Bootstrap 这样设计
良好的扩展能让程序具有强大的功能。

#### 4.5　重定向和用户会话

最新版的hello.py 存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷新按钮，会看到一个莫名其妙的警告，要求在再次提交表单之前进行确认。之所以出现这种情况，是因为刷新页面时浏览器会重新发送之前已经发送过的最后一个请求。如果这个请求是一个包含表单数据的POST 请求，刷新页面后会再次提交表单。大多数情况下，这并不是理想的处理方式。

很多用户都不理解浏览器发出的这个警告。基于这个原因，最好别让Web 程序把POST 请求作为浏览器发送的最后一个请求。

这种需求的实现方式是，使用重定向作为POST 请求的响应，而不是使用常规响应。重定向是一种特殊的响应，响应内容是URL，而不是包含HTML 代码的字符串。浏览器收到这种响应时，会向重定向的URL 发起GET 请求，显示页面的内容。这个页面的加载可能要多花几微秒，因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不同。现在，最后一个请求是GET 请求，所以刷新命令能像预期的那样正常使用了。这个技巧称为Post/ 重定向/Get 模式。

但这种方法会带来另一个问题。程序处理POST 请求时，使用form.name.data 获取用户输入的名字，可是一旦这个请求结束，数据也就丢失了。因为这个POST 请求使用重定向处理，所以程序需要保存输入的名字，这样重定向后的请求才能获得并使用这个名字，从而构建真正的响应。

程序可以把数据存储在用户会话中，在请求之间“记住”数据。用户会话是一种私有存储，存在于每个连接到服务器的客户端中。我们在第2 章介绍过用户会话，它是请求上下文中的变量，名为session，像标准的Python 字典一样操作。默认情况下，用户会话保存在客户端cookie 中，使用设置SECRET_KEY 进行加密签名。如果篡改了cookie 中的内容，签名就会失效，会话也会随之失效。

```python
示例4-5 是index() 视图函数的新版本，实现了重定向和用户会话。
示例4-5　hello.py：重定向和用户会话
from flask import Flask, render_template, session, redirect, url_for
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))
```

在程序的前一个版本中，局部变量name 被用于存储用户在表单中输入的名字。这个变量现在保存在用户会话中，即session['name']，所以在两次请求之间也能记住输入的值。现在，包含合法表单数据的请求最后会调用redirect() 函数。redirect() 是个辅助函数，用来生成HTTP 重定向响应。redirect() 函数的参数是重定向的URL，这里使用的重定向URL 是程序的根地址，因此重定向响应本可以写得更简单一些，写成redirect('/')，但却会使用Flask 提供的URL 生成函数url_for()。推荐使用url_for() 生成URL，因为这个函数使用URL 映射生成URL，从而保证URL 和定义的路由兼容，而且修改路由名字后依然可用。url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字。默认情况下，路由的端点是相应视图函数的名字。在这个示例中，处理根地址的视图函数是index()，因此传给url_for() 函数的名字是index。

最后一处改动位于render_function() 函数中，使用session.get('name') 直接从会话中读取name 参数的值。和普通的字典一样，这里使用get() 获取字典中键对应的值以避免未找到键的异常情况，因为对于不存在的键，get() 会返回默认值None。

使用这个版本的程序时，刷新浏览器页面，你看到的新页面就和预期一样了。

#### 4.6　Flash消息

请求完成后，有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错误提醒。一个典型例子是，用户提交了有一项错误的登录表单后，服务器发回的响应重新渲染了登录表单，并在表单上面显示一个消息，提示用户用户名或密码错误。

这种功能是Flask 的核心特性。如示例4-6 所示，flash() 函数可实现这种效果。

```python
示例4-6　hello.py：Flash 消息
from flask import Flask, render_template, session, redirect, url_for, flash
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
    	old_name = session.get('name')
    	if old_name is not None and old_name != form.name.data:
    		flash('Looks like you have changed your name!')
    	session['name'] = form.name.data
    	return redirect(url_for('index'))
    return render_template('index.html',
                           form = form, name = session.get('name'))
```

在这个示例中，每次提交的名字都会和存储在用户会话中的名字进行比较，而会话中存储的名字是前一次在这个表单中提交的数据。如果两个名字不一样，就会调用flash() 函数，在发给客户端的下一个响应中显示一个消息。

仅调用flash() 函数并不能把消息显示出来，程序使用的模板要渲染这些消息。最好在基模板中渲Flash 消息，因为这样所有页面都能使用这些消息。Flask 把get_flashed_messages() 函数开放给模板，用来获取并渲染消息，如示例4-7 所示。
示例4-7　templates/base.html：渲染Flash 消息

```html
{% block content %}

<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    {{ message }}
    </div>
    {% endfor %}
    {% block page_content %}{% endblock %}
</div>

{% endblock %}
```

在这个示例中，使用Bootstrap 提供的警报CSS 样式渲染警告消息（如图4-4 所示）。

在模板中使用循环是因为在之前的请求循环中每次调用flash() 函数时都会生成一个消息，所以可能有多个消息在排队等待显示。get_flashed_messages() 函数获取的消息在下次调用时不会再次返回，因此Flash 消息只显示一次，然后就消失了。
