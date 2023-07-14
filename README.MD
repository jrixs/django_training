install requirements: 
`pip install -r requirements.txt`

run project:
`python manage.py runserver`

run django-extensions console: 
`python manage.py shell_plus --ipython`

dumpdata fixture
`python manage.py dumpdata MainApp.Snippet > fixture/MainApp_Snippet.json`
loaddata fixture
`python manage.py loaddata fixture/MainApp_Snippet.json`