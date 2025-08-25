# Test addition and average
score1 = 85
score2 = 92.5
score3 = 78
total_score = score1 + score2 + score3
average1 = total_score / 3
average2 = int(total_score / 3)
print(f" 85 + 92.5 + 78 = {total_score} (type {type(total_score)}) ")
print(f" total_score/3 = {average1} (type {type(average1)}) ")
print(f" total_score/3 = {average2} (type {type(average2)}) ")

# Test a complex expression
complex_compression = score1 ** 2 / score2 + score3 % 7
print(f" 85 ** 2 / 92.5 + 78 % 7 = {complex_compression} (type{type(complex_compression)}) ")

int(score2)
float(score1)
print(f"int(92.5) = {int(score2)} (type {type(int(score2))}) ")
print(f"float(85) = {float(score1)} (type {type(float(score1))}) ")