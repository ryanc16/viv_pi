import math

class Stats:
  def mean(values):
    return sum(values)/len(values)

  def std(values):
    mean = Stats.mean(values)
    squares = []
    for v in values:
      squares.append(math.pow(abs(v-mean), 2))
    return math.sqrt(sum(squares)/len(values))

  def weighted_std(values):
    mean = Stats.weighted_average(values)
    squares = []
    for v in values:
      squares.append(math.pow(abs(v-mean), 2))
    return math.sqrt(sum(squares)/len(values))

  def adjusted_mean(values, value):
    mean = Stats.mean(values)
    return Stats.mean([mean, value])

  def adjusted_weighted_mean(values, value):
    newlist = ([] + values)
    newlist.append(value)
    return Stats.weighted_average(newlist)

  def weighted_average(values):
    weighted_sum = 0
    weights = list(range(1, len(values)+1))
    for i in weights:
      weighted_sum += i * values[i-1]
    return weighted_sum/sum(weights)

def within_std(values, value, std_factor = 2):
  mean = Stats.mean(values)
  std = Stats.std(values)
  return value > mean - std_factor * std and value < mean + std_factor * std

def within_weighted_std(values, value, std_factor = 2):
  mean = Stats.weighted_average(values)
  std = Stats.weighted_std(values)
  lower_bound = mean - std_factor * std
  upper_bound = mean + std_factor * std
  print(f"{value} must be between {lower_bound} and {upper_bound}")
  return value > lower_bound and value < upper_bound