# van-exercise
Backend that store the latitude and longitude of an object

# Setup
* This project needs Postgres and GDAL dependencies:
    - I recomend to run this project using a Docker image having all the depandencies already installed. You can try with this one: `kevinloygtz0907/devops-test:latest`
    - Also, you can use a virtual env to install the dependancies

* Run app: `python3 manage.py runserver`
* Run migrations: `python3 manage.py migrate`  

## Misc

Create migrations: `python3 manage.py makemigrations`

Run migrations: `python3 manage.py migrate`

Sample GET: `curl --header "Content-Type: application/json" --request GET 'http://localhost:8000/van/?lat=19.438057&lng=-99.204968'`

Sample POST: `curl --header "Content-Type: application/json" --request POST  --data '{"code":"ABCD","lat":"19.3910038","lng":"-99.2836966"}'   http://localhost:8000/van/`



*** If you have any question about this project please send me an email me@kevingtz.dev ***