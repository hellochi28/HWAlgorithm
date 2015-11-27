############### Open file .txt ###############
lines = [line.rstrip('\n') for line in open('product.txt')]

key = raw_input("Product Search - Input your keyword (s): ")

############### Boyer Moore ###############
def BoyerMoore(input_search,lines):
    m = len(input_search)
    n = len(lines)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(input_search[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and lines[i] == input_search[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(lines[k])]
    return -1

############### Radix Sort ###############
def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX

############### Main ###############
random_data=[0]*len(lines)
if __name__ == '__main__':
    z=key.split()
    for i in range (0,len(lines)):
        value=0
        s0 = BoyerMoore(z[0],lines[i])
        s1 = BoyerMoore(z[1],lines[i])
        if s0 > -1 or s1 > -1 :
            if(s0>=0):
                value=200000000
                value2=s0*1000000
                if(s1>=0):
                    value=100000000
                    value2=s0*1000000
            else:
                if(s1>=0):
                    value=300000000
                    value2=s1*1000000
            if s0 > -1 or s1 >= -1 :
                value3 = abs(s1-s0)*10000
            random_data[i]=value+value2+value3+i   
    random_data=[x for x in random_data if x != 0]
    radixsort(random_data)

    for i in range(0,len(random_data)):
        if (i>9):
            break
        print lines[random_data[i]%10000]
    
