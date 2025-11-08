class Node:
    def __init__(self, sku, nama, harga, jumlah):
        self.sku = sku
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, sku, nama, harga, jumlah):
        if self.root is None:
            self.root = Node(sku, nama, harga, jumlah)
            print("Barang berhasil ditambahkan ke stok.")
        else:
            self._insert(self.root, sku, nama, harga, jumlah)

    def _insert(self, current, sku, nama, harga, jumlah):
        if sku == current.sku:
            print("Gagal: SKU sudah terdaftar di stok.")
        elif sku < current.sku:
            if current.left:
                self._insert(current.left, sku, nama, harga, jumlah)
            else:
                current.left = Node(sku, nama, harga, jumlah)
                print("Barang berhasil ditambahkan ke stok.")
        else:
            if current.right:
                self._insert(current.right, sku, nama, harga, jumlah)
            else:
                current.right = Node(sku, nama, harga, jumlah)
                print("Barang berhasil ditambahkan ke stok.")

    def search(self, sku):
        return self._search(self.root, sku)

    def _search(self, current, sku):
        if current is None:
            return None
        if sku == current.sku:
            return current
        elif sku < current.sku:
            return self._search(current.left, sku)
        else:
            return self._search(current.right, sku)

def input_data_stok(BST):
    try:
        sku = int(input("Masukkan No. SKU (4 digit): "))
        if sku < 1000 or sku > 9999:
            print("No. SKU harus terdiri dari 4 digit angka.")
            return
        if BST.search(sku):
            print("SKU sudah ada. Gunakan menu restok untuk menambah stok barang.")
            return
        nama = input("Masukkan Nama Barang: ")
        harga = float(input("Masukkan Harga Satuan: "))
        jumlah = int(input("Masukkan Jumlah Stok: "))
        if harga < 0 or jumlah < 0:
            print("Harga dan jumlah stok tidak boleh negatif.")
            return
        BST.insert(sku, nama, harga, jumlah)
    except ValueError:
        print("Input tidak valid. Pastikan angka dimasukkan dengan benar.")

