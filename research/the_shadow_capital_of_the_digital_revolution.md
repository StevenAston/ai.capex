# The Shadow Capital of the Digital Revolution
## Household-financed computing inputs during the U.S. transition, 1980–2010

**Reconciled working paper — 28 October 2026**

This revision reconciles the 26 October draft's embedded annual arrays, formulas, tables, sensitivity results and code. All monetary totals are cumulative **nominal U.S. dollars**. They are not inflation-adjusted dollars, present values or surviving capital stocks. The arrays remain **provisional model inputs pending source-level authentication**.

## Abstract

Computerization depended on more than corporate equipment and software. Households also supplied hardware, connectivity, learning materials and unpaid adaptation. This paper proposes accounting for the work-attributable portion of those inputs. Using the exported draft's arrays, corporate IT expenditure totals **$9.852 trillion**. Uniform 40% career attribution gives **$707.20 billion** of direct household cost. Valuing 1.5 unpaid learning hours per week for the modelled exposed workforce at 75% of its assigned hourly wage gives **$1.90449 trillion**. Combined gross household cost is **$2.61169 trillion**, equivalent in scale to **26.51%** of the corporate denominator.

These are conditional cost scenarios. They do not identify an uncompensated transfer, a causal contribution to productivity or a statistical bound. Establishing net employer capture requires a counterfactual and an account of the returns households received.

## 1. The research question

Did firm-centred accounts of computerization omit material resources supplied by households? Off-the-clock learning could improve workplace effectiveness and reduce enterprise implementation costs. Ownership or leisure use alone cannot establish that effect.

Four questions must remain separate:

1. What money and time did households supply?
2. How much was attributable to work rather than personal consumption?
3. What productive services or avoided costs did employers receive?
4. What portion did households fail to recover through wages, employment access, leisure or other benefits?

The calculations below model the first two. They do not directly estimate the last two.

The productivity J-curve literature supplies a framework for complementary investments that are difficult to measure. General-training theory and labour-market frictions address who finances skills and receives their returns. Neither validates this paper's input series or establishes an exact transfer.

## 2. Accounting and assumptions

Let H, I, S and A be annual household hardware, ISP, software/materials and ancillary expenditure. Let a, b, c and e be their respective work-attribution shares. Let N be exposed workers, h unpaid learning hours per week, w hourly wage and q the shadow-wage factor.

- **Direct cost:** D = Σ(aH + bI + cS + eA).
- **Time value:** T = Σ(N × 52 × h × q × w).
- **Combined gross cost:** G = D + T, conditional on no overlap.
- **Scale ratios:** D/ΣK, T/ΣK and G/ΣK, where K is corporate IT expenditure.

The baseline uses **a = b = c = e = 0.40**, **h = 1.50 hours/week**, and **q = 0.75**. These are assumptions, not estimated population parameters. The 52-week convention means h is a full-year weekly average.

Worker counts are in millions; dividing the product by 1,000 produces billions of dollars. The baseline implies **180.921 billion learning hours** over the period. That large implied quantity should be checked against independent time-use evidence.

### Removing the extra multiplier

The previous code included an additional **1.815 learning-intensity multiplier** absent from the stated model. This revision removes it. Repeated learning or turnover requires its own evidence and a demonstration that it is not already counted in exposure or weekly hours. It cannot be introduced to recover a preferred headline.

### Cash and time are separate categories

Direct expenditure is not a demonstrated lower bound on uncompensated transfer. Time value is not a demonstrated upper bound. Both may contain private benefits; employer reimbursement reduces net household cost. Scenario ranges are not confidence intervals.

### Ancillary overlap

The baseline includes the exported code's ancillary series to reconcile that implementation, conditional on eliminating overlap with hardware and training materials. Excluding ancillary gives **$591.36B** direct, **$2,495.85B** combined and **25.33%** combined/corporate. Neither choice authenticates the series.

## 3. Input provenance

The exported draft cited BEA, Census, BLS, FCC, company filings and industry sources. Those citations are research leads, not verified extraction logs for all 31 annual values.

Every observation needs its exact source table or variable, release vintage, unit, coverage, transformation, and observed/interpolated status. In particular:

