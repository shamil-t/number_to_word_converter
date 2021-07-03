below_20 = ["","one","two","three","four","five","six","seven","eight","nine",
"ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
"eighteen","ninteen"];

above_20 = ["","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

thousands = {100:'hundred', 1000:'thousand', 100000:'million', 1000000000:'billion'}

def num_to_word(num):

  if num == 0:
    return 'zero'

  if num<20:
    return below_20[num]

  if num<100:
    if num%10 ==0:
      return above_20[(int)(num/10) - 1]
    else:
      return above_20[(int)(num/10) - 1] +' '+ below_20[num%10]
  
  if num > 100:
    element = max([key for key in thousands.keys() if key <= num])

    word= num_to_word((int)(num/element)) + ' ' + thousands[element]+ ('' if num%element==0 else ' ' + num_to_word(num%element))

    return word

print(num_to_word(0)+' dollars')
print(num_to_word(250)+' dollars')
print(num_to_word(8950)+' dollars')
print(num_to_word(75603)+' dollars')
print(num_to_word(1234567)+' dollars')
print(num_to_word(123456789)+' dollars')
print(num_to_word(1234567890)+' dollars')
print(num_to_word(7654321)+' dollars')