def find_nth_occurrence(substring, string, ocurrence=1):
  
    try:
      x=string.count(substring)
      if x<ocurrence:
        return (-1)
      elif  ocurrence==1:
        start=string.find(substring)
        return (start)

      elif x>= ocurrence or x==ocurrence:

        # z=string.find(substring,[-1,)
          y=string.split()
          for i in range(len(y)):
            if y[i] != substring:
                z=len(y[i]) 
                y[i]=z*'#'
              
                
          word=' '.join(y)
          start=word.find(substring)
          #print(start)
          if ocurrence==2:
            return (start)
          else: 
            final=word.find(substring,start+len(substring))
            return (final)
    except TypeError:
        print('Wrong input')


def solve(a,b):
  if a == b: return True
  if "*" not in a: return False
 
  pos = a.find('*') 
  missing = b[pos:len(b)-len(a)+pos+1]
  a = a.replace("*", missing)
  return a == b
  
def is_palindrome(s):
  s=s.lower()
  n=-1
  try:
    if len(s)%2==0:
      for i in range(len(s)//2):
        if s[i]!=s[n]:
          return False
        n-=1
      return True
          
    else:
      for i in range(len(s)):
        if s[i]==s[n] :
            n-=1
            if i == len(s)//2:
              return True
              
        else:
          return False
  except TypeError:
     print("Wrong input")      




def f(string):
  try:
    for i in range (len(string)):
      sub = string[:i+1]
      print(sub)
      k = len(string)//len(sub)
      print(sub * k)
      if sub * k == string:
        return (sub, k)
  except TypeError:
    print("Wrong Input")               


