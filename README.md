# CTFwriteup

## picoCTF
### Cryptography
1. New Caesar
2. Mini RSA
  > 當RSA的e(e=3)很小，且C^e<N時
  > 
  > M=根號3(C+k*N)
                    
3. Dachshund Attacks
  >當RSA的d很小時，可以透過wiener attack來破解。
  >
  >安裝wiener套件來找出d
  
  `pip install owiener`
  ```python
  d = owiener.attack(e, n)
  if d is None:
    print("Failed")
  else:
    print("Hacked d={}".format(d))
  ```
