# The 30-Minute Strategy Document Your Patients Will Actually Read

### AI-Powered Health Strategy for Direct Primary Care

---

## You Became a DPC Doctor for a Reason

You left fee-for-service because you wanted to practice medicine the way it should be practiced — longer visits, deeper relationships, whole-patient thinking. No prior authorizations. No 7-minute appointments. No coding gymnastics.

But the promise of DPC comes with a trade-off you feel every day: **you are the entire clinical team.** The specialist referrals take weeks. The follow-up research happens after hours. The patient education materials are generic PDFs from 2014. And the truly integrative analysis — the kind that weighs conventional, functional, and lifestyle medicine perspectives against each other — takes time you don't have.

What if you could hand a patient profile to a system that runs that analysis for you in minutes?

---

## What This Toolchain Does

**DOCTOR.md** is a clinical strategy framework. You provide a patient profile — labs, medications, diet, lifestyle, health history — and it produces a comprehensive, personalized health strategy document.

Not a chatbot summary. Not a symptom checker. A structured clinical analysis built through a **multi-perspective panel debate** among:

- A Functional Medicine Practitioner
- A Standard Line of Care Physician
- A Direct Primary Care Provider
- A Naturopath
- A Patient Advocate representing the patient's actual goals and constraints

Plus any specialists the case warrants — endocrinology, cardiology, rheumatology — automatically added based on the clinical picture.

The output is a complete strategy document covering:

1. **Executive Summary** — the clinical picture at a glance
2. **Lab Review & Gaps** — what the labs show and what's missing
3. **Supplement Protocol** — evidence-grounded recommendations with dosing
4. **Diet & Lifestyle Plan** — tailored to where the patient actually is today
5. **Medication Optimization** — tapering strategies where appropriate, with monitoring plans
6. **Action Items & Next Steps** — a prioritized checklist the patient can follow

The document is then converted to a professionally formatted PDF that looks like it came from an integrative medicine institute — because the analysis behind it is that thorough.

---

## The Math That Matters

### Time

A comprehensive integrative analysis of a complex patient — reviewing labs, cross-referencing medications, weighing supplement interactions, building a lifestyle plan, considering multiple clinical perspectives — takes **3 to 5 hours** of focused physician time.

This toolchain produces a first draft in **under 30 minutes.** You review it, apply your clinical judgment, modify what needs modifying, and hand your patient a finished document. Total physician time: **45 minutes to an hour**, including your review.

That is 3 to 4 hours returned to your day. Per complex patient.

### Revenue

Most DPC practices charge a flat monthly membership. The patients who extract the most value — and who stay enrolled the longest — are the ones who feel their doctor is doing something no one else can.

A personalized, multi-perspective health strategy document is tangible proof of that value. It is something the patient holds in their hands, shares with their spouse, brings to specialist appointments. It justifies the membership. It drives referrals.

Some DPC practices offer strategy documents as a premium add-on service:

| Model | Structure | Price Point |
|---|---|---|
| Included in membership | Part of onboarding or annual review | Increases perceived membership value |
| Premium tier | Available to higher-tier members | Justifies $200–$400/mo premium tier |
| A la carte | Per-document fee | $250–$500 per strategy document |
| Corporate wellness | Employer-sponsored for employee panels | $150–$300 per employee |

Even at the included-in-membership tier, the retention impact alone justifies the cost. Patients who receive a strategy document have a reason to stay, a reason to comply, and a reason to refer.

### Quality

You already know more than any single specialist about your patients. You have the full picture — the labs, the medications, the diet they actually eat (not the diet they tell their cardiologist they eat), the stress, the sleep, the family history.

What you lack is **processing bandwidth.** You cannot run a five-perspective clinical debate in your head during a 30-minute appointment while also being present with the patient.

This toolchain is processing bandwidth. It takes everything you know about the patient and runs the analysis you would do if you had unlimited time. You then apply the one thing AI cannot replicate: **your clinical judgment and your relationship with the patient.**

The result is not AI-generated medicine. It is physician-directed medicine with AI-augmented analysis. There is an enormous difference.

---

## What Your Patients Experience

### Before

- A good appointment where you discuss concerns and order labs
- A follow-up where you review results and adjust medications
- Verbal recommendations they half-remember by the time they get home
- A vague sense that they should "eat better and exercise more"

### After

- The same good appointment — nothing changes about your clinical interaction
- A **20-page personalized strategy document** waiting in their inbox after the visit
- Specific supplement recommendations with dosing and rationale
- A diet plan built around their actual current eating patterns
- A medication optimization roadmap they can discuss with specialists
- A prioritized action checklist with short-term and long-term milestones
- The confidence that their doctor used every available tool to help them

