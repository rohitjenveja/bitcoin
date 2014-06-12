#!/usr/bin/python

"""Practice code for parsing a CSV without using a csv parser."""


class Data(object):

  def __init(self, elements, validity):
    self.elements = elements
    self.validity = validity

  def GetValidity(self):
    return self.validity

  def GetElements(self):
    return self.elements


def Parse(string):
  elements = []
  _queue = []
  str_len = len(string)
  validity = True

  for index, letter in enumerate(string):
    if skip_next_item:
      continue

    if letter == '/':
      # look ahead one item
      if index + 1 < str_len:
        if string[index+1] in (',', '/'):
          _queue.append(string[index+1])
          skip_next_item = True
        else:
          validity = False
          elements.append(_queue)
          return Data(elements, validity)


    elif letter == ',':
      # flush the queue
      elements.append(_queue)
      _queue = []
    else:
      _queue.append(letter)

  elements.append(_queue)
  return Data(elements, validity)
