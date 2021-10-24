def runLengthEncoding(message):
    dic = {}
    for i in message:
        if i in dic:
           dic[i] += 1
        else:
            dic[i] = 1
    result = ''.join(''.join((key,str(val))) for (key,val) in dic.items())
    return result

# example
result = runLengthEncoding("wwweeeeeff")
print(result);
