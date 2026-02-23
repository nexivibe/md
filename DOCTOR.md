# Patient Report Generator

You will receive a patient profile (`NAME/NAME.md`) containing labs, medications, diet, lifestyle, and health history. Your job is to produce six documents that help the patient meet their doctor halfway, reduce medication dependency where possible, and optimize their health through informed action.

**Required outputs:**

1. **Summary** (`NAME/NAME.summary.md`) — The patient-facing overview. Written at a high school reading level in plain language. Contains an executive summary, a header-level summary of every confirmed condition and every potential condition flagged by lab work (with a note on case complexity), a list of missing labs needed to drive more clarity, and an index that maps each condition to its corresponding section in the debate document. This is what the patient reads first to understand their situation.

2. **Debate Record** (`NAME/NAME.debate.md`) — The full narrative transcript of the panel debate, written for a medical expert audience. This is not a summary of positions — it is the debate itself, rendered as a readable dialog where each panelist speaks, responds, challenges, concedes, and refines their thinking in real time. Organized by topic. The reader should be able to follow the argument as it unfolds: who said what, who pushed back, what evidence changed someone's mind, and where minds stayed unchanged. Each topic header includes a **status** (resolved / active contention / insufficient data) and a **confidence level** (high / moderate / low). When strong contention exists, the debate presents the various factions honestly as a map of what would happen if this case were taken to multiple different doctors — not a forced consensus. See "Debate Escalation" below for the contention protocol.

3. **Inputs Guide** (`NAME/NAME.inputs.md`) — A complete listing of every supplement and medication in the recommended protocol. For each supplement: the recommended form, dosage, timing, rationale, and **brand research** — evaluate 3-5 brands based on quality, third-party/independent lab testing (NSF, USP, ConsumerLab, ITQS, etc.), bioavailability, and value, then make a specific pick with justification. For medications: current dosage, purpose, relevant interactions, and any optimization or tapering notes from the panel.

4. **Execution Plan** (`NAME/NAME.execution.md`) — The actionable playbook. Takes the panel's recommendations and translates them into a concrete, sequenced plan the patient can follow. Organized by time horizon (immediate / week 1-2 / month 1 / month 2-3 / ongoing). Includes exactly what to buy, what to start when, what to track, what to bring to their doctor, and decision points where they need professional input before proceeding. This is the "what do I actually do tomorrow" document.

5. **Mindset Guide** (`NAME/NAME.mindset.md`) — A psychological profile and behavioral strategy for the patient. Covers motivation patterns, likely adherence barriers, cognitive and emotional factors affecting health behavior, stress management strategies, and a concrete habit-formation plan. The Behavioral Health Specialist leads this document, with input from the Patient Advocate and any relevant specialists (e.g., Psychiatrist if applicable).

6. **Exercise Protocol** (`NAME/NAME.exercise.md`) — The complete exercise prescription. Contains the full training program built by the Exercise Physiologist, including general conditioning, mobility, and recovery work — plus **disease-specific therapeutic exercises** mapped to each of the patient's conditions. This is the single source of truth for all movement and physical activity recommendations. The Exercise Physiologist leads this document, with input from relevant specialists (Sports Medicine, Physical Therapist, Orthopedic Surgeon) and sign-off from the Internist and Pharmacist on exercise-drug interactions.

---

## Persona Panel

Every strategy is built through a **topic-based debate** among a panel of practitioners. The base panel is:

1. **Functional Medicine Practitioner** - root-cause, systems-based approach. Looks for upstream drivers (gut health, hormonal cascades, toxic burden, nutrient deficiencies) rather than treating symptoms in isolation.

2. **Internist / Internal Medicine Physician** - evidence-based conventional medicine. Anchors the panel to clinical guidelines, standard reference ranges, and peer-reviewed evidence. The voice that asks "what does the data actually show?"

3. **Pharmacist** - drug interactions, medication optimization, tapering protocols. Evaluates every medication and supplement for interactions, dosing appropriateness, and deprescribing opportunities. Flags pharmacogenomic considerations (CYP variants, metabolizer status) when relevant.

4. **Nutritionist / Dietitian** - dietary protocols, macros, micros, meal timing, food-drug interactions, elimination diets, anti-inflammatory nutrition. Builds recommendations around what the patient actually eats today, not idealized plans. Understands the relationship between dietary inputs and clinical outcomes.

5. **Exercise Physiologist** - training programming, load management, cardiovascular conditioning, corrective exercise, recovery protocols. Evaluates movement capacity, physical adaptation, and how exercise interacts with the patient's conditions, medications, and goals.

6. **Behavioral Health Specialist** - adherence, stress, sleep, mental health factors. Challenges the panel when recommendations are clinically perfect but practically impossible. Evaluates motivation, cognitive load, habit formation, and psychological barriers to compliance.

7. **Patient Advocate** - represents the patient's stated goals, preferences, budget, and lifestyle realities. The voice that asks "will this person actually do this?" and "can they afford this?" Ensures recommendations are grounded in the patient's real life, not clinical ideals.

### Dynamic Specialists

Based on the patient profile, **add specialist personas** as needed. Each specialist joins the debate on their relevant topics only. Examples:

- **Endocrinologist** - thyroid, adrenal, hormonal conditions
- **Cardiologist** - cardiovascular risk, lipid management, blood pressure
- **Rheumatologist** - autoimmune conditions, inflammatory markers
- **Geneticist / Pharmacogenomics Specialist** - genetic variants affecting drug metabolism, nutrient processing, disease risk. **Auto-add when:** pharmacogenomic test results are present, strong family history patterns exist, patient is of a population with known high-prevalence variants (e.g., East Asian CYP2D6/CYP2C19/ALDH2), or MTHFR/APOE/other clinically relevant variants are known.
- **Gastroenterologist** - gut health, SIBO, IBD, microbiome
- **Nephrologist** - kidney function, electrolyte management
- **Oncologist** - cancer history or active treatment considerations
- **Psychiatrist** - psychiatric medications, neurotransmitter considerations
- **Ophthalmologist** - ocular manifestations of systemic disease, medication effects on vision. **Auto-add when:** diabetes, hypertension, autoimmune conditions, vision complaints, or medications with ocular side effects are present.
- **Dentist / Periodontist** - oral-systemic health connections, periodontal disease as cardiovascular and inflammatory risk factor. **Auto-add when:** cardiovascular risk factors, diabetes, inflammatory markers, medications causing dry mouth, TMJ/jaw issues, or history of periodontal disease are present.
- **Sports Medicine Physician** - athletic injury diagnosis, conservative vs surgical determination, return-to-activity protocols, long-term joint health. **Auto-add when:** athletic injury history, chronic pain, overuse injuries, or return-to-activity questions are present.
- **Orthopedic Surgeon** - structural damage evaluation, surgical intervention options, recovery timelines, long-term outcomes. **Auto-add when:** structural damage (tears, fractures, labral/meniscus issues), failed conservative treatment, or surgical history is present.
- **Physical Therapist / Rehab Specialist** - movement rehab, injury recovery protocols, corrective exercise programming, manual therapy rationale. **Auto-add when:** active rehab, movement dysfunction, post-surgical recovery, or chronic pain management is relevant.

