#!/usr/bin/python3
# learning python - edX - Intro to Computer Science with Python - MITx
#
# python3.5 
#
# example of Babylonain method (also known as the Heron method) of calculating the
# square root for any given value, as presented during the Intro video for the course
#
# for a non-negative value 'x' compute the square root within some error (e) = (1/1000000):
# algorithm:
# 1. initial guess 'g'
# 2. while the | x -g^2 | > e,
#    g = (g + x/g)/2
# 3. repeat steps 1 & 2 until | x - g^2 | <= e

def next_guess(initial_value,last_guess):
  next=(last_guess+(initial_value/last_guess))/2
  print("next_guess: next {}".format(next))
  return next

def close_enough(initial_value,current_guess):
  delta = abs(initial_value-current_guess**2)
  print("close_enough: (delta*1000000) == {}".format(delta))
  if (delta*1000000) < 1:	# millionths
    return True
  return False
  
## begin main ##
print("Enter a number:")
value=int(input("> "))
print("\nI will try to find the square root for: {}".format(value))

## simple guess method: int(value/2)
guess=value//2
print("My initial guess: {}".format(guess))

# start the algorithm, track the number of interations required for fun
close = False
iterations = 0

while not close:
  iterations += 1
  guess = next_guess(value,guess)
  print("Iteration: {} guess: {}".format(iterations,guess))
  close = close_enough(value,guess)

# print the results
print("\nMy calculated answer for the square root of: {} is: {}".format(value,guess))
print("\nThis took {} iterations of the Babylonian method.".format(iterations))
