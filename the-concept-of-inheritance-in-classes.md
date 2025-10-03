# Inheritance in Python

## What is Inheritance?
- **Parent Class**: Base class that contains common attributes and methods.  
- **Child Class**: Inherits from the parent class and can extend or override functionality.  
- **Overriding**: Child class provides its own implementation of a method from the parent.  
- **Multiple Inheritance**: In Python, a child class can inherit from **more than one parent class**.  

---

## Example: Devices and Smart Home

```python
# Base class
class Device:
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name

    def info(self):
        return f"Device {self.name} with IP {self.ip} and MAC {self.mac}"

# Child Class 1 → TV
class TV(Device):
    def __init__(self, ip, mac, name):
        super().__init__(ip, mac, name)

    def turn_on(self):
        # connect to self.ip and turn on
        print(f"{self.name} is now ON")

    def turn_off(self):
        # connect to self.ip and turn off
        print(f"{self.name} is now OFF")

# Child Class 2 → Thermo
class Thermo(Device):
    def __init__(self, ip, mac, name):
        super().__init__(ip, mac, name)

    def get_degree(self):
        # connect to self.ip and return degree
        return "Temperature is 25°C"

# Child Class 3 → SmartTV (inherits from TV)
class SmartTV(TV):
    def __init__(self, ip, mac, name):
        super().__init__(ip, mac, name)

    def turn_on(self):
        # overriding parent method
        print(f"{self.name} (Smart) is starting with Smart features...")

# Usage
my_tv = TV("192.168.1.10", "84:84:48:12", "Living Room TV")
my_tv.turn_on()   # Living Room TV is now ON
my_tv.turn_off()  # Living Room TV is now OFF

thermo = Thermo("192.168.1.20", "84:84:48:34", "Hall Thermostat")
print(thermo.get_degree())  # Temperature is 25°C

smart = SmartTV("192.168.1.30", "84:84:48:56", "Smart TV")
smart.turn_on()  # Smart TV (Smart) is starting with Smart features...
```
# Key Notes

- super().__init__() calls the parent constructor to initialize common attributes.

- Child classes can reuse code from parent classes.

- You can override methods in the child class for customization.

- Python supports multiple inheritance:

```Python
class SmartDevice(TV, Thermo):
    pass
```
- Use multiple inheritance carefully → it can make code harder to maintain.
