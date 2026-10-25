```python
from collections import Counter

def second_most_common(s):
    filtered_s = [c for c in s if c != ' ']
    
    if len(set(filtered_s)) < 2:
        return None
        
    counts = Counter(filtered_s)
    
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], filtered_s.index(x[0])))
    
    return sorted_chars[1][0]
```