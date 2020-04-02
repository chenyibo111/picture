import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
formB = plt.axes([0.3, 0.5, 0.5, 0.075])
formT = plt.axes([0.3, 0.1, 0.5, 0.075])
button = Button(formB, "calculate")
number1 = '0B0110011001100000'
number2 = '0B0101010101010101'
number3 = '0B1000111100001100'

def calculate(num1, num2):
    n1 = int(num1, 2)
    n2 = int(num2, 2)
    n3 = int('10000000000000000', 2)

    result = n1 + n2
    if result >= n3:
        result = result - n3 + 1

    return format(result, '#018b')


def flip(num):
    return bin(((1 << 16) + (~int(num, 2))))


def button_clicked(event):
    textbox4 = TextBox(formT, "result",
                       initial=flip(calculate(calculate(number1, number2), number3)))
    plt.show()

button.on_clicked(button_clicked)
plt.show()