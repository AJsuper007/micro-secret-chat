input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("Micro Chat!")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString("Where are you?")
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
})
radio.setGroup(1)
