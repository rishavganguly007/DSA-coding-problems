## Bit Manipulations Notes

#### <ins>Right shift Operator:</ins>
         101 >> 2 -> shifts towards right
  Trick: right Shift 8 by n, means, val will be 8 / 2<sup>n</sup> 
#### <ins>Left shift Operator:</ins>
         101 << 2 -> shifts towards right
  Trick: Left Shift 8 by n, means, val will be 8 * 2<sup>n</sup> 
  
  ### <ins>problem-1</ins>
  <samp>Find the XOR of 1st N numbers in O(1)</samp>
  

    # XOR repeats in cycle of 4
    if n % 4 == 0: 
	    val = n
	if n % 4 == 1:
	    val = 1
	if n % 4 == 0:
	    val = n + 1
	if n % 4 == 0:
	    val = 0
### <ins>problem-2</ins>
  <samp>Find the XOR in [L, R] in O(1)</samp>
  

    XOR_till(R) ^ XOR_till(L)
### <ins>problem-3</ins>
  <samp>Check if N is Odd or Even</samp>
  

    if n & 1 == 0:
	    return 'even'
	else:
		return 'odd'
## Properties

 1. <samp>(N, i) -> check if the ith is set or not, 
	 eg. (1101), i =3 , it's set</samp>
	 

    N = 			011001	,	i = 3
    mask = 	001000
    Ans=	001000
   

     code:
        mask = (1 << i)
        set = (mask & n)

  

 2.  <samp>Set the ith bit</samp>
 

    n = n or (1 << i)
 N = 			110010,	i = 2
    mask = 	000100
    Ans=	(OR) 110110, 	2nd bit got set
 3. <samp>clear the ith bit (make it zero)</samp>
	 

    N = N and ~( 1 << i )
    N = 110010
    ~mask = 101111
    (and) 100010

 4. <samp>Remove the last set bit</samp>
 
     ans = N & N -1
