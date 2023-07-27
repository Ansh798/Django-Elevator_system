# Elevator Management
An elevator system, which can be initialised with N elevators and maintains the elevator states as well. 

To check out the video of this project running [click here](/video/elevator_demo.mp4)

## Prerequisites

1. Clone this project [Click here](https://github.com/Sagarkkr/elevator-system) 

2. Installing Requirements 
```
pip install -r requirements.txt
```
3. Create Database
```
python manage.py migrate
```
4. Create superuser
```
python manage.py createsuperuser
```
5. Runserver for displaying 
```
python manage.py runserver
```
6. To run pytest
```
coverage run -m pytest
```

## Usage
* GET API to list down all the elevators present 

    ```
    curl --location 'http://127.0.0.1:8000/api/elevator/' 
    ```

* POST API to create a new elevator 

    ```
    curl --location 'http://127.0.0.1:8000/api/elevator/' \
    --header 'Content-Type: application/json' \
    --data '{
    "current_floor":4,
    "destination_floor":8,
    "status": 2,
    "direction": "up",
    "max_occupancy": 10,
    "current_occupancy": 5,
    "min_floor": -2,
    "max_floor":10
    }'  
    ```

* POST API to call an elevator and enter destination floor

    ```
    curl --location 'http://127.0.0.1:8000/api/elevator/call_elevator/' \
    --header 'Content-Type: application/json' \
    --data '{
    "elevator_id":1,
    "current_floor":4,
    "destination_floor":1
    }'    
    ```

* GET API to mark an elevator as non operational

    ```
    curl --location 'http://127.0.0.1:8000/api/elevator/2/non_operational/'
    ```

* Fetch an elevator using id
    ```
    curl --location 'http://127.0.0.1:8000/api/elev_retr/4'
    ```

## Todo