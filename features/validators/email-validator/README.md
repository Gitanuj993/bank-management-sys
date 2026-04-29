This document outlines the do’s and don’ts for validating email addresses. The goal is to ensure correctness, avoid false positives, and not reject valid emails like an overconfident gatekeeper.
✅ DO’s (What to Validate)
1. Basic Structure
Must contain exactly one @ symbol
Format:

local-part@domain
2. Local Part Rules (before @)
Can contain:
Alphabets (a-z, A-Z)
Digits (0-9)
Special characters: . _ % + -
Must NOT:
Start or end with .
Have consecutive dots (..)
3. Domain Rules (after @)
Must contain at least one .
Example: example.com
Domain name:
Only letters, digits, hyphens (-)
Cannot start or end with -
Top-Level Domain (TLD):
At least 2 characters (e.g., .com, .org)
4. Length Constraints
Total email length ≤ 254 characters
Local part ≤ 64 characters
5. Case Handling
Treat email as case-insensitive (especially domain part)
❌ DON'Ts (Common Mistakes to Avoid)
1. Multiple @ Symbols
❌ user@@gmail.com
2. Missing Parts
❌ @gmail.com (missing local part)
❌ user@ (missing domain)
3. Invalid Characters
❌ Spaces are not allowed
user name@gmail.com
❌ Special characters outside allowed set
user#gmail.com
4. Invalid Dot Usage
❌ user..name@gmail.com
❌ .username@gmail.com
❌ username.@gmail.com
5. Invalid Domain Format
❌ user@.com
❌ user@com
❌ user@gmail..com
6. Invalid TLD
❌ user@gmail.c
❌ user@gmail.123

<hr>

⚠️ Things to Keep in Mind (Real-World Reality)
1. Regex is Not Enough
Even perfect regex cannot guarantee a real email exists
It only checks format, not deliverability
2. Domain Validation (Optional Advanced)
Check if domain exists using DNS lookup (MX records)
3. Avoid Over-Strict Rules
Some valid emails look weird:
user+tag@gmail.com
firstname.lastname@sub.domain.com
4. International Emails (Advanced)
Emails can contain Unicode (rare but valid)
Example: 用户@例子.公司
5. Disposable Emails
You may want to block temporary email services (business logic)

## 🧠 Suggested Validation Levels
Level 1 (Basic)
Check @ presence
Check . in domain
Length validation
Level 2 (Intermediate)
Regex pattern validation
No invalid characters
Proper dot usage
## Level 3 (Advanced)
DNS check (MX records)
## Block disposable domains
## Email verification (OTP)

🧪 Example Valid Emails
test@gmail.com
user.name123@yahoo.co.in
first_last+tag@domain.org
🧪 Example Invalid Emails
test@.com
user@@domain.com
user name@gmail.com



🧩 Final Thought
If your validator rejects valid emails, users hate you.
If it accepts garbage, your database hates you.
Balance it like a sane developer, not like someone trying to prove regex supremacy.

If you actually implement all this cleanly,
 you’re already ahead of half the “I built my own email validator” crowd.