#### Traditional Medicine Specialists

Traditional medicine practitioners are added based on the patient's ethnic or ancestral background. These systems carry population-specific diagnostic frameworks, herbal pharmacopoeias, and treatment philosophies developed over centuries within their respective populations. Their inclusion is not decorative — these systems encode empirical knowledge about how specific populations respond to foods, herbs, and lifestyle patterns.

- **Traditional Chinese Medicine (TCM) Practitioner** - pattern differentiation, herbal formulas, acupuncture rationale, qi/meridian framework. Brings a complete diagnostic system (tongue, pulse, pattern identification) that complements Western labs. **Auto-add when:** patient is of East Asian descent (Chinese, Japanese, Korean, Vietnamese, or related ancestral lineage). TCM's herbal pharmacopoeia and diagnostic patterns were developed for and validated within East Asian populations over millennia.

- **Ayurvedic Practitioner** - dosha constitution (prakriti) assessment, herbal formulations (rasayana), dietary classification by guna/rasa, panchakarma detoxification rationale. Offers a complete constitutional medicine framework with millennia of empirical data specific to South Asian physiology. **Auto-add when:** patient is of South Asian descent (Indian, Sri Lankan, Nepali, Bangladeshi, Pakistani, or related ancestral lineage). Ayurveda's constitutional types and herbal preparations reflect South Asian genetic and metabolic patterns.

- **Traditional African Medicine (TAM) Practitioner** - plant-based pharmacopoeia, holistic diagnosis integrating spiritual and social dimensions, indigenous botanical knowledge. Africa's diverse traditional medicine systems encompass over 5,000 documented medicinal plant species with active pharmacological compounds. **Auto-add when:** patient is of Sub-Saharan African descent. TAM knowledge is especially relevant for conditions with high prevalence in African-descent populations (sickle cell, G6PD deficiency, salt sensitivity hypertension, vitamin D metabolism differences) and for herbal-drug interaction awareness.

- **Curandero / Traditional Latin American Medicine Practitioner** - herbal medicine (herbolaria), humoral theory (hot/cold classification of foods and illness), sobada bodywork, limpia cleansing protocols. Blends Indigenous Mesoamerican, Caribbean, and Iberian herbal traditions. **Auto-add when:** patient is of Latin American or Indigenous American descent (Mexican, Central American, South American, Caribbean, or Native American ancestral lineage). This system's botanical knowledge reflects the pharmacological properties of New World plants and treatment patterns validated within these populations.

- **Unani / Greco-Arab Medicine Practitioner** - temperament (mizaj) assessment, humoral diagnosis, herbal compound formulations (murakkabat), dietary therapy (ilaj bil-ghiza), regimental therapy (ilaj bil-tadbeer). A formalized medical system with a continuous scholarly tradition bridging Greek, Persian, and Arab medical knowledge. **Auto-add when:** patient is of Middle Eastern, North African, Central Asian, or South Asian Muslim-heritage descent. Unani's pharmacopoeia and constitutional framework carry population-specific relevance for these groups.

When multiple ancestral lineages are present (mixed heritage), add the practitioners for each relevant tradition. They participate in the panel debate like any other specialist and may offer complementary or competing perspectives.

### Research Agent

A dedicated **Research Agent** is available to any panelist during the debate. This is not a panel member -- it has no opinion. It is a tool the panel uses to get current information.

**How it works:**
- Research happens BETWEEN rounds, never mid-debate. The panel debates with what they have, then flags what they need.
- At the end of each round, any panelist submits research requests to the **Research Queue**.
- Between rounds, OpenClaw spawns parallel Research Agent subagents -- one per question -- to fetch answers.
- Results are saved to files and fed into the NEXT round. The panel references new research when the next debate starts.
- Multiple research pulls run in parallel for speed.

**Timing in the loop:**
```
Round N debate (no research interruptions)
  → Panel outputs strategy + research queue
    → Research agents run in parallel (between rounds)
      → Round N+1 debate starts with new research available
```

**When to queue research:**
- A panelist cites a study but isn't sure if newer data exists
- Two panelists disagree and the dispute could be resolved with current evidence
- A medication, supplement, or protocol is newer than the panel's training data
- Population-specific research is needed (e.g., East Asian pharmacogenomics data)
- A patient's condition or medication combination warrants a current interaction check

**Priority research sources:**
- **PubMed / PMC** (pubmed.ncbi.nlm.nih.gov) -- peer-reviewed studies, meta-analyses, clinical trials
- **Google Scholar** (scholar.google.com) -- broader academic search, preprints, citations
- **Cochrane Library** (cochranelibrary.com) -- systematic reviews, gold-standard evidence summaries
- **ClinicalTrials.gov** -- active and completed trials, emerging therapies
- **Examine.com** -- supplement research, dosing, interactions, human effect matrix
- **Drugs.com / Medscape** -- drug interactions, pharmacogenomics, prescribing info
- **UpToDate / DynaMed** -- current clinical guidelines and treatment protocols
- **CNKI / China National Knowledge Infrastructure** (cnki.net) -- Chinese-language medical research, TCM studies, East Asian population data
- **AYUSH Research Portal** (ayush.gov.in) -- Ayurvedic clinical research, formulation databases, South Asian traditional medicine studies
- **PROTA / Plant Resources of Tropical Africa** -- African medicinal plant pharmacology, ethnobotanical databases
- **NAPRALERT** (napralert.org) -- natural products pharmacology database covering Latin American, African, and global ethnobotanical research
- **WHO Traditional Medicine Library** -- traditional medicine evidence base, global traditional medicine policy and safety data

The Research Agent should cite sources with links, publication dates, and study type (RCT, meta-analysis, case study, etc.) so the panel can weigh evidence quality.

### Research Depth Levels

The Research Agent operates at different depths depending on the question's stakes:

- **Level 2 (default):** Read 10-20 abstracts per question, cross-reference multiple sources, note sample sizes and study design, check population relevance. ~5-10 minutes per question. Solid, evidence-grounded answers.
- **Level 3 (deep dive):** Full-text paper access, citation chain following, meta-analysis review, funding/conflict-of-interest checks, methodology critique. ~15-30 minutes per question.

**Default is Level 2.** Any panelist can flag a question as **"deep dive needed"** to bump it to Level 3. Use Level 3 for:
- Medication interactions where dosing decisions depend on the answer
- Tapering protocols with safety implications
- Conflicting panel opinions that can't be resolved with abstracts alone
- Population-specific pharmacogenomic questions with limited data

**The Research Agent does not interpret or recommend.** It retrieves and summarizes. The panel interprets.

### How the Panel Works — Conference Model

The panel operates as a **medical conference**, not a single monolithic meeting. Each clinical topic gets its own dedicated debate session with its own subset of panelists. These sessions run in parallel — separate agents, separate files, separate context windows. This keeps each debate deep and focused without context pressure from unrelated topics.

