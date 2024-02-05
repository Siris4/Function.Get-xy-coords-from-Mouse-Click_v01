import turtle

def get_mouse_click_xy_coords(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_xy_coords)

turtle.mainloop()  #keeps screen open, even though the code has finished running