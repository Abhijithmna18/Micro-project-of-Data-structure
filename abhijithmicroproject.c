#include <stdio.h>

#define SIZE 3

// Function to initialize the board
void initializeBoard(char board[SIZE][SIZE]) {
    int i, j;
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            board[i][j] = ' ';
        }
    }
}

// Function to print the board
void printBoard(char board[SIZE][SIZE]) {
    int i, j;
    printf("\n");
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            printf(" %c ", board[i][j]);
            if (j < SIZE - 1) printf("|");
        }
        printf("\n");
        if (i < SIZE - 1) {
            printf("---|---|---\n");
        }
    }
    printf("\n");
}

// Function to check if a player has won
int checkWinner(char board[SIZE][SIZE], char player) {
    int i;
    // Check rows and columns
    for (i = 0; i < SIZE; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) || // Row
            (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {  // Column
            return 1;
        }
    }

    // Check diagonals
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) || // Diagonal 1
        (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {  // Diagonal 2
        return 1;
    }

    return 0;
}

// Function to check if the board is full (i.e., a draw)
int isBoardFull(char board[SIZE][SIZE]) {
    int i, j;
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            if (board[i][j] == ' ') {
                return 0;  // Empty space found
            }
        }
    }
    return 1;  // Board is full
}

// Function to take a player's move
void playerMove(char board[SIZE][SIZE], char player) {
    int row, col;
    do {
        printf("Player %c, enter row and column (1-3) for your move: ", player);
        scanf("%d %d", &row, &col);
        row--;  // Adjust to 0-based index
        col--;  // Adjust to 0-based index
    } while (row < 0 || row >= SIZE || col < 0 || col >= SIZE || board[row][col] != ' ');

    board[row][col] = player;
}

int main() {
    char board[SIZE][SIZE];
    initializeBoard(board);

    char currentPlayer = 'X';  // X starts the game

    while (1) {
        printBoard(board);
        playerMove(board, currentPlayer);

        // Check if the current player has won
        if (checkWinner(board, currentPlayer)) {
            printBoard(board);
            printf("Player %c wins!\n", currentPlayer);
            break;
        }

        // Check if the board is full (draw)
        if (isBoardFull(board)) {
            printBoard(board);
            printf("It's a draw!\n");
            break;
        }

        // Switch players
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}

