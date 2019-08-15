from assets.battle_properties import Round
from events import event_queue



def button_feedback(self, event, clock):
    round_up()
    event_queue.append(["set_screen", "battle"])    

def round_up_e(self, event, clock):
    round_up()



def round_up():
    global Round
    global event_queue 

    round = Round
    round += 1
    Round = round
    

handler_dict = {"button_feedback": button_feedback}



    