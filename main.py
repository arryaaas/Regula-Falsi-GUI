"""
    Nama                : Mochammad Arya Salsabila 
    NPM                 : 19081010001 
    Kelas               : Metode Numerik (D) 
    Tanggal Pembuatan   : 28 Oktober 2020 
    Judul Program       : "Metode Regula Falsi"
                                                                                            """
#==============================================================================================
                                    # Import Library

from tkinter import *
from tkinter import messagebox
#==============================================================================================
                                    # Layout GUI

root = Tk()
root.title("Mochammad Arya Salsabila / 19081010001")
root.geometry("600x550")

f1 = Frame(root, width=600, height=50)
f1.pack(side=TOP, pady=(16, 0))

f2 = Frame(root, width=600, height=100)
f2.pack(side=TOP, pady=(16, 0))

f3 = Frame(root, width=600, height=50)
f3.pack(side=TOP, pady=(16, 0))

f4 = Frame(root, width=600, height=350)
f4.pack(side=TOP, pady=(16, 0))
#==============================================================================================
                                    # Deklarasi Fungsi

def f(x, p):
    return (eval(p))

def cetak(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            entry = Entry(f4, width=10, justify="center")
            entry.grid(row=i, column=j)
            entry.insert(0, data[i][j])

def kesimpulan(n, e, x):
    messagebox.showinfo(
        title="Kesimpulan",
        message="Karena pada iterasi ke-{} nilai ERROR lebih kecil dari {} \n".format(n, e)
                + "Maka iterasi dihentikan dan diperoleh solusi persamaan non linier "
                + "yang diinginkan yaitu APROKSIMASI AKAR = {:.6f}".format(x)
        )

def syarat():
    persamaan = str(ent_persamaan.get())
    a = float(ent_batas_atas.get())
    b = float(ent_batas_bawah.get())

    if f(a, persamaan) * f(b, persamaan) < 0:
        btn_hitung["state"] = NORMAL
        btn_syarat["state"] = DISABLED
        messagebox.showinfo(
            title="Syarat Terpenuhi",
            message="F(a).F(b) < 0 \n"
                    + "Maka terdapat akar persamaan pada selang [{}, {}] \n".format(a, b)
                    + "Selanjutnya tekan button hitung..."
            )
    else:
        btn_hitung["state"] = DISABLED
        messagebox.showinfo(
            title="Syarat Tidak Terpenuhi",
            message="F(a).F(b) > 0 \n"
                    + "tidak terdapat akar persamaan pada selang [{}, {}] \n".format(a, b)
                    + "Silakan cari selang baru..."
            )

def hitung():
    btn_hitung["state"] = DISABLED
    btn_hapus["state"] = NORMAL

    persamaan = str(ent_persamaan.get())
    toleransi_error = float(ent_toleransi_error.get())
    a = float(ent_batas_atas.get())
    b = float(ent_batas_bawah.get())
    i = 1
    hasil = [["iterasi", "a", "c", "b", "F(a)", "F(c)", "F(b)", "error"]]

    while (True):
        fa = f(a, persamaan)
        fb = f(b, persamaan)

        c = b - (fb*(b - a) / (fb - fa))
        fc = f(c, persamaan)

        error = abs(fc)

        hasil.append([
            "{}".format(i), "{:.6f}".format(a), "{:.6f}".format(c),
            "{:.6f}".format(b), "{:.6f}".format(fa), "{:.6f}".format(fc),
            "{:.6f}".format(fb), "{:.6f}".format(error)
            ])

        if (error < toleransi_error):
            cetak(hasil)
            kesimpulan(i, toleransi_error, c)
            break

        if (fa*fc) < 0:
            b = c
        else:
            a = c

        i += 1

def hapus():
    btn_syarat["state"] = NORMAL
    btn_hapus["state"] = DISABLED

    ent_persamaan.delete(0, END)
    ent_toleransi_error.delete(0, END)
    ent_batas_atas.delete(0, END)
    ent_batas_bawah.delete(0, END)

    for widget in f4.winfo_children():
        widget.destroy()
#==============================================================================================
                                    # Pembuatan Widget Layout GUI

lbl_judul = Label(f1, font=("arial", "12", "bold"), text="Metode Regula Falsi")
lbl_judul.pack()

lbl_persamaan = Label(f2, text="Persamaan")
lbl_persamaan.grid(row=0, column=0, sticky="w")
ent_persamaan = Entry(f2, justify="right")
ent_persamaan.grid(row=0, column=1)

lbl_toleransi_error = Label(f2, text="Toleransi Error")
lbl_toleransi_error.grid(row=1, column=0, sticky="w")
ent_toleransi_error = Entry(f2, justify="right")
ent_toleransi_error.grid(row=1, column=1, pady=(4, 0))

lbl_batas_atas = Label(f2, text="Batas Atas")
lbl_batas_atas.grid(row=0, column=2, padx=(20,0), sticky="w")
ent_batas_atas = Entry(f2, justify="right")
ent_batas_atas.grid(row=0, column=3)

lbl_batas_bawah = Label(f2, text="Batas Bawah")
lbl_batas_bawah.grid(row=1, column=2, padx=(20,0), sticky="w")
ent_batas_bawah = Entry(f2, justify="right")
ent_batas_bawah.grid(row=1, column=3, pady=(4, 0))

btn_syarat = Button(f3, text="Syarat", width=16, command=syarat)
btn_syarat.grid(row=0, column=1)

btn_hitung = Button(f3, text="Hitung", width=16, command=hitung, state=DISABLED)
btn_hitung.grid(row=0, column=2, padx=(8, 8))

btn_hapus = Button(f3, text="Hapus", width=16, command=hapus, state=DISABLED)
btn_hapus.grid(row=0, column= 3)
#==============================================================================================
                                    # Mainloop Window Tkinter

root.mainloop()