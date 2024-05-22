
import gooeypie as gp

app = gp.GooeyPieApp('Password Checker')

app.width = 800
app.height =500
app.title = "Password Checker"

# setup a grid
app.set_grid(2,1)


def on_text_change(event):
    text = text_box.text
    print(text)

    length_message = length_measure(event, text)
    non_alphabetic_message = non_alphabetic_characters(event, text)

    label.text = length_message + " " + non_alphabetic_message

def length_measure(event, text):
    if len(text) <= 16:
        label.text = "Too short, more than 16 characters please :) "
    else:
        return ""

def non_alphabetic_characters(event,text):
    non_alpha_count = len([char for char in text if not char.isalpha()])
    if non_alpha_count < 5:
        label.text = "Not enough special characters (at least 5 non-alphabetic characters)"
    else:
        return ""



text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'blank')

app.set_grid(2,1)
app.add(text_box, 1,1, align = 'center')
app.add(label,2,1, align = 'center')

app.run()


    # non_alpha_count = len([char for char in text if not char.isalpha()])

    # if len(text) <= 16:
    #     label.text = "Too short, more than 16 characters"
    # if non_alpha_count < 5:
    #     label.text = "Not enough special characters (at least 5 non-alphabetic characters)"
    # else:
    #     label.text = ""
