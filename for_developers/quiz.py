from ipywidgets import widgets, Layout
from IPython.display import clear_output
import json

#maybe use Question as an interface and implement checkquestion and radioquestion
class QuestionInterface:
  def question_widget(self) -> widgets.Widget:
    #create the question widget
    pass
  def check_solution(self) -> bool:
    #check if the chosen colution is correct
    pass
  def reset_question(self) -> None:
    #reset the question into its original state
    pass

class RadioQuestion(QuestionInterface):
  def __init__(self, num, quest_dict):
    self.num = num
    self.prompt = quest_dict['question']
    self.options = quest_dict['options']
    self.feedback = quest_dict['feedback']
    self.answer = quest_dict['answer']
    self.alt_widget = None #widget which drives the different alternatives
  
  def question_widget(self) -> widgets.VBox:
    #create question widget
    question_out = widgets.Output(layout=Layout(width='auto'))
    with question_out:
      print('Fråga', str(self.num) + ':', self.prompt)
    alts_widget = self._create_radio_widget()
    return widgets.VBox([question_out, alts_widget])
    
  def check_solution(self) -> bool:
    # check if the chosen alternatives are correct, also output feedback
    correct = True
    alt, feedback_out = self.alt_widget.children
    color_backgroud = '\u001b[48;5;2m'
    color_text = '\u001b[38;5;250m'
    color_reset = '\u001b[0m'
    if alt.value == None:
      return False
    if alt.value != self.answer[0]:
      correct = False
      color_backgroud = '\u001b[48;5;1m'
    with feedback_out:
      clear_output()
      print(color_backgroud + color_text + self.feedback[alt.value] + color_reset)
    print(self.feedback[alt.value])
    
    return correct
  
  def reset_question(self) -> None:
    alt, feedback_out = self.alt_widget.children
    alt.value = None
    with feedback_out:
      clear_output()

        
  def _create_radio_widget(self) -> widgets.HBox:
    # create a radio widget and set value of self.alt_widget
    alternatives = widgets.RadioButtons(
      options = self.options,
      description = '',
      disabled = False,
      indent = False,
      align = 'center',
      value = None)
    quest_box = widgets.HBox([alternatives, widgets.Output()], 
                             layout=widgets.Layout(align_items='center', 
                                                   display='inline-flex',
                                                   flex_flow='row wrap'))
    self.alt_widget = quest_box
    return quest_box


class CheckboxQuestion(QuestionInterface):
  def __init__(self, num, quest_dict):
    self.num = num
    self.prompt = quest_dict['question']
    self.options = quest_dict['options']
    self.feedback = quest_dict['feedback']
    self.answer = quest_dict['answer']
    self.alt_widget = None #widget which monitors the different alternatives
  
  def question_widget(self) -> widgets.VBox:
    #create question widget
    question_out = widgets.Output(layout=Layout(width='auto'))
    with question_out:
      print('Fråga', str(self.num) + ':', self.prompt)
    alts_widget = self._create_checkbox_widget()
    return widgets.VBox([question_out, alts_widget])
    
  def check_solution(self) -> bool:
    # check if the chosen alternatives are correct, also output feedback
    correct = True
    nbr_chosen = 0
    color_text = '\u001b[38;5;250m'
    color_reset = '\u001b[0m'
    for i, alt in enumerate(self.alt_widget):
      color_background = '\u001b[48;5;2m'
      chosen = alt.children[0].value
      feedback_out = alt.children[1]
      with feedback_out:
        clear_output()
        if chosen:
          nbr_chosen += 1
          if self.options[i] not in self.answer:
            correct = False
            color_background = '\u001b[48;5;1m'
          print(color_background + color_text + self.feedback[self.options[i]] + color_reset)
    if nbr_chosen < len(self.answer):
      correct = False
    return correct
  
  def reset_question(self) -> None:
    for box in self.alt_widget:
      alt, feedback_out = box.children
      alt.value = False
      with feedback_out:
        clear_output()
  
  def _create_checkbox_widget(self) -> widgets.VBox:
    # create a checkbox widget and set value of self.alt_widget
    checkboxes = []
    for i, opt in enumerate(self.options):
      chkbox = widgets.Checkbox(
                        value=False,
                        description=opt,
                        disabled=False,
                        indent=False)
      checkboxes.append(widgets.HBox([chkbox, widgets.Output()],
                                     layout=widgets.Layout(display='inline-flex',
                                                           flex_flow='row wrap')))
    self.alt_widget = checkboxes
    return widgets.VBox(checkboxes,
                        indent=False,
                        layout=Layout(display='flex', 
                                      flex_flow='column', 
                                      align_items='stretch', 
                                      width='auto'))



class Quiz:
  def __init__(self, quest_list):
    self.questions = []
    for i, q_d in enumerate(quest_list, 1):
      if len(q_d['answer']) > 1:
        self.questions.append(CheckboxQuestion(i, q_d))
      else:
        self.questions.append(RadioQuestion(i, q_d))
    self.quest_widgets = [q.question_widget() for q in self.questions]
    self.button_exe = self._button_exe()
    self.button_init = self._button_init()
    self.result_out = widgets.Output()
    all_widgets = self.quest_widgets.copy()
    all_widgets.extend([
        widgets.HBox([self.button_exe, 
                      self.button_init]), 
        self.result_out])
    self.quiz = widgets.VBox(all_widgets,
                             layout=Layout(display='flex',
                                           flex_flow='column',
                                           align_items='stretch',
                                           width='auto'))
  
  def show_quiz(self) -> None:
    display(self.quiz)

  def check_quiz(self, button_c) -> None:
    nbr_correct = 0
    for q in self.questions:
      if q.check_solution():
        nbr_correct += 1
    self.show_result(nbr_correct)
  
  def show_result(self, nbr_correct) -> None:
    nbr_quest = len(self.quest_widgets)
    with self.result_out:
      clear_output()
      print(nbr_correct, 'av', nbr_quest, 'rätt')
  
  def reset_quiz(self, button_c) -> None:
    for q in self.questions:
      q.reset_question()
    with self.result_out:
      clear_output()
  

  def _button_exe(self) -> widgets.Button:
    button_exe = widgets.Button(description='Visa resultat',
                        disabled=False,
                        button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
                        tooltip='Tryck på knappen för att visa resultat',
                        icon='check')
    button_exe.style.button_color = '#3973ac'
    button_exe.layout.width = '250px'
    button_exe.layout.margin = '50px 100px 40px 300px'
    button_exe.on_click(self.check_quiz)
    return button_exe

  def _button_init(self) -> widgets.Button:
    button_init = widgets.Button(description='   Försök igen',
                         disabled=False,
                         button_style='success', # 'success', 'info', 'warning', 'danger' or ''
                         tooltip='Tryck på knappen för att ta om testet',
                         icon='repeat')
    button_init.layout.width = '130px'
    button_init.layout.margin = '50px 50px 40px 100px'
    button_init.on_click(self.reset_quiz)
    return button_init

def main(quest_dict):
  q = Quiz(quest_dict)
  q.show_quiz()
