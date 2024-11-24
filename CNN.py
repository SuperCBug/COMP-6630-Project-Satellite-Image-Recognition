# Unfortunately, I did not manage to get a lot done on the CNN
# section, as I ended up getting sucked into the data management side.
# My deepest apologies.
class CNN():
  def __init__(self):
    self.layers = []
    self.loss = None

class CNNLayer(input,filters,stride):
  def __init__(self,inputs,filters,stride):
    self.inputs = inputs
    self.stride = stride
    self.output = None
    self.filters = filters

  def forward_pass(self, input):
    # Create an Empty Array and start appending values to it based on stride size
    output = []
    # Assume we're starting at 0,0 for now
    currentX = 0
    currentY = 0
    maxX = self.input.shape[0]
    maxY = self.input.shape[1]

    # Forward Pass to Set Weights
    for filterNumber in range(filters):
      filterMaxX = maxX - filters[filterNumber].shape[0]
      for y in range(0,maxY,self.stride):
        for x in range(0,maxX,self.stride):
          # This will add a single value per activation per evaluation
          output[filterNumber] = output + evaluate_section(x,y,,input)

    self.output = output
    return output
  def backward_prop(self):
    pass

  def update_weights(self):
    pass

  def update_bias(self):
    pass

  def evaluate_section(self,x,y,filter,input):




class Node():
  def __init__(self):
    self.weight = None
    self.bias = None
    self.input = None
    self.output = None

def sigmoid_function(input):
  return