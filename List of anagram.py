def count(arr1, arr2, n, m):

    freq = {}
    c=0
 
    for word in arr1:
         
        
        word = ' '.join(sorted(word))
 
        
        if word in freq.keys():
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
 
    for word in arr2:

        word = ' '.join(sorted(word))

        if word in freq.keys():
            c+=freq[word]
             
    print(c)    
    
if __name__ == '__main__':
      
    arr1 =eval(input())
    n = len(arr1)
     
    arr2 =eval(input())
    m = len(arr2)
 
    count(arr1, arr2, n, m)
