# Panel Econometrics Audit Checklist

## Universal checks

- Define the estimand and source of identifying variation.
- Verify panel key uniqueness and time ordering.
- Report sample construction and attrition.
- Distinguish time-invariant, slow-moving, and within-unit variation.
- Audit transformations, lags, leads, interactions, centering, and nonlinear terms.
- Justify fixed effects and clustering level.
- Test whether substantive conclusions survive plausible alternatives.

## Estimator checklist

| Design | Required scrutiny |
| --- | --- |
| Pooled OLS | Ignored heterogeneity, dependence, clustering, functional form |
| Fixed effects | Within variation, time effects, absorption, dynamic bias, limited generalisability |
| Random effects | Correlated heterogeneity assumptions and defensible tests beyond mechanical Hausman use |
| FGLS or PCSE | Error structure, time dimension, cross-sectional dependence, feasibility |
| Dynamic GMM | Instrument validity, proliferation, lags, AR tests, Hansen sensitivity, finite-sample correction |
| IV or 2SLS | Relevance, exclusion, weak instruments, endogeneity test, local estimand |
| Difference-in-Differences | Timing, pre-trends, anticipation, staggered adoption, heterogeneous effects, spillovers |
| Threshold or nonlinear | Threshold identification, confidence interval, support, turning point, marginal effects |
| Panel quantile | Estimator assumptions, fixed-effect treatment, interpretation across quantiles |
| Spatial panel | Weight matrix, spillovers, direct and indirect effects, dependence diagnostics |

## Dynamic GMM minimum report

- number of groups and observations
- number of instruments
- one-step and two-step rationale
- robust finite-sample correction when appropriate
- lag ranges and collapse status
- AR(1) and AR(2)
- Hansen or Sargan
- difference-in-Hansen where instrument subsets matter
- sensitivity to reduced instrument counts

Instrument count should remain materially below the number of groups unless a stronger justification exists.

## Interaction and nonlinear interpretation

1. Confirm hierarchical specification.
2. Check constituent-term scaling and support.
3. Report marginal effects or predicted outcomes with uncertainty.
4. Identify regions of support and avoid extrapolation.
5. For quadratic models, calculate the turning point and confirm it lies within observed data.

## Repair priority

1. Data corruption or variable-construction error
2. Identification failure
3. Estimator-assumption failure
4. Missing diagnostics
5. Inference and standard-error error
6. Interpretation overreach
7. Optional efficiency or presentation improvement
