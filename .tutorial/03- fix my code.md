# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
try:  
f.open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

for row in myStuff:
  print(row)
```

<details> <summary> 👀 Answer </summary>

```python
myStuff = [] # Didn't create the list.

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# The 'open' lines weren't indented inside the 'try'

except Exception as err:
  print("ERROR: Unable to load")
  print(err)
# Missing 'except'

for row in myStuff:
  print(row)
```
</details>