The patient who receives a strategy document does not cancel their membership. They forward it to their spouse. They bring it to their endocrinologist. They tell their friends about the DPC doctor who actually gave them a plan.

---

## Addressing the Objections

### "I don't trust AI with clinical decisions."

Good — you shouldn't. And this toolchain doesn't ask you to. It produces a **draft analysis** that you review, modify, and approve before it reaches the patient. You are the physician. The AI is a research assistant that works at machine speed. Every recommendation in the final document carries your judgment, not the AI's.

### "What about patient privacy?"

The recommended workflow uses **de-identified data**. Patient names, dates of birth, addresses, and all other identifiers are stripped before the data enters the AI system. What Claude sees is a clinical profile — labs, medications, conditions — with no identifying information attached. This is the same de-identification standard that has governed health data research for decades. (See LEGAL.md for the full legal analysis.)

### "My patients will think I'm lazy."

Your patients think you're a superhero for spending 30 minutes with them instead of 7. When they receive a comprehensive strategy document that clearly required hours of analysis, they will think you're a superhero with a research team. Disclose that you use AI tools — transparency builds trust — and let the quality of the output speak for itself.

### "I can do this myself."

You can. But you don't. Not for every patient, not with this depth, and not with five competing clinical perspectives synthesized into a unified strategy. The bottleneck in DPC has never been knowledge — it's time. This removes the bottleneck.

### "What if the AI is wrong?"

It will be, sometimes. Just like UpToDate is sometimes incomplete, clinical calculators sometimes mislead, and specialist consultants sometimes disagree with your assessment. The difference is that you review the output before it reaches the patient. You catch the errors, apply your judgment, and produce a better final document than either you or the AI would produce alone.

### "This feels like it's moving too fast."

The FDA carved out clinical decision support tools from device regulation in January 2026. The FSMB has published guidance on responsible AI integration in clinical practice. Medical schools are teaching AI literacy. The question is no longer whether AI will be part of medicine — it's whether you'll adopt it thoughtfully on your terms or be forced to adopt it reactively on someone else's.

---

## How It Works in Practice

### The Workflow

```
1. Patient visit → you gather/update the patient profile
2. De-identify → strip names, DOB, and other identifiers
3. Run the toolchain → feed the profile through DOCTOR.md via Claude
4. Review → read the strategy, apply your clinical judgment, edit as needed
5. Generate PDF → run pdfize.py to produce the finished document
6. Deliver → send to the patient with a brief personal note
```

### The Stack

| Component | Role |
|---|---|
| **Patient profile** (`NAME.md`) | Structured patient data — labs, meds, diet, lifestyle, history |
| **DOCTOR.md** | The clinical strategy prompt — defines the panel, the debate format, the output structure |
| **Claude** | The AI engine — runs the multi-perspective analysis |
| **ralph** | Workflow orchestration — manages the pipeline from profile to strategy |
| **pdfize.py** | PDF generation — converts the strategy to a professionally formatted medical document via LaTeX |

### Time Investment

- **Setup:** 1–2 hours to learn the workflow and configure for your practice
- **Per patient:** 10 minutes to prepare the de-identified profile, 30 minutes for AI processing, 15–30 minutes for physician review and editing
- **Ongoing:** Zero maintenance. The prompt and tools are self-contained.

---

## The Competitive Advantage

There are approximately 2,500 DPC practices in the United States. Most of them offer the same core value proposition: more time, better access, no insurance hassle.

That value proposition is real. It is also identical across practices.

The practices that will define the next decade of DPC are the ones that use the time advantage to **do things other practices cannot.** A comprehensive, multi-perspective, professionally formatted health strategy document — produced for every complex patient, delivered within days of their visit — is something a fee-for-service practice literally cannot do. They don't have the time. You do.

This is not a gimmick. It is not a chatbot widget on your website. It is a substantive clinical tool that produces substantive clinical output. It makes your patients healthier. It makes your practice more valuable. It makes the case for DPC in terms patients can hold in their hands.

---

## Next Steps

1. **Read LEGAL.md** to understand the privacy framework and compliance requirements for your state.
2. **Review DOCTOR.md** to see the clinical strategy prompt and customize it for your practice style.
3. **Try it with a de-identified test case.** Take a complex patient, strip the identifiers, run the toolchain, and read the output. Judge the quality for yourself.
4. **Start with your most engaged patients.** The ones who ask questions, do their own research, and want a plan. They will be your best evangelists.

---

*The future of medicine is not AI replacing physicians. It is physicians who use AI replacing physicians who don't.*
