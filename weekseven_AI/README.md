#  AI Ethics: Designing Responsible and Fair AI Systems

This repository contains the code, visualizations, and written analysis for the PLP Academy AI Ethics Assignment. We explored algorithmic fairness, conducted a technical audit using AIF360, and proposed ethical solutions to real-world AI dilemmas.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Part 1: Theoretical Understanding](#part-1-theoretical-understanding)
- [Part 2: Case Study Analysis](#part-2-case-study-analysis)
- [Part 3: Practical Fairness Audit](#part-3-practical-fairness-audit)
- [Part 4: Ethical Reflection](#part-4-ethical-reflection)
- [Bonus: AI in Healthcare Ethics Policy](#bonus-ai-in-healthcare-ethics-policy)

---

##  Project Overview

This project evaluates fairness in AI systems by:
- Understanding core ethics concepts (bias, transparency, GDPR).
- Analyzing case studies on hiring and facial recognition.
- Conducting a technical audit on the COMPAS dataset using AIF360.
- Reflecting on how to build responsible AI systems.

---

## Part 1: Theoretical Understanding

We answered key questions on:
- Algorithmic bias (definitions + real examples).
- Transparency vs. explainability.
- GDPR's impact on AI design.
- Ethical principles (justice, non-maleficence, autonomy, sustainability).

---

## Part 2: Case Study Analysis

**Case 1: Biased Hiring Tool**
- Source of bias: biased training data and historical discrimination.
- Solutions: diverse data, algorithmic auditing, gender-neutral feature selection.

**Case 2: Facial Recognition in Policing**
- Risks: misidentification, civil rights violations.
- Recommendations: human-in-the-loop review, regulation, and public transparency.

---

## Part 3: Practical Fairness Audit

###  Dataset: COMPAS Recidivism Dataset

Used IBM’s AI Fairness 360 (AIF360) to assess racial bias in recidivism predictions.

### ⚙️ Tools Used:
- AIF360
- Pandas, Numpy, Scikit-learn
- Matplotlib

###  Key Metrics:
| Metric | Value | Interpretation |
|--------|-------|----------------|
| Accuracy | ~69.16% | Acceptable baseline |
| Disparate Impact | 0.64 |  Bias detected (below 0.8) |
| Equal Opportunity Difference | -0.16 |  Less favorable outcomes for African-Americans |

---

## Part 4: Ethical Reflection

We reflected on an Edge AI project (waste classification) and ensured ethical principles like:
- Privacy protection
- Model transparency
- Inclusivity across regions
- Environmental and social sustainability

---

## 🎯 Bonus: AI in Healthcare Ethics Policy

We proposed a 1-page ethical framework with:
- Consent protocols
- Bias mitigation strategies
- Transparent and explainable decision-making in clinical settings



Assignment: AI Ethics
Theme: "Designing Responsible and Fair AI Systems" 🌍⚖️

Objective & Guidelnes

This assignment evaluates your understanding of AI ethics principles, ability to identify and mitigate biases, and skill in applying ethical frameworks to real-world scenarios. You will analyze case studies, audit AI systems, and propose solutions to ethical dilemmas.

The Asignment should be handled in peer groups. 

Submission Guidelines

Written Answers: PDF with case study analyses and reflections. (Group Peer Reviews)

Code & Visualizations: Jupyter Notebook or Python script with fairness audit. (Shared on GitHub)

Bonus Task: Separate document (To be shared as an article in the PLP Academy Community).

Grading Rubric
Criteria	Weight
Theoretical Accuracy	30%
Case Study Depth & Solutions	40%
Technical Audit Execution	25%
Reflection & Creativity	5%
Tools & Resources

Libraries: AI Fairness 360, Pandas, Matplotlib.

Datasets: COMPAS (provided), ProPublica’s Analysis.

Frameworks: EU Ethics Guidelines for Trustworthy AI.

Why This Matters

Societal Impact: Ethical AI prevents harm and fosters trust in technology.

Career Skill: Employers prioritize ethical competency in AI roles.

Deadline: 7 days. Build AI that’s fair, transparent, and human-centric! 🌟

Need Help?

Use AI Fairness 360 GitHub Repository.

Join the PLP Academy Community discussion: #AIEthicsAssignment.

Pro Tip: Start with fairness metrics like disparate impact ratio and equal opportunity difference. Small steps lead to big ethical wins! 🔍
Part 1: Theoretical Understanding (30%)
1. Short Answer Questions

Q1: Define algorithmic bias and provide two examples of how it manifests in AI systems.

Q2: Explain the difference between transparency and explainability in AI. Why are both important?

Q3: How does GDPR (General Data Protection Regulation) impact AI development in the EU?

2. Ethical Principles Matching

Match the following principles to their definitions:

A) Justice

B) Non-maleficence

C) Autonomy

D) Sustainability

Ensuring AI does not harm individuals or society.

Respecting users’ right to control their data and decisions.

Designing AI to be environmentally friendly.

Fair distribution of AI benefits and risks.



Part 2: Case Study Analysis (40%)
Case 1: Biased Hiring Tool

Scenario: Amazon’s AI recruiting tool penalized female candidates.

Tasks:

Identify the source of bias (e.g., training data, model design).

Propose three fixes to make the tool fairer.

Suggest metrics to evaluate fairness post-correction.

Case 2: Facial Recognition in Policing

Scenario: A facial recognition system misidentifies minorities at higher rates.

Tasks:

Discuss ethical risks (e.g., wrongful arrests, privacy violations).

Recommend policies for responsible deployment.

Part 3: Practical Audit (25%)
Task: Audit a Dataset for Bias

Dataset: COMPAS Recidivism Dataset.

Goal:

Use Python and AI Fairness 360 (IBM’s toolkit) to analyze racial bias in risk scores.

Generate visualizations (e.g., disparity in false positive rates).

Write a 300-word report summarizing findings and remediation steps.

Deliverable: Code + report.

Part 4: Ethical Reflection (5%)

Prompt: Reflect on a personal project (past or future). How will you ensure it adheres to ethical AI principles?

Bonus Task (Extra 10%)

Policy Proposal: Draft a 1-page guideline for ethical AI use in healthcare. Include:

Patient consent protocols.

Bias mitigation strategies.

Transparency requirements.