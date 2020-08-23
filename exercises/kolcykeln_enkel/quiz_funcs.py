def create_coding_quiz_question(question_num, correct_answer):
    
    #Import modules:
    from ipywidgets import FloatText, Button, Output, HBox, Valid, Label
    from IPython.display import clear_output
    

    #Create a FloatText widget:
    py_q = FloatText(value=0.01,
                     #description=str(question_num)+'.',
                     disabled=False)

    #Create button widget:
    answer_btn = Button(description='Kontrollera resultat',
                        disabled=False,
                        button_style='danger', # 'success', 'info', 'warning', 'danger', 'primary' or ''
                        tooltip='Tryck på knappen för att kontrollera ditt svar') 


    #Style button:
    answer_btn.style.button_color ='#3973ac'
    answer_btn.layout.width = '140px'


    #Create output widget:
    feedback_out = Output()

    #Create Valid widget to mark answer:
    #feedback = Valid(value=True,
                     #description='',
                     #readout='')


    def on_btn_click(btn):

        #Check user's answer:
        if((py_q.value < correct_answer+1.0) and (py_q.value > correct_answer-1.0)):

            #Change feedback-value to TRUE:
            #feedback.value = True

            #Correct answer:
            feedback_text = '\033[1;32m'+u'\u2713'+ '\033[0m'


        else:

            #Change feedback-value to FALSE:
            #feedback.value = False

            #Wrong answer:
            feedback_text = '\033[1;33m'+'X'+ '\033[0m'

        #Clear previous feedback output and add mark:
        with feedback_out:
            
            #Clear previous output:
            clear_output()
            
            #display(feedback)
            
            #Display new feedback:
            print(feedback_text)
            
        return




    #Call function on button_click-event:
    answer_btn.on_click(on_btn_click)



    #Display widget:
    return HBox([Label(str(question_num)+'.'), py_q, answer_btn, feedback_out])
###################################################################################


def create_coding_quiz_question_true_false(question_num, correct_answer):
    
    #Import modules:
    from ipywidgets import FloatText, Dropdown, Button, Output, HBox, Valid
    from IPython.display import clear_output
    
    

        
    #Create a Dropdown widget (with True-False options):
    py_q = Dropdown(options=['Vet inte', 'Ja', 'Nej'],
                    value='Vet inte',
                    #description=str(question_num)+'.',
                    disabled=False)
        
        

    #Create button widget:
    answer_btn = Button(description='Kontrollera resultat',
                        disabled=False,
                        button_style='danger', # 'success', 'info', 'warning', 'danger', 'primary' or ''
                        tooltip='Tryck på knappen för att kontrollera ditt svar') 


    #Style button:
    answer_btn.style.button_color ='#3973ac'
    answer_btn.layout.width = '140px'


    #Create output widget:
    feedback_out = Output()

    #Create Valid widget to mark answer:
    #feedback = Valid(value=True,
                     #description='',
                     #readout='')


    def on_btn_click(btn):

        #Check user's answer:
        if(py_q.value == correct_answer):

            #Change feedback-value to TRUE:
            #feedback.value = True

            #Correct answer:
            feedback_text = '\033[1;32m'+u'\u2713'+ '\033[0m'


        else:

            #Change feedback-value to FALSE:
            #feedback.value = False

            #Wrong answer:
            feedback_text = '\033[1;33m'+'X'+ '\033[0m'

        #Clear previous feedback output and add mark:
        with feedback_out:
            
            #Clear previous output:
            clear_output()
            
            #display(feedback)
            
            #Display new feedback:
            print(feedback_text)
            
        return




    #Call function on button_click-event:
    answer_btn.on_click(on_btn_click)



    #Display widget:
    return HBox([Label(str(question_num)+'.'), py_q, answer_btn, feedback_out])
####################################################################################



def create_coding_quiz_question_dropdown(question_num, answer_list, correct_answer):
    
    #Import modules:
    from ipywidgets import FloatText, Dropdown, Button, Output, HBox, Valid
    from IPython.display import clear_output
    
    

        
    #Create a Dropdown widget:
    py_q = Dropdown(options=sorted(answer_list),
                    value=sorted(answer_list)[0],
                    #description=str(question_num)+'.',
                    disabled=False)
        
        

    #Create button widget:
    answer_btn = Button(description='Kontrollera resultat',
                        disabled=False,
                        button_style='danger', # 'success', 'info', 'warning', 'danger', 'primary' or ''
                        tooltip='Tryck på knappen för att kontrollera ditt svar') 


    #Style button:
    answer_btn.style.button_color ='#3973ac'
    answer_btn.layout.width = '140px'


    #Create output widget:
    feedback_out = Output()

    #Create Valid widget to mark answer:
    #feedback = Valid(value=True,
                     #description='',
                     #readout='')


    def on_btn_click(btn):

        #Check user's answer:
        if(py_q.value == correct_answer):

            #Change feedback-value to TRUE:
            #feedback.value = True

            #Correct answer:
            feedback_text = '\033[1;32m'+u'\u2713'+ '\033[0m'


        else:

            #Change feedback-value to FALSE:
            #feedback.value = False

            #Wrong answer:
            feedback_text = '\033[1;33m'+'X'+ '\033[0m'

        #Clear previous feedback output and add mark:
        with feedback_out:
            
            #Clear previous output:
            clear_output()
            
            #display(feedback)
            
            #Display new feedback:
            print(feedback_text)
            
        return




    #Call function on button_click-event:
    answer_btn.on_click(on_btn_click)



    #Display widget:
    return HBox([Label(str(question_num)+'.'), py_q, answer_btn, feedback_out])
###################################################################################
