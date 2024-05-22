import gooeypie as gp 

def on_text_change(event):
    text = text_box.text
    print(text)

    if text == "Fonginator":
        label.text = "Shiterpool"
    elif text == "Fongy":
        label.text = "Shit teacher"
    else:
        label.text = ""


app = gp.GooeyPieApp('Might be useful for your assessment')

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'blank')

app.set_grid(2,1)
app.add(text_box, 1,1)
app.add(label,2,1)

app.run()

