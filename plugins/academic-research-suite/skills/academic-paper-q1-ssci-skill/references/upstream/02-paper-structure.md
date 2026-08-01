# Standard Paper Structure — IMRaD+ Format

## 1. TITLE (10-15 words)
- Include key variables and relationship
- Pattern: "[DV] through [Mechanism]: The Role of [Moderator/Context]"
- No abbreviations

## 2. ABSTRACT (150-250 words)
Strict structure:
- **Context**: 1-2 sentences on the research gap
- **Purpose**: 1 sentence stating the objective
- **Method**: 1-2 sentences on methodology
- **Findings**: 2-3 sentences on key results
- **Contribution**: 1-2 sentences on implications
- **Keywords**: 4-6 (methodology + theory + key constructs)

## 3. INTRODUCTION (1500-2000 words)
Follow "Hook > Gap > Purpose > Contribution":
- P1: Hook, compelling phenomenon, statistic, or paradox
- P2: Context, what we know from literature
- P3: Gap, what remains unclear ("however," "yet," "limited attention")
- P4: Purpose, research questions + methodology
- P5: Contributions, list 2-3 explicitly

## 4. LITERATURE REVIEW & THEORY (3000-4000 words)
- Organize THEMATICALLY, not chronologically
- State theoretical lens explicitly
- Build logically toward hypotheses
- Each hypothesis: Theory > Logic > Prediction
- Include conceptual model figure

## 5. METHODOLOGY (2000-3000 words)