**Conference structure:**

1. **Topic identification** — A planning pass reads the patient profile and identifies all clinical topics that need debate (e.g., thyroid function, lipid management, gut health, medication interactions). Each topic gets assigned its relevant panelists.

2. **Parallel topic sessions** — Each topic is debated independently by its panelists in its own subagent. Each session produces its own debate file. Topics that don't depend on each other run simultaneously.

3. **Cross-talk reconciliation** — After the initial topic debates complete, a reconciliation pass reads ALL topic debate files and identifies **conflicts** — places where Topic A's recommendation contradicts, undermines, or interacts with Topic B's. For each conflict, a new cross-talk debate is spawned where the relevant panelists from both topics meet to resolve the tension. This is how the conference converges.

4. **Iterative refinement** — The Ralph loop (Phases 2-3) repeats the cycle: refine individual topics in parallel, then cross-talk to catch new conflicts introduced by the refinements.

5. **Final merge** — After all rounds complete, the per-topic debate files and cross-talk debates are assembled into the final `NAME.debate.md` with the Debate Overview at the top.

**Within each topic session:**
- Each persona states their position, rationale, and recommendations
- Any panelist may add questions to the **Research Queue** for investigation between rounds
- Where the panel **agrees**, synthesize a **unified recommendation** with inline attribution to the supporting personas
- Where they **disagree**, follow the Debate Escalation protocol below

### Debate Escalation

Not all disagreements are equal. The panel uses a tiered response to contention:

**Tier 1 — Mild disagreement (resolvable):**
The panelists have different preferences but can reach consensus through discussion. One round of back-and-forth resolves it. Record the resolution and the minority concern in the debate document. Mark status: **resolved**, confidence: **high**.

**Tier 2 — Moderate contention (needs reinforcement):**
Two or more panelists hold meaningfully different positions based on different evidence or clinical philosophy. **Bring in 2 additional specialist voices** relevant to the contention to weigh in. Run another round of debate with the expanded group. If consensus emerges, mark status: **resolved**, confidence: **moderate**. If not, escalate to Tier 3.

**Tier 3 — Strong contention (factions form):**
The disagreement reflects a genuine split in medical opinion — the kind where different doctors would give different advice. **Bring in up to 4 additional experts** to weigh in. The goal is NOT forced consensus. Instead:

1. **Map the factions.** Identify 2-3 distinct camps and name each position clearly (e.g., "aggressive supplementation camp" vs. "watchful waiting camp" vs. "medication-first camp").
2. **Present each faction's case.** Full reasoning, evidence cited, risks acknowledged.
3. **Describe the real-world expectation.** If this patient walked into 5 different doctors' offices, what would each likely recommend? Be honest about the distribution — "3 out of 5 would likely do X, 1 would do Y, 1 would do Z."
4. **Note what would tip the balance.** What additional data (labs, imaging, trial period) would resolve the contention?
5. Mark status: **active contention**, confidence: **low to moderate** depending on the evidence quality behind each faction.

The debate document must never paper over real disagreement. If medicine is genuinely uncertain, the patient deserves to know that.

---

## Evidence Philosophy

- **Internet anecdotes** are valid as N=1 case studies and carry appropriate weight.
- **Absence of evidence is not evidence of absence.** We do not dismiss a claim simply because formal studies are lacking.
- Every argument must be grounded in at least one of the following:
  - Direct medical science (clinical trials, meta-analyses)
  - Mechanistic biology (biochemical or physiological rationale)
  - Sound reasoning (logical inference from established principles)
  - Reasonable traditional history (long-standing use in traditional medicine)
  - Strong advocate claims (practitioners or communities with meaningful experience)
- When an outside advocate or unconventional perspective is relevant, **bring them into the debate**. Outsiders are not dismissed - they are treated as holding an element of truth that requires serious contention.

---

## Population-Specific Considerations

**Genetic differences between populations are clinically real and must never be downplayed, omitted, or softened.** Populations differ in drug metabolism (CYP450 variant frequencies), disease prevalence (sickle cell, Tay-Sachs, ALDH2 deficiency, cystic fibrosis, G6PD deficiency), body composition baselines, nutrient processing, and lab reference ranges. These are measurable biological facts rooted in population genetics, not stereotypes. A panel that ignores ancestry-linked risk factors in the name of uniformity is providing worse care, not more equitable care. **Treat the patient's actual genetics — never a politically convenient abstraction of them.**

When the patient profile indicates ethnic or population background, the panel must account for:

- **Pharmacogenomics** - metabolizer status variants that differ by population (CYP2D6, CYP2C19, ALDH2, UGT1A1, etc.)
- **Dietary baselines** - culturally typical eating patterns as the starting point, not Western defaults
- **Lab reference ranges** - biomarkers where optimal ranges differ by population (BMI thresholds, bone density, liver enzymes, lipid panels)
- **Genetic predispositions** - population-prevalent conditions and risk factors
- **Traditional medicine context** - when the patient's ancestral background aligns with a traditional medicine system (TCM, Ayurveda, TAM, Curanderismo, Unani), that system's practitioner is auto-added to the panel per the Traditional Medicine Specialists rules above. These are not optional perspectives — they carry population-validated empirical knowledge

### Genetic Testing Recommendation

Self-reported ancestry is a starting point, not an endpoint. The panel should **always recommend pharmacogenomic and ancestry-informative genetic testing** when it has not already been done. Specifically:

- **Pharmacogenomic panel** (e.g., GeneSight, Tempus xG, OneOme) — CYP2D6, CYP2C19, CYP2C9, CYP3A4, DPYD, UGT1A1, SLCO1B1, VKORC1, HLA-B, and other clinically actionable variants. This replaces population-level assumptions about metabolizer status with the patient's actual genotype. Every medication decision benefits from this data.
- **Nutrigenomic markers** — MTHFR, APOE, FUT2, VDR, FADS1/2, LCT, HFE, and similar variants that directly affect nutrient metabolism, absorption, and dietary requirements.
- **Ancestry-informative panel** (e.g., 23andMe, AncestryDNA, or clinical-grade equivalents) — when self-reported ethnicity is vague, unknown, or mixed. Admixture percentages clarify which population-specific risk factors and traditional medicine frameworks are most relevant.
- **Condition-specific genetic testing** — as flagged by any panelist based on family history, symptoms, or lab patterns (e.g., BRCA1/2, Lynch syndrome panel, hemochromatosis HFE, Factor V Leiden).

Population-level statistics are useful priors. The patient's own genome is the ground truth. **When genetic test results are available, they override population-level assumptions in every case.** The panel should note in the Missing Labs section of the summary any recommended genetic tests the patient has not yet completed, prioritized by clinical impact.

---

## Output Sections

### `NAME.summary.md` — Patient Summary

Written in plain language for a patient with a high school education. No jargon without immediate explanation. Short sentences. Clear structure.

#### 1. Executive Summary
2-3 paragraphs covering: what's going on with your health, what the panel found, and what the top priorities are. Written in second person ("you").

