from django.shortcuts import render,HttpResponse

courses = [  
        {  
            "title": "دوره برنامه‌نویسی پایتون",  
            "description": "این دوره به شما اصول و مبانی برنامه‌نویسی با زبان پایتون را آموزش می‌دهد.",  
            "start_date": "2023-10-01",  
            "price": 1500000  
        },  
        {  
            "title": "دوره برنامه‌نویسی جاوااسکریپت",  
            "description": "در این دوره با زبان برنامه‌نویسی جاوااسکریپت و چگونگی استفاده از آن در توسعه وب آشنا می‌شوید.",  
            "start_date": "2023-11-15",  
            "price": 1200000  
        },  
        {  
            "title": "دوره توسعه وب با React",  
            "description": "این دوره به یادگیری فریم‌ورک React برای توسعه رابط‌های کاربری وب اختصاص داده شده است.",  
            "start_date": "2023-12-10",  
            "price": 1800000  
        },  
        {  
            "title": "دوره برنامه‌نویسی جافا",  
            "description": "در این دوره با زبان برنامه‌نویسی جافا و توسعه برنامه‌های کاربردی آشنا می‌شوید.",  
            "start_date": "2024-01-05",  
            "price": 1600000  
        },  
        {  
            "title": "دوره علم داده با پایتون",  
            "description": "این دوره به شما علوم داده و تحلیل داده‌ها با استفاده از پایتون را آموزش می‌دهد.",  
            "start_date": "2024-02-20",  
            "price": 2000000  
        }  
]  

def show_courses(request):
    
    return HttpResponse(f"عنوان: {course['title']}<br>توضیحات: {course['description']}<br>تاریخ آغاز: {course['start_date']}<br>قیمت: {course['price']} تومان<br>") 

