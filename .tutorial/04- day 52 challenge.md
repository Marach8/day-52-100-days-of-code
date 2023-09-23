# 👉 Day 52 Challenge

There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.  

Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely do not visit on my way home from a night out.

That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard. Man that stuff *never* washes out.

Regardless, your program today must:

1. Prompt the user to input the quantity and size of pizzas.
2. Multiply the two inputs together to calculate the cost of the pizzas.
3. Store that in a 2D list with the user's name.
4. Use `try.... except` for **two** reasons:
    
    1. Include auto-save and auto-load. Use it with the auto-load.
    2. When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again.
   

Example:

```
🌟Dave's Dodgy Pizzas🌟

How many pizzas? > three
You must input a numerical character, try again. > 3

What size? > XXXXXX

Name please > David

Thanks David, your pizzas will cost XXXXX
```

<details> <summary> 💡 Hints </summary>
  
- Use subroutines for 'add' and 'view'
- Use a `while.... true` loop for the main menu
- Use a 2d list to store the details of each pizza.
- Use selection to decide which subroutine to run, then write the 2d list to the file.
- For add, get all the inputs in variables and append to a list. Append this list to a 2d one that stores all the pizza details.
- For view, get each index from one row of the 2d list at a time.





</details>