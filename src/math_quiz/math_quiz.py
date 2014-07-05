#!python
operation = 'addition'
operation_sign = '+'
import operator
test_operator = operator.add
min_lhs = 0
max_lhs = 11
min_rhs = 0
max_rhs = 9

class Question(object):
  def __init__(self, lhs, operation_sign, rhs, answer):
    self._lhs = lhs
    self._operation_sign = operation_sign
    self._rhs = rhs
    self._answer = answer

  def __str__(self):
    retval = ''
    retval += '%d %s %s = %d' % (self._lhs, self._operation_sign, self._rhs, self._answer)
    return retval

  def state_problem(self):
    retval = ''
    retval += '%d %s %s = ???' % (self._lhs, self._operation_sign, self._rhs)
    return retval

class QnA(object): #represents question posed and student's answer
  def __init__(self, question, students_answer):
    self._question = question
    self._students_answer = students_answer
    self._correct = (students_answer == question._answer)

  def __str__(self):
    retval = ''
    retval += '%s ------- ' % str(self._question)
    retval += 'You chose %s - ' % str(self._students_answer)
    retval += 'CORRECT' if self._correct else 'You were wrong'
    return retval

class QuestionParams(object):
  def __init__(self, test_operator, operation_sign, min_lhs, max_lhs, min_rhs, max_rhs):
    self._test_operator = test_operator
    self._operation_sign = operation_sign
    self._min_lhs = min_lhs
    self._max_lhs = max_lhs
    self._min_rhs = min_rhs
    self._max_rhs = max_rhs

def generate_question(question_params):
  import random
  qp = question_params
  lhs = random.randint(qp._min_lhs, qp._max_lhs)
  rhs = random.randint(qp._min_rhs, qp._max_rhs)
  answer = qp._test_operator(lhs, rhs)
  question = Question(lhs=lhs, operation_sign=qp._operation_sign, rhs=rhs, answer=answer)
  return question

def make_test(question_params, num_questions=10):
  import random
  test = []
  for i in range(num_questions):
    question = generate_question(question_params)
    test.append(question)
  return test

from Tkinter import *
class Game(object):
  def __init__(self):
    self._current_question = 0
    self._question_number = 1
    self._total_correct = 0

  def choose_answer(self, students_answer):
    qna = QnA(self._test[self._current_question], students_answer)
    self._qnas.append(qna)
    self._label_frame.config(text=str(qna))
    if qna._correct:
      self._total_correct += 1
    if self._current_question < 9:
      for i in range(10):
        self._buttons[i].config(text='NEXT!', command=self.next_question)
    else:
      summary = '%d out of 10 correct.\n' % self._total_correct
      for i in range(10):
        self._buttons[i].config(text='DONE!', command=lambda: self.write_report_and_quit(operation, summary, self._qnas))


  def next_question(self):
    self._question_number = self._question_number + 1
    self._current_question = self._current_question + 1
    self._label_frame.config(text='#%d ------- %s' % (self._question_number, self._test[self._current_question].state_problem()))
    import random
    offset = random.randint(-9, 0)
    answer = self._test[self._current_question]._answer
    for i in range(10):
      button_num = offset + i + answer
      self._buttons[i].config(text='%d' % button_num, command=lambda num=button_num: self.choose_answer(students_answer=num))

  def start_new_test(self):
    question_params = QuestionParams(test_operator, operation_sign, min_lhs, max_lhs, min_rhs, max_rhs)
    self._test = make_test(question_params=question_params)
    self._qnas = []
    self._current_question = 0
    self._question_number = 1
    self._total_correct = 0
    self._label_frame.config(text='#%d ------- %s' % (self._question_number, self._test[self._current_question].state_problem()))
    import random
    offset = random.randint(-9, 0)
    answer = self._test[self._current_question]._answer
    for i in range(10):
      button_num = offset + i + answer
      self._buttons[i].config(text='%d' % button_num, command=lambda num=button_num: self.choose_answer(students_answer=num))

  def play_again(self):
    import tkMessageBox
    if tkMessageBox.askyesno('Play again?', 'Would you like to play again?'):
      self.start_new_test()
    else:
      self._root.destroy()

  def write_report_and_quit(self, operation, summary, qnas): #could use hash to ensure uniqueness of test
    import datetime
    report_id = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M__') + operation
    report = ''
    report += str(summary) + '\n'
    for qna in qnas:
      report += str(qna) + '\n'
    import tkMessageBox
    tkMessageBox.showinfo('Great effort!', report + '\n\nPlay again some time!')    
    report = 'TEST: %s\n' % report_id + report
    report_file = open(report_id + '.txt', 'w')
    report_file.write(report)
    report_file.close()
    #for i in range(9):
    #  self._buttons[i].pack_forget()
    for i in range(10):
      self._buttons[i].config(text='Great!', command=self.play_again)
    self._label_frame.config(text='Thanks for playing!')

  def play_game(self):
    question_params = QuestionParams(test_operator, operation_sign, min_lhs, max_lhs, min_rhs, max_rhs)
    self._test = make_test(question_params=question_params)
    self._qnas = []
    self._root = Tk()
    self._root.wm_title(operation)
    self._root.wm_state('zoomed')
    import tkFont
    helv32 = tkFont.Font(family='Helvetica', size=32, weight='bold')
    helv22 = tkFont.Font(family='Helvetica', size=20, weight='bold')
    self._label_frame = LabelFrame(self._root, font=helv32, text='#%d ------- %s' % (self._question_number, self._test[self._current_question].state_problem()))
    self._label_frame.pack()
    self._buttons = []
    import random
    offset = random.randint(-9, 0)
    answer = self._test[self._current_question]._answer
    for i in range(10):
      button_num = offset + i + answer
      b = Button(self._label_frame, width=40, font=helv22, text='%d' % button_num, command=lambda num=button_num: self.choose_answer(students_answer=num))
      b.pack()
      self._buttons.append(b)
    self._root.mainloop()

if __name__ == '__main__':
  Game().play_game()


