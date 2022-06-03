# Problem Set 4A
# Name: <Naseem ahmadzai>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1: # single character only
        return [sequence]
    else: # inductive step
        firstChar = sequence[0]
        remaining = sequence[1:]
        perms = get_permutations(remaining)
        newPerms = [] # empty list
        
        for word in perms:
            
            for i in range (len(word)+ 1):
                newPerms.append(word[:i]+ firstChar + word[i:])
        return newPerms
                
print(get_permutations("bust"))            
        
        
        
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here
        
