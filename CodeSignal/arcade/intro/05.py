def solution(n):
    return (n**2+(n-1)**2)

''' explain:
- the side are always n
- if n = 3, the shape has for 3 squares on each other => n * n (the area of square)
- But n * n doesn't count for all squares. There are squares inside
- Except the squares in outside, you will notice now that the side inside is n-1
- Thus, the formula is n**2 + (n-1)**2 '''