- Internet connection counts do not directly measure household ISP spending.
- Computer ownership does not reveal career motivation.
- Broad time-use codes do not directly identify informal digital learning.
- Combined home/work exposure differs from computer use at work.
- Production/nonsupervisory wages may not represent all exposed workers.
- A lower wage assumption does not make a calculation a formal bound.
- Ancillary tuition and peripherals may overlap other categories.
- The corporate denominator must consistently define equipment, software, services and sector coverage.
- A cumulative nominal comparison describes historical outlays, not a constant-purchasing-power or present-value transfer.

Historical Census ownership benchmarks support diffusion: 8.2% of households in 1984 and 15.0% in 1989. They do not validate a 40% occupational-attribution assumption.

## 4. Reconciled annual scenario

Monetary values are nominal $B; workforce is millions; wages are $/hour. Displayed rows are rounded, while totals use unrounded calculations.

| Year | Corporate IT | Hardware | ISP | Software/materials | Ancillary | Workers M | Wage | Direct D | Time T | Combined G |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1980 | 45.00 | 0.80 | 0.00 | 0.20 | 0.10 | 5.50 | 6.75 | 0.44 | 2.17 | 2.61 |
| 1981 | 52.00 | 1.50 | 0.00 | 0.40 | 0.20 | 7.20 | 7.25 | 0.84 | 3.05 | 3.89 |
| 1982 | 60.00 | 2.70 | 0.00 | 0.70 | 0.40 | 9.50 | 7.68 | 1.52 | 4.27 | 5.79 |
| 1983 | 71.00 | 4.20 | 0.00 | 1.10 | 0.60 | 12.80 | 8.02 | 2.36 | 6.01 | 8.37 |
| 1984 | 83.00 | 5.80 | 0.00 | 1.60 | 0.90 | 16.50 | 8.33 | 3.32 | 8.04 | 11.36 |
| 1985 | 95.00 | 7.20 | 0.00 | 2.20 | 1.20 | 21.00 | 8.57 | 4.24 | 10.53 | 14.77 |
| 1986 | 108.00 | 8.50 | 0.00 | 2.90 | 1.60 | 26.20 | 8.76 | 5.20 | 13.43 | 18.63 |
| 1987 | 122.00 | 9.80 | 0.00 | 3.80 | 2.10 | 32.00 | 8.98 | 6.28 | 16.81 | 23.09 |
| 1988 | 138.00 | 11.20 | 0.00 | 4.80 | 2.70 | 38.50 | 9.28 | 7.48 | 20.90 | 28.38 |
| 1989 | 152.00 | 12.50 | 0.00 | 5.80 | 3.30 | 45.00 | 9.66 | 8.64 | 25.43 | 34.07 |
| 1990 | 165.00 | 13.80 | 0.00 | 6.80 | 4.00 | 52.00 | 10.01 | 9.84 | 30.45 | 40.29 |
| 1991 | 178.00 | 14.50 | 0.00 | 7.50 | 4.60 | 58.50 | 10.32 | 10.64 | 35.32 | 45.96 |
| 1992 | 195.00 | 15.80 | 0.00 | 8.20 | 5.20 | 65.00 | 10.57 | 11.68 | 40.19 | 51.87 |
| 1993 | 220.00 | 18.20 | 0.50 | 9.00 | 6.00 | 72.00 | 10.83 | 13.48 | 45.62 | 59.10 |
| 1994 | 248.00 | 22.00 | 1.20 | 10.20 | 7.10 | 79.50 | 11.12 | 16.20 | 51.72 | 67.92 |
| 1995 | 275.00 | 25.50 | 2.50 | 11.50 | 8.20 | 87.00 | 11.43 | 19.08 | 58.17 | 77.25 |
| 1996 | 310.00 | 28.20 | 4.20 | 12.80 | 9.50 | 93.50 | 11.82 | 21.88 | 64.65 | 86.53 |
| 1997 | 355.00 | 30.10 | 6.80 | 13.50 | 10.80 | 99.00 | 12.28 | 24.48 | 71.12 | 95.60 |
| 1998 | 410.00 | 30.80 | 12.10 | 14.20 | 12.20 | 103.50 | 12.78 | 27.72 | 77.38 | 105.10 |
| 1999 | 445.00 | 32.50 | 16.50 | 14.80 | 13.50 | 107.00 | 13.24 | 30.92 | 82.88 | 113.80 |
| 2000 | 450.00 | 35.20 | 22.50 | 15.20 | 14.80 | 109.50 | 13.76 | 35.08 | 88.14 | 123.22 |
| 2001 | 435.00 | 36.80 | 26.00 | 15.00 | 15.50 | 111.00 | 14.31 | 37.32 | 92.92 | 130.24 |
| 2002 | 420.00 | 38.00 | 28.50 | 14.80 | 16.00 | 112.50 | 14.77 | 38.92 | 97.21 | 136.13 |
| 2003 | 460.00 | 39.20 | 30.20 | 15.20 | 16.80 | 114.20 | 15.18 | 40.56 | 101.41 | 141.97 |
| 2004 | 510.00 | 40.00 | 32.50 | 16.00 | 17.50 | 116.50 | 15.69 | 42.40 | 106.93 | 149.33 |
| 2005 | 580.00 | 40.60 | 35.80 | 16.80 | 18.20 | 118.80 | 16.13 | 44.56 | 112.10 | 156.66 |
| 2006 | 620.00 | 40.20 | 39.20 | 17.50 | 18.80 | 120.50 | 16.76 | 46.28 | 118.15 | 164.43 |
| 2007 | 650.00 | 39.80 | 42.10 | 18.00 | 19.20 | 121.80 | 17.43 | 47.64 | 124.19 | 171.83 |
| 2008 | 620.00 | 38.50 | 44.80 | 17.80 | 19.00 | 120.20 | 18.08 | 48.04 | 127.13 | 175.17 |
| 2009 | 670.00 | 39.20 | 46.50 | 18.20 | 19.50 | 120.80 | 18.63 | 49.36 | 131.65 | 181.01 |
| 2010 | 710.00 | 39.70 | 48.70 | 18.50 | 20.10 | 122.50 | 19.05 | 50.80 | 136.52 | 187.32 |
| **Total** | **9,852.00** | **722.80** | **440.60** | **315.00** | **289.60** | — | — | **707.20** | **1,904.49** | **2,611.69** |

