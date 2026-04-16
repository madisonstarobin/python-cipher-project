# 🔐 Caesar Cipher Encoder (Shift‑15)

A Python implementation of a **Caesar cipher** that shifts alphabetic characters by **15 positions**. This project demonstrates ASCII manipulation, modular programming, and clean code structure. It was originally built as part of a capstone assignment and now lives in my developer portfolio.

---

## 🚀 Features

- Encodes messages using a **shift of 15**
- Supports:
  - ✔ Lowercase letters  
  - ✔ Uppercase letters  
  - ✔ Alphabet wrap‑around  
  - ✔ Spaces, punctuation, and numbers (unchanged)
- Uses ASCII values (`ord()` / `chr()`) instead of alphabet arrays
- Fully commented and beginner‑friendly
- Clean, modular function design

---

## 🧠 How It Works

The Caesar cipher shifts each alphabetic character forward by 15 positions.

Example:

```
a → p
b → q
c → r
```

Wrap‑around is handled automatically:

```
z → o
Z → O
```

Non‑alphabetic characters (spaces, punctuation, numbers) are preserved exactly as they are.

---

## 📌 Usage

Run the script:

```bash
python cipher.py
```

Enter a message when prompted:

```
Enter a message to encode: Hello World!
```

Output:

```
Encoded message: Wtaad Ldgvs!
```

---

## 📁 Project Structure

```
cipher/
│── cipher.py
└── README.md
```

(Optional additions you can include later)

```
examples/
└── sample_output.txt
```

---


---

## 🧑‍💻 Author

**Madison**  
Cybersecurity & Python Developer  
