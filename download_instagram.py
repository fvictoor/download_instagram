from tkinter import Tk, Canvas, PhotoImage, Button, Entry, filedialog, messagebox
import instaloader
import re
import os
import sys

def btn_clicked():
    try:
        url = [entry0.get()]
    except IndexError:
        messagebox.showerror(message="URL Inválido")
        sys.exit()
    save_path = filedialog.askdirectory(title="Salvar Arquivo")

    downloadDir = save_path
    os.chdir(downloadDir)

    loader = instaloader.Instaloader(
    download_pictures=True, 
    download_videos=True, 
    download_video_thumbnails=False, 
    download_geotags=False,
    download_comments=False, 
    save_metadata=False, 
    compress_json=False,
    filename_pattern='{profile}_{mediaid}')

    expr = r'\/p\/([^\/]*)/'
    found = re.search(expr, str(url))

    if found:
        post = instaloader.Post.from_shortcode(loader.context, found.group(1))
        loader.download_post(post, 'Downloader Instagam')
        messagebox.showinfo(message="Downloado realizado com sucesso!")

window = Tk()
window.geometry("1000x800")
window.title("Download Instagram")
window.configure(bg = "#FFFFFF")
canvas = Canvas(window, bg = "#FFFFFF", height = 800,  width = 1000,  bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

icon_img = (r"img\instagram.ico")
window.iconbitmap(False, icon_img)

background_img = PhotoImage(file = r"img\\background.png")
background = canvas.create_image( 500.0, 400.0, image=background_img)

entry0_img = PhotoImage(file = r"img\\img_textBox0.png")
entry0_bg = canvas.create_image( 673.5, 309.0, image = entry0_img)

entry0 = Entry(bd = 0, bg = "#dc97ff", highlightthickness = 0)
entry0.place(x = 412.0, y = 288, width = 525.0, height = 43)

img0 = PhotoImage(file = r"img\\img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place( x = 538, y = 396,width = 280, height = 58)

window.resizable(False, False)
window.mainloop()
