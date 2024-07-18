import re

def input_string(string):
  string = re.sub('[a-zA-Z]','',string)   # deleted letter
  number = float(string) * 1.00   # convert to float type, get decima
  number_int, number_float = str(number).split('.')   #split by '.', int & float
  number_float = '{:0<2}'.format(number_float)  # get 2 decima
  number = number_int + '.' + number_float[0:2]
  return print(number)


  # test 
  input_string('abc123.456')
  input_string('abc123')
