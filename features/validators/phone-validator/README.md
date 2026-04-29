# 📱 Phone Number Validator Guidelines

## 🎯 Purpose
Define rules and best practices for validating phone numbers to ensure correct format, usability, and real-world compatibility.

---

## ✅ DO’s (What to Validate)

### 1. Basic Structure
- Allow only:
  - Digits (0-9)
  - Optional symbols: `+`, `-`, space
- Example valid formats:
  - `9876543210`
  - `+919876543210`
  - `+91 98765 43210`

---

### 2. Country Code Handling
- Allow optional `+` at the start
- Country code should be valid (e.g., `+91`, `+1`)
- If no country code, assume default (based on system)

---

### 3. Length Constraints
- International standard (E.164):
  - Minimum: **10 digits**
  - Maximum: **15 digits**
- Strip spaces/symbols before counting

---

### 4. Normalize Input
- Remove:
  - Spaces
  - Dashes
- Store in standard format:
  ```
  +919876543210
  ```

---

### 5. Digit Validation
- Ensure all characters (after cleaning) are digits except leading `+`

---

## ❌ DON'Ts (Common Mistakes to Avoid)

### 1. Alphabets or Special Characters
- ❌ `98A7654321`
- ❌ `98765@3210`

---

### 2. Multiple `+` Signs
- ❌ `++919876543210`
- ❌ `+91+9876543210`

---

### 3. Wrong Length
- ❌ Too short: `12345`
- ❌ Too long: `12345678901234567890`

---

### 4. Incorrect Placement of Symbols
- ❌ `91+9876543210`
- ❌ `+ 91 9876543210` (space after +)

---

### 5. Leading Zeros Misuse
- ❌ `00919876543210` (unless explicitly supported format)

---

## ⚠️ Things to Keep in Mind (Real-World Reality)

### 1. Formatting Varies by Country
- India: `+91 98765 43210`
- US: `+1 123-456-7890`
- Don’t hardcode one format globally

---

### 2. Validation ≠ Verification
- Just because format is valid doesn’t mean:
  - Number exists
  - Number is active
- Use OTP verification for real validation

---

### 3. Extensions (Advanced Case)
- Some numbers include extensions:
  - `+1 1234567890 x123`
- Usually ignored in basic validation

---

### 4. Avoid Over-Strict Rules
- Users enter numbers in messy ways:
  - `98765-43210`
  - `98765 43210`
- Clean first, then validate

---

## 🧠 Suggested Validation Levels

### Level 1 (Basic)
- Check digits only
- Length validation

---

### Level 2 (Intermediate)
- Allow `+` and formatting symbols
- Normalize input

---

### Level 3 (Advanced)
- Country-specific validation
- OTP verification
- Carrier/API validation

---

## 🧪 Example Valid Numbers
- `9876543210`
- `+919876543210`
- `+1 1234567890`

---

## 🧪 Example Invalid Numbers
- `12345`
- `98A7654321`
- `++919876543210`

---

## 🧩 Final 
If your validator rejects valid numbers, users get annoyed.  
If it accepts garbage, your backend suffers.

Clean → Normalize → Validate → Verify  
That’s the order. Not whatever random logic people usually write at 2 AM
