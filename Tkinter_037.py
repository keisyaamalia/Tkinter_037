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