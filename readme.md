set up django project
    terminal > django-admin startproject highchart
    To Run django project
    terminal > python manage.py runserver

    creation new app 
        terminal > python manage.py startapp home
        home>urls.py
    redirection of project to app
        project>urls.py
            from django.contrib import admin
            from django.urls import path
            from django.urls.conf import include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include("home.urls")),
            ]
        app>urls.py
            from django.contrib import admin
            from django.urls import path
            from home import views
            urlpatterns = [
            path("",views.index,name='home')
            ]
        app>views.py
            from django.shortcuts import render,HttpResponse
            # Create your views here.
            def index(req):
                return HttpResponse("this is home page")
        create folder static and templates folder
        project>setting.py 
            STATICFILES_DIRS = [
                    BASE_DIR / "static"
                ]
            import os
            os.path.join(BASE_DIR,"templates")
        render HTML pages
            set html page
                app>views.py
                    return render(req,'index.html')
            send variable 
                app>views.py
                    context = {
                            'variable': "this is send"
                        }
                templates>index.html
                    {{variable}}
        terminal > python manage.py makemigrations
        terminal > python manage.py migrate
        terminal > python manage.py createsuperuser
            username:admin 
            password:admin
        creation common file for header and footer 
            create file base.html under templates
            base.html
                <div class="container">
                {% block title %} {% endblock title %}
                {% block body %} {% endblock body %}
                </div>
            index.html
                {% extends 'base.html' %}
                {% block title %}
                    <div>Home / About Us </div>
                {% endblock title %}
                {% block body %}
                    <div>Dynamic div</div>
                {% endblock body %}
            Insert into database 
                >database.html
                <form method="post" action="/database" >
                {% csrf_token %}
                    <input type="text" name="name" >  
                    <input type="password" name="password" >
                    <input type="date" name="dob" >
                    <input type="number" name="mob" >
                    <input type="email" name="email" >
                    <button class="btn btn-primary" type="submit">Submit</button>
                </form>

            app>view.py
                if req.method =="POST":
                    name = req.POST.get('name')
                    password = req.POST.get('password')
                    dob = req.POST.get('dob')
                    mob = req.POST.get('mob')
                    email = req.POST.get('email')
                    print(password)
                    database = Dashboard(name=name,password=password,dob=dob,mob=mob,email=email)
                    database.save()
            app>model.py
                    # Create your models here.
                    class Dashboard(models.Model):
                        name = models.TextField()
                        password = models.TextField()
                        dob = models.TextField()
                        mob = models.TextField()
                        email = models.TextField()

                        def __str__(self):
                            return self.name
            app>admin.py
                    from django.contrib import admin
                    from home.models import Dashboard
                    # Register your models here.
                    admin.site.register(Dashboard)
            project>setting.py
                    
                    INSTALLED_APPS = [
                        'home.apps.HomeConfig',
                        ...
                        ]
            terminal>python manage.py makemigrations
            terminal>python manage.py migrate

Architecture of Django
    Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application. 
    Model: The model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySql, Postgres). To check more, visit – Django Models 

    View: The View is the user interface — what you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files. To check more, visit – Django Views. 

    Template: A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. To check more, visit – Django Templates 

