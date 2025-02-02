# main.py

class SmartDevice:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.status = False  # Default status is OFF

    def turn_on(self):
        """Turn the device on."""
        self.status = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        """Turn the device off."""
        self.status = False
        print(f"{self.name} is now OFF.")

    def get_status(self):
        """Get the current status of the device."""
        return "ON" if self.status else "OFF"

    def __repr__(self):
        return f"{self.device_type}: {self.name} - Status: {self.get_status()}"


class SmartHomeSystem:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        """Add a new device to the system."""
        self.devices[device.name] = device
        print(f"{device.device_type} '{device.name}' added to the system.")

    def control_device(self, device_name, action):
        """Control a specific device (turn on/off)."""
        device = self.devices.get(device_name)
        if not device:
            print(f"Device '{device_name}' not found.")
            return

        if action == "on":
            device.turn_on()
        elif action == "off":
            device.turn_off()
        else:
            print("Invalid action. Please use 'on' or 'off'.")
    
    def view_devices(self):
        """View all devices and their statuses."""
        if not self.devices:
            print("No devices in the system.")
        else:
            for device in self.devices.values():
                print(device)


def main():
    home_system = SmartHomeSystem()

    # Add devices to the system
    light = SmartDevice("Living Room Light", "Light")
    fan = SmartDevice("Bedroom Fan", "Fan")
    thermostat = SmartDevice("Main Thermostat", "Thermostat")

    home_system.add_device(light)
    home_system.add_device(fan)
    home_system.add_device(thermostat)

    while True:
        print("\nSmart Home Automation System")
        print("1. View Devices and Status")
        print("2. Control Device")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            home_system.view_devices()

        elif choice == '2':
            device_name = input("Enter device name: ").strip()
            action = input("Enter action (on/off): ").strip().lower()
            home_system.control_device(device_name, action)

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
