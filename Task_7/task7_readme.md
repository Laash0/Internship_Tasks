This document is created in correspondence to **Task 7 :Identify and Remove Suspicious Browser Extensions**.

---

### What are Extensions and their Purpose ?

**Browser extensions** are small software programs that integrate with web browsers to add, modify, or enhance their functionality.

They allow users to customize their browsing experience by enabling features such as ad blocking, password management, user interface changes, privacy controls, and productivity tools. Extensions are typically installed from browser-specific stores (like Chrome Web Store or Firefox Add-ons) and run alongside websites visited by the user.

🔧 **Purpose of Extensions:**

1. **Enhance Productivity** – Manage tabs, take notes, or organize tasks.
2. **Improve Privacy & Security** – Block trackers, ads, or manage passwords.
3. **Customize Browsing Experience** – Change themes, enable dark mode, etc.
4. **Integrate Tools** – Sync with external services (e.g., mail, cloud storage).
5. **Automate Actions** – Autofill forms, translate pages, or manage downloads.

They extend browser capabilities without modifying the core software.

## Gathering Extensions

To gather real world usage of a user , this study will consider my own setup based on web browser **Firefox** version _Version 139.0.1 (64-bit)_ .

So to get the required list of extensions , follow one of these steps :

1. Click ≡ (3 lines) > Add-ons and Themes > Extensions

OR

2. or visit -> `about:addons` in your address bar

The extensions being considered are :

| #  | Extension Name         | Purpose                                                                 |
|----|------------------------|-------------------------------------------------------------------------|
| 1  | **uBlock Origin**      | Blocks ads, trackers, and malicious domains to enhance privacy         |
| 2  | **Privacy Badger**     | Automatically detects and blocks invisible trackers based on behavior  |
| 3  | **Decentraleyes**      | Serves local CDN resources to prevent third-party tracking              |
| 4  | **Dark Reader**        | Applies dark mode to websites for better readability and eye comfort    |
| 5  | **Simple Tab Groups**  | Organizes tabs into groups for improved tab management and productivity |
| 6  | **Strict Pop-up Blocker** | Blocks unwanted pop-ups and overlays to reduce distractions            |
| 7  | **Proton Pass**        | Manages passwords securely with encryption and autofill capabilities    |
| 8  | **Plasma Integration** | Connects Firefox with KDE desktop features like notifications and file handling |


---

## Extension Reviews and Permissions

Understanding the permissions each extension requests is crucial for assessing its impact on privacy and security.

| Extension Name           | Average Rating | Permissions Required                                                                                                                                                                                                                                          | Remarks                                                                      |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **uBlock Origin**        | ⭐ 4.8 / 5      | - Read and modify privacy settings  <br> - Access browser tabs  <br> - Access browser activity during navigation  <br> - Access your data for all websites                                                                                                    | Widely trusted; permissions are essential for blocking trackers and ads      |
| **Privacy Badger**       | ⭐ 4.8 / 5      | - Read and modify privacy settings  <br> - Access browser tabs  <br> - Access browser activity during navigation  <br> - Access your data for all websites                                                                                                     | Developed by EFF; respects user privacy and is transparent                   |
| **Decentraleyes**        | ⭐ 4.8 / 5      | - Read and modify privacy settings  <br> - Access browser tabs  <br> - Access browser activity during navigation  <br> *May also ask to:* Access your data for all websites                                                                                   | Lightweight; minimal data exposure, focused on local CDN delivery            |
| **Dark Reader**          | ⭐ 4.5 / 5      | - Access browser tabs  <br> - Access your data for all websites                                                                                                                                                                                               | Cosmetic tool; requires access to apply themes site-wide                     |
| **Simple Tab Groups**    | ⭐ 4 / 5        | - Download files and read/modify download history  <br> - Manage themes  <br> - Show notifications  <br> - Access recently closed tabs  <br> - Hide/show browser tabs  <br> - Access browser tabs  <br> - Access your data for all websites  <br> *May also ask to:* Read and modify bookmarks | Feature-rich; broad permissions necessary for tab management, use cautiously |
| **Strict Pop-up Blocker**| ⭐ 4 / 5        | - Read and modify browser settings                                                                                                                                                                                                                            | Low permissions; safe and lightweight alternative to older blockers          |
| **Proton Pass**          | ⭐ 4.7 / 5      | - Access your data for all websites  <br> *May also ask to:* Read and modify privacy settings                                                                                                                                                                 | Encrypted password manager from Proton AG; high trust                        |
| **Plasma Integration**   | ⭐ 4.7 / 5      | - Exchange messages with external programs  <br> - Read/modify download history  <br> - Display notifications  <br> - Access browser tabs  <br> - Access your data for all websites  <br> *May also ask to:* Access browsing history                          | KDE integration only; excessive permissions for general users                |


