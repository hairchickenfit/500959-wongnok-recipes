# wongnok_devpool_2024

1. install python version 3.9.13
2. create virtualenv
3. activate created virtualenv
4. pip install -r requirements.txt
5. py manage.py makemigrations
6. py manage.py migrate
7. py manage.py createsuperuser (to be used as admin for admin page)
8. I think you are good to go now ==> py manage.py runserver

URL(S)
{main_url}/admin/ => [GET, ]

{main_url}/base/
{main_url}/base/home/ => [GET, ] 
{main_url}/base/login/ => [GET, POST]
{main_url}/base/register/ => [GET, POST]
{main_url}/base/logout/ => [GET, ]

{main_url}/recipe/
{main_url}/recipe/all_recipe/ => [GET, ]
{main_url}/recipe/view_recipe/ => [GET, POST]
{main_url}/recipe/my_recipe/ => [GET, ]
{main_url}/recipe/create_my_recipe/ => [GET, POST]
{main_url}/recipe/edit_my_recipe/ => [GET, POST]
{main_url}/recipe/delete_my_recipe/ => [GET, ]

Full Stack by Django, SO, there is no need to use POSTMAN