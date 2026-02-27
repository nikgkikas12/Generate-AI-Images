# Generate-AI-Images
# PolyGenix

**AI Idea Generation Engine for 3D Printable Designs**

PolyGenix is a desktop application that generates **creative 3D printable design ideas** and automatically creates **AI-generated concept images** for each idea.

Built with **Python + Tkinter + OpenAI API**, PolyGenix helps makers, designers, and hobbyists quickly discover new 3D printing concepts.

---

## ✨ Features

* 🧠 AI-generated 3D printing ideas
* 🎨 Automatic concept image generation
* 🖼 Image preview inside the app
* ⬅️➡️ Keyboard navigation between images
* 📂 Automatic image saving
* 🌙 Dark theme interface
* ⚡ Fast generation

---

## 🖥 Screenshot

*(Add a screenshot here)*

Example:

```
screenshots/app.png
```

---

## 🚀 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourname/polygenix.git

cd polygenix
```

---

### 2️⃣ Install dependencies

```
pip install openai
pip install pillow
pip install ttkthemes
pip install requests
```

Or:

```
pip install -r requirements.txt
```

---

### 3️⃣ Add your OpenAI API key

Open the main file and replace:

```
client = openai.OpenAI(api_key='')
```

With:

```
client = openai.OpenAI(api_key='YOUR_API_KEY')
```

---

## ▶️ Running PolyGenix

```
python main.py
```

---

## 🎮 How To Use

1. Enter a topic

Example:

```
dragon lamp
```

2. Select generation mode

**Short**

* Fast
* Fewer ideas

**Extended**

* More ideas
* More images

3. Press **Enter**

PolyGenix will:

* Generate ideas
* Generate images
* Display previews

---

## ⌨ Controls

| Key         | Action         |
| ----------- | -------------- |
| Left Arrow  | Previous Image |
| Right Arrow | Next Image     |

---

## 📁 Output Folder

Generated images are saved in:

```
/outputs
```

Example:

```
outputs/request_1.jpg
outputs/request_2.jpg
outputs/request_3.jpg
```

---

## 🧠 How It Works

### Step 1 — Idea Generation

PolyGenix uses AI to generate creative 3D design ideas.

Example:

* Mechanical dragon phone stand
* Geometric desk organizer
* Modular plant holder

---

### Step 2 — Image Generation

Each idea is converted into an AI-generated concept image.

This helps visualize the design before modeling.

---

## 🛠 Built With

* Python
* Tkinter
* OpenAI API
* Pillow
* ttkThemes

---

## 🔧 Requirements

* Python 3.10+
* Internet connection
* OpenAI API key

---

## 📜 requirements.txt

```
openai
pillow
ttkthemes
requests
```

---

## ⚠ Notes

* First generation may take 10–20 seconds
* Images require internet connection
* API usage costs money

---

## 💡 Example Ideas

Input:

```
space theme desk accessories
```

Output:

* Rocket pen holder
* Planet lamp
* Satellite phone stand

---

## 🔒 API Key Safety

Never upload your API key publicly.

## 🧪 Future Features

Planned:

* STL export support
* Prompt templates
* Style selection
* Idea history
* Faster generation
* 3D model suggestions
