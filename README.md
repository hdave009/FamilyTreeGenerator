# FamilyTreeGenerator
This is a simple Python script that takes in celebrities name, and a `MAX_GENERATIONS` positive integer.

The purpose of this script is to scrape the web using the Selenium web driver for Python, and recursively build a family tree for the given celebrity.
Since this is a recursive algorithm for generating a tree, it has an exponential time complexity. The `MAX_GENERATIONS` variable is used to prevent overflow.

There are some sample trees that provided in the repository. 
