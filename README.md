# Happy Cow Puzzle

## Introduction
The puzzle for this semester is "Happy Cows Farm", a piece placement game. The objective of the game is to place in a field in a way that maximizes a score. Multiple algorithms are used to achieve the maximum score.

### The Farm
The farm is a square grid board where every cell location is either grass,  a haystack, or a water pond. Help Clayton the happy farmer place his cows 🐮 in the field while observing the following rules and preferences:
1. There are as many cows as haystacks.
2. Cows can only be placed in grass cells.
3. Cows prefer to be adjacent to a haystack either horizontally or vertically.
4. Cows are most happy if they are adjacent ( horizontally or vertically ) to both a haystack and a water pond.
5. Cows dislike being next to another cow, horizontally, vertically and even diagonally.

### The Scoring
Every cow placement has a corresponding score, which is the sum of the scores assigned to each cow. A cow's score is the sum of the following applicable rules :
<p>+1 : If a cow is horizontally or vertically adjacent to a haystack.</p>
<p>+2 : If a cow is horizontally or vertically adjacent to both a haystack and a water pond.</p>
<p>-3 : If a cow is next to another cow ( horizontally, vertically or diagonally )</p>
Note hat a cow surrounded by grass cells has a score of 0.

## Technologies Used

- **Programming Language**: Python3
- **Libraries/Frameworks**: 
  - AI Algorithms: [Best First Search, Breadth First Search, Iterative Deepening Depth First Search]

## Running the Project

1. Clone the repository:
   ```bash
   https://github.com/Prithviraj03/Happy_Cow_Farm.git
   cd Happy_Cow_Farm
   ```

2. Run the Program:
   ```bash
   # Make the script executable (if not already)
   chmod +x run.sh

   # Run the script
   ./run.sh
   ```