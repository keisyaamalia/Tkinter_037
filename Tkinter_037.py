import tkinter as tk
def hasil_prediksi():
    var_hasil.set("Teknologi Informasi")
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)

lebar, tinggi = 520, 520
x = (root.winfo_screenwidth() - lebar) // 2
y = (root.winfo_screenheight() - tinggi) // 2
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")

label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    fg="#1a4f8b",
)
label_judul.pack(pady=(20, 10))

frame_input = tk.LabelFrame(
    root, text=" Masukkan Nilai Mata Pelajaran ", font=("Arial", 11, "bold"),
    padx=20, pady=15,
)
frame_input.pack(padx=25, pady=10, fill="x")
mapel = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]

entries = []
for i, nama in enumerate(mapel):
    baris = i % 5          # 5 baris
    kolom = (i // 5) * 2   # 2 kolom (masing-masing label + entry)
    tk.Label(frame_input, text=nama + ":", anchor="w", width=16).grid(
        row=baris, column=kolom, sticky="w", padx=(0, 5), pady=6
    )
    e = tk.Entry(frame_input, width=8, bd=3, justify="center")
    e.grid(row=baris, column=kolom + 1, padx=(0, 25), pady=6)
    entries.append(e)

    tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Arial", 12, "bold"),
    bg="#1a4f8b",
    fg="white",
    padx=20,
    pady=5,
    command=hasil_prediksi,
)
tombol.pack(pady=15)

var_hasil = tk.StringVar()
var_hasil.set("-")

tk.Label(root, text="Prodi yang direkomendasikan:", font=("Arial", 11)).pack()
label_hasil = tk.Label(
    root,
    textvariable=var_hasil,
    font=("Arial", 16, "bold"),
    fg="#0b7a3b",
    relief=tk.RAISED,
    width=28,
    pady=8,
)
label_hasil.pack(pady=(5, 20))

root.mainloop()