### 5.1 Required Elements (All Methods)
- Research design + justification
- Sample: population, strategy, response rate, timeframe
- Measures: DV, IV, mediator/moderator, controls (all with sources, items, alpha)
- Validity: CFA, HTMT, CMB (Harman's test), endogeneity
- Analysis strategy + justification for method choice

### 5.2 Choosing the Right Method

Select methodology based on research purpose:

| Research Purpose | Recommended Method | Software |
|---|---|---|
| Test linear causal relationships | PLS-SEM, CB-SEM | SmartPLS, AMOS, Mplus |
| Prediction-oriented modeling | PLS-SEM + PLSpredict | SmartPLS 4 |
| Identify necessary conditions (bottlenecks) | NCA | R (NCA package), SmartPLS 4 |
| Explore combinatorial causal recipes | fsQCA | fsQCA software, R (QCA package) |
| Integrated necessity + sufficiency + causality | PLS-SEM + NCA + fsQCA | SmartPLS 4 + R + fsQCA |
| Address endogeneity (observational data) | IV, Heckman, GMM | Stata |
| Causal inference from policy/treatment | DiD, RDD, PSM, SCM | Stata |
| High-dimensional variable selection | LASSO, Elastic Net | Stata 18, R |
| Heterogeneous treatment effects | Causal Forest, DML | R (grf), Python (econml), Stata |
| Dynamic panel with lagged effects | System GMM | Stata (xtabond2) |

---

### 5.3 PLS-SEM: Advanced Techniques

#### 5.3.1 Core PLS-SEM Analysis
- Measurement model: indicator loadings, Cronbach's alpha, CR, AVE
- Discriminant validity: Fornell-Larcker criterion, HTMT ratio (threshold < 0.90)
- Structural model: path coefficients (beta), t-values, p-values, R squared, f squared
- Bootstrapping: minimum 5,000 subsamples (Hair et al., 2022)

#### 5.3.2 PLSpredict (Predictive Power Assessment)
- Purpose: evaluate out-of-sample predictive relevance beyond in-sample R squared
- Metrics: Q squared predict, RMSE, MAE
- Benchmark: compare PLS-SEM predictions against linear model (LM) benchmark
- Interpretation:
  - All indicators RMSE(PLS) < RMSE(LM): high predictive power
  - Majority indicators RMSE(PLS) < RMSE(LM): medium predictive power
  - Minority or none: low predictive power
- Reference: Shmueli et al. (2019); Hair et al. (2024, 4th Edition)

#### 5.3.3 IPMA (Importance-Performance Map Analysis)
- Purpose: identify which constructs have high importance but low performance
- Combines total effects (importance) with average latent variable scores (performance)
- Visualization: importance-performance map (quadrant chart)
- Practical use: prioritize managerial action on high-importance, low-performance areas
- Report: unstandardized total effects + rescaled scores (0-100)

#### 5.3.4 Higher-Order Constructs (HOC)
- Types: reflective-reflective, reflective-formative, formative-reflective, formative-formative
- Recommended approach: disjoint two-stage approach (Sarstedt et al., 2019)
  - Stage 1: estimate lower-order component scores
  - Stage 2: use scores as indicators for higher-order construct
- Report: both lower-order and higher-order measurement model results

#### 5.3.5 Multigroup Analysis (MGA) and MICOM
- MICOM (Measurement Invariance of Composite Models):
  - Step 1: configural invariance
  - Step 2: compositional invariance (permutation test)
  - Step 3: equality of composite means and variances
- MGA: compare path coefficients across groups ONLY after establishing MICOM
- Report: permutation p-values, confidence intervals, group-specific results
- Reference: Henseler et al. (2016); Hair et al. (2024)

#### 5.3.6 Endogeneity in PLS-SEM: Gaussian Copula Approach
- Purpose: detect and correct endogeneity without requiring instrumental variables
- Procedure:
  1. Create copula terms for suspected endogenous constructs
  2. Include copula terms as additional predictors in the structural model
  3. If copula coefficient is significant, endogeneity is present
  4. Report corrected path coefficients
- Assumption: non-normal distribution of endogenous construct (check skewness)
- Reference: Hult et al. (2018); Sarstedt et al. (2020)

#### 5.3.7 Mediation and Moderation in PLS-SEM
- Mediation:
  - Report direct effect, indirect effect, total effect
  - Use bootstrapping for indirect effect significance (bias-corrected CI)
  - Classify: complementary, competitive, indirect-only, direct-only, no effect
  - Reference: Zhao et al. (2010); Nitzl et al. (2016)
- Moderation:
  - Orthogonalizing approach or product indicator approach
  - Report interaction effect, simple slopes, Johnson-Neyman region
  - Moderated mediation: combine both with conditional indirect effects

---

### 5.4 NCA: Necessary Condition Analysis

#### 5.4.1 Core NCA Concepts
- Purpose: identify conditions that are NECESSARY (but not sufficient) for an outcome
- Logic: "X is necessary for Y" means Y cannot occur without a minimum level of X
- Differs from regression/SEM: regression tests "average effect"; NCA tests "ceiling constraint"

#### 5.4.2 Analysis Procedure
1. Generate scatterplots: X (condition) vs Y (outcome)
2. Draw ceiling lines using:
   - CE-FDH (Ceiling Envelopment, Free Disposal Hull): step function, non-parametric
   - CR-FDH (Ceiling Regression, Free Disposal Hull): regression-based, smoother
3. Calculate effect size (d):
   - d = ceiling zone / total scope
   - Interpretation: 0 < d < 0.1 (small), 0.1 < d < 0.3 (medium), 0.3 < d < 0.5 (large), d > 0.5 (very large)
4. Significance test: permutation test (p < 0.05)
5. Create bottleneck table: for each desired outcome level (e.g., 50%, 60%, ..., 100%), what is the minimum required level of each condition?

#### 5.4.3 Reporting Standards
- Ceiling line plots for each condition-outcome pair
- Effect size table: condition, CE-FDH d, CR-FDH d, p-value
- Bottleneck table: outcome levels vs. minimum condition levels
- Interpretation: which conditions are true bottlenecks?
- Reference: Dul (2016); Dul (2024, Advances in NCA)

#### 5.4.4 Software
- R: NCA package (install.packages("NCA"))
- SmartPLS 4: built-in NCA module (since 2023)
- Web tool: NCAweb (https://nca.shinyapps.io)

---

### 5.5 fsQCA: Fuzzy-Set Qualitative Comparative Analysis

#### 5.5.1 Core Concepts
- Purpose: identify COMBINATIONS (configurations) of conditions sufficient for an outcome
- Logic: equifinality (multiple paths to same outcome), conjunctural causation, asymmetry
- Differs from regression: does NOT assume linear, additive, symmetric relationships

#### 5.5.2 Analysis Procedure
1. Calibration: transform raw data into fuzzy-set membership scores (0 to 1)
   - Define three anchors: full non-membership (0.05), crossover (0.50), full membership (0.95)
   - Use direct calibration method (Ragin, 2008)
2. Necessity analysis:
   - Test each condition individually
   - Threshold: consistency > 0.90 for necessary condition
   - Report: consistency, coverage, relevance of necessity (RoN)
3. Truth table construction:
   - Create 2^k rows (k = number of conditions)
   - Set frequency threshold (typically n > 1 for small samples, n > 3 for large)
   - Set consistency threshold (typically > 0.80, ideally > 0.85)
4. Boolean minimization: generate three solutions
   - Complex solution (no simplifying assumptions)
   - Parsimonious solution (all remainders used)
   - Intermediate solution (only theoretically justified remainders)
5. Report: intermediate solution is primary; parsimonious identifies core conditions

#### 5.5.3 Reporting Standards
- Calibration thresholds and justification
- Necessity analysis table: condition, consistency, coverage
- Truth table: configurations, raw consistency, PRI
- Solution table: configuration, raw coverage, unique coverage, consistency
- Overall solution consistency and coverage
- Notation: black circles (presence), crossed circles (absence), blank (don't care)
- Reference: Ragin (2008); Fiss (2011); Schneider and Wagemann (2012)

#### 5.5.4 Advanced fsQCA Techniques (2024-2025)
- **Robustness testing**:
  - Vary consistency thresholds (e.g., 0.80, 0.85, 0.90)
  - Vary frequency thresholds
  - Vary calibration anchors (sensitivity analysis)
  - Permutation-based tests (SetMethods R package)
- **Enhanced Standard Analysis (ESA)**:
  - Full exploitation of solution space
  - More rigorous counterfactual analysis
  - Reference: Schneider and Wagemann (2024)
- **Temporal/longitudinal fsQCA**: panel configurations over time
- **Negation analysis**: analyze configurations for the ABSENCE of outcome
- **fsQCA + NCA integration**: use NCA first to identify necessary conditions, then fsQCA for sufficient configurations

#### 5.5.5 Software
- fsQCA 3.0 / 4.0 (Ragin and Davey)
- R: QCA package, SetMethods package
- Stata: user-written QCA modules (SSC)

---

### 5.6 Integrated Approach: PLS-SEM + NCA + fsQCA

#### 5.6.1 Rationale for Integration
This is the most comprehensive analytical framework currently published in Q1/SSCI journals (2024-2025). Each method answers a different question:

| Method | Question Answered | Nature |
|---|---|---|
| PLS-SEM | "What is the average net effect of X on Y?" | Symmetric, sufficiency-based |
| NCA | "What minimum level of X is required for Y to occur?" | Asymmetric, necessity-based |
| fsQCA | "What combinations of conditions lead to Y?" | Asymmetric, configurational |

#### 5.6.2 Step-by-Step Integration Protocol
1. **Step 1: PLS-SEM**
   - Test hypothesized relationships (H1, H2, ...)
   - Report: beta, t-value, p-value, R squared, f squared
   - Run PLSpredict for predictive assessment
   - Run IPMA for importance-performance insights
   - Address endogeneity via Gaussian Copula if applicable

2. **Step 2: NCA**
   - Test each significant predictor as necessary condition for outcome
   - Report: effect sizes (d), significance, bottleneck table
   - Identify which factors are true bottlenecks
   - Practical insight: "To achieve outcome level X%, condition Y must be at least Z%"

3. **Step 3: fsQCA**
   - Calibrate all variables into fuzzy sets
   - Test necessity (consistency > 0.90)
   - Construct truth table and run Boolean minimization
   - Report: sufficient configurations (recipes)
   - Compare with PLS-SEM: which paths are confirmed configurationally?

4. **Step 4: Triangulated Interpretation**
   - Compare results across all three methods
   - Identify: which findings converge? which diverge?
   - Stronger evidence for convergent findings
   - Discuss divergences as nuanced contributions

#### 5.6.3 Key References for Integrated Approach
- Dul (2016). Necessary Condition Analysis. Organizational Research Methods.
- Sukhov et al. (2023). Unlocking potential: PLS-SEM, NCA, and fsQCA. JBR.
- Hair et al. (2024). A Primer on PLS-SEM, 4th Edition.
- Ragin (2008). Redesigning Social Inquiry. University of Chicago Press.

---

### 5.7 Advanced Stata-Based Methods

#### 5.7.1 Endogeneity Correction

**A. Instrumental Variables (IV/2SLS)**
- Purpose: address endogeneity from omitted variables, reverse causality, measurement error
- Stata commands: ivregress 2sls, ivreg2
- Requirements:
  - Instrument relevance: F-statistic > 10 (Staiger and Stock rule)
  - Instrument exogeneity: Hansen J-test (p > 0.10)
- Report: first-stage F-stat, Sargan/Hansen test, Durbin-Wu-Hausman test

**B. Heckman Selection Model**
- Purpose: correct sample selection bias
- Stata command: heckman
- Procedure:
  - Step 1: selection equation (Probit) for participation/observation
  - Step 2: outcome equation with Inverse Mills Ratio (lambda)
- Report: lambda coefficient and significance, rho, selection equation results
- Use when: sample is non-random (e.g., only observe firms that adopt innovation)

**C. Gaussian Copula (Stata Implementation)**
- Purpose: endogeneity correction without instrumental variables
- Procedure: create copula term from non-normal endogenous variable
- Stata: manually generate copula via inverse normal CDF transformation
- Report: copula coefficient significance, corrected estimates

#### 5.7.2 Causal Inference Methods

**D. Difference-in-Differences (DiD)**
- Purpose: estimate causal effect of treatment/policy using pre-post, treatment-control design
- Stata commands: regress (with interaction), didregress (Stata 17+), csdid
- Model: Y = alpha + beta(Post) + gamma(Treat) + delta(Post x Treat) + epsilon
- Key assumption: parallel trends (test with pre-treatment trend plots)
- Advanced extensions (2024-2025):
  - Staggered DiD: Callaway and Sant'Anna (2021), csdid in Stata
  - Heterogeneity-robust DiD: Sun and Abraham (2021), eventstudyinteract
  - Doubly robust DiD: combines propensity score with outcome modeling
- Report: delta coefficient, parallel trends test, event study plot

**E. Regression Discontinuity Design (RDD)**
- Purpose: exploit cutoff/threshold for causal inference
- Stata commands: rdrobust, rddensity, rdplot
- Types:
  - Sharp RDD: treatment perfectly determined by cutoff
  - Fuzzy RDD: cutoff affects probability of treatment (use IV at cutoff)
- Report: bandwidth selection, local polynomial estimates, manipulation test (McCrary/rddensity)
- Visualization: rdplot with confidence intervals around cutoff

**F. Propensity Score Matching (PSM)**
- Purpose: create comparable treatment/control groups from observational data
- Stata commands: psmatch2, teffects psmatch, teffects ipw
- Procedure:
  1. Estimate propensity scores via logistic regression
  2. Match: nearest neighbor, caliper, kernel, or radius matching
  3. Check balance: standardized mean differences < 0.10
  4. Estimate ATT (Average Treatment effect on the Treated)
- Report: balance table, common support, ATT with bootstrapped SE
- Advanced: Inverse Probability Weighting (IPW), doubly robust estimators

**G. Synthetic Control Method (SCM)**
- Purpose: construct counterfactual for single treated unit using weighted combination of control units
- Stata commands: synth, sdid (synthetic DiD)
- Use when: single or few treated units (e.g., one country, one policy change)
- Report: synthetic vs. actual outcome trajectory, placebo tests, RMSPE ratios
- Advanced (2024-2025): Synthetic Difference-in-Differences (SDID) by Arkhangelsky et al. (2021)

#### 5.7.3 Dynamic Panel Methods

**H. System GMM (Generalized Method of Moments)**
- Purpose: estimate dynamic panel models with lagged DV, endogeneity, unobserved heterogeneity
- Stata command: xtabond2
- When to use: panel data with N > T, lagged dependent variable, persistent series
- Specification:
  - Use system GMM (combines difference and level equations)
  - Forward orthogonal deviations for unbalanced panels
- Diagnostics:
  - AR(1) test: should be significant (expected)
  - AR(2) test: should be non-significant (no second-order autocorrelation)
  - Hansen J-test: p > 0.10 (instrument validity)
  - Number of instruments < number of groups (avoid instrument proliferation)
- Report: GMM estimates, AR tests, Hansen test, instrument count

#### 5.7.4 Machine Learning-Enhanced Causal Methods

**I. LASSO and Elastic Net (Variable Selection)**
- Purpose: select relevant variables in high-dimensional settings, reduce overfitting
- Stata commands: lasso, elasticnet, lassologit (Stata 16+)
- Types:
  - LASSO: L1 penalty (drives coefficients to zero)
  - Elastic Net: combines L1 + L2 penalty
  - Post-LASSO: run OLS on LASSO-selected variables for unbiased estimates
- Use in causal research: post-double-selection (Belloni et al., 2014)
- Report: selected variables, lambda value, cross-validation results

**J. Double Machine Learning (DML)**
- Purpose: estimate causal effects in high-dimensional settings using ML for nuisance parameters
- Stata: dml package (SSC), or interface with R/Python
- Procedure (Chernozhukov et al., 2018):
  1. Use ML (LASSO, random forest, boosting) to model outcome and treatment
  2. Compute residuals from both models
  3. Estimate causal effect from residual-on-residual regression
  4. Cross-fitting to avoid overfitting bias
- Report: ATE/ATT estimates, confidence intervals, ML method used

**K. Causal Forest (Heterogeneous Treatment Effects)**
- Purpose: estimate treatment effects that vary across subgroups
- Software: R (grf package), Python (econml), interface with Stata via rcall/pystata
- Procedure:
  1. Estimate CATE (Conditional Average Treatment Effect) for each observation
  2. Identify subgroups with highest/lowest treatment effects
  3. Variable importance: which covariates drive heterogeneity?
- Report: average treatment effect, CATE distribution, variable importance, calibration test
- Reference: Athey and Imbens (2019); Wager and Athey (2018)

---

### 5.8 Method Selection Decision Tree

```
START: What is your research goal?
|
|--- Test hypothesized relationships (H1, H2...)?
|    |--- Prediction-focused? --> PLS-SEM + PLSpredict
|    |--- Explanation-focused? --> CB-SEM (AMOS, Mplus)
|    |--- Both? --> PLS-SEM + PLSpredict + IPMA
|
|--- Identify necessary conditions (bottlenecks)?
|    --> NCA (standalone or combined with PLS-SEM)
|
|--- Explore causal combinations/recipes?
|    --> fsQCA (standalone or combined with NCA)
|
|--- Comprehensive analysis?
|    --> PLS-SEM + NCA + fsQCA (integrated approach)
|
|--- Establish causality from observational data?
|    |--- Treatment/policy with before-after data?
|    |    --> DiD (or Staggered DiD)
|    |--- Cutoff/threshold exists?
|    |    --> RDD (Sharp or Fuzzy)
|    |--- Treatment/control groups, no randomization?
|    |    --> PSM or IPW
|    |--- Single treated unit (country/firm)?
|    |    --> Synthetic Control Method
|    |--- Endogeneity concern?
|    |    |--- Good instrument available? --> IV/2SLS
|    |    |--- No instrument? --> Gaussian Copula or Heckman
|    |    |--- Dynamic panel? --> System GMM
|    |
|--- High-dimensional data (many variables)?
|    |--- Variable selection? --> LASSO / Elastic Net
|    |--- Causal effect estimation? --> Double Machine Learning
|    |--- Heterogeneous effects? --> Causal Forest
|
END: Always combine with robustness checks
```

---

## 6. RESULTS (1500-2500 words)
- Descriptive statistics and correlation matrix
- Measurement model (CFA/EFA)
- Hypothesis testing: beta, SE, t/z-value, p-value, CI
- Effect sizes: R squared, f squared, Cohen's d
- Robustness checks (alternative models, split samples, bootstrapping)
- If integrated approach: present PLS-SEM results, then NCA results, then fsQCA results

## 7. DISCUSSION (2000-3000 words)
- Summary of findings
- Theoretical implications (link each finding to theory)
- Practical implications (actionable)
- Limitations + future research (min 3-4, each paired)
- Conclusion (3-5 sentences)

## 8. REFERENCES
- APA 7th Edition
- 60-80 minimum
- 40%+ from last 5 years
- Include target journal's own publications