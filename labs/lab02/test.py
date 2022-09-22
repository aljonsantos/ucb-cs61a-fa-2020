from ucb import trace

@trace
def mul(m, n):
    if n == 1:
        return m
    else:
        return m + mul(m, n-1)

@trace
def hail(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hail(n // 2)
    else:
        return 1 + hail(n * 3 + 1)


def merge(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2)*10 + (n1 % 10)
    else:
        return merge(n1, n2 // 10)*10 + (n2 % 10)


@trace
def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    # res = ''
    # while len(w2) > 0:
    #     if w2[0] in w1:
    #         w1 = w1.replace(w2[0], '')
    #     else:
    #         res += w2[0]
    #     w2 = w2[1:]
    # return res

    @trace
    def helper(res, w1, w2):
        if len(w2) == 0:
            return res
        elif w2[0] in w1:
            return helper(res, w1.replace(w2[0], ''), w2[1:])
        else:
            return helper(res+w2[0], w1, w2[1:])
    return helper('', w1, w2)