### Decomposition

At 40% attribution: hardware **$289.12B**, ISP **$176.24B**, software/materials **$126.00B**, and ancillary **$115.84B**, totaling **$707.20B**.

Direct, time and combined ratios to the corporate denominator are **7.18%**, **19.33%** and **26.51%**. These are relative cost scales, not shares of output, profits or causally identified capital capture.

### Non-overlapping periods

| Period | Corporate IT $B | Direct $B | Time $B | Combined $B |
| --- | ---: | ---: | ---: | ---: |
| 1980–1989 | 926.00 | 40.32 | 110.64 | 150.96 |
| 1990–1999 | 2,801.00 | 185.92 | 557.49 | 743.41 |
| 2000–2009 | 5,415.00 | 430.16 | 1,099.84 | 1,530.00 |
| 2010 | 710.00 | 50.80 | 136.52 | 187.32 |

The endpoint 2010 appears separately so no annual row is counted twice.

### Joint parameter scenarios

| Scenario | Attribution | Hours/week | Wage factor | Direct $B | Time $B | Combined $B | Combined/corporate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Low-input | 20% | 0.50 | 0.50 | 353.60 | 423.22 | 776.82 | 7.88% |
| Baseline | 40% | 1.50 | 0.75 | 707.20 | 1,904.49 | 2,611.69 | 26.51% |
| High-input | 60% | 4.00 | 1.00 | 1,060.80 | 6,771.51 | 7,832.31 | 79.50% |

These are selected joint scenarios, not probability bounds. A full sensitivity exercise should vary parameters independently. Four hours/week across the entire modelled exposed population is a strong assumption, not an observed upper bound.

## 5. Reconciliation of the export

