class DroneState:
    OUT_OF_ORDER = 1 << 0
    IDLE = 1 << 1
    TAKE_OFF = 1 << 2
    LANDING = 1 << 3
    FLYING = 1 << 4
    RUNNING = 1 << 5
    IN_AIR = 1 << 6
    SHIPPING = 1 << 7
    DELYVERING = 1 << 8
    WAITING_FOR_BATTERY_EXCH = 1 << 9
    OFF = 1 << 10
    ON_LAND = 1 << 11
