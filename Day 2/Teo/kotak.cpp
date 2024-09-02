#include <iostream>
#include <string>

int main() {
    int width = 20;  // Lebar kotak
    int height = 7;  // Tinggi kotak
    std::string text = "231511068";

    // Hitung posisi tengah untuk teks
    int textPosX = (width - text.length()) / 2;
    int textPosY = height / 2;

    // Loop untuk mencetak kotak
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (i == 0 || i == height - 1 || j == 0 || j == width - 1) {
                std::cout << "*";  // Tepi kotak
            } else if (i == textPosY && j >= textPosX && j < textPosX + text.length()) {
                std::cout << text[j - textPosX];  // Tulis "NIM" di tengah
            } else {
                std::cout << " ";  // Spasi di dalam kotak
            }
        }
        std::cout << std::endl;
    }
    std:: cout << "----------------------------------\n";
    std:: cout << "|                                |\n";
    std:: cout << "|           231511068            |\n";
    std:: cout << "|                                |\n";
    std:: cout << "----------------------------------\n";

    return 0;

    
}
