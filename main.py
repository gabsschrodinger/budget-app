import math

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description = ""):
    self.ledger.append({ "amount": amount, "description": description })

  def withdraw(self, amount, description = ""):
    if(self.check_funds(amount)):
      self.ledger.append({ "amount": -amount, "description": description })
      return True
    else: return False

  def get_balance(self):
    return sum(map(lambda i: i["amount"], self.ledger))
    
  def transfer(self, amount, category):
    if(self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else: return False

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def __str__(self):
    total = 0
    output = ""
    for i in range(int((30 - len(self.name)) / 2)):
      output += "*"
    output += self.name
    for i in range(int((30 - len(self.name)) / 2)):
      output += "*"
    output += "\n"
    for i in self.ledger:
      total += i['amount']
      if(len(i['description']) > 30 - 1 - len(str("{:.2f}".format(i['amount'])))):
        number = 30 - 1 - len(str("{:.2f}".format(i['amount'])))
        output += i['description'][:number]
        output += " "
        output += str("{:.2f}".format(i['amount']))
      else:
        output += i['description']
        for j in range(30 - len(str("{:.2f}".format(i['amount']))) - len(i['description'])):
          output += " "
        output += str("{:.2f}".format(i['amount']))
      output += "\n"
    output += "Total: " + str("{:.2f}".format(total))
    return output


def create_spend_chart(categories):
  percentages = []
  total_value = 0
  for i in categories:
    withdraws = 0
    for j in i.ledger:
      if(j["amount"] < 0): withdraws += abs(j["amount"])
    total_value += withdraws
  for i in categories:
    withdraws = 0
    for j in i.ledger:
      if(j["amount"] < 0): withdraws += abs(j["amount"])
    percentages.append(math.floor(100 * withdraws / total_value))
  output = "Percentage spent by category\n"
  initial_value = 100
  for i in range(11):
    for j in range(3 - len(str(initial_value))):
      output += " "
    output += str(initial_value) + "| "
    for i in range(len(categories)):
      if(percentages[i] >= initial_value): output += "o"
      else: output += " "
      output += "  "
    output += "\n"  
    initial_value -= 10
  output += "    "
  for i in range(len(categories) * 3 + 1):
    output += "-"
  output += "\n"
  catetegories_len = []
  for i in categories:
    catetegories_len.append(len(i.name))
  for i in range(max(catetegories_len)):
    output += "     "
    for j in categories:
      try:
        output += j.name[i]
      except:
        output += " "
      output += "  "
      if(j.name == categories[-1].name and i != max(catetegories_len) - 1): output += "\n"
  return output