Kode yang diberikan mengimplementasikan pendekatan bruteforce untuk menyelesaikan masalah Knapsack 0/1. Berikut adalah penjelasan cara kerja kode tersebut:

1. Fungsi `knapsack_brute_force` menerima input berupa nilai-nilai (values), berat-berat (weights), dan kapasitas (capacity). Fungsi ini menginisialisasi `num_items` sebagai jumlah item, `max_value` dan `best_combination` sebagai variabel untuk melacak nilai maksimum dan kombinasi item dengan nilai maksimum.

2. Dalam loop pertama, dari 0 hingga 2^num_items, semua kemungkinan kombinasi item diperiksa menggunakan representasi bit (bitmasking). Misalnya, jika num_items = 4, iterasi akan berjalan dari 0 hingga 15 (2^4 - 1).

3. Di dalam loop pertama, variabel `combination`, `total_value`, dan `total_weight` diinisialisasi untuk setiap iterasi kombinasi yang sedang diperiksa.

4. Dalam loop kedua, dari 0 hingga num_items, setiap item diperiksa. Jika bit ke-j dalam representasi biner dari iterasi pertama adalah 1, maka item ke-j termasuk dalam kombinasi. Total nilai dan total berat diperbarui sesuai.

5. Setelah selesai memeriksa semua item, dicek apakah total berat kurang dari atau sama dengan kapasitas dan total nilai lebih besar dari `max_value`. Jika ya, maka `max_value` dan `best_combination` diperbarui dengan nilai dan kombinasi saat ini.

6. Setelah semua kombinasi diperiksa, `knapsack_brute_force` mengembalikan `max_value` dan `best_combination`.

7. Contoh penggunaan diberikan dengan mendefinisikan nilai-nilai, berat-berat, dan kapasitas. Waktu mulai direkam menggunakan `time.time()`.

8. Fungsi `knapsack_brute_force` dipanggil dengan nilai-nilai contoh, dan `max_value` dan `best_combination` diperoleh.

9. Waktu berakhir direkam menggunakan `time.time()`.

10. Waktu eksekusi dihitung dengan mengurangkan waktu mulai dari waktu berakhir.

11. Terakhir, kombinasi terbaik dari item, total nilai, dan waktu eksekusi dicetak.

Metode ini menggunakan pendekatan bruteforce, di mana semua kombinasi mungkin dari item-item diperiksa secara berurutan. Hal ini dapat bekerja untuk masalah dengan jumlah item yang kecil, namun kompleksitasnya adalah O(2^n) karena jumlah kombinasi yang diperiksa meningkat secara eksponensial dengan jumlah item.