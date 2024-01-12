import csv
import sys

srts = []
db_val = []
dna_seq = []
profiles = []

def main():

  # TODO: Check for command-line usage
  if len(sys.argv) < 3:
    print("Usage: python dna.py database.csv sequence.txt")
    return

  reader()
  testers()
  dna_reader()
  str_finder()
  profile_matcher()

db = sys.argv[1]
seq = sys.argv[2]

  # TODO: Read database file into a variable
def reader():

    with open(db, 'r') as file:
        reader = csv.DictReader(file)
        srts.append(reader.fieldnames)

def testers():

    with open(db, 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
          db_val.append(row)

  # TODO: Read DNA sequence file into a variable

def dna_reader():

    with open(seq, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
          dna_seq.insert(0, row)

  # TODO: Find longest match of each STR in DNA sequence
def str_finder():

    for j in range(len(srts)):
      j = 1
      match = [longest_match(dna_seq[0][0], srts[0][j])]
      match.insert(0, f"{srts[0][j]}")
      profiles.append(match)

  # TODO: Check database for matching profiles
def profile_matcher():
    for k in range(len(db_val)):
      if profiles[0][0]:
        srtsToComp = db_val[k].get(profiles[0][0])
        if str(profiles[0][1]) == srtsToComp:
          return print(db_val[k].get("name"))

    return print("No match")



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
