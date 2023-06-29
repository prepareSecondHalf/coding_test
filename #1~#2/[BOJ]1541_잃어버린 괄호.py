import sys
input = sys.stdin.readline()
existMinus = input.find('-')
result = []
isEmpty = False

# input에 '-'가 존재할 경우
if existMinus > -1:
  temp = input.split('-')

  for t in temp:
    if (len(t) > 1) :
      plusTemp = t.split('+')
      plusTempArr = []
      for s in plusTemp:
        plusTempArr.append(s.lstrip("0"))
      
      finalPlusStatement = plusTempArr[0]
      for s in plusTempArr[1:]:
        if s is plusTempArr[-1]:
          finalPlusStatement = finalPlusStatement + '+' + s
        else: finalPlusStatement = finalPlusStatement + '+' + s
      result.append(finalPlusStatement)
    else: result.append(t.lstrip("0"))

  for t in range(len(result)):
    if (result[t] == ''): result[t] = 0
    
  if len(result) == 1:
      isEmpty = True
      sum = result[0]
  else:
    for idx in range(len(result)):
      if result[idx] and result[idx] != ' ':
        item = eval(result[idx])
        result[idx] = item
  
  if (isEmpty):
    print(sum)
  else:
    if result[0] == '': sum = 0 
    else: sum = result[0]
    for t in result[1:]:
      sum -= t
      
    print(sum)

# input에 '-'가 없는 경우
else:
  temp = input.split('+')
  
    
  for t in temp:
    if (len(t) > 1) :
      plusTemp = t.split('+')
      plusTempArr = []
      for s in plusTemp:
        plusTempArr.append(s.lstrip("0"))
      
      finalPlusStatement = plusTempArr[0]
      for s in plusTempArr[1:]:
        if s is plusTempArr[-1]:
          finalPlusStatement = finalPlusStatement + '+' + s
        else: finalPlusStatement = finalPlusStatement + '+' + s
      result.append(finalPlusStatement)
    else: result.append(t.lstrip("0"))
  for t in range(len(result)):
    if (result[t] == ''): result[t] = 0
    
  if len(result) == 1:
      isEmpty = True
      sum = result[0]
  else:
    for idx in range(len(result)):
      if result[idx] and result[idx] != ' ':
        item = eval(result[idx])
        result[idx] = item
  
  if (isEmpty):
    print(sum)
  else:
    if result[0] == '': sum = 0 
    else: sum = result[0]
    sum = int(result[0])
    for t in result[1:]:
      sum += t
    print(sum)