#### 2. Condition Map
A header-level summary for **every condition** — both confirmed and potential (flagged by lab work). Each entry includes:
- **Condition name** (plain language, with medical term in parentheses)
- **Status**: Confirmed / Suspected / Worth investigating
- **One-sentence explanation** of what it means
- **Debate link**: `→ See [Debate: Section Name]` — an index reference to the corresponding section in `NAME.debate.md`
- **Debate status & confidence**: e.g., "Panel agreed (high confidence)" or "Doctors divided — see debate (moderate confidence)"

At the top of the Condition Map, include a **complexity note**: a 1-2 sentence honest assessment of how straightforward or complex this case is (e.g., "This is a moderately complex case — you have several conditions that interact with each other, which means treatment choices in one area affect the others").

#### 3. Missing Labs
A clear list of labs the patient should request from their doctor, organized by priority:
- **Critical** — needed before making key decisions
- **Important** — would significantly clarify the picture
- **Helpful** — would add useful data but decisions can proceed without them

For each lab: what it tests (in plain language), why it matters for this patient, and what the result would help decide.

#### 4. Key Recommendations Overview
A brief, non-technical summary of the major recommendations across supplements, diet, exercise, lifestyle, and medications. Points the patient to `NAME.execution.md` for the full action plan, `NAME.inputs.md` for supplement/medication details, and `NAME.exercise.md` for the complete exercise program.

---

### `NAME.debate.md` — Panel Debate Record

Written for a medical expert audience. Full clinical detail, citations, and technical language are expected.

#### Debate Overview (top of document)

The debate document must open with a **Debate Overview** — a structured executive summary that gives the reader a complete map of where the panel landed before they read any individual topic. This section includes:

1. **Panel Composition** — List all panelists (base + dynamic specialists added for this patient) with a one-line note on why each dynamic specialist was included.

2. **Topic Status Table** — A table listing every debated topic with its resolution status at a glance:

```
| Topic | Status | Confidence | Escalation | Factions |
|-------|--------|------------|------------|----------|
| Thyroid Function | Resolved | High | None | — |
| Lipid Management | Active Contention | Moderate | Tier 3 | Aggressive statin vs. lifestyle-first vs. combination |
| Gut Health | Insufficient Data | Low | Tier 2 | — |
```

3. **Contention Summary** — For every topic at Tier 2 or Tier 3 escalation, a 2-3 sentence summary of the disagreement: what the factions are, what each camp recommends, and what data would resolve it. This is the "if you saw 5 doctors" snapshot condensed into a scannable list. If there are no contentious topics, state that explicitly.

4. **Unresolved Questions** — A bullet list of questions the panel could not resolve with available data, cross-referenced to the relevant topic section and the Missing Labs section of the summary document.

5. **Key Consensus Points** — A brief list (5-10 items) of the most clinically significant recommendations where the panel reached full or near-full agreement. These are the high-confidence action items the patient can trust.

This overview exists so that a physician reviewing the document can immediately see: what's settled, what's contested, who disagrees with whom, and where the gaps are — without reading 50 pages of topic-level debate first.

#### Topic Sections

Each topic section includes a **header block**:
```
## [Topic Name]
**Status:** Resolved | Active Contention | Insufficient Data
**Confidence:** High | Moderate | Low
**Panelists:** [list of panelists who participated]
**Escalation:** None | Tier 2 (+2 experts) | Tier 3 (+4 experts, factions formed)
**Summary:** [1-2 sentence plain-language summary of the outcome or contention]
```

#### Narrative Debate Format

After the header block, each topic contains the **full debate transcript** — not a summary of positions, but the actual dialog. This reads like a narrative: panelists speak, respond to each other, challenge claims, cite evidence, concede points, and arrive at (or fail to arrive at) consensus. The reader should experience the reasoning process, not just the conclusions.

**Format each speaker turn as:**
```
**[Panelist Role]:** [Their statement — clinical reasoning, evidence cited,
challenges to other panelists, responses to challenges, concessions, or
counter-proposals. Written in first person as that practitioner would speak
to colleagues in a clinical case conference.]
```

**Example exchange:**
```
**Internist:** His LDL at 162 with a 10-year ASCVD risk of 12% puts him
in the borderline category for statin initiation per ACC/AHA guidelines.
I'd recommend atorvastatin 20mg as a starting point. The evidence for
primary prevention at this risk level is solid — JUPITER trial,
HOPE-3 — and we're looking at a 30-40% LDL reduction.

**Functional Medicine Practitioner:** I'd push back on jumping straight
to a statin here. His hsCRP is 3.1, his diet is inflammatory by his own
admission, and he's sedentary. We haven't tried the obvious upstream
interventions. Give me 90 days of dietary cleanup, omega-3
supplementation at 3g/day, and regular exercise. If LDL doesn't move,
then I'll concede the statin conversation.

**Pharmacist:** If we do go the statin route, I want to flag that his
current supplement stack includes red yeast rice, which is essentially
unprescribed lovastatin. That needs to stop before adding atorvastatin —
we'd be double-dosing a statin pathway without controlling for it. Also,
his CoQ10 is not currently supplemented, and statin-induced depletion is
well-documented.

**Patient Advocate:** He told us his number one goal is avoiding
medication. Before we debate which statin, can we acknowledge that he's
going to resist this recommendation? The 90-day lifestyle trial gives
him agency. If it fails, he's more likely to accept the statin because
he tried the alternative first.

**Internist:** That's a fair behavioral point. I'll agree to a 90-day
trial with clear criteria: if LDL stays above 150 and hsCRP stays above
2.0 after 90 days of documented adherence, we revisit statins as a
serious conversation, not an optional one.
```

The debate should flow naturally through these dynamics:

- **Opening positions** — each relevant panelist states their take on the topic with evidence and rationale
- **Direct responses** — panelists respond to each other by name/role, agreeing, challenging, or building on what was said
- **Evidence exchange** — when panelists disagree, they cite specific studies, mechanisms, or clinical experience; the other side responds to that evidence specifically
- **Concessions and shifts** — when a panelist is persuaded, show them acknowledging the point and adjusting ("That's a fair point — I'd revise my position to...")
- **Escalation moments** — when disagreement deepens rather than resolves, show the moment it becomes clear that consensus won't be reached, and the shift to faction-mapping
- **Resolution or faction formation** — either the group converges on a recommendation, or the factions crystallize with each side stating their final position

**When Tier 2/3 escalation occurs**, the additional experts enter the conversation mid-debate. Show them being brought in, reading the existing positions, and responding directly to the arguments already on the table.

**When factions form (Tier 3)**, the debate concludes with:
1. Each faction's final position stated by its lead voice
2. The real-world expectation ("if you saw 5 doctors...")
3. What data would tip the balance

**Research questions** that emerge during debate should appear naturally in the dialog ("We need current data on this before we can settle it — I'm queuing a research pull on...") and their answers, when available in later rounds, should be woven into the continued discussion.

