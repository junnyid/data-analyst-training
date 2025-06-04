def solution(statues):
    return max(statues) - min(statues) - 1 - (len(statues) - 2)

#explain:
"""- tính số chữ số của chuỗi: số lớn nhất - số bé nhất - 1
   - tính độ dài của chuỗi - 2 ( 2 là số đầu và số cuối của chuỗi)
   - ta được, (số chữ số của chuỗi) trừ (độ dài của chuỗi trừ 2)"""
   
"""- calculate the number of digits: max - min - 1  [1]
   - Length of the number - 2 (2: the first and the last number)  [2]
   - Then, ratiorg = [1] - [2]"""
    
    