# TODO: Complete the check_spell function
def check_spell(expression):
# TODO: Add logic to determine if the expression contains spells
    IndexList=findVowel(expression)
    if(len(IndexList) < 5):
        return False
    while(True):
        firstWord=expression[0:IndexList[1]+1]
        # before first word letters removal
        while(beforeFirstWord(expression,firstWord)=="-1"):
            expression=expression.replace(firstWord,"",1)
            IndexList.pop(0)
            IndexList.pop(0)
            if(len(IndexList) < 5):
                return False
            firstWord=expression[0:IndexList[1]+1]
        firstWord=beforeFirstWord(expression,firstWord)
        lastWord=expression[(expression.rfind(firstWord)):]
        while(afterLastWord(expression,lastWord)=="-1"):
            expression=expression[:(expression.rfind(lastWord))]
            IndexList.pop(-1)
            IndexList.pop(-1)
            if(len(IndexList) < 5):
                return False
            lastWord=expression[IndexList[-2]:]
        lastWord=afterLastWord(expression,lastWord)
        if(expression.count(lastWord)>1 and len(IndexList) >= 5):
            if(len(findVowel(lastWord))>=2):
                return True
        elif(len(IndexList) < 5):
            return False
        expression=expression.replace(lastWord,"",1)
        expression=expression[:(expression.rfind(lastWord))]
        IndexList.pop(0)
        IndexList.pop(0)
        IndexList.pop(-1)
        IndexList.pop(-1)
        continue
    
def beforeFirstWord(expression,firstWord):
    if(firstWord==""):
        return "-1"
    alpha=firstWord[0]
    if(expression.rfind(firstWord)!=expression.find(firstWord)):
        return firstWord
    else:
        firstWord=firstWord.replace(alpha,"",1)
        return beforeFirstWord(expression,firstWord)
    
def afterLastWord(expression,lastWord):
    if(lastWord==""):
        return "-1"
    if(expression.rfind(lastWord)!=expression.find(lastWord)):
        return lastWord
    else:
        lastWord=lastWord[:-1]
        return afterLastWord(expression,lastWord)

def findVowel(expression):
    vowel="aeiou"
    indexList=[]
    for i in vowel:
        while(expression.find(i)!=-1):
            indexList.append(expression.find(i))
            expression=expression.replace(i,"",1)
    return merge_sort(indexList) 
    
def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res
def main():
    # Get the number of test cases
    num_tests = int(input())
    for t in range(num_tests):
        # Get the Witch's expression
        expression = input()
        answer = 'Nothing.'
        if(check_spell(expression)):
            answer = 'Spell!'
        print(f'Case #{t+1}: {answer}')

if __name__ == '__main__':
  main()