| Item | Exported value | Reconciled treatment |
| --- | --- | --- |
| Corporate denominator | $4.651T | $9.852T, sum of original array |
| Hardware total | $747.8B | $722.8B |
| ISP total | $485.1B | $440.6B |
| Software/materials total | $332.9B | $315.0B |
| Direct cost | $842.36B | $707.20B with ancillary, $591.36B without |
| Time value | $3,479.41B | $1,904.4878B without extra multiplier |
| Bounds terminology | Direct floor / time ceiling | Separate gross cost categories |
| Decade summaries | Inconsistent totals | Non-overlapping, generated from annual rows |
| Series status | Described as verified | Provisional pending source recovery |

The printed time column summed to $1,904.56B because of its row-level rounding. The unrounded formula gives $1,904.4878B. Retaining the extra multiplier would give $3,456.6454B, still not the exported headline. No input has been tuned to preserve that headline.

## 6. Interpretation and worker returns

Household learning can be rewarding to the worker and useful to employers simultaneously. General skills can improve wages, job access, personal consumption and autonomy. The presence of such benefits does not settle whether the distribution was equitable, but it prevents treating gross household cost as automatically uncompensated.

A net-transfer estimate needs an employer counterfactual: what productive services were received, what would firms otherwise have paid, and what did households recover? The current expenditure model does not establish that every worker received no return.

Productivity–compensation comparisons must match deflators, benefits, populations and sectors. Distributional gaps alone do not identify unpaid household learning as their cause.

The AI connection is an incentive hypothesis: where implementation requires discretionary worker adaptation and knowledge, expectations about wages, security, autonomy and gain sharing may affect cooperation. That hypothesis needs its own test.

## 7. Growth accounting and stocks

Expenditure is not immediately equivalent to productive capital. A growth-accounting extension needs stocks, service flows, depreciation, skill formation and justified factor weights. Household hardware and knowledge should not share one arbitrary depreciation rate.

The exported Solow-residual equation is not retained as an established identity. It combined hardware and skill growth under an unsupported shared weight and introduced an underived coordination term. The expenditure calculation does not by itself show that household learning explains the 1995–2005 productivity acceleration.

## 8. Reproducibility and next work

The accompanying model and CSV generate annual, period and sensitivity tables from one dataset. The baseline is a deterministic scenario.

1. Authenticate the annual inputs and identify interpolation.
2. Remove category overlap and employer reimbursements.
3. Estimate attribution, exposure and learning hours from evidence.
4. Measure household private returns.
5. Define employer avoided costs and the net-capture counterfactual.
6. Derive any stock/service model explicitly.
7. Test whether credible benefit sharing changes AI cooperation and net outcomes.

## References

The original bibliography below is retained as a source-recovery list. It does not imply that every market-size, time-use or novelty claim in the exported draft was verified in this revision.



