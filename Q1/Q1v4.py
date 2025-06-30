import random

# folding technique
def folding(num):
    num_str = str(num).zfill(12)  # Pad to 12 digits
    blocks = [int(num_str[i:i+4]) for i in range(0, 12, 4)]  # Fold into 3 blocks
    return sum(blocks)  # Return folded sum

# generates 12 digit numbers
def gen_num():
    # Year: 70-99 (1970-1999) or 00-25 (2000-2025)
    year = random.choice(list(range(70, 100)) + list(range(0, 26)))

    # Month: 01-12
    month = random.randint(1, 12)

    # Day: 01-28 (to avoid invalid dates)
    day = random.randint(1, 28)

    # Place of birth code: 01-59 (simplified Malaysian state codes)
    place = random.randint(1, 59)

    # Last 4 digits: ###G (sequential number + gender)
    last_four = random.randint(0, 9999)

    # Combine all parts into 12-digit number
    ic_number = f"{year:02d}{month:02d}{day:02d}{place:02d}{last_four:04d}"
    return ic_number

# creates the hash table for separate chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def insert(self, num):
        index = folding(num) % self.size
        if self.table[index]:  # collision
            self.collisions += 1
        self.table[index].append(num)

    def display(self, max_entries=10):
        print(f"\nHash Table with size {self.size} (showing first 5 and last 5 slots):")

        total_slots = len(self.table)

        # Show first 5 slots
        for i in range(5):
            if self.table[i]:
                print(f"table[{i}] --> " + " --> ".join(map(str, self.table[i])))
            else:
                print(f"table[{i}] --> [...]")

        if total_slots > 10:
            print("...")

        # Show last 5 slots
        for i in range(total_slots - 5, total_slots):
            if self.table[i]:
                print(f"table[{i}] --> " + " --> ".join(map(str, self.table[i])))
            else:
                print(f"table[{i}] --> [...]")
#main driver program
def main():
    num_ics = 1000
    size1 = 1009
    size2 = 2003

    total_collisions1 = 0
    total_collisions2 = 0

    # Display tables only once at the start (Round 1)
    first_round_display = True

    for round_num in range(1, 11):
        print(f"\n{'='*50}")
        print(f"ROUND {round_num}")
        print(f"{'='*50}")

        table1 = HashTable(size1)
        table2 = HashTable(size2)

        ic_list = [gen_num() for _ in range(num_ics)]
        for ic in ic_list:
            table1.insert(ic)
            table2.insert(ic)

        # Display sample of both tables only in the first round
        if first_round_display:
            table1.display()
            table2.display()
            first_round_display = False

        # Calculate rates
        rate1 = (table1.collisions / num_ics) * 100
        rate2 = (table2.collisions / num_ics) * 100

        # Display collision statistics for this round
        print(f"\n--- Round {round_num} Collision Statistics ---")
        print(f"Table Size {size1}: The total number of collisions is {table1.collisions} and the collision rate is {rate1:.2f}% ")
        print(f"Table Size {size2}: The total number of collisions is {table2.collisions} and the collision rate is {rate2:.2f}% ")

        total_collisions1 += table1.collisions
        total_collisions2 += table2.collisions

    # Final average after 10 rounds
    avg_collisions1 = total_collisions1 / 10
    avg_collisions2 = total_collisions2 / 10
    avg_rate1 = (total_collisions1 / (num_ics * 10)) * 100
    avg_rate2 = (total_collisions2 / (num_ics * 10)) * 100

    print(f"\n{'='*60}")
    print("FINAL SUMMARY AFTER 10 ROUNDS")
    print(f"{'='*60}")
    print(f"Table Size {size1}:")
    print(f"  Total collisions across all rounds: {total_collisions1}")
    print(f"  Average collisions per round: {avg_collisions1:.2f}")
    print(f"  Average collision rate: {avg_rate1:.2f}%")
    print()
    print(f"Table Size {size2}:")
    print(f"  Total collisions across all rounds: {total_collisions2}")
    print(f"  Average collisions per round: {avg_collisions2:.2f}")
    print(f"  Average collision rate: {avg_rate2:.2f}%")

if __name__ == "__main__":
    main()
