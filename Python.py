from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import openai
import requests
import os
import base64

client = openai.OpenAI(api_key = 'PUT_YOUR_OPENAI_KEY')
OUTPUT_DIR = "outputs"

#===========CCOMANDS===========
window = ThemedTk(theme="equilux")
window.configure(themebg="equilux")
window.geometry("500x800")
window.title("PolyGenix")
window.resizable(False, False)
image_paths = []
cIndex = 0

def generate_ideas(user_text, n):
    prompt = f"Generate {n} my creative 3D about: {user_text}\n" \
             f"Return ONLY {n}"

    resp=client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.9)

    ideas=[]
    for line in resp.choices[0].message.content.splitlines():
        print(line)
        line=line.strip()
        if line!="":
            ideas.append(line)
    return ideas[:n]

def process(event=None):
    global image_paths

    user = text_widget.get()                 # simple: get text from Entry
    if rb.get() == "Choice15":         # simple if
        n = 3
    else:
        n = 2

    ideas = generate_ideas(user, n)
    image_paths = generate_images_from_ideas2(ideas)

    cIndex = 0
    showImage(0)

def generate_images_from_ideas(ideas):
    paths = []
    for i in range(len(ideas)):
        idea = ideas[i]
        img = client.images.generate(
            model='dall-e-3',
            prompt=idea,
            size='1024x1024',
            n=1
        )
        url = img.data[0].url
        print(url)


def generate_images_from_ideas2(ideas):
    paths = []
    for i in range(len(ideas)):
        idea = ideas[i]

        img = client.images.generate(
            model="gpt-image-1.5",
            prompt=ideas[i],
            size="1024x1024",
            n=1,
            output_format="jpeg"
        )

        filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")

        b64 = img.data[0].b64_json
        print(b64)

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(b64))

        paths.append(filepath)

    return paths

def showImage(ind):
    global imagePreview

    img = Image.open(image_paths[ind])
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    imagePreview = ImageTk.PhotoImage(img)
    image_label.configure(image=imagePreview)

def nextImg(event=None):
    global cIndex

    cIndex = (cIndex + 1) % len(image_paths)
    showImage(cIndex)


def prevImg(event=None):
    global cIndex
    if not image_paths:
        return

    cIndex = (cIndex - 1) % len(image_paths)
    showImage(cIndex)


def preview_first():
    # Opens the first downloaded image in Windows (default image viewer / explorer behavior)
    if image_paths:
        os.startfile(image_paths[0])


window.bind("<Left>", prevImg)
window.bind("<Right>", nextImg)

#===========UI===========
title = ttk.Label(window, text="PolyGenix", font=("Agency FB Bold", 35))
title.place(x=180, y=30)

subTitle = ttk.Label(
    window,
    text="Idea Generation Engine for 3D Printable Designs",
    font=("Agency FB", 15)
)
subTitle.place(x=110, y=89)

rb = StringVar(value="Choice5")

rad1 = ttk.Radiobutton(window, text="Short [5 variants]", value="Choice5", variable=rb)
rad1.place(x=110, y=135)

rad2 = ttk.Radiobutton(window, text="Extended [15 Variants]", value="Choice15", variable=rb)
rad2.place(x=260, y=135)

text_widget = ttk.Entry(window, width=35, font=("Segoe UI", 15))
text_widget.place(x=50, y=200)

enter_button = ttk.Button(window, text="Enter", command=process)
enter_button.place(x=310, y=290, height=40, width=140)

preview_button = ttk.Button(window, text="Preview")
preview_button.place(x=50, y=290, height=40, width=140)

image_label = ttk.Label(window)
image_label.place(x=50, y=330, width=400, height=400)

window.mainloop()
