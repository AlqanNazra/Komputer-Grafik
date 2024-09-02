#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ROWS 64  // Jumlah baris dalam grid
#define COLS 246  // Jumlah kolom dalam grid

// Grid untuk menampilkan garis
int grid[ROWS][COLS];

// Mengisi grid dengan nilai 0
void clearGrid() {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            grid[i][j] = 0;
        }
    }
}

// Menampilkan grid ke layar
void displayGrid() {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d", grid[i][j]);
        }
        //printf("\n");
    }
}

// Memasukkan garis ke grid menggunakan algoritma Bresenham
void bresenhamLine(int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = x1 < x2 ? 1 : -1;
    int sy = y1 < y2 ? 1 : -1;
    int err = dx - dy;

    while (1) {
        if (x1 >= 0 && x1 < COLS && y1 >= 0 && y1 < ROWS) {
            grid[y1][x1] = 1;
        }
        if (x1 == x2 && y1 == y2) break;
        int e2 = err * 2;
        if (e2 > -dy) { err -= dy; x1 += sx; }
        if (e2 < dx) { err += dx; y1 += sy; }
    }
}

// Memasukkan garis ke grid menggunakan algoritma DDA
void ddaLine(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    float xIncrement = dx / (float) steps;
    float yIncrement = dy / (float) steps;

    float x = x1, y = y1;
    if (x >= 0 && x < COLS && y >= 0 && y < ROWS) {
        grid[(int)(y + 0.5)][(int)(x + 0.5)] = 1;
    }

    for (int i = 0; i < steps; i++) {
        x += xIncrement;
        y += yIncrement;
        if (x >= 0 && x < COLS && y >= 0 && y < ROWS) {
            grid[(int)(y + 0.5)][(int)(x + 0.5)] = 1;
        }
    }
}

int main() {
    int x1, y1, x2, y2;
    int choice;

    // Memilih algoritma yang akan digunakan
    printf("Pilih algoritma untuk menggambar garis:\n");
    printf("1. Bresenham\n");
    printf("2. DDA\n");
    printf("Masukkan pilihan Anda: ");
    scanf("%d", &choice);

    // Memasukkan koordinat titik awal dan akhir
    printf("Masukkan koordinat titik awal (x1 y1): ");
    scanf("%d %d", &x1, &y1);
    printf("Masukkan koordinat titik akhir (x2 y2): ");
    scanf("%d %d", &x2, &y2);

    clearGrid();  // Bersihkan grid

    // Memilih algoritma yang sesuai
    if (choice == 1) {
        bresenhamLine(x1, y1, x2, y2);
    } else if (choice == 2) {
        ddaLine(x1, y1, x2, y2);
    } else {
        printf("Pilihan tidak valid.\n");
        return 1;
    }

    // Menampilkan grid dengan garis yang digambar
    printf("\nGrid hasil:\n");
    displayGrid();
    system("pause");
    return 0;
}