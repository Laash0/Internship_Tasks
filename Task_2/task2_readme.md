This file is made in correspondence to **Task 2: Analyze a Phishing Email Sample**.

---

**Phishing** is a type of **cyberattack** where attackers attempt to trick individuals into revealing sensitive information, such as passwords, or other personal details, by impersonating a trustworthy entity in electronic communication, most commonly email. Attackers often use social engineering tactics in phishing to manipulate victims into taking desired actions, such as clicking malicious links or downloading attachments.

## Phishing Email Analysis Report 1

### 1. Sender Email Address
- **Email:** support@careerbuildcompany.com  
- **Analysis:** This is not a LinkedIn domain. Legitimate LinkedIn emails come from `@linkedin.com`. This domain appears spoofed or misleading.

---

### 2. Displayed Branding
- **Observation:** Mimics LinkedIn branding and layout.
- **Analysis:** Visual styling and elements are similar to legitimate LinkedIn communications, which may mislead recipients.

---

### 3. Email Content
- **Details:** Includes LinkedIn-style notifications:
  - "1 message"
  - "2 invitations"
  - "24 new updates"
  - "See what’s new" button
- **Analysis:** While the content appears familiar, the sender’s domain raises red flags.

---

### 4. Call to Action (CTA)
- **Text:** "See what’s new"
- **Analysis:** The CTA button may redirect to a phishing site. The actual link URL is not shown in the screenshot and should not be clicked without inspection.

---

### 5. Hyperlinks in Body
- **Observation:** Multiple links such as "1 message", "2 invitations".
- **Analysis:** These may lead to phishing sites or malware downloads, especially given the suspicious sender domain.

---

### 6. Language and Grammar
- **Observation:** No obvious grammar or spelling errors.
- **Analysis:** Neutral. Clean language doesn't confirm legitimacy.

---

### Summary of Phishing Indicators

| Indicator                     | Present | Notes                                                     |
|------------------------------|---------|-----------------------------------------------------------|
| Spoofed sender domain        | Yes     | Domain does not match LinkedIn                            |
| Use of impersonated branding | Yes     | Mimics LinkedIn layout and logo                           |
| Suspicious links             | Likely  | Cannot verify destination without inspecting URL          |
| Urgent/clickbait language    | Moderate| Encourages user to click with action-driven wording       |
| Grammar/spelling issues      | No      | Text appears correct                                      |
| Unexpected source            | Yes     | Unsolicited and from an unknown domain                    |

### Conclusion
This email demonstrates multiple characteristics of a phishing attempt, including a spoofed sender address, impersonation of LinkedIn branding, and suspicious links. It should be considered unsafe and either deleted or reported.

---

## Phishing Email Analysis Report 2

### 1. **Sample Email Source:**  
   Email headers and metadata provided, suspicious message claiming a login attempt notification from "Facebook."

### 2. **Sender’s Email Address Examination:**  
   - Sender: `yxvr6@ba4f9cojas.com` — domain looks random and unrelated to Facebook.  
   - Reply-to address: `ssecnewssotrecognizd@gmail.com` (generic Gmail address, suspicious).  
   - Return-path domain: `liakmndukeety.uk` — unrelated and suspicious domain.

### 3. **Header Discrepancies:**  
   - SPF check: **None** (domain does not authorize sending IP).  
   - DKIM: None (no digital signature).  
   - DMARC: None (no policy).  
   - CompAuth: **Fail** (composite authentication failed).  
   - Multiple different domains in path, none match legitimate Facebook servers.  
   - Sender IP (89.144.44.18) does not match official Facebook sending IPs.

### 4. **Suspicious Links or Attachments:**  
   - No direct attachments shown here, but the Reply-To and From addresses hint at phishing attempts.  
   - Email likely contains links redirecting to phishing sites (not in provided snippet).

### 5. **Urgent/Threatening Language:**  
   - Subject: *"Someone tried to Iog in To Your Account, User lD : phishing@pot"* — spelling error in "Iog" (should be "log").  
   - Creates false sense of urgency to prompt action.

### 6. **Mismatched URLs:**  
   - Not visible in the headers, but Reply-To is a Gmail account unrelated to Facebook, indicating URL mismatch or redirection.

### 7. **Spelling or Grammar Errors:**  
   - "Iog" instead of "log" in subject line.  
   - Irregular capitalization and punctuation (e.g., "User lD", random spaces).  
   - Domains and sender addresses look suspicious and unprofessional.