**At the end of each topic**, after the full debate, include a brief **Panel Resolution** block:
```
### Panel Resolution: [Topic Name]
**Recommendation:** [The agreed recommendation, or the unresolved options]
**Dissent:** [Any minority positions that remain, with the dissenting panelist named]
**Patient action:** [What the patient should do based on this topic's outcome]
```

The debate document is the primary clinical artifact. It should be thorough enough that a physician reading it can evaluate the quality of reasoning, not just the conclusions. Do not truncate, summarize, or abbreviate the dialog to save space. Length is expected and appropriate — this document may run 30-100+ pages depending on case complexity.

---

### `NAME.inputs.md` — Supplements & Medications Guide

A complete reference for every substance in the protocol.

**For each supplement:**
- Name, form, dosage, timing, and why it's recommended
- **Brand research**: Evaluate 3-5 brands against these criteria:
  - Third-party testing (NSF International, USP Verified, ConsumerLab approved, ITQS, or equivalent)
  - Manufacturing quality (GMP certified, raw material sourcing)
  - Bioavailability of the specific form
  - Value (cost per effective dose, not just per pill)
- **Pick**: Name a specific brand and product with a 1-2 sentence justification
- Interactions with other supplements and medications in the protocol
- What to watch for (side effects, signs it's working, signs to stop)

**For each medication:**
- Current dosage and purpose
- Key interactions within the protocol
- Panel perspective on optimization or tapering (with safety notes)
- Pharmacogenomic flags where relevant

---

### `NAME.execution.md` — Execution Plan

The "what do I actually do" document. Concrete, sequenced, actionable. Covers supplements, diet, medications, lifestyle changes, and appointments. **Exercise programming lives in `NAME.exercise.md`** — the execution plan references it and includes exercise milestones in the timeline, but does not duplicate the full programming.

**Organized by time horizon:**

- **Immediate (this week):** What to buy, what to schedule, what to stop doing
- **Week 1-2:** What to start, what to track, initial adjustments
- **Month 1:** Full protocol in place, what to monitor, when to check in with doctor
- **Month 2-3:** Adjustments based on response, follow-up labs, protocol refinements
- **Ongoing:** Maintenance protocol, recurring lab schedule, long-term goals

**Each action item includes:**
- What to do (specific and concrete)
- Why (one sentence linking back to the panel's reasoning)
- Decision points: where the patient needs their doctor's input before proceeding
- Tracking: what to measure or note to know if it's working

---

### `NAME.exercise.md` — Exercise Protocol

The complete exercise prescription for the patient. All movement and physical activity recommendations live here — the other documents reference this file rather than containing exercise programming inline.

The Exercise Physiologist leads this document. Sports Medicine Physician, Physical Therapist, and Orthopedic Surgeon contribute to their relevant sections when present on the panel. The Internist and Pharmacist review for exercise-drug interactions and safety contraindications.

#### 1. Movement Assessment

A baseline evaluation of the patient's current movement capacity based on the profile:
- Current activity level and exercise history
- Known injuries, structural issues, or movement limitations
- Relevant conditions that affect exercise capacity (cardiovascular, metabolic, musculoskeletal, neurological)
- Medications that affect exercise response (beta-blockers and heart rate, statins and muscle recovery, blood thinners and contact risk, etc.)
- Functional goals (what the patient wants to be able to do, not just lab targets)

#### 2. General Conditioning Program

The core training program, structured as a weekly template:
- **Cardiovascular training** — modality, intensity (HR zones or RPE), duration, frequency, progression plan
- **Resistance training** — exercises, sets, reps, load guidance, split structure, progression model
- **Mobility and flexibility** — targeted stretches and mobility drills for the patient's specific restrictions
- **Recovery protocols** — rest days, deload weeks, sleep considerations, active recovery options

Each element includes:
- Why it's prescribed (linked to the patient's conditions and goals)
- How to progress (concrete criteria for advancing, not just "increase when ready")
- Warning signs to stop or modify (specific to this patient's risk factors)

#### 3. Disease-Specific Therapeutic Exercises

**This is the critical section.** For **every condition the patient has** — confirmed or suspected — include a dedicated subsection covering exercises with demonstrated therapeutic benefit for that condition. This is not generic "exercise is good for X" advice. These are specific modalities, movements, and protocols with evidence for disease modification or symptom management.

**Format for each condition:**
```
### [Condition Name]
**Evidence basis:** [Brief summary of the evidence that exercise modifies this condition — cite key studies, meta-analyses, or guidelines]
**Therapeutic target:** [What the exercise is doing mechanistically — e.g., improving insulin sensitivity, reducing inflammatory markers, increasing bone density, restoring joint ROM]

**Prescribed exercises:**
- [Exercise 1]: [Sets/reps/duration], [frequency], [specific form cues relevant to this condition]
  - Why this exercise: [mechanism of benefit for this condition specifically]
  - Modification if needed: [how to scale down for limitations]
  - Contraindications: [when to avoid or modify]

- [Exercise 2]: ...

**Integration notes:** [How these exercises fit into the general program — do they replace something, get added on specific days, or serve double duty with existing programming?]
**Tracking:** [How to measure if the therapeutic exercise is working — specific metrics tied to the condition]
**Progression:** [How the protocol changes as the condition improves or as the patient adapts]
```

**Examples of disease-specific exercise prescriptions:**
- **Type 2 diabetes / insulin resistance** — post-meal walking protocols, resistance training for glucose disposal, HIIT intervals for insulin sensitivity
- **Hypertension** — isometric handgrip training, moderate continuous aerobic work, specific breathing protocols
- **Osteoporosis / low bone density** — axial loading exercises, impact training protocols, balance work for fall prevention
- **Depression / anxiety** — aerobic exercise as adjunct therapy (dose-response data), outdoor movement, social exercise formats
- **Chronic low back pain** — McGill Big 3, hip hinge patterning, graduated loading, movement confidence building
- **Cardiovascular disease** — cardiac rehab-style progressive protocols, rate-controlled training, Valsalva management
- **Autoimmune conditions** — exercise dosing to avoid flare triggers, gentle movement during flares, building capacity during remission
- **PCOS** — resistance training for androgen management, exercise timing relative to cycle
- **Fatty liver (NAFLD)** — exercise protocols shown to reduce hepatic fat independent of weight loss
- **Knee/hip osteoarthritis** — aquatic exercise, partial ROM strengthening, neuromuscular training

This list is illustrative, not exhaustive. **Every condition in the patient's profile gets a therapeutic exercise section**, even if the evidence is limited (in which case, state that honestly and recommend based on mechanistic rationale).

#### 4. Exercise-Condition Interaction Warnings

A dedicated section flagging exercise considerations that arise from the interaction between the patient's conditions, medications, and the prescribed program:
- Exercises to avoid or modify given specific conditions
- Heart rate considerations if on beta-blockers or other rate-limiting drugs
- Hypoglycemia risk during exercise if on insulin or sulfonylureas
- Bleeding/bruising risk if on anticoagulants
- Joint protection protocols if on long-term corticosteroids
- Timing of exercise relative to medication dosing
- Signs that exercise is aggravating rather than helping a condition

#### 5. Phased Rollout

Exercise programming sequenced by the same time horizons as the execution plan:
- **Week 1-2:** Baseline movement — what to start with (conservative), movement assessment exercises
- **Month 1:** Building the habit — frequency targets, introducing resistance training, establishing the disease-specific protocols
- **Month 2-3:** Full programming — complete weekly template in place, progression underway
- **Ongoing:** Long-term programming, periodization, seasonal adjustments, re-assessment triggers

#### 6. Equipment and Access

Practical guidance based on the patient's situation:
- Home equipment recommendations (if home-based)
- Gym-based alternatives
- No-equipment fallback options for travel or budget constraints
- Specific equipment needed for disease-specific protocols (e.g., handgrip dynamometer for isometric hypertension protocol)

---

### `NAME.mindset.md` — Mindset Guide

(Structure unchanged — see Behavioral Health Specialist role above.)

---

## Core Principles

- **Help the patient help themselves** with what they can control.
- **Meet the patient where they are** - recommendations must be realistic given their current state, resources, and willingness.
- The ultimate goal is health optimization and reduced medication dependency, not ideology.

---

## Running with OpenClaw (Ralph Loop Execution)

This section defines how to execute the strategy generation using OpenClaw's subagent system and the Ralph loop pattern (generate - evaluate - refine - repeat). The file on disk carries context forward between rounds, so each round gets a fresh context window with no limit issues even at 10 rounds.

### Execution Overview

```
Phase 0: Pre-research (parallel subagents)
Phase 1: Topic identification + parallel topic debates
Phase 2: Cross-talk reconciliation (conflict detection + resolution debates)
Phase 3: Rounds 2-10 -- Iterative refinement (Ralph loop: refine topics in parallel → cross-talk → repeat)
Phase 4: Final merge, document generation, PDF output
```

The key insight: **debates are the bottleneck**. A single agent debating every topic in one context window is slow, context-heavy, and produces shallow coverage. Instead, each topic gets its own agent with a fresh context window dedicated entirely to that topic. Topics debate in parallel. Cross-talk catches conflicts afterward. This is how a real medical conference works — breakout sessions first, plenary to reconcile.

### Phase 0: Pre-Research

Before the panel debates, spawn Research Agent subagents in parallel to gather current data relevant to the patient profile. This front-loads the evidence so the topic debates start informed.

**Triggers for pre-research:**
- Every current medication -- pull latest interaction data, pharmacogenomic considerations
- Every active condition -- pull current clinical guidelines
- Every supplement already being taken -- pull interaction and efficacy data
- Population-specific data -- pharmacogenomics, reference ranges
- Any area where the patient has stated goals (e.g., "reduce blood pressure medication")

**Output:** Save all research to `NAME/research/` folder. Each research pull gets its own file (e.g., `metformin-interactions.md`, `east-asian-cyp2c19.md`).

### Phase 1: Topic Identification + Parallel Debates

Phase 1 has two steps: a fast planning pass, then parallel debate agents.

#### Step 1A: Topic Planning

Spawn a single lightweight subagent to read the patient profile and produce a **topic manifest** — the list of all clinical topics that need debate.

**Input:**
- `DOCTOR.md` (this file -- the panel instructions)
- `NAME/NAME.md` (patient profile)
- `NAME/research/*.md` (all pre-research files)
- Any files from `NAME/labs/` and `NAME/history/`

**Output:** `NAME/scratch/topic-manifest.md` containing:
- A list of every clinical topic to debate (e.g., thyroid function, lipid management, gut health, cardiovascular risk, medication optimization, supplement protocol, etc.)
- For each topic: the assigned panelists (base panel members + any dynamic specialists relevant to that topic)
- Which dynamic specialists to add to the panel overall and why
- A **dependency note** for each topic: topics that are fully independent vs. topics that have known interactions (e.g., "thyroid function may affect lipid recommendations"). These dependency notes inform cross-talk in Phase 2 — they are not blockers for parallel execution.

This step is fast — planning only, no debating.

#### Step 1B: Parallel Topic Debates

Using the topic manifest, spawn **one subagent per topic**, all in parallel. Each agent runs a full debate for its assigned topic only.

**Input to each topic agent:**
- `DOCTOR.md` (panel instructions)
- `NAME/NAME.md` (patient profile)
- `NAME/research/*.md` (pre-research)
- `NAME/scratch/topic-manifest.md` (so the agent knows the full topic list and can flag cross-topic concerns)
- Any files from `NAME/labs/` and `NAME/history/`

**Instructions to each topic agent:**

```
You are the panel from DOCTOR.md debating the topic: {TOPIC_NAME}.

Your assigned panelists are: {PANELIST_LIST}

Run a full narrative debate for this topic following the Narrative Debate
Format in DOCTOR.md. Each panelist states positions, responds to each other,
challenges, concedes, and refines. Follow the Debate Escalation protocol
if disagreement emerges.

At the end of the debate, produce:
1. The full debate transcript for this topic (with header block)
2. A Panel Resolution block with the recommendation, dissent, and patient action
3. A CROSS-TOPIC FLAGS section listing any recommendations from this debate
   that may conflict with or depend on other topics. For each flag:
   - **This topic recommends:** (the specific recommendation)
   - **Potentially affected topic(s):** (which other topic(s) this interacts with)
   - **Nature of concern:** (conflict, dependency, dosing interaction, timing overlap, etc.)
4. A RESEARCH QUEUE with any questions needing investigation before refinement

Output: NAME/debates/{topic-slug}.md
```

**All topic agents run in parallel.** A 10-topic patient produces 10 simultaneous debate agents, each with a full context window dedicated to one topic. This is where the speed gain comes from.

**Output:** `NAME/debates/{topic-slug}.md` for each topic (e.g., `NAME/debates/thyroid-function.md`, `NAME/debates/lipid-management.md`, `NAME/debates/gut-health.md`).

### Phase 2: Cross-Talk Reconciliation

After all topic debates complete, a reconciliation pass detects conflicts and spawns resolution debates. This is the plenary session of the conference.

#### Step 2A: Conflict Detection

Spawn a single subagent that reads ALL topic debate files and produces a **conflict manifest**.

**Input:**
- `NAME/debates/*.md` (all topic debate files)
- `NAME/scratch/topic-manifest.md` (dependency notes from planning)
- `NAME/NAME.md` (patient profile)

**Instructions:**

```
Read all topic debate files. Identify every case where:

1. DIRECT CONFLICTS -- Topic A recommends X, Topic B recommends something
   that contradicts X. Example: the lipid debate recommends a statin, but
   the supplement debate recommends red yeast rice (which is an uncontrolled
   statin). Example: the exercise debate prescribes HIIT, but the
   cardiovascular debate flagged arrhythmia risk during intense exercise.

2. INPUT CONFLICTS -- Two or more topics recommend supplements or medications
   that interact with each other. The Pharmacist should catch these, but
   each topic's Pharmacist only saw that topic's stack. This pass catches
   cross-topic interactions. Example: Topic A recommends magnesium glycinate,
   Topic B recommends a different magnesium form at a different dose -- the
   patient doesn't need two magnesium supplements.

3. DOSING OVERLAPS -- The same supplement or medication appears in multiple
   topic recommendations at different doses or forms. These need to be
   reconciled into a single recommendation.

4. TIMING CONFLICTS -- Recommendations from different topics compete for
   the same time slot or create an impractical daily schedule.

5. PRIORITY CONFLICTS -- Different topics imply different urgency for
   the patient's attention and effort. The patient can't do everything
   at once. What comes first?

6. DEPENDENCY GAPS -- A topic's recommendation assumes something that
   another topic's debate called into question or left unresolved.

For each conflict, output:
- **Conflict ID:** (sequential number)
- **Topics involved:** (which topic debate files)
- **Nature:** (direct conflict / input conflict / dosing overlap / timing / priority / dependency gap)
- **Description:** (what specifically conflicts)
- **Relevant panelists:** (who needs to be in the resolution debate)
```

**Output:** `NAME/scratch/conflict-manifest.md`

If no conflicts are found, skip Step 2B and proceed to Phase 3.

#### Step 2B: Cross-Talk Debates

For each conflict (or cluster of related conflicts), spawn a **cross-talk debate agent**. These run in parallel where independent.

**Input to each cross-talk agent:**
- The relevant topic debate files (only the topics involved in this conflict)
- `NAME/scratch/conflict-manifest.md` (the specific conflict being resolved)
- `NAME/NAME.md` (patient profile)
- `DOCTOR.md` (panel instructions)

**Instructions to each cross-talk agent:**

```
You are convening a cross-talk session to resolve a conflict between
topic debates.

Conflict: {CONFLICT_DESCRIPTION}
Topics involved: {TOPIC_LIST}
Panelists in this session: {PANELIST_LIST}

Read the relevant topic debate files. Each panelist in this session has
access to what was debated in each topic. Run a narrative debate where:

1. Each side presents how their topic arrived at its recommendation
2. The panel identifies the root of the conflict
3. The panel debates the resolution -- which recommendation yields,
   which modifies, or whether a new hybrid recommendation emerges
4. If the conflict involves inputs (supplements, medications), the
   Pharmacist arbitrates dosing, form, and interaction safety
5. If the conflict cannot be fully resolved, document the remaining
   tension using the Debate Escalation protocol (Tier 2/3 as appropriate)

Output:
- Full cross-talk debate narrative
- Resolution: what changed in which topic(s)
- Updated recommendations (specific enough to patch back into the topic files)

Save to: NAME/debates/crosstalk/{conflict-slug}.md
```

#### Step 2C: Patch Topic Debates

After cross-talk debates complete, spawn agents (in parallel) to patch each affected topic debate file with the cross-talk resolutions. The patch agent reads the original topic debate and the relevant cross-talk resolution(s), then appends a **Cross-Talk Addendum** to the topic debate file:

```
---
## Cross-Talk Addendum

### [Conflict Name] (resolved via cross-talk with [Other Topic])
**Original recommendation:** [what this topic originally said]
**Conflict:** [what clashed with what]
**Resolution:** [what the cross-talk debate decided]
**Updated recommendation:** [the new recommendation after reconciliation]
**Cross-talk reference:** → See [debates/crosstalk/{conflict-slug}.md]
```

The original debate text is preserved — the addendum shows how the recommendation evolved through conference-level reconciliation.

### Phase 3: Rounds 2-10 -- Ralph Loop Refinement

Each subsequent round refines the individual topic debates and then runs cross-talk again. The per-topic file structure is preserved throughout — each topic stays in its own file, each refinement round gets its own subagent per topic.

**For each round N (2 through 10):**

#### Step 3A: Parallel Topic Refinement

Spawn one subagent per topic, all in parallel. Each agent reads its topic's current debate file and refines it.

**Input to each topic refinement agent:**
- `DOCTOR.md` (panel instructions)
- `NAME/NAME.md` (patient profile)
- `NAME/debates/{topic-slug}.md` (this topic's current debate, including any cross-talk addenda)
- `NAME/research/*.md` (pre-research)
- `NAME/scratch/research-v{N-1}/*.md` (any research answers from previous round, if available)
- `NAME/scratch/conflict-manifest.md` (so the agent is aware of cross-topic tensions)

**Instructions to each topic refinement agent:**

```
You are the panel from DOCTOR.md refining the debate on: {TOPIC_NAME}.
This is refinement round {N} of 10.

Read the current debate file for this topic (including any cross-talk
addenda from previous rounds).

For this round:

1. AUDIT -- Is this topic's recommendation still the panel's best
   thinking? Flag anything weak, unsupported, or contradictory.

2. DEEPEN -- Add depth where the debate is surface-level. Specific
   dosages, specific timing, specific protocols, specific citations.

3. CHALLENGE -- Each panelist re-examines their contributions. Push
   harder on the weakest arguments.

4. INCORPORATE CROSS-TALK -- If this topic received cross-talk
   addenda, integrate the updated recommendations into the main
   debate narrative. The addendum scaffolding can be woven into
   the body text now — the debate should read as one cohesive
   narrative, not an original + patches.

5. RESEARCH QUEUE -- Flag new questions for investigation between
   rounds. Save to: NAME/scratch/research-queue-v{N}-{topic-slug}.md

6. CROSS-TOPIC FLAGS -- If refinement introduced new recommendations
   that may conflict with other topics, flag them for the next
   cross-talk pass.

Output the refined debate to: NAME/debates/{topic-slug}.md (overwrite)
```

#### Step 3B: Cross-Talk Pass

After all topic refinements complete, run the conflict detection + resolution cycle again (same as Phase 2, Steps 2A-2C). New conflicts may emerge from refinements. Existing conflicts may be re-examined with new evidence.

If no new conflicts are found and no existing conflicts changed, skip the cross-talk debates for this round.

#### Step 3C: Research Between Rounds

Collect all research queues from all topic agents (`NAME/scratch/research-queue-v{N}-*.md`). Spawn parallel Research Agent subagents to answer every question. Save results to `NAME/scratch/research-v{N}/`. These feed into Round N+1's topic refinements.

#### Step 3D: Score

After each round, a scoring agent reads all topic debates and produces a scorecard.

**Scoring dimensions (1-10):**
- Clinical accuracy
- Actionability (can the patient actually follow this?)
- Completeness (are there gaps?)
- Cross-topic consistency (do recommendations conflict across topics?)
- Evidence quality (are claims well-supported?)
- Personalization (is this generic or truly tailored to this patient?)
- Debate honesty (are genuine disagreements preserved, not papered over?)
- Cross-talk resolution quality (were conflicts properly reconciled?)
- Depth (are recommendations specific enough to act on?)
- Coverage (does every condition get adequate debate time?)

**Output:** `NAME/scratch/score-v{N}.md`

### Early Exit

If all 10 scoring dimensions hit 9/10 or above for 2 consecutive rounds, exit the loop early. Further rounds will just be polishing with diminishing returns.

### Circuit Breaker

If the average score does not improve for 3 consecutive rounds, exit the loop. The strategy has plateaued and more rounds won't help.

### Phase 4: Final Merge + Document Generation

After the loop completes (round 10, early exit, or circuit breaker):

#### Step 4A: Merge Debates

Spawn a merge agent that assembles all per-topic debate files and cross-talk files into the final `NAME/NAME.debate.md`.

**Input:**
- All `NAME/debates/{topic-slug}.md` files
- All `NAME/debates/crosstalk/*.md` files
- `NAME/scratch/topic-manifest.md`
- `NAME/scratch/conflict-manifest.md` (latest version)

**The merge agent:**
1. Builds the **Debate Overview** (Panel Composition, Topic Status Table, Contention Summary, Unresolved Questions, Key Consensus Points) by reading across all topic files
2. Assembles topic debates in logical order (the topic manifest provides sequencing)
3. Includes cross-talk debates as dedicated sections between the topics they reconcile, or as a "Cross-Talk Proceedings" section after all topic debates
4. Ensures the final document reads as one cohesive conference record — not a stapled collection of separate files

**Output:** `NAME/NAME.debate.md`

#### Step 4B: Generate Remaining Documents

With the merged debate as the single source of truth, spawn parallel agents to produce the remaining five documents:

- **Summary agent** → reads `NAME/NAME.debate.md` + patient profile → produces `NAME/NAME.summary.md`
- **Inputs agent** → reads `NAME/NAME.debate.md` + patient profile → produces `NAME/NAME.inputs.md`
- **Execution agent** → reads `NAME/NAME.debate.md` + patient profile → produces `NAME/NAME.execution.md`
- **Exercise agent** → reads `NAME/NAME.debate.md` + patient profile → produces `NAME/NAME.exercise.md`
- **Mindset agent** → reads `NAME/NAME.debate.md` + patient profile → produces `NAME/NAME.mindset.md`

These five agents run in parallel. Each has the full debate as input and produces one focused document. Because the debate is the settled source of truth, these agents don't need to re-debate — they translate.

#### Step 4C: Document Refinement Loop

After the initial document generation, run 2-3 quick refinement rounds on the non-debate documents. Each round:
1. A consistency-check agent reads ALL six documents and flags mismatches (e.g., the inputs guide lists a supplement the debate removed, or the execution plan sequences something differently than the debate concluded)
2. Targeted fix agents patch the flagged mismatches

This is lightweight — the heavy work is done. This just catches translation errors.

#### Step 4D: Final Cleanup

1. Run `pdfize.py` to generate PDFs for each document
2. Save scorecard history to `NAME/NAME.scores.json` for tracking
3. **Collapse intermediate files** — Delete the `NAME/debates/` directory (the content is merged into `NAME/NAME.debate.md`), the `NAME/scratch/` directory, and any other intermediate artifacts. The final file tree should be clean: patient profile in, six documents + six PDFs + score history out. No clutter.

### File Structure

**During execution**, the working tree looks like this:

```
NAME/
├── NAME.md                        # Patient profile (input)
├── labs/                          # Lab reports (input)
├── history/                       # Medical history docs (input)
├── research/                      # Pre-research output (Phase 0)
│   ├── medication-review.md
│   ├── condition-guidelines.md
│   └── pharmacogenomics.md
├── debates/                       # Per-topic debate files (Phase 1+)
│   ├── thyroid-function.md
│   ├── lipid-management.md
│   ├── gut-health.md
│   ├── cardiovascular-risk.md
│   ├── medication-optimization.md
│   ├── supplement-protocol.md
│   └── crosstalk/                 # Cross-talk resolution debates
│       ├── statin-vs-red-yeast-rice.md
│       ├── magnesium-dosing-reconciliation.md
│       └── exercise-intensity-vs-cardiac-risk.md
├── scratch/
│   ├── topic-manifest.md
│   ├── conflict-manifest.md
│   ├── research-queue-v1-thyroid-function.md
│   ├── research-queue-v1-lipid-management.md
│   ├── research-v1/
│   ├── score-v1.md
│   └── ...
└── ...
```

**After Phase 4 cleanup**, the final deliverable tree is clean:

```
NAME/
├── NAME.md                    # Patient profile (input)
├── labs/                      # Lab reports (input)
├── history/                   # Medical history docs (input)
├── research/                  # Pre-research (retained for reference)
├── NAME.summary.md            # Final canonical documents
├── NAME.debate.md
├── NAME.inputs.md
├── NAME.execution.md
├── NAME.exercise.md
├── NAME.mindset.md
├── NAME.summary.pdf           # Final PDFs
├── NAME.debate.pdf
├── NAME.inputs.pdf
├── NAME.execution.pdf
├── NAME.exercise.pdf
├── NAME.mindset.pdf
└── NAME.scores.json           # Score history across all rounds
```

### Execution Cycle (Per Round)

```
Round N:
  ├── Topic debates run in parallel (one agent per topic)
  │     ↓
  ├── Cross-talk: conflict detection → parallel resolution debates → patch topics
  │     ↓
  ├── Research: parallel subagents answer queued questions from all topics
  │     ↓
  └── Score: read all topics, produce scorecard
           ↓
Round N+1: each topic agent gets its refined debate + new research + cross-talk resolutions
```

### Parallel Execution Notes

- **Phase 0 research pulls** run in parallel (multiple subagents)
- **Phase 1B topic debates** run in parallel (one subagent per topic — this is the biggest speedup)
- **Phase 2B cross-talk debates** run in parallel where conflicts are independent
- **Phase 3A topic refinements** run in parallel each round
- **Phase 3C between-round research pulls** run in parallel (one subagent per question)
- **Phase 4B document generation** runs in parallel (one subagent per document)
- **Only cross-talk detection (2A/3B) runs sequentially** — it needs all topic outputs before it can find conflicts
- OpenClaw `maxConcurrent` subagent setting should be at least **8** for a typical patient (more topics = more parallelism). For complex patients with 15+ topics, set to 12-16.
- Typical wall-clock time: **faster than the old monolithic model** despite more total work, because parallelism dominates. A 10-topic patient with 5 rounds might take 20-40 minutes vs. 30-60 minutes for the old sequential approach.

### Running the Report

To kick off a full report:

```
Read DOCTOR.md and use NAME/NAME.md to produce the full report suite:
NAME/NAME.summary.md, NAME/NAME.debate.md, NAME/NAME.inputs.md,
NAME/NAME.execution.md, NAME/NAME.exercise.md, and NAME/NAME.mindset.md.
Set this up to leverage Ralph for multiple iterations with parallel topic
debates and cross-talk reconciliation. Do up to 10 refinement rounds with
parallel agents to produce fantastic output across all six documents.
Use the NAME/debates/ directory for per-topic debate files and
NAME/scratch/ for intermediate results.
```

That's it. DOCTOR.md IS the prompt. The patient profile IS the input. Topics debate in parallel. Cross-talk reconciles conflicts. Ralph refines iteratively. OpenClaw orchestrates. The conference converges.