* Acemoglu, D., & Pischke, J.-S. (1998). Why do firms train? Theory and evidence. *Quarterly Journal of Economics*, 113(1), 79–119.
* Acemoglu, D., & Pischke, J.-S. (1999). The structure of wages and investment in general training. *Journal of Political Economy*, 107(3), 539–572.
* America Online, Inc. / Time Warner Inc. (1994–2008). *Form 10-K Annual Reports Pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934*. Washington, DC: U.S. Securities and Exchange Commission.
* Autor, D. H., Katz, L. F., & Krueger, A. B. (1998). Computing inequality: Have computers changed the labor market? *Quarterly Journal of Economics*, 113(4), 1169–1213.
* Barrero, J. M., Bloom, N., & Davis, S. J. (2021). *Why working from home will stick* (NBER Working Paper No. 28731). Cambridge, MA: National Bureau of Economic Research.
* Becker, G. S. (1964). *Human Capital: A Theoretical and Empirical Analysis, with Special Reference to Education*. New York, NY: National Bureau of Economic Research / Columbia University Press.
* Becker, G. S. (1965). A theory of the allocation of time. *The Economic Journal*, 75(299), 493–517.
* Berndt, E. R., & Rappaport, N. J. (2001). Price and quality of desktop and mobile personal computers: A quarter-century historical overview. *American Economic Review*, 91(2), 268–273.
* Bianchi, S. M., Robinson, J. P., & Milkie, M. A. (2006). *Changing Rhythms of American Family Life*. New York, NY: Russell Sage Foundation.
* Bresnahan, T. F., Brynjolfsson, E., & Hitt, L. M. (2002). Information technology, workplace organization, and the demand for skilled labor: Firm-level evidence. *Quarterly Journal of Economics*, 117(1), 339–376.
* Bresnahan, T. F., & Trajtenberg, M. (1995). General purpose technologies: "Engines of growth"? *Journal of Econometrics*, 65(1), 83–108.
* Brynjolfsson, E., & Hitt, L. M. (2000). Beyond computation: Information technology, organizational transformation and business performance. *Journal of Economic Perspectives*, 14(4), 23–48.
* Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, 13(1), 333–372.
* Bureau of Economic Analysis (BEA). (2012). *National Income and Product Accounts (NIPA) Table 5.5.5: Private Fixed Investment in Information Processing Equipment and Software*. Washington, DC: U.S. Department of Commerce.
* Bureau of Labor Statistics (BLS). (2011). *Current Employment Statistics (CES): Average Hourly Earnings of Production and Nonsupervisory Employees, Total Private (Series CES0500000008)*. Washington, DC: U.S. Department of Labor.
* Bureau of Labor Statistics (BLS). (2011). *American Time Use Survey (ATUS) Microdata Files (2003–2010)*. Washington, DC: U.S. Department of Labor.
* Corrado, C., Hulten, C., & Sichel, D. (2005). Measuring capital and technology: An expanded framework. In *Measuring Capital in the New Economy* (pp. 11–46). Chicago, IL: University of Chicago Press.
* Corrado, C., Hulten, C., & Sichel, D. (2009). Intangible capital and U.S. economic growth. *Review of Income and Wealth*, 55(3), 661–685.
* David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. *American Economic Review*, 80(2), 355–361.
* Davies, M. W. (1982). *Woman's Place Is at the Typewriter: Office Work and Office Workers, 1870–1930*. Philadelphia, PA: Temple University Press.
* Day, J. C., Janus, A., & Davis, J. (2005). *Computer and Internet Use in the United States: 2003* (Current Population Reports, P23-208). Washington, DC: U.S. Census Bureau.
* DiNardo, J. E., & Pischke, J.-S. (1997). The returns to computer use revisited: Have pencils changed the wage structure too? *Quarterly Journal of Economics*, 112(1), 291–303.
* Federal Communications Commission (FCC). (2000–2011). *High-Speed Services for Internet Access: Status Reports (Form 477 Data)*. Washington, DC: Wireline Competition Bureau.
* Goldin, C., & Katz, L. F. (2008). *The Race between Education and Technology*. Cambridge, MA: Harvard University Press.
* Horrigan, J. B. (2008, 2010). *Home Broadband Adoption*. Washington, DC: Pew Internet & American Life Project.
* IDG Books Worldwide, Inc. (1999). *Form 10-K Annual Report*. Foster City, CA: U.S. Securities and Exchange Commission.
* Illich, I. (1981). *Shadow Work*. Boston, MA: Marion Boyars.
* Krueger, A. B. (1993). How computers have changed the wage structure: Evidence from microdata, 1984–1989. *Quarterly Journal of Economics*, 108(1), 33–60.
* Lambert, C. (2015). *Shadow Work: The Unpaid, Unseen Jobs That Fill Your Day*. Berkeley, CA: Counterpoint.
* Newburger, E. C. (2001). *Home Computers and Internet Use in the United States: August 2000* (Current Population Reports, P23-207). Washington, DC: U.S. Census Bureau.
* Robinson, J. P., & Godbey, G. (1997). *Time for Life: The Surprising Ways Americans Use Their Time*. University Park, PA: Pennsylvania State University Press.
* Small, K. A. (2012). Valuation of travel time. *Economics of Transportation*, 1(1–2), 2–14.
* Solow, R. M. (1987, July 12). We'd better watch out. *The New York Times Book Review*, p. 36.
* U.S. Census Bureau. (1985–2012). *Statistical Abstract of the United States* & *Current Industrial Reports: Computers and Office and Accounting Machines (Series MA35R/MQ35R)*. Washington, DC: U.S. Government Printing Office.