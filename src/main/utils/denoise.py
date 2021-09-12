from src.main.utils.stats import Stats

# function which eliminates the noise
# by using a statistical model
# we determine the standard normal deviation and we exclude anything that goes beyond a threshold
# think of a probability distribution plot - we remove the extremes
# the greater the std_factor, the more "forgiving" is the algorithm with the extreme values
def eliminateNoise(values, std_factor = 2):
  # print("input: ", values)
  mean = Stats.mean(values)
  standard_deviation = Stats.std(values)

  if standard_deviation == 0:
    return values

  final_values = [element for element in values if element > mean - std_factor * standard_deviation]
  final_values = [element for element in final_values if element < mean + std_factor * standard_deviation]
  # print("output: ", final_values)
  return final_values