import turtle
from turtle import Turtle, Screen
import pandas
from states_on_map import StatesOnMap


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=750, height=720)
turtle.shape(image)
states_on_map = StatesOnMap()



# def get_mouse_click_coor(x, y): #Quando clica na tela ele mostra as coordenadas, mas ela já deixou feito isso
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

states = data.to_dict()


# for item in range(0, 49):
#     states_list.append(states["state"][item])

states_list = data.state.to_list()

correct_answers = []


while len(correct_answers) < 50:
    answer_state = screen.textinput(f"{len(correct_answers)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        states_to_learn = []
        for item in states_list:
            if item not in correct_answers:
                states_to_learn.append(item)

        data_dict = {
            "state": states_to_learn
        }
        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        if answer_state not in correct_answers:
            x_cor = int(data[data.state == answer_state].x)
            y_cor = int(data[data.state == answer_state].y)
            states_on_map.goto(x_cor, y_cor)
            states_on_map.write(answer_state, False, "left", ("Courier", 8, "normal"))
            #aqui também poderia escrever
            #states_on_map.write(data.state.item()) - Ele traz o item correspondente ao state (sem considerar o resto)
            correct_answers.append(answer_state)






