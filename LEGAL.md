# Legal Framework for AI-Assisted Patient Strategy in Direct Primary Care

This document addresses the legal landscape surrounding a Direct Primary Care (DPC) physician's use of AI tooling — specifically Claude, ralph, and the DOCTOR.md prompt system — to generate personalized patient health strategies. It is written for the practicing DPC physician who wants clarity, not paralysis.

**This document is not legal advice.** It is a practical orientation to the regulatory terrain. Consult a healthcare attorney in your state before implementing any AI workflow involving patient data.

---

## The Core Question

> Can a DPC doctor feed patient health data into an AI system and produce a strategy document — without violating privacy law or exposing the practice to unacceptable liability?

The answer is **yes**, but the path you take matters enormously.

---

## 1. HIPAA: Does It Even Apply to You?

HIPAA applies to **covered entities** — healthcare providers who electronically transmit health information in connection with standard transactions (insurance claims, eligibility checks, referral authorizations, etc.).

### Pure DPC Practices May Not Be Covered Entities

A DPC practice that:

- Does **not** bill any insurance, including Medicare and Medicaid
- Does **not** submit electronic claims or eligibility checks
- Collects only membership fees directly from patients

...has a legitimate argument that it falls outside HIPAA's jurisdictional reach. The statute's definition of "covered entity" hinges on electronic standard transactions. If you don't perform them, the regulatory hook is absent.

### This Is Not a Free Pass

Even if your practice is not a HIPAA covered entity:

- **State medical privacy laws still apply.** California's CMIA, Washington's My Health My Data Act, and similar statutes govern medical data handling independently of HIPAA.
- **Medical board standards of care still apply.** Your state licensing board expects reasonable privacy protections regardless of HIPAA status.
- **Malpractice exposure persists.** A data breach or unauthorized disclosure can give rise to civil liability under state tort law.
- **If you perform even one electronic standard transaction** — a single insurance claim, a single electronic eligibility check — you are a covered entity and HIPAA applies fully.

### Recommendation

Even pure DPC practices should treat HIPAA as a floor, not a ceiling. The compliance habits are good practice and provide a defensible posture if your HIPAA status is ever challenged.

---

## 2. Three Paths to Using AI Legally

There are three legally distinct approaches to processing patient data through this toolchain. They carry very different risk profiles.

### Path A: De-Identification (Recommended)

Under 45 CFR 164.514, properly de-identified health information is **not PHI**. The HIPAA Privacy Rule does not restrict its use or disclosure. De-identified data can be freely processed by any AI service without a BAA, without patient authorization, and without HIPAA exposure.

The **Safe Harbor method** requires removing all 18 categories of identifiers:

| # | Identifier | Example |
|---|---|---|
| 1 | Names | First, last, middle, initials |
| 2 | Geographic data smaller than state | Street address, city, county, ZIP code |
| 3 | Dates (except year) related to an individual | Birth date, admission date, discharge date; ages over 89 aggregated to 90+ |
| 4 | Phone numbers | All |
| 5 | Fax numbers | All |
| 6 | Email addresses | All |
| 7 | Social Security numbers | All |
| 8 | Medical record numbers | All |
| 9 | Health plan beneficiary numbers | All |
| 10 | Account numbers | All |
| 11 | Certificate/license numbers | All |
| 12 | Vehicle identifiers | VIN, license plate |
| 13 | Device identifiers | Serial numbers, UDIs |
| 14 | Web URLs | All |
| 15 | IP addresses | All |
| 16 | Biometric identifiers | Fingerprints, voiceprints |
| 17 | Full-face photos | And comparable images |
| 18 | Any other unique identifying number | Anything that could re-identify |

**In practice for this toolchain:** Before feeding a patient profile into Claude via DOCTOR.md, strip the patient's name, date of birth, addresses, phone numbers, email, SSN, and any other identifying details. Use a placeholder like "Patient A" or a first-name-only alias. Retain the clinical data — labs, medications, diagnoses, lifestyle factors — which are the substance of the analysis.

**The risk:** Incomplete de-identification. With rare conditions or small patient populations, clinical details alone may be re-identifying. The physician bears responsibility for ensuring the de-identification is genuine, not cosmetic.

### Path B: Patient Authorization (Viable with Caveats)

Under 45 CFR 164.508, a patient may sign a written authorization permitting disclosure of their PHI to a specific third party — including a non-HIPAA-covered AI service.

