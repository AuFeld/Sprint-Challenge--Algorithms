#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) | The while loop runs as long as ```a``` is smaller than ```n^3```. As 
```a``` increases with ```n^2``` w/ each loop, the runtime is ```n^3``` divided 
by ```n^2```, eg in ```n``` times. 


b) O(n log n) | The outer loop runs ```n``` times. For each run of the outer 
loop, the inner while loops runs ```log n``` times (base 2, as ```j``` is 
doubled in each run of the inner loop). Multiplying run times, this code will 
run ```n long n``` times.


c) O(n) | This function calls itself ```n``` (bunnies) times. We can disregard 
the constants.

## Exercise II

I would recommend a BST like algo with a run time of ```O(log n)```. Pseudocode 
would look similar to:

```python
def egg_floor(low, high):
    if low < high:
        floor = (low + high) // 2
        if 'egg breaks':
            return egg_floor(low, floor-1)
        elif: 
            return egg_floor(floor+1, high)
        else: 
            return floor
```
