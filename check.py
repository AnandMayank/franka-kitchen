from inputs import devices

gamepads = devices.gamepads

if not gamepads:
    print("No gamepads found.")
else:
    print("Available gamepads:")
    print(f"Type of gamepads: {type(gamepads)}")
    print(f"Length of gamepads: {len(gamepads)}")
    for i, gamepad in enumerate(gamepads):
        print(f"Gamepad {i}:")
        print(f"  Name: {gamepad.name}")
        print(f"  Path: {gamepad.path}")
        print(f"  Capabilities: {gamepad.capabilities()}")