### 8. **Summary of Phishing Traits:**  
   - Spoofed sender address using unrelated domains.  
   - Missing SPF, DKIM, DMARC protections.  
   - Failed authentication checks.  
   - Use of urgent language with spelling errors.  
   - Suspicious Reply-To address not related to claimed sender.  
   - Likely to contain malicious links or attempt credential theft.

This email is a classic phishing attempt and should be treated as spam and deleted immediately. Never click on any links or reply to suspicious emails like this.

---

## Phishing Email Analysis Report 3

### 1. Basic Email Metadata

- **From:** Microsoft account team `<no-reply@access-accsecurity.com>`
- **Reply-To:** `sotrecognizd@gmail.com`
- **Return-Path:** `bounce@sintxjoji.servifans.com`
- **To:** `phishing@pot`
- **Subject:** Microsoft account unusual signin activity
- **Date:** Sat, 16 Sep 2023 19:17:20 +0000

### 2. Sender Domain and IP Inspection

- **Originating IP:** `89.144.9.91` (belongs to `sintxjoji.servifans.com`)
- **SPF Check:** Failed – No SPF record found for `servifans.com`
- **DKIM:** Failed – No DKIM signature present
- **DMARC:** PermError – DMARC policy missing or misconfigured
- **Sender Domain Legitimacy:**
  - `access-accsecurity.com`: Impersonates Microsoft-style domain
  - `servifans.com`: Possibly compromised or used for malicious purposes
  - `gmail.com` in Reply-To: Not associated with Microsoft

### 3. Header Chain Overview

| Hop | Server/Domain | Notes |
|-----|----------------|-------|
| 1 | `sintxjoji.servifans.com (89.144.9.91)` | Suspicious origin |
| 2 | `SN1NAM02FT0050.mail.protection.outlook.com` | Microsoft EOP relay |
| 3 | `SA1PR04CA0021.outlook.office365.com` | Exchange |
| 4 | `DM4PR19MB6123.namprd19.prod.outlook.com` | Delivered to Outlook mailbox |

- **AuthAs:** Anonymous
- **AuthSource:** External (via EOP)
- **SCL (Spam Confidence Level):** 5 – Likely spam
- **BCL (Bulk Complaint Level):** 6 – Indicates bulk or phishing-like behavior

### 4. Suspicious Indicators

- Spoofed identity – Appears to be from Microsoft but uses unrelated domains
- Mismatched email addresses – From, Return-Path, and Reply-To are inconsistent
- Urgent subject – “Unusual sign-in activity” used to provoke fear
- High priority flag – Set to Priority 1 to draw immediate attention
- Bulk email characteristics – Detected by Microsoft antispam tools

### 5. Conclusion: Malicious/Phishing Email

This message is a phishing attempt designed to impersonate Microsoft and trick the recipient into clicking malicious links or disclosing sensitive information. It lacks proper authentication and uses misleading sender details and urgent language.

### Recommended Action

- Do not click on any links in the message
- Do not reply to the sender
- Report the email as phishing using your email platform’s built-in tools
- Delete the message from your inbox

---

## Recognizing Malicious Email Attempts

Identifying deceptive emails is crucial for safeguarding sensitive information. Here are common indicators to be aware of:

* **Examine Sender Information:** Pay close attention to the sender's email address and display name. Look for inconsistencies, misspellings of legitimate organizations, or unusual domains that don't align with the expected sender.
* **Analyze Email Metadata (Headers):** Utilize tools to examine the full email headers for discrepancies. These headers can reveal the true origin and path of the email, potentially exposing forged sender details or unusual routing.
* **Exercise Caution with Embedded Content:** Be highly suspicious of links and attachments. Always hover over elements that appear to be links to preview the actual URL without clicking. Look for mismatched text and link destinations, shortened URLs, or unexpected file types in attachments. Never interact with suspicious content directly.
* **Detect Persuasive or Coercive Language:** Be alert for urgent or threatening language in the email body. Attackers frequently employ social engineering tactics to pressure recipients into immediate action, often by instilling fear, curiosity, or a sense of urgency.
* **Identify Quality and Consistency Issues:** Look for spelling or grammar errors, awkward phrasing, or inconsistencies in branding or design. While some sophisticated attacks may be flawless, many deceptive emails still contain obvious mistakes that legitimate communications typically avoid.
* **Be Wary of Generic Salutations:** Be suspicious of emails that use generic greetings (e.g., "Dear Customer," "Dear Sir/Madam") instead of your specific name.
* **Verify Independently:** If an email raises any suspicion, do not use the contact information provided within the email itself. Instead, independently verify the legitimacy of the communication by contacting the organization directly through official and verified channels (e.g., their official website, a known customer service number).