A valid HIPAA authorization must include:

- Specific description of the information to be disclosed
- Name of the entity making the disclosure (your practice)
- Name of the entity receiving the disclosure (Anthropic / Claude)
- Purpose of the disclosure (AI-assisted health strategy generation)
- Expiration date or event
- Statement that the patient may revoke the authorization in writing
- **Redisclosure warning**: a statement that once disclosed, the information may no longer be protected by HIPAA
- Patient signature and date

**Critical constraints:**

- You **cannot condition treatment on signing the authorization** (45 CFR 164.508(b)(4)). A patient who refuses must still receive care.
- The redisclosure warning is not a formality — it is a genuine risk disclosure. Once data reaches Anthropic, HIPAA no longer governs what happens to it.
- **State laws may be stricter.** California's CMIA has its own authorization requirements. Some states require additional disclosures for AI processing specifically.

### Path C: HIPAA-Compliant API with BAA (Enterprise Path)

Anthropic offers Business Associate Agreements for:

- **Claude API** customers with a **zero data retention agreement**
- **HIPAA-ready Enterprise plans** (sales-assisted, not self-serve)

Under a BAA, Anthropic becomes a business associate and HIPAA governs the relationship. PHI can be processed through the API without de-identification or patient authorization (for treatment, payment, and healthcare operations purposes).

**Reality check for solo/small DPC practices:** The Enterprise path involves sales negotiations, custom pricing, and organizational-scale compliance infrastructure. It is designed for health systems and large organizations. For most DPC practices, Path A (de-identification) is far more practical.

---

## 3. What About Consumer Claude?

**Consumer Claude (Free, Pro, Max, Team plans) should not be used with identifiable patient data.** Period.

As of September 2025, Anthropic's consumer terms allow chat transcripts to be used for model training by default, with a 5-year data retention period. There is no BAA available for consumer plans. Even with patient authorization, the training data use and extended retention create unacceptable risk.

**The de-identification path still works with consumer Claude.** If you have genuinely removed all 18 identifiers before the data enters the system, there is no PHI in play and the consumer product's data practices are irrelevant to HIPAA.

For identifiable data, use the API with appropriate agreements.

---

## 4. State Law Overlay

HIPAA is a floor. Several states have enacted laws that go further, and these apply regardless of your HIPAA covered entity status.

### California

- **CMIA (Confidentiality of Medical Information Act):** Broader than HIPAA, applies to most healthcare providers and businesses maintaining medical information. Private right of action with penalties up to $250,000 per violation.
- **AB 3030 (effective 2025):** If you use generative AI in patient communications, you must disclose that AI was involved — unless a healthcare provider reviews the communication before it reaches the patient.
- **AB 489 (effective January 2026):** Regulates AI systems that simulate interactions with licensed medical professionals. Ensures patients know they are not receiving care directly from a licensed provider.

### Texas

- **SB 1188 (effective January 2026):** Requires written disclosure to patients that AI is being used, before or on the date of service. Practitioners must personally review all AI-generated content before clinical decisions.

### Washington

- **My Health My Data Act:** Applies to all entities collecting consumer health data in Washington, regardless of HIPAA status. Requires consent for uses beyond what is necessary to provide the requested service.

### Practical Takeaway

If you practice in a state with healthcare AI disclosure requirements: **disclose.** Tell your patients you use AI tools as part of your clinical thinking process. Transparency is both a legal requirement and a trust builder. The DPC model — built on longer relationships and patient partnership — makes this disclosure natural, not adversarial.

---

## 5. FDA: Is This a Medical Device?

The FDA's January 2026 revised guidance on Clinical Decision Support (CDS) software is favorable for this use case.

AI tools that **assist clinicians** — summarizing patient data, suggesting options for independent evaluation, supporting clinical reasoning — are generally exempt from FDA device regulation when they meet the four-criteria test:

1. Not intended to acquire, process, or analyze a medical image, signal, or pattern
2. Intended for displaying, analyzing, or printing medical information
3. Intended for supporting or providing recommendations to a healthcare professional
4. Intended for enabling the healthcare professional to **independently review the basis** for recommendations

This toolchain fits squarely within the exemption. The physician provides patient data, Claude generates a strategy through the DOCTOR.md framework, and **the physician reviews, validates, and decides independently.** The AI is a thinking partner, not an autonomous diagnostician.

