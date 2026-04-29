# 🧑 Name Validator Guidelines

## 🎯 Purpose
Define rules for validating human names while balancing correctness, flexibility, and inclusivity.

---

## ✅ DO’s (What to Validate)

### 1. Basic Structure
- Allow:
  - Alphabets (a-z, A-Z)
  - Spaces
  - Common separators: `'` (apostrophe), `-` (hyphen)
- Examples:
  - `Anuj Sharma`
  - `Jean-Luc Picard`
  - `O'Connor`

---

### 2. Length Constraints
- Minimum: **2 characters**
- Maximum: **50–100 characters** (depending on system)

---

### 3. Trim Input
- Remove leading/trailing spaces
- Convert multiple spaces into single space

---

### 4. Capitalization (Optional)
- Normalize:
  - `anuj sharma` → `Anuj Sharma`
- Store clean format, not raw messy input

---

### 5. Unicode Support (Important)
- Allow international characters:
  - `José`, `Renée`, `李雷`, `अभिषेक`
- Use Unicode-friendly validation

---

## ❌ DON'Ts (Common Mistakes to Avoid)

### 1. Restricting Only A-Z
- ❌ Rejecting valid names like:
  - `Élise`
  - `Łukasz`
  - `नरेश`

---

### 2. Blocking Valid Symbols
- ❌ Rejecting:
  - `O'Neill`
  - `Mary-Jane`

---

### 3. Allowing Numbers
- ❌ `Anuj123`
- ❌ `John2Doe`

---

### 4. Excessive Special Characters
- ❌ `@@@John###`
- ❌ `--Anuj--`

---

### 5. Empty or Single Character Names
- ❌ `""`
- ❌ `"A"` (usually invalid unless special case)

---

### 6. Multiple Consecutive Spaces or Symbols
- ❌ `Anuj   Sharma`
- ❌ `John--Doe`
- ❌ `O''Connor`

---

## ⚠️ Things to Keep in Mind (Real-World Reality)

### 1. Names Are Not Uniform
- Some people:
  - Have no last name
  - Have multiple middle names
  - Use initials (`A P J Abdul Kalam`)
- Don’t force rigid formats like:
  - “First Name + Last Name mandatory”

---

### 2. Cultural Sensitivity
- Different cultures follow different naming systems:
  - Western: First + Last
  - Indian: Given + Father’s name
  - Some: Single name only

---

### 3. Avoid Over-Validation
- You are not verifying identity, just format
- Don’t reject valid humans because your regex is insecure

---

### 4. Security Considerations
- Prevent:
  - SQL Injection (`' OR 1=1 --`)
- Sanitize input before storing

---

## 🧠 Suggested Validation Levels

### Level 1 (Basic)
- Check non-empty
- Allow alphabets + spaces

---

### Level 2 (Intermediate)
- Allow `'` and `-`
- Remove extra spaces
- Length validation

---

### Level 3 (Advanced)
- Unicode support
- Normalization (capitalization)
- Security sanitization

---

## 🧪 Example Valid Names
- `Anuj Sharma`
- `Mary-Jane Watson`
- `O'Connor`
- `José Alvarez`
- `अमित कुमार`

---

## 🧪 Example Invalid Names
- `Anuj123`
- `@@John`
- ``
- `A`
- `John--Doe`

---

## 🧩 Final : Conclusion
If your validator is too strict, you’ll reject real people.  
If it’s too loose, you’ll accept nonsense.

Names are messy. Accept that early, or your validation logic will become a joke in production.