> 🔒 **Tip**: Only allow extensions that request permissions truly necessary for their function. Avoid those asking for sensitive access without a clear purpose.


### Summary of Browser Extensions Permissions and Trustworthiness

The evaluation of the installed browser extensions reveals a mix of highly trusted and feature-rich tools with varying permission requirements:

- **Highly Trusted Extensions:**  
  - *uBlock Origin*, *Privacy Badger*, and *Proton Pass* rank high in user ratings (4.7–4.8) and come from reputable developers focused on privacy and security. Although they request broad permissions like access to all website data and browser activity, these are necessary for their core functions such as ad-blocking, tracker blocking, and secure password management.

- **Moderate Permissions and Utility:**  
  - *Decentraleyes* and *Dark Reader* maintain strong privacy focuses with moderate permissions mainly related to accessing tabs and site data. Their roles (local CDN proxy and dark mode application) justify these permissions with minimal privacy risk.

- **Feature-Rich Extensions with Broad Permissions:**  
  - *Simple Tab Groups* demands extensive permissions including managing downloads, notifications, and bookmarks, reflecting its complex functionality. While useful, such broad access warrants careful monitoring for security implications.

- **Lightweight and Minimal Permissions:**  
  - *Strict Pop-up Blocker* is a lightweight tool with limited permissions, making it a safer choice for popup management.

- **Specialized Integration Extension:**  
  - *Plasma Integration* is designed for KDE desktop integration, requiring extensive permissions. For general users without KDE, this extension could present unnecessary security risks due to its broad access.

---

### Key Takeaways

- Extensions requesting **access to all website data and browser activity** should be trusted and regularly reviewed, as these permissions can expose sensitive information.
- Extensions with **minimal and clear permission scopes** are generally safer but may offer limited functionality.
- It is important to **remove unused or suspicious extensions**, especially those with broad permissions but unclear reputations.
- Regularly auditing extensions helps reduce the browser’s attack surface and improve overall cybersecurity posture.


> Regularly reviewing permissions and understanding why each is needed is crucial for **minimizing the browser attack surface**.

---

## Identifying Suspicious or Unused Extensions

All currently installed extensions are actively used, which is a positive sign of mindful extension management. However, based on user reviews and permission analysis, two extensions raise mild concerns:

- **Simple Tab Groups (Rating: ⭐ 4.0 / 5)**  
  While feature-rich, this extension demands extensive permissions including access to download history, recently closed tabs, and bookmarks. Although it is popular among power users, the relatively lower rating may reflect occasional bugs or performance issues. No major security incidents have been reported as of now, but its broad access makes it a candidate for periodic review.

- **Strict Pop-up Blocker (Rating: ⭐ 4.0 / 5)**  
  This extension operates with limited permissions, which is good from a security perspective. However, lower ratings might suggest inconsistent performance or usability problems rather than security flaws. Again, no critical security vulnerabilities are reported.

