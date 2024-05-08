import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
writes = turtle.Turtle()
writes.hideturtle()
writes.penup()

states = pandas.read_csv('./50_states.csv', sep=',')

states_count = 0
guessed_states = []

while states_count < 50:
    answer_state = screen.textinput(title=f"{states_count}/50 Guess the State", prompt="What's another state's name?")
    answer_state = answer_state[0].upper() + answer_state[1:]
    if answer_state == 'Exit':
        break
    find = states[states["state"] == answer_state]
    if len(find) != 0:
        guessed_states.append(answer_state)
        states_count += 1
        x_coor = find.x.values[0]
        y_coor = find.y.values[0]
        writes.goto(x=x_coor, y=y_coor)
        writes.write(find.state.values[0])

states_list = states['state'].to_list()
for i in guessed_states:
    states_list.remove(i)
states_to_learn = {
    "State": states_list
}
answers = pandas.DataFrame(states_to_learn)
answers.to_csv('./states_to_learn.csv')

#for mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
