def on_forever():
    basic.show_number(input.temperature())
basic.forever(on_forever)

def on_forever2():
    if input.temperature() > 19:
        basic.show_string("Too Hot!")
    elif input.temperature() == 19:
        basic.show_string("Correct Temperature")
    else:
        basic.show_string("Temp Too Low!")
basic.forever(on_forever2)
