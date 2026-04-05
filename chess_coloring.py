#chessboard color problem

def determine_color(s):
    """
    Determines the color of a chess square based on its position.
    Parameters:
        s (str): Input string representing a position (e.g., "a1", "h8").
    Returns:
        str: "Black" or "White" based on the problem statement.
    """
    # Map column character to 0-indexed integer (a->0, b->1, ..., h->7)
    col_char = s[0].lower()
    if not ('a' <= col_char <= 'h'):
        raise ValueError("Invalid column character. Must be 'a' through 'h'.")
    col_index = ord(col_char) - ord('a')

    # Map row character to 0-indexed integer (1->0, 2->1, ..., 8->7)
    row_char = s[1]
    if not ('1' <= row_char <= '8'):
        raise ValueError("Invalid row number. Must be '1' through '8'.")
    row_index = int(row_char) - 1

    # Chessboard coloring: (row + col) sum even -> Black, odd -> White (assuming a1 is black)
    # A1 is (0,0), sum is 0 (even), which is typically Black.
    if (row_index + col_index) % 2 == 0:
        return "Black"
    else:
        return "White"

def main():
    import sys
    # sys.stdin.read() will read all input until EOF. For testing in Colab,
    # you might need to manually provide input or modify to use `input()` for interactive prompts.
    s = input("Enter the position: ")# Read the input string

    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()