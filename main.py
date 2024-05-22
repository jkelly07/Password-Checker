import gooeypie as gp
# imports all of the classes downloaded via the pip install

app = gp.GooeyPieApp('Hello')
# instantiate a 'GooeyPieApp'

app.width = 600
app.height = 400
app.title = "Password Checker"
# sets the width, height and name attribute

# setup a grid
app.set_grid(2,1)

def submit(event):
    lbl.text = "I work!!"

# create some widgets
btn = gp.Button(app, "Submit", submit)
lbl = gp.Label(app, "This is a label")


# put stuff in grid!!
app.add(btn, 1,1)
app.add(lbl, 2,1)
app.run()