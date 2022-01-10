## Test-Bravi

### Clone the repository
```
git clone https://github.com/caetasousa/Test-Bravi.git
```
### Access the folder
```bash
cd Test-Bravi
```
### In linux terminal create and activate virtual env
```bash
virtualenv venv
source venv/bin/activate
```
### In Windows terminal create and activate virtual env
```
python -m venv venv
venv\Scripts\activate
```  
### install dependencies
```
pip install -r requirements.txt
```
### Run the migrations
```
python manage.py migrate
```
### Create a super user 
```
python manage.py createsuperuser
```
### Run tests
```
 python manage.py test
```
### Start server
```
python manage.py runserver
```
### Login and register the pieces
```
http://127.0.0.1:8000/admin/
```
## After register we can get consult pieces
  ### Example url for name and color
  ```
  http://127.0.0.1:8000/piece-id/?name=knight&color=black
  ```
  Here will have the return of the id
  ### Example url for id and coordinate
  ```
  http://127.0.0.1:8000/piece-move/?id=1&coordinate=d4
  ```
  Here will have the return the name, color, possibilities first turn and possibilities second turn. 




