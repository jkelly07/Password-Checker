# Password checker attempt 2


import gooeypie as gp

app = gp.GooeyPieApp('Password Checker')

app.width = 1000
app.height = 300
app.title = "Password Checker"



def toggle_password_visibility(event):
    pass_inp.toggle()


def checks(event):
    # first check length
    if len(pass_inp.text) <= 16:
        len_lbl.text = 'Password too short, longer than 16 characters please'
    else:
        len_lbl.text = 'Password length is good, however the more characters the better'

    # then check chars
    
    total = 0
    for character in pass_inp.text:
        special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
        if character in special_characters:
            total += 1
        
    if total < 3:
        special_lbl.text = 'Not enough special characters, at least 3 please'
    
    
    
    if total >= 3:
        special_lbl.text = 'Good job, you have enough special characters but the more the better'

    
        

# def check_len(event):
#     if len(pass_inp.text) <= 16:
#         len_lbl.text = 'Password too short, longer than 16 characters please'
#     else:
#         len_lbl.text = 'Password length is good, however the more characters the better'

# special_characters = "`~!@#$%^&*()_-+={[}]|;:'<,>.?/"

# # 
# def check_special_characters(event):

#     special_characters = "!"

#     total = 0
#     for character in pass_inp.text:
 
#         if character in special_characters:
#             total += 1
    



#     if total < 3:
#         special_lbl.text = 'Not enough special characters, at least 3 please'
#     # if special_characters >= 3:
#     #     special_lbl.text = 'Good job, you have enough special characters but the more the better'

    
        
    





# setup a grid
app.set_grid(8,2)


pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
len_lbl = gp.Label(app, '')
check = gp.Checkbox(app, 'Show password')
special_lbl = gp.Label(app, '')

pass_inp.width = 50




app.add(pass_lbl, 1,1)
app.add(pass_inp,1,2)
app.add(check, 2, 2)
app.add(len_lbl, 3,1)
app.add(special_lbl, 4,1)





pass_inp.add_event_listener('change', checks)
check.add_event_listener('change', toggle_password_visibility)

app.run()
