# Created by: Jacob Liberty
# Created on: Oct 3 2017
# Created for: ICS3U
# This program height of an object after falling for a given time

import ui

def calculate_touch_up_inside(sender):
    #declaring constants
    GRAVITY = 9.81
    
    #variable
    seconds = float(view['seconds_textbox'].text)
    
    #calculation
    height = 100 - 0.5 * GRAVITY * seconds ** 2
    
    #show answer
    view['answer_label'].text = 'The object is {0}m above the ground'.format(height)
    

view = ui.load_view()
view.present('sheet')