**Document your independent review.** Note in the patient record that AI-assisted analysis was used and that you independently evaluated and modified the recommendations. This is both good practice and a liability shield.

---

## 6. Malpractice and Liability

Two emerging liability vectors are relevant:

### Reliance Liability

If you rely on an AI recommendation that turns out to be wrong and the patient is harmed, standard negligence analysis applies. The question is whether a reasonably prudent physician would have caught the error. **The AI does not replace your clinical judgment — it augments it.** Document your reasoning, especially when you override or modify AI-generated recommendations.

### Non-Use Liability

Legal commentators have begun noting that physicians may face liability for **failing** to use available AI tools that could have improved diagnostic accuracy. This is still speculative, but the trajectory is clear: AI competency is becoming part of the standard of care.

### The DPC Advantage

DPC physicians typically have longer appointment times, deeper patient relationships, and more context than physicians operating under insurance-driven time constraints. This means:

- You are better positioned to **review AI output critically** rather than rubber-stamping it
- You have the time to **discuss AI-assisted findings with patients** and incorporate their feedback
- Your documentation can reflect genuine clinical reasoning, not box-checking

---

## 7. Practical Compliance Checklist

For a DPC physician implementing this toolchain today:

- [ ] **Determine your HIPAA status.** If you perform any electronic standard transactions, you are a covered entity. If not, document why you believe you are not.
- [ ] **Choose your data path.** De-identification (Path A) is recommended for most DPC practices. If you want to use identifiable data, pursue either patient authorization (Path B) or an API BAA (Path C).
- [ ] **Create a de-identification protocol.** Document the steps you follow to strip identifiers before data enters the AI system. Make it repeatable and auditable.
- [ ] **Draft a patient disclosure.** Inform patients that you use AI tools as part of your clinical process. In states that require it, this is mandatory. In all states, it is good practice.
- [ ] **If using patient authorization**, have a healthcare attorney draft the authorization form for your state. Do not use a generic template.
- [ ] **Document AI involvement in the medical record.** Note that AI-assisted analysis was performed and that you independently reviewed and approved the final recommendations.
- [ ] **Review state-specific requirements.** AI disclosure laws, medical privacy statutes, and medical board guidance vary by state.
- [ ] **Use the API for identifiable data, consumer Claude only for de-identified data.** Do not send PHI through consumer-tier AI products.
- [ ] **Stay current.** This landscape is evolving rapidly. Revisit your compliance posture at least annually.

---

## 8. The Confidence Case

The legal landscape is not a barrier — it is a framework. Here is why a DPC physician should feel confident adopting AI-assisted clinical strategy:

1. **De-identification is well-established law.** Stripping identifiers from patient data before AI processing is a decades-old compliance mechanism. It is not novel, experimental, or legally uncertain. The Safe Harbor method has clear, enumerated requirements. Follow them and you are on solid ground.

2. **The FDA has explicitly carved out clinical decision support.** The January 2026 guidance confirms that AI tools used to support physician decision-making — exactly what this toolchain does — are not regulated as medical devices. The physician retains independent judgment. The AI is a tool, like a reference textbook or a clinical calculator, but vastly more capable.

3. **DPC is structurally advantaged for AI adoption.** No insurance billing means potential HIPAA exemption. Longer appointments mean genuine review of AI output. Direct patient relationships mean transparent communication about how their care is informed. The DPC model was built for this moment.

4. **The standard of care is moving toward AI, not away from it.** Physicians who thoughtfully integrate AI into their practice are not taking a risk — they are staying ahead of an inevitable shift. The greater long-term liability risk is refusing to use tools that could have improved patient outcomes.

5. **Patients want this.** They want a physician who uses every available tool to understand their health. The DOCTOR.md framework — multi-perspective panel debate, evidence-grounded reasoning, actionable strategy — produces output that patients can actually use. That is the promise of DPC fulfilled.

The law does not require you to practice medicine with one hand tied behind your back. It requires you to protect patient privacy, exercise independent clinical judgment, and document your reasoning. This toolchain, properly implemented, is fully compatible with all three.

---

*Last updated: February 2026. This document reflects federal and state law as of the date of writing. Laws and regulatory guidance in this area are evolving rapidly. Consult qualified legal counsel before implementing any AI workflow involving patient data.*
