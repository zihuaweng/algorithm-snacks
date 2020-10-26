"""
1. Requirement
- move up and down, from 1 to maxFloor
- open door and close door
- pick up passagers

Clarification:
- Do we need to consider overweight
- Is it a passanger elevator or freight elevator
- How many elevators can response the car call (one of many)
- Do we need zoning?
- peak time?


2. main actors & user case
    actor: 
        passagers: make car calls, select the floor, close door, open door, get in out of the car
    
    use case of the system
        process car calls, move car up and down, indicate direction and cur floor, open and close door, trigger emergency brake

3. class
    Request
        floor   
    ElevatorControl (singleton)
        car_list: []
        door: []
        hall_button: []

        select_elevator()
    Door
        status: open, closed
        close()
        open()
        is_open()
    car
        max_floor
        min_floor
        cur floor
        max_weight
        status: idle, move_up, move_down
        up_list: min_heap / boolen list, true is to stop
        down_list: max_heap / boolen list, true is to stop
        indicator: 
        
        add_floor_by_passenger()
        move()
        stop()
        open_door()
        close_door()
        update_indicator()
    Button:
        Hall Button
            cur_floor
            status: on, off
        elevator button
            status: on, off
    Indicator
        show_floor()
        show_direction()
    Exception



4. activities:
- process car call:
    - passenger press button
    - hall buttom turn on
    - car add the cur floor to destination
        - if the car is not moving: 
            - compare car floor and cur floor, set direction to car add cur to destination
        - if the car is not moving: 
            - same direction: 
                - up: car floor < cur floor: add to up list
                - down: car floor > cur floor: add to down list
            - opposite direction: add to cur direction to list
                - up: car floor >= cur floor: add to down list
                - down: car floor <= cur floor: add to up list
    - car move to the destination
    - open the door
    - close the door
    - turn off the hall button


- move car up and down
    - car overwight:
        - yes: alarm
        - no: 
            - passenger select close door:
                - door -> closed
            - passenger not select close door:
                - door closes in 5 sec
    - passenger select floor
        - not select:
            - up: go through the up list
            - down: go through the down list
        - select:
            - up: 
                - car floor < target floor: add to up list
                - car floor > target floor: add to down list
            - down: 
                - car floor > target floor: add to down list
                - car floor < target floor: add to up list
    - move car
        - update indicator
        - up date direction:
            - up: 
                - not up and down: swich to down, go through down list
                - not up and not down: stop
            - down: 
                - not down and up: swich to up, go through up list
                - not down and not up: stop
            - still:
                - stop

"""


def get_new_size(n_items):
    new_size = n_items + (n_items >> 3)
    if n_items < 9:
        new_size += 3
    else:
        new_size += 6
    return new_size

print(get_new_size(26))