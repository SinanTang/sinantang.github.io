---
title: Lecture Series Notes - Design of Computer Programs with Peter Norvig
date: 01-11-2017 23:31:06
categories: 
- Lecture Series Notes - Design of Computer Programs with Peter Norvig
tags:
- design pattern
- python
---

I started a new online lecture **[Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212)** taught by **[Peter Norvig](http://norvig.com/)** on Udacity. The quality of this lecture series is exceptional - once again proving the importance of a great teacher! Highly recommend this course for people who are familar with Python and some basic knowledge in computer science. It's freely available on Udacity.

I will be updating my notes for these lectures. 

FYI: They are not meant to be self-containing. 

.

#### Lesson 1 - playing poker

- ##### Map ordinal of characters into some integers:

My attempt:

```python
def card_ranks(hand):
	d = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    ranks = [d[r] for r,s in hand]
    ranks.sort(reverse=True)
    return ranks
```

Peter's solution - simpler:

```python
def card_ranks(hand):
	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks
```



- ##### Descending/ascending order & same element tests

My attempt:

```python
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    for i in range(1, len(ranks)):
        if ranks[i] != ranks[i-1]-1: return False
    return True

def flush(hand):
    "Return True if all the cards have the same suit."
    for i in range(1, len(hand)):
        if hand[i][1] != hand[0][1]: return False
    return True
```

Peter's solution - using `set`:

```python
def straight(ranks):
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
  
def flush(hand):
  	suits = [s for r, s in hand]
    return len(set(suits)) == 1
```



- ##### Find n consecutive elements with the same value in a list:

My attempt:

```python
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    i, kinds = 0, []
    while i < len(ranks):
        length = 1
        while (i+1) < len(ranks) and ranks[i+1] == ranks[i]:
            i, length = i + 1, length + 1
        kinds.append((length, ranks[i]))
        i += 1
    for l, s in kinds:
        if l == n: return s
    return None
```

Peter's solution - using list method `.count()`, much simpler:

```python
def kind(n, ranks):
	for r in ranks:
      	if ranks.count(r) == n: return r
    return None
```



- ##### Find 2 pairs of elements with same rank in a list:

My attempt: 

```python
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    res = []
    for r in ranks:
        if ranks.count(r) == 2 and (r not in res): res.append(r)
    if len(res) == 2: return tuple(sorted(res, reverse=True))
    return None
```

Peter's solution - :

```Python
def two_pair(ranks):
	pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
      	return (pair, lowpair)
    else:
      	return None
```



- ##### Making changes to our program - counting [A,2,3,4,5] as straight too

  - the number of places to change in the code should correspond to changes in the conceptualisation of the program

Peter's version:

```python
def card_ranks(hand):
  	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks = [14, 5, 4, 3, 2]) else ranks
```



- ##### Handling ties - return all maximum values from a list

My attempt - gives `None` in Python2.7, `TypeError` in Python3.6:

```python
def poker(hands):
	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
  	res = []
    for i in iterable:
      if hand_rank(i) == max(iterable, key):
      	res.append(i)
    return res
```

Peter's version:

```python
def allmax(iterable, key=None):
	result, maxval = [], None
    key = key or (lambda x: x)
    # not very clear about what's the difference bewteen key=key & key=lambda x:x
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result
```



- ##### Write `deal()` function

My attempt:

```python
import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    """ return hands in a list
    """
    hands = []
    random.shuffle(deck)
    for i in range(numhands):
        hand = random.sample(deck, k=n)
        update_deck(deck, hand)
        hands.append(hand)
    return hands

def update_deck(deck, hand):
    """remove cards in hand from deck
    """
    for i in hand:
        deck.remove(i)
```

Peter's solution - much shorter...

```Python
def deal(numhands, n=5, deck=mydeck):
    """return hands in a list
    """
	random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    # slicing the deck of cards with step of n
    # no need to random sample the deck as it's already shuffled
```



- ##### Hand frequencies

```python
def hand_percentages(n=700*1000):
	"""
	sample n random hands and print a table of percentages for each type of hand.
	"""
	counts = [0]*9
    for i in range(n/10):
      for hand in deal(10):
        ranking = hand_rank(hand)[0]
        counts[ranking] += 1
    for i in reversed(range(9)):
      print('{}: {:.3f} %'.format(hand_names[i], 100.*counts[i]/n))
```



- ##### Dimensions of programming

**Efficiencies, Correctness, Features, Elegance** (buying time for the future)

> "The best is the enemy of the good."



- ##### Refactoring (more elegant)

e.g. 

```python
...
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
...
```

> principal DRY: Dont't Repeat Yourself.

a way to refactor -> group(7, 10, 9, 7, 7) ->> (3, 1, 1), (7, 10, 9)

Implement this refactoring (very enlightening!):

```python
def hand_rank(hand):
	"""return a value indicating how high the hand ranks.
	counts: the count of each rank;
	ranks: lists corresponding ranks.
	e.g. '7 T 7 9 7' => counts = (3,1,1); ranks = (7,10,9)
	"""
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else
            8 if straight and flush else
            7 if (4, 1) == counts else
            6 if (3, 2) == counts else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) == counts else
            2 if (2, 2, 1) == counts else
            1 if (2, 1, 1, 1) == counts else
            0), ranks

def group(items):
    """return a list of [(count, x)...], highest count first, then highest x first
    """
	groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)
```

Another possibility - even more concise but less explicit:

```python
def hand_rank(hand):
	groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5,4,3,2,1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks

count_rankings = {(5,):10, (4,7):7, (3,2):6, (3,1,1):3, (2,2,1):2, (2,1,1,1):1, (1,1,1,1,1):0}
```

I prefer the first explicit version.

- ##### Lessons Learned

1. **Understand** the problem
2. **Define** pieces of the problem
3. **Reuse** pieces of code already existing
4. **Test** along the way
5. **Explore** the design space (4 dimensions)