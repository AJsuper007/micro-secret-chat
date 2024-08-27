def on_button_pressed_a():
    radio.send_string("Micro Chat!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string("Where are you?")
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    pass
radio.on_received_value(on_received_value)

radio.set_group(1)