**Conclusion:**  
At present, no extensions appear overtly malicious or unnecessary. However, *Simple Tab Groups* and *Strict Pop-up Blocker* should be kept under review due to their ratings and (in the former's case) extensive permissions.

---

## Extension Review Revisions and Improvements

Following the initial evaluation, two extensions were identified for reconsideration based on user ratings, Firefox recommendations, and evolving functionality needs:

### 1. Replacement of **Strict Pop-up Blocker** with **Popup Blocker (strict)**

- **Reason for Change:**  
  The previously used **Strict Pop-up Blocker** had a modest rating (⭐ 4.0) and lacked recommendation by Mozilla. After further research, **Popup Blocker (strict)** was identified as a **Firefox Recommended** extension with a slightly higher rating (⭐ 4.2) and better community feedback.

- **Advantages of Popup Blocker (strict):**
  - Firefox officially recommends it.
  - Simpler and cleaner UI for blocking pop-ups.
  - Fewer permissions while still effectively blocking pop-ups.
  - Actively maintained and transparent on GitHub.

> **Action Taken:** Uninstalled **Strict Pop-up Blocker** and installed **Popup Blocker (strict)** as a safer and more effective alternative.

---

### 2. Replacement of **Simple Tab Groups** with **Tree Style Tab**

- **Reason for Change:**  
  While **Simple Tab Groups** offered tab organization features, it had a lower average rating (⭐ 4.0) and required broad permissions (e.g., bookmark and download management). In contrast, **Tree Style Tab** is rated higher (⭐ 4.5), has a more focused permission set, and provides a vertical, tree-structured tab interface that aligns better with workflow needs.

- **Advantages of Tree Style Tab:**
  - Highly rated and actively developed.
  - Firefox Recommended.
  - Cleaner interface with vertical tree layout.
  - Fewer and safer permissions compared to Simple Tab Groups.
  - Integrates seamlessly with Firefox tab behavior without managing bookmarks or download history.

> **Action Taken:** Removed **Simple Tab Groups** and installed **Tree Style Tab** to improve usability and reduce permission exposure.

---

### Updated List of Active Extensions (Post-Replacement):

| Extension Name           | Average Rating | Permissions Required                                                                                                                                                                                                                  | Remarks                                                                 |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Popup Blocker (strict)** | ⭐ 4.2 / 5      | - Access browser tabs <br> - Read and modify browser settings                                                                                                                                                                         | Firefox-recommended; lightweight and effective popup blocker           |
| **Tree Style Tab**       | ⭐ 4.5 / 5      | - Access browser tabs <br> - Store and access user data in the browser                                                                                                                          | Highly rated; vertical tab manager with cleaner UI and better usability |


1. uBlock Origin
2. Privacy Badger
3. Decentraleyes
4. Dark Reader
5. **Popup Blocker (strict)** ✅ *(Replaced Strict Pop-up Blocker)*
6. Proton Pass
7. Plasma Integration
8. **Tree Style Tab** ✅ *(Replaced Simple Tab Groups)*

---

> These adjustments reflect a proactive cybersecurity practice—regularly auditing and refining the browser environment for optimal performance, usability, and privacy.

---

## How Malicious Extensions Can Harm Users

Browser extensions can significantly enhance usability—but when malicious or compromised, they pose serious **security, privacy, and integrity risks**. Unlike traditional malware, malicious extensions often operate **within the browser’s permission model**, making them harder to detect.

### Common Threat Vectors

1. **Data Exfiltration**  
   Malicious extensions can **access all browsing data**, including login credentials, cookies, session tokens, and input fields.  
   Some silently monitor keystrokes or capture form data from sensitive sites (e.g., banking, email).

2. **Unauthorized Web Requests**  
   Extensions can make **background requests** to third-party servers, exfiltrating data or injecting malicious scripts into webpages.

3. **Ad Injections & Affiliate Hijacking**  
   Injects **unauthorized advertisements**, overlays, or popups into visited sites.  
   Alters referral links to hijack **affiliate revenue** without user knowledge.

4. **Surveillance & Tracking**  
   Can bypass anti-tracking tools by **building persistent user profiles** across websites using unique fingerprinting or tracking pixels.

5. **Privilege Escalation & Code Injection**  
   Some exploit vulnerabilities in the browser or escalate permissions over time.  
   May **inject JavaScript** into trusted sites (Cross-Site Scripting - XSS), leading to session hijacking or redirection to phishing sites.

6. **Updates as Attack Vectors**  
   Even legitimate extensions can be **compromised via malicious updates**, especially if ownership changes hands and the new developer inserts harmful code.

---

### Real-World Incidents

- **DataSpii Breach (2019):**  
  Several Chrome and Firefox extensions were found collecting and leaking sensitive browsing data of over 4 million users, including internal URLs of major companies.

- **Nano Adblocker Incident (2020):**  
  A popular ad blocker was sold to a third party and quickly became a malicious tool to inject scripts and track users.

---

### ⚠️ Why This Matters

Since browser extensions operate with **elevated privileges**, malicious or careless use can:

- Undermine even strong security setups (e.g., VPNs, password managers).
- Cause data leaks that lead to identity theft or financial loss.
- Weaken organizational cybersecurity if used on enterprise machines.

> **Takeaway:** Every extension must be treated as a potential risk. Vet, review, and limit them like any critical software on your system.

---
