#  a progarm that allows voters to enter either A, B or C for the e-voting app 

A_count = 0
B_count = 0
C_count = 0
total_votes = 0

while True:
    choice = input("Enter your vote (A, B, or C), or 'END' to stop: ")

    if choice == 'END':
        break

    if choice == 'A':
        A_count += 1
    elif choice == 'B':
        B_count += 1
    elif choice == 'C':
        C_count += 1

    total_votes += 1

print("Number of votes for A:", A_count)
print("Number of votes for B:", B_count)
print("Number of votes for C:", C_count)
print("Total votes:", total_votes)
