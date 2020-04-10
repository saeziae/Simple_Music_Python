# Simple_Music_Python
Play music from notes

---
## usage
You have to install `pyaudio` (`pip install pyaudio`, you'll need a C compiler)

run `main.py` and you'll get music from it.

## Make your own tune:
### Now you can use `new_make.py` to generate a `music.txt`:
write like this in `in.txt`, then run `new_make.py`
```
3 3_ 5_ |6_ 1._ 1._ 6_	|5 5_ 6_ |5- |
3 3_ 5_ |6_ 1._ 1._ 6_	|5 5_ 6_ |5- |
5 5     |5  3_  5_      |6 6     |5- |
3 2_ 3_ |5  3_  2_      |1 1_ 2_ |1- |
```
- `_` half-beat,
- `.` ottava,
- `,` ottava bassa.
- `|`, TAB, SPACE and newlines make no difference.
---
Here is the low-level method:

`music.txt` format:
```
tone beats  
tone beats  
tone beats  
tone beats  
tone beats  
...
```

For example
```
C4 0.5
D4 0.5
E4 1
D4 0.75
C4 0.25
C4 1
```
significar:
```
         4 
1 = C   --- 
         4 
|              |
| 1 2 3 2. 1 1 |
| ---   ---=   |
```

