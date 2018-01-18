"""
Andrew Ward - Tesla Knowledge Check

Question 2 - Mirror Words
  Implement the procedure 'find_mirrors' found on the next page.
  o in_file contains a list of words, one word per line.
  o a sample list of words is available at: http://www.cs.duke.edu/~ola/ap/linuxwords

  You will write to out_file a list of in_file words where the first word is a mirror image (letter reversed) copy of the second word, and both words exist in in_file. There should be one pair of words per line.
  * For example, out_file might contain:
      o Bard/draB, Bud/duB, Are/erA, Bag/gaB, Brag/garB, etc.
  * Requirements:
    o Describe how your algorithm works
    o Describe why you chose to implement it the way you did.
    o Eliminate Palindrome words like eye, civic and deed
    o Use a case sensitive compare: Aa would match aA but not aa
    o Include a copy of out_file in your response
    o Just implement find_mirrors, we're not looking for other improvements


def find_mirrors(in_file, out_file): 
  raise NotImplementedError # change this 

with open("linuxwords", 'r') as in_file: 
  with open('output.txt', 'w') as out_file: 
    find_mirrors(in_file, out_file)
"""

def find_mirrors(in_file, out_file): 
    in_list = in_file.read().splitlines()
    
    # Eliminate Palindromes
    # use a  generator to iterate the list, but only the word is NOT the same if reversed
    in_list_cleaned = [word for word in in_list if list(word) != list(reversed(word))]

    # Create python sets  (for finding an *intersection* later
    in_list_as_set = set(in_list_cleaned)

    # Create a set of the words reversed (Use a generator to reverse the words)
    in_list_reversed_as_set = set([''.join(list(reversed(word))) for word in in_list_as_set])

    # Get the intersection of the two sets.... That *IS* the mirrored words.
    mirrors = in_list_as_set & in_list_reversed_as_set

    # Save the output in the  file
    out_file.write("\n".join(mirrors))

if __name__ == '__main__':
    with open("tesla_linuxwords.txt", 'r') as in_file: 
      with open('tesla_output.txt', 'w') as out_file: 
        find_mirrors(in_file, out_file)