def restok_barang(BST):
    try:
        sku = int(input("Masukkan No. SKU untuk restok: "))
        if sku < 1000 or sku > 9999:
            print("No. SKU harus terdiri dari 4 digit angka.")
            return
        node = BST.search(sku)
        if node:
            print(f"Barang ditemukan: {node.nama}")
            print(f"Jumlah stok saat ini: {node.jumlah}")
            stok_baru = int(input("Masukkan jumlah stok baru yang akan ditambahkan: "))
            if stok_baru < 0:
                print("Jumlah stok tidak boleh negatif.")
                return
            node.jumlah += stok_baru
            print(f"Restok berhasil. Jumlah stok sekarang: {node.jumlah}")
        else:
            print("No. SKU tidak ditemukan. Silakan input data stok barang terlebih dahulu.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

def input_transaksi_baru(BST, daftar_transaksi):
    nama_konsumen = input("Masukkan Nama Konsumen: ")
    while True:
        try:
            sku = int(input("Masukkan No. SKU barang yang dibeli: "))
            if len(str(sku)) != 4:
                print("No. SKU harus 4 digit.")
                continue
            barang = BST.search(sku)
            if not barang:
                print("No. SKU yang diinputkan belum terdaftar")
                lanjut = input("Apakah ingin melanjutkan transaksi? (Ya atau Tidak): ").strip().lower()
                if lanjut != "ya":
                    break
                continue
            print(f"Barang ditemukan: {barang.nama} - Harga: {barang.harga} - Stok: {barang.jumlah}")
            jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
            if jumlah <= 0:
                print("Jumlah beli harus lebih dari 0.")
                continue
            if barang.jumlah >= jumlah:
                barang.jumlah -= jumlah
                subtotal = barang.harga * jumlah
                transaksi = {
                    "nama": nama_konsumen,
                    "sku": sku,
                    "jumlah": jumlah,
                    "subtotal": subtotal
                }
                daftar_transaksi.append(transaksi)
                print("Data Transaksi Konsumen Berhasil Diinputkan")
                tambah = input("Apakah ingin menambahkan data pembelian untuk konsumen ini? (Ya atau Tidak): ").strip().lower()
                if tambah != "ya":
                    break
            else:
                print("Jumlah Stok No.SKU yang Anda beli tidak mencukupi")
                lanjut = input("Apakah ingin melanjutkan transaksi? (Ya atau Tidak): ").strip().lower()
                if lanjut == "tidak":
                    break
        except ValueError:
            print("Input tidak valid. Pastikan angka dimasukkan dengan benar.")

def tampilkan_seluruh_transaksi(daftar_transaksi):
    if not daftar_transaksi:
        print("Belum ada data transaksi yang tersimpan.")
    else:
        print("\nData Seluruh Transaksi Konsumen:")
        i = 1
        for transaksi in daftar_transaksi:
            print(f"{i}. Nama Konsumen : {transaksi['nama']}")
            print(f"   No. SKU      : {transaksi['sku']}")
            print(f"   Jumlah Beli  : {transaksi['jumlah']}")
            print(f"   Subtotal     : Rp{transaksi['subtotal']:,.2f}".replace(",", ".").replace(".", ",", 1))
            print("-" * 40)
            i += 1

def insertion_sort_transaksi_desc(transaksi_list):
    for i in range(1, len(transaksi_list)):
        key = transaksi_list[i]
        j = i - 1
        while j >= 0 and transaksi_list[j]['subtotal'] < key['subtotal']:
            transaksi_list[j + 1] = transaksi_list[j]
            j -= 1
        transaksi_list[j + 1] = key

def tampilkan_transaksi_urut_subtotal(daftar_transaksi):
    if not daftar_transaksi:
        print("Belum ada data transaksi yang tersimpan.")
        return
    insertion_sort_transaksi_desc(daftar_transaksi)
    print("\nData Transaksi Konsumen (Urut Subtotal Descending):")
    i = 1
    for transaksi in daftar_transaksi:
        print(f"{i}. Nama Konsumen : {transaksi['nama']}")
        print(f"   No. SKU      : {transaksi['sku']}")
        print(f"   Jumlah Beli  : {transaksi['jumlah']}")
        print(f"   Subtotal     : Rp{transaksi['subtotal']:,.2f}".replace(",", ".").replace(".", ",", 1))
        print("-" * 40)
        i += 1

if __name__ == "__main__":
    BST = BinarySearchTree()
    daftar_transaksi = []
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Kelola Stok Barang")
        print("2. Kelola Transaksi Konsumen")
        print("0. Exit Program")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            while True:
                print("\n--- Kelola Stok Barang ---")
                print("1. Input Data Stok Barang")
                print("2. Restok Barang")
                print("0. Kembali ke Menu Utama")
                sub_pilih = input("Pilih menu: ")
                if sub_pilih == "1":
                    input_data_stok(BST)
                elif sub_pilih == "2":
                    restok_barang(BST)
                elif sub_pilih == "0":
                    break
                else:
                    print("Pilihan tidak valid.")
        elif pilih == "2":
            while True:
                print("\n--- Kelola Transaksi Konsumen ---")
                print("1. Input Data Transaksi Baru")
                print("2. Lihat Data Seluruh Transaksi Konsumen")
                print("3. Lihat Data Transaksi Berdasarkan Subtotal")
                print("0. Kembali ke Menu Utama")
                sub_pilih = input("Pilih menu: ")
                if sub_pilih == "1":
                    input_transaksi_baru(BST, daftar_transaksi)
                elif sub_pilih == "2":
                    tampilkan_seluruh_transaksi(daftar_transaksi)
                elif sub_pilih == "3":
                    tampilkan_transaksi_urut_subtotal(daftar_transaksi)
                elif sub_pilih == "0":
                    break
                else:
                    print("Pilihan tidak valid.")
        elif pilih == "0":
            print("Terima kasih telah menggunakan program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
