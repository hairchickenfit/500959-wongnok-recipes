# wongnok_devpool_2024

How to run this Project

1. install python version 3.9.13
2. create virtualenv
3. activate created virtualenv
4. pip install -r requirements.txt
5. py manage.py makemigrations
6. py manage.py migrate
7. py manage.py createsuperuser (to be used as admin for admin page)
8. I think you are good to go now ==> py manage.py runserver


URL(S)

1. {main_url}/admin/ => [GET, ]

2. {main_url}/base/home/ => [GET, ] 
3. {main_url}/base/login/ => [GET, POST]
4. {main_url}/base/register/ => [GET, POST]
5. {main_url}/base/logout/ => [GET, ]

6. {main_url}/recipe/all_recipe/ => [GET, ]
7. {main_url}/recipe/view_recipe/ => [GET, POST]
8. {main_url}/recipe/my_recipe/ => [GET, ]
9. {main_url}/recipe/create_my_recipe/ => [GET, POST]
10. {main_url}/recipe/edit_my_recipe/ => [GET, POST]
11. {main_url}/recipe/delete_my_recipe/ => [GET, ]


Full Stack by Django, SO, there is no need to use POSTMAN