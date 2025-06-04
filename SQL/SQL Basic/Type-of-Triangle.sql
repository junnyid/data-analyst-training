SELECT 
    case
        When A + B <= C or A + C <= B or B + C <= A then 'Not A Triangle'
        When A = B and B = C then 'Equilateral'
        When A = B or B = C or C = A then 'Isosceles'
        Else 'Scalene'
    End As Triangles
From TRIANGLES