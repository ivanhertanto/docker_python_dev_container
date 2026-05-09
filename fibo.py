def first_n_fib(n): # Mendefinisikan fungsi bernama first_n_fib yang menerima satu parameter n (jumlah elemen Fibonacci yang akan dibuat).
    a, b = 0, 1 # Menginisialisasi dua variabel: a = 0 (F(0)) dan b = 1 (F(1)). Ini pengaturan awal untuk menghasilkan deret Fibonacci.
    result = [] # Membuat list kosong bernama result untuk menampung nilai-nilai Fibonacci yang dihasilkan.
    for _ in range(n): # Memulai loop yang akan berjalan sebanyak n kali. Variabel loop diabaikan dengan menggunakan _ karena tidak diperlukan.
        result.append(b) # Menambahkan nilai b saat ini ke akhir list result. b adalah nilai Fibonacci berikutnya dalam deret.
        a, b = b, a + b # Memperbarui pasangan (a,b) untuk iterasi berikutnya: a menjadi nilai b sebelumnya, dan b menjadi jumlah a + b sebelumnya—ini menghasilkan nilai Fibonacci selanjutnya.
    return result # Mengembalikan list result yang sudah berisi n nilai Fibonacci.

if __name__ == "__main__": # Memeriksa apakah skrip dijalankan langsung (bukan diimpor sebagai modul). Jika ya, blok berikut dijalankan.
    try:
        n = int(input("Masukkan jumlah bilangan Fibonacci yang diinginkan: "))
        if n <= 0:
            raise ValueError
    except ValueError: # Memulai blok untuk menangani kemungkinan kesalahan saat membaca dan mengonversi input pengguna.
        print("Masukkan bilangan bulat positif.")
    else: # Blok else dijalankan jika tidak ada pengecualian pada blok try (input valid dan n positif).
        seq = first_n_fib(n) # Memanggil fungsi first_n_fib dengan nilai n yang valid dan menyimpan hasil (list Fibonacci) ke variabel seq.
        print(", ".join(str(x) for x in seq)) # Mengonversi tiap angka di seq menjadi string, menggabungkannya dengan pemisah , , lalu mencetak barisan bilangan Fibonacci sebagai satu baris teks (mis. 1, 1, 2, 3, 5).