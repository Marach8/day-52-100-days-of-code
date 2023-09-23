# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Try, Try, Try Again

👉 What's the problem here?

```python
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

for row in myStuff:
  print(row)
```

<details> <summary> 👀 Answer </summary>

- No `except` to catch the error. `try` is not finished without an except.

```python
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

except:
  print(traceback)

for row in myStuff:
  print(row))
```

</details>


