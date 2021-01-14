# Knight-s-Problem

#dictionary for base cases lookup
#key: tuple (n,m)
#value: (closed_matrix, stretched_matrix, double_matrix)
base_cases = {(3,10):[3x10closed,None,None]
              (3,12):[3x12closed,None,None]
              (5,6):[5x6closed,5x6streched,None]
              (4,5):[None,4x5streched,4x5double]
              (10,10):[None,10x10streched,None]
              (3,4):[None,3x4streched,None]
              (5,6):[5x6closed,5x6streched,None]
              (5,8):[None,5x8streched,None]
              (5,10):[None,5x10streched,None]
              (6,6):[None,6x6streched,None]
              (6,8):[None,6x8streched,None]
              (10:6):[None,10x6streched,None]
              (7,6):[None,7x6streched,None]
              (10,8):[None,10x8streched,None]
	      (9,10):[None,9x10streched,None]
	      (8,8):[None,8x8streched,None]
	      (9,8):[None,9x8streched,None]
	      (8,6):[None,8x6streched,None]
	      (9,6):[None,9x6streched,None]
              }
3x10closed = [[1, 28, 25, 18, 5, 20, 23, 14, 11, 8],
[26, 17, 30, 3, 24, 15, 6, 9, 22, 13],
[29, 2, 27, 16, 19, 4, 21, 12, 7, 10]]

3x12closed = [[1, 28, 25, 18, 5, 20, 23, 14, 11, 8],
[26, 17, 30, 3, 24, 15, 6, 9, 22, 13].
[29, 2, 27, 16, 19, 4, 21, 12, 7, 10]]

5x6closed = [[1, 22, 27, 10, 7, 16],
[28, 11, 30, 15, 26, 9],
[21, 2, 23, 8, 17, 6],
[12, 29, 4, 19, 14, 25],
[3, 20, 13, 24, 5, 18]]

4x5double = [[6,20,2,14,8],
             [1,15,7,19,3],
             [11,5,17,9,13],
              [16,10,12,4,18]]
      
10x10streched = [[1,90,99,20,79,88,39,44,77,70],
                 [100,17,2,89,36,21,78,71,40,43],
                 [91,98,19,80,87,38,45,42,69,76],
                 [18,3,16,37,22,35,72,75,46,41],
                 [5,92,97,24,81,86,47,54,73,68],
                 [96,15,4,85,34,23,74,59,48,53],
                 [93,6,95,82,25,84,55,52,67,60],
                 [14,9,12,33,28,31,66,63,58,49],
                 [11,94,7,30,83,26,51,56,61,64],
                 [8,13,10,27,32,29,62,65,50,57]]
                
4x5streched = [[1, 6, 19, 14],
              [20, 15, 10, 5],
              [7, 2, 13, 18],
              [16, 11, 4, 9],
              [3, 8, 17, 12]]

3x4streched = [[1, 4, 7, 10],
              [12, 9, 2, 5],
              [3, 6, 11, 8]]

5x6streched = [[1, 26, 29, 10, 19],
              [30, 11, 20, 25, 28],
              [21, 2, 27, 18, 9],
              [12, 7, 14, 3, 24],
              [15, 22, 5, 8, 17],
              [6, 13, 16, 23, 4]]

5x8streched = [[1,36, 39, 10, 7],
              [40, 11, 8, 19, 38],
              [35, 2, 37, 6, 9],
              [12, 29, 20, 25, 18],
              [21, 34, 3, 30, 5],
              [28, 13, 26, 17, 24],
              [33, 22, 15, 4, 31],
              [14, 27, 32, 23, 16]]


5x10streched = [[1, 12, 49, 22, 25],
                [50, 21, 24, 11, 48],
                [29, 2, 13, 26, 23],
                [20, 43, 28, 47, 10],
                [41, 30, 3, 14, 27],
                [44, 19, 42, 9, 46],
                [31, 40, 45, 4, 15],
                [18, 37, 6, 33, 8],
                [39, 32, 35, 16, 5],
                [36, 17, 38, 7, 34]]

6x6streched = [[1, 8, 35, 26, 17, 6],
              [36, 25, 18, 7, 34, 27],
              [9, 2, 33, 24, 5, 16],
              [32, 19, 12, 3, 28, 23],
              [13, 10, 21, 30, 15, 4],
              [20, 31, 14, 11, 22, 29]] #edit

6x8streched = [[1, 22, 9, 18, 45, 20],
              [48, 37, 46, 21, 8, 17],
              [23, 2, 39, 10, 19, 44],
              [38, 47, 36, 43, 16, 7],
              [35, 24, 3, 40, 11, 42],
              [30, 27, 32, 13, 6, 15],
              [25, 34, 29, 4, 41, 12],
              [28, 31, 26, 33, 14, 5]]  #edit

6x10streched = [[1, 52, 59, 20, 9, 22],
                [60, 55, 10, 23, 58, 19],
                [51, 2, 53, 56, 21, 8],
                [54, 47, 24, 11, 18, 57],
                [41, 50, 3, 46, 7, 44],
                [48, 25, 40, 43, 12, 17],  
                [39, 42, 49, 4, 45, 6],
                [26, 31, 28, 35, 16, 13],
                [29, 38, 33, 14, 5, 36],
                [32, 27, 30, 37, 34, 15]]  #edit

