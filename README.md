# knapsack

Items of different sizes (or weights or price, or …) and values are put in a container of finite space in a way that optimizes value.


Cases for recursion rule
Item won't fit in bag at all.  Skip it.
Adding the item makes things worse.  Don't use it.
Adding the item to the solution for bag small enough to fit in the current bag along with the item makes things better. Use the item along with the solution for the smaller bag.

See this presentation:
https://docs.google.com/presentation/d/1R76yGluDifun1Ggsx-QsKf1I3Abbjaith5Il4jvISiU/edit?usp=sharing
