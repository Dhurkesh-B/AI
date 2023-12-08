# Get the number of queens from user input
numQueen = int(input("Enter the number of Queens: "))
currentSolution = [0 for x in range(numQueen)]
solution = []

def isSafe(testrow, testcol):
    if testrow == 0:
        return True
    else:
        for row in range(testrow):
            if testcol == currentSolution[row]:
                return False
            if abs(currentSolution[row] - testcol) == abs(row - testrow):
                return False
        return True

def placeQueen(row):
    global currentSolution, solution, numQueen
    for col in range(numQueen):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col
            if row == numQueen - 1:
                solution.append(currentSolution.copy())
            else:
                placeQueen(row + 1)

placeQueen(0)

# Generate HTML representation with navigation buttons
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        table {{
            border-collapse: collapse;
            width: {numQueen * 50}px;  /* Adjusted width based on the number of queens */
            height: {numQueen * 50}px; /* Set height equal to width for a square chessboard */
            margin: 0 auto;  /* Center the chessboard */
        }}
        table, td, th {{
            border: 1px solid black;
        }}
        td {{
            height: 50px;
            width: 50px;
            text-align: center;
        }}
        #board-container {{
            text-align: center;
        }}
        #nav-buttons {{
            margin-top: 20px;
        }}
    </style>
    <script>
        var currentIndex = 0;

        // Function to show a specific board
        function showBoard(index) {{
            currentIndex = index;
            var boards = {solution};
            var board = boards[index];
            var tableHTML = "<table>";
            for (var row = 0; row < board.length; row++) {{
                tableHTML += "<tr>";
                for (var col = 0; col < board.length; col++) {{
                    if (col == board[row]) {{
                        tableHTML += "<td>&#9819;</td>";  // &#9819; is the Unicode character for chess queen
                    }} else {{
                        tableHTML += "<td></td>";
                    }}
                }}
                tableHTML += "</tr>";
            }}
            tableHTML += "</table>";
            document.getElementById("board-container").innerHTML = tableHTML;
        }}

        // Function to show the next board
        function showNext() {{
            currentIndex = (currentIndex + 1) % {len(solution)};
            showBoard(currentIndex);
        }}

        // Function to show the previous board
        function showPrevious() {{
            currentIndex = (currentIndex - 1 + {len(solution)}) % {len(solution)};
            showBoard(currentIndex);
        }}
    </script>
</head>
<body>
    <h2>N-Queens Solution</h2>
    <div id="board-container"></div>
    <div id="nav-buttons">
        <button onclick="showPrevious()">Previous</button>
        <button onclick="showNext()">Next</button>
    </div>
    <script>
        showBoard(currentIndex);
    </script>
</body>
</html>
"""

# Save HTML content to a file
with open("n_queens_solution.html", "w") as html_file:
    html_file.write(html_content)

print(f"HTML representation with {numQueen} queens saved to 'n_queens_solution.html'")
