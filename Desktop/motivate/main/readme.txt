This test works for user authentication

Start app, eg
register app, eg.apps.EgConfig


create model user
register model in admin

=====
add to settings

AUTH_USER_MODEL = 'users.User'
=====
makemigrations
migrate

create forms
create views
create urls
