This task is in correspondence to **Task 6: Create a Strong Password and Evaluate Its Strength**

Strong passwords are essential today because they protect your accounts and personal data from hackers who use automated tools to guess weak or common passwords. With rising cyber threats, data breaches, and identity theft, a strong, unique password is a simple but critical defense against unauthorized access and online fraud.

---

## Guidelines for Strong Passwords

### NIST Guidelines according to NIST SP 800-63B-4 in August 2024

1. **Minimum Length**
   - Must be at least **8 characters**
   - Recommended: **15 characters** or more

2. **Maximum Length**
   - Support passwords up to **64 characters**

3. **Character Requirements**
   - No mandatory complexity (e.g., symbols or numbers)
   - All **printable ASCII and Unicode characters** allowed (including spaces, emojis)

4. **Passphrase Use**
   - Encourage long, **memorable passphrases**

5. **Password Screening**
   - Block:
     - **Known compromised passwords**
     - **Common or easily guessable passwords**

6. **Password Expiration**
   - **No routine changes** required unless compromised

7. **User Experience**
   - Allow **copy-paste** and **password manager use**
   - Avoid restrictions that hurt usability

8. **Authentication Security**
   - Enforce **rate limiting** and lockouts after repeated failed attempts

### General Guidelines for Strong Passwords

1. **Length**
   - Use at least **12–16 characters**

2. **Character Variety**
   - Mix of uppercase, lowercase, numbers, and symbols

3. **Avoid Common Passwords**
   - Don’t use predictable passwords like `123456` or `password`

4. **Avoid Personal Info**
   - Exclude names, birthdays, and common details

5. **Use Passphrases**
   - Example: `PurpleBanana!TricycleMoon`

6. **Unique Per Account**
   - Never reuse passwords across sites

7. **Use a Password Manager**
   - Store and generate strong passwords securely

8. **Enable MFA**
   - Add an extra layer of login security

---

## Example Passwords for Study

1. **Simple but Not Recommended:** `sunshine123`  
   * Too short and predictable. Easily cracked in brute-force attacks.

2. **Strong Random Password (High Entropy):** `B7$gT!kQp@X9z#rM`  
   * Highly secure due to randomness. Best used with a password manager.

3. **Memorable Passphrase:** `Cactus Sunset Pizza Dance`  
   * Long and easy to remember. Passphrases are more user-friendly and secure.

4. **Mixed Character Types:** `R@inB0w_H0rse_2025!`  
   * Good complexity, combining letters, numbers, and symbols.

5. **Predictable Pattern (Weak Practice):** `Password!2025`  
   * Looks complex but is commonly used and easily guessable.

6. **Unicode-Inclusive:** `MySecureLogin🔥`  
   * Demonstrates support for Unicode characters. Check if your system allows this.

7. **Keyboard Pattern (Weak):** `qwerty!@#123`  
   * Based on keyboard layout. Very predictable and not secure.

8. **Sentence-Based Passphrase:** `TheCakeWas4$DeliciousToday`  
   * Natural language with slight complexity. Easy to remember and fairly strong.

9. **Unique Per Service:** `Netflix-Rain$82Series`  
   * Customized for a specific service. Better than reusing the same password.

10. **Word Mash with Symbols:** `Frog#Planet^Dust!3`  
    * Combines unrelated words with symbols and a number. Balanced and memorable.

11. **Default-Style (Weak Practice):** `Welcome@123`  
    * Common structure used by many systems. Weak due to predictability.

12. **Corporate-Style Password (Moderate):** `Admin2024!`  
    * Slight complexity, but highly predictable. Common in enterprise defaults.

13. **Phrase-Based but Predictable:** `LetMeIn!!`  
    * Easily guessed. A known phrase with weak complexity.

14. **xkcd-Style Passphrase (Still Good):** `Tr0ub4dor&3`  
    * Previously considered strong; now semi-known and slightly predictable.

15. **Classic Passphrase (Strong):** `CorrectHorseBatteryStaple`  
    * Still strong due to length and randomness, despite being well-known.



## Password Strength Testing

The above mentioned passwords were tested one by one to gauge their strenth on the [Bitwarden Password Strength Testing Tool](https://bitwarden.com/password-strength/).

| #  | Password                         | Strength Rating | Estimated Time to Crack |
|----|----------------------------------|------------------|---------------------------|
| 1  | sunshine123                      | Very Weak        | 2 seconds                 |
| 2  | B7$gT!kQp@X9z#rM                 | Strong           | Centuries                 |
| 3  | Cactus Sunset Pizza Dance       | Strong           | Centuries                 |
| 4  | R@inB0w_H0rse_2025!              | Strong           | Centuries                 |
| 5  | Password!2025                    | Weak             | 17 minutes                |
| 6  | MySecureLogin🔥                 | Strong           | 31 years                  |
| 7  | qwerty!@#123                     | Good             | 3 hours                   |
| 8  | TheCakeWas4$DeliciousToday      | Strong           | Centuries                 |
| 9  | Netflix-Rain$82Series           | Strong           | Centuries                 |
| 10 | Frog#Planet^Dust!3              | Strong           | Centuries                 |
| 11 | Welcome@123                     | Weak             | 7 minutes                 |
| 12 | Admin2024!                      | Good             | 6 hours                   |
| 13 | LetMeIn!!                       | Very Weak        | 11 seconds                |
| 14 | Tr0ub4dor&3                     | Strong           | 4 months                  |
| 15 | CorrectHorseBatteryStaple       | Strong           | Centuries                 |

---



## Summary and Discussion

Here’s a concise summary of what the results show:

- Length and randomness matter most: Long passphrases or random strings are hardest to crack.

- Predictable patterns are weak: Passwords like Welcome@123 or Password!2025 may look complex but are easily guessed.

- Common phrases = quick crack times: Even with symbols, phrases like LetMeIn!! are very weak.

- Passphrases can be both strong and memorable: CorrectHorseBatteryStaple and similar structures are secure if not reused.

- Unique passwords per site are essential: Reuse—even of strong passwords—creates major security risks.

### **Common Password Attacks**

- **Brute Force Attack:**  
  Tries all possible character combinations.  
  → *Longer and more complex passwords take exponentially longer to crack.*

- **Dictionary Attack:**  
  Uses a list of common passwords and known words.  
  → *Short or simple passwords are highly vulnerable.*

- **Credential Stuffing:**  
  Uses leaked usernames/passwords from other breaches.  
  → *Reused passwords are a major risk.*

- **Phishing:**  
  Tricks users into revealing passwords via fake emails or websites.  
  → *No password complexity can defend against this — only awareness and MFA can.*

- **Keylogging & MITM (Man-in-the-Middle):**  
  Capture passwords as they’re typed or transmitted.  
  → *Only secure systems and encrypted connections protect against this.*

### **How Password Complexity Affects Security?**

- **Increased complexity (length + randomness)** significantly raises the time and computational effort needed to crack passwords.
- **Simple or common passwords** (e.g. "qwerty", "password123") can be cracked in seconds using dictionary or brute force attacks.
- **Complex passwords** with mixed characters, symbols, and no predictable patterns resist automated guessing tools.
- **Passphrases** (e.g. "Cactus Sunset Pizza Dance") offer strong security while remaining memorable.
- **Conclusion:** Complexity and uniqueness are critical. They directly defend against automated attacks and make brute-force impractical.

---
