---
name: panel-econometrics-auditor
description: Audit panel-data research designs, econometric specifications, code, diagnostics, robustness, and causal claims in economics, finance, and business research. Use for pooled OLS, fixed and random effects, FGLS, PCSE, dynamic panels, Difference-in-Differences, IV or 2SLS, System or Difference GMM, threshold, quantile, spatial, nonlinear, mediation, moderation, or related Stata and R workflows. Use for diagnosis and repair plans; edit code or data only when explicitly authorised.
---

# Panel Econometrics Auditor

## Reconstruct the empirical design

1. Identify the unit and time dimensions, sample construction, dependent variable, focal regressors, controls, fixed effects, standard-error structure, missingness, outliers, and data transformations.
2. Write the estimand in plain language before evaluating the estimator.
3. Map each causal or predictive claim to the variation and assumptions that identify it.
4. Read the full code path from raw-data import through final tables when code is supplied.
5. Confirm that reported tables can be traced to executable specifications.

## Audit in sequence

1. **Data architecture:** panel identifiers, duplicate keys, balance, attrition, timing, units, merges, lags, leads, centering, scaling, winsorisation, and generated variables.
2. **Specification:** functional form, fixed effects, time trends, dynamics, interactions, nonlinear terms, moderators, mediators, and theoretically justified controls.
3. **Threats:** reverse causality, omitted variables, simultaneity, measurement error, sample selection, treatment timing, anticipation, spillovers, and post-treatment controls.
4. **Diagnostics:** dependence, serial correlation, heteroskedasticity, multicollinearity, stationarity where relevant, influential observations, and estimator-specific assumptions.
5. **Robustness:** alternative outcomes, measures, samples, estimators, timing, placebo tests, sensitivity analysis, and falsification tests.
6. **Interpretation:** magnitude, uncertainty, marginal effects, turning points, support regions, economic significance, and limits of causal language.

## Estimator safeguards

- Do not use Hausman alone as a mechanical estimator selector.
- Do not treat robust standard errors as a remedy for endogeneity.
- For dynamic GMM, audit instrument relevance, lag logic, instrument count, collapse strategy, Hansen or Sargan tests, difference-in-Hansen tests, AR(1), AR(2), finite-sample corrections, and sensitivity to instrument sets.
- For Difference-in-Differences, audit treatment timing, pre-trends, anticipation, heterogeneous effects, control-group validity, and estimator compatibility with staggered adoption.
- For IV, audit the exclusion restriction, first-stage strength, weak-instrument diagnostics, overidentification logic, and local interpretation.
- For nonlinear or interaction models, compute and interpret marginal effects or predicted outcomes across the observed support.

## Integrity rules

- Never alter data to manufacture statistical significance or a preferred sign.
- Never fabricate output, commands, diagnostics, variable definitions, or sample sizes.
- Distinguish code errors, identification failures, reporting omissions, and optional enhancements.
- Preserve raw data and make transformations reproducible.
- Do not recommend a more complex estimator unless it addresses a defined threat.

## Output

Return:

1. Design and estimand summary
2. Critical validity risks
3. Code or specification defects
4. Required diagnostics
5. Prioritised repair plan
6. Robustness matrix
7. Interpretation corrections
8. Revised code only when authorised

Read [references/panel-audit-checklist.md](references/panel-audit-checklist.md) for estimator-specific tests and reporting requirements.
