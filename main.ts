basic.forever(function () {
    basic.showNumber(input.temperature())
})
basic.forever(function () {
    if (input.temperature() > 19) {
        basic.showString("Too Hot!")
    } else if (input.temperature() == 19) {
        basic.showString("Correct Temperature")
    } else {
        basic.showString("Temp Too Low!")
    }
})
