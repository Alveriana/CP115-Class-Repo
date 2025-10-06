num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score
final_score = 0
rounds_processed = 0
bonus = 0

for i in range (num_rounds):
    round_score = float(input())

    if round_score > 100:
        bonus = round_score * 0.2
        round_score += bonus

    final_score += round_score
    rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)