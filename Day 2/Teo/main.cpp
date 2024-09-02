#include <windows.h>
#include <iostream>
using namespace std;

int main() {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    int columns;
    int bawah;
    // Mendapatkan informasi tentang ukuran terminal
    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
    columns = csbi.srWindow.Right - csbi.srWindow.Left + 1; // ini merupakan fungsi dari windows.h dengan struct console screen dimana code ini memiliki fungsi untuk mengentahui banyak cher pada monitor
        bawah = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
    int current_position = 0;
    int n = 0;

    cout << "screen bawah = " << csbi.srWindow.Bottom << endl;
    cout << "screen atas = " << csbi.srWindow.Top << endl;
    cout << "screen kiri = " << csbi.srWindow.Left <<endl;
    cout << "screen kanan = " << csbi.srWindow.Right <<endl;
    while (current_position <= columns) {
        n = n + 1;
        cout << " " << n;
        fflush(stdout);
        current_position++;

    printf("\nLoop berhenti karena mencapai ujung kanan monitor.\n");
    }
        while (current_position <= bawah) {
        n = n + 1;
        cout << " " << n << endl;
                // printf("*\n");

        fflush(stdout);
        current_position++;

    }
    printf("\nLoop berhenti karena mencapai ujung bawah monitor.\n");
    //  CONSOLE_SCREEN_BUFFER_INFO csbi;
    // int columns;
    // int rows;
    // // Mendapatkan informasi tentang ukuran terminal
    // GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
    // columns = csbi.srWindow.Right - csbi.srWindow.Left + 1;

    // std::cout << "Lebar terminal: " << columns << " karakter" << std::endl;
    //     rows = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;

    // std::cout << "Tinggi terminal: " << rows << " baris" << std::endl;
    return 0;
}


/*pada programa ini merupakan berfungsi untuk mencari lebar dan panjang dari suatu layar cara kerja program ini dengan memanfaatkan
CONSOLE_SCREEN_BUFFER_INFO dimana stturktur ini digunakan untuk mendapatkan informasi dari layar konsol lalu informasi ini disimpan
mengambil informasi buffer layar dengan outptu C++ menggunakan STD lalu mentimpannya pada csbi yang dimaan 
csbi ini menjadi data yang tersambung pada data komposit mengenai informasi layar lalu kita melakukan assignment
csbi.srWindow. assigment ini memiliki arti csbi -> srWindow yang berarti csbi menunjuk informasi yang dimiliki 
srWindow (screen window) lalu dipanggil sisi kiri dan kanan bawah dan atas seperti ini
columns = csbi.srWindow.Right - csbi.srWindow.Left + 1;
bawah = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
dimana colums menghitung lebar dan bawah menghitung tinggi dengan contoh opersai seperti ini 
Jika Right = 119 dan Left = 0, maka columns = 119 - 0 + 1 = 120. Artinya, jendela konsol memiliki lebar 120 karakter.
proses ini juga dilakukan sama untuk proses mencari tinggi lalu nilai 2 ini akan dilooping untuk mendapatkan jumlah 
karater yang dibutuhkan  */