7x6streched = [[1, 28, 41, 8, 19, 10],
              [42, 39, 20, 11, 30, 7],
              [27, 2, 29, 40, 9, 18],
              [38, 35, 12, 21, 6, 31],
              [13, 26, 3, 36, 17, 22],
              [34, 37, 24, 15, 32, 5],
              [25, 14, 33, 4, 23, 16] ]
							
							
10x8streched = [[1 ,6, 79,32,39,44,77,70],
		[80,33, 2, 5,78,71,40,43],
		[7, 4, 31,38,45,42,69,76],
		[34,37, 8, 3,72,75,46,41],
		[9, 16,35,30,47,54,73,68],
		[36,21,10,15,74,59,48,53],
		[17,14,29,22,55,52,67,60],
		[28,25,20,11,66,63,58,49],
		[13,18,23,26,51,56,61,64],
		[24,27,12,19,62,65,50,57]]
#ayman stopped here
10x6streched = [[1 ,50,,59,20,39,48],
                [60,17,2 ,49,36,21],
                [51,58,14,40,47,38],
                [18,3 ,16,37,22,35],
                [5,52,57,24,41,46],
                [56,15,4 ,45,34,23],
                [53,6 ,55,42,25,44],
                [14,9 ,12,33,28,31],
                [11,54,7 ,30,43,26]
                [8 ,13,10,27,32,29]]

9x6streched = [[1 ,26,21,16,3 ,28],
               [54,15,2 ,27,20,17],
               [25,22,53,18,29, 4],
               [14,41,24,51,34,19],
               [23,52,35,42,5,30],
               [40,13,50,31,46,33],
               [49,10,47,36,43, 6],
               [12,39,8,45,32,37],
               [9 ,48,11,38, 7,44]]
              
8x6streched = [[1 ,14,47,38,25,16],
               [48,41,2 ,15,22,37],
               [13,46,39,26,17,24],
               [40,3 ,42,23,36,21],
               [43,12,45,20,27,18],
               [6 ,9 ,4 ,33,30,35],
               [11,44, 7,28,19,32],
               [8 , 5,10,31,34,29]]

9x8streched = [[1, 6, 71,30,35,40,69,64],
               [72,29, 2, 5,70,63,36,39],
               [7, 4, 31,34,41,38,65,68],
               [28,33, 8, 3,62,67,42,37],
               [9 ,18,23,32,43,52,57,66],
               [22,27,10,17,56,61,44,51],
               [13,16,19,24,47,50,53,58],
               [26,21,14,11,60,55,48,45]
               [15,12,25,50,49,46,59,54]]

8x8streched = [[1 ,6 ,63,26,31,36,61,56],
               [64,25, 2, 5,62,55,32,35],
               [7 , 4,27,30,37,34,57,60],
               [24,29, 8, 3,54,59,38,33],
               [9 ,16,23,28,39,46,53,58],
               [22,19,12,15,52,49,42,45],
               [13,10,17,20,43,40,47,50],
               [18,21,14,11,48,51,44,41]]

9x10streched = [[1 ,62,57,52, 3,64,39,34, 5,10],
                [90,51, 2,63,56,53, 4,11,38,35],
                [61,58,89,54,65,40,33,36, 9, 6]
                [50,77,60,87,70,55,12, 7,32,37]
                [59,88,71,78,41,66,31,22,17, 8]
                [76,49,86,67,82,69,18,13,30,23]
                [85,46,83,72,79,42,27,24,21,16]
                [48,75,44,81,68,73,14,19,26,29]
                [45,84,47,74,43,80,25,23,15,20]]

closed_6_6 = [[1,24,27,8,3,16],
[26,9,2,15,28,7],
[23,36,25,6,17,4],
[10,33,18,21,14,29],
[35,22,31,12,5,20],
[32,11,34,19,30,13]]

closed_6_8 = [[1,18,43,36,3,16,13,34],
[42,37,2,17,44,35,4,15],
[19,48,9,38,5,14,33,12],
[8,41,22,47,10,45,30,27],
[23,20,39,6,25,28,11,32],
[40,7,24,21,46,31,26,29]]

closed_6_10 = [[1,20,59,24,3,22,11,14,5,44],
[58,35,2,21,40,25,4,43,10,13],
[19,60,39,36,23,42,15,12,45,6],
[34,57,32,41,26,37,28,9,48,51],
[31,18,55,38,29,16,53,50,7,46],
[56,33,30,17,54,27,8,47,52,49]]

closed_7_8 = [[1,22,43,32,3,20,45,34],
[42,31,2,21,44,33,6,19],
[23,56,11,4,17,28,35,46],
[52,41,30,27,12,5,18,7],
[55,24,53,10,29,16,47,36],
[40,51,26,13,38,49,8,15],
[25,54,39,50,9,14,37,48]]

closed_7_10 = [[1,18,69,32,3,20,47,24,5,22],
[68,65,2,19,60,31,4,21,38,25],
[17,70,63,66,33,48,41,46,23,6],
[64,67,52,59,42,61,30,37,26,39],
[53,16,55,62,49,34,45,40,7,10],
[56,51,14,43,58,29,12,9,36,27],
[15,54,57,50,13,44,35,28,11,8]]

closed_8_8 = [[1,16,41,22,3,18,43,48],
[40,23,2,17,42,47,4,19],
[15,64,39,46,21,54,49,44],
[24,37,56,63,52,45,20,5],
[57,14,61,38,55,50,53,30],
[36,25,58,51,62,31,6,9],
[13,60,27,34,11,8,29,32],
[26,35,12,59,28,33,10,7]]