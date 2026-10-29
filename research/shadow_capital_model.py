"""Reconciled deterministic scenario; provisional historical input arrays."""
import json, csv, argparse
from pathlib import Path
def calculate(data, attribution=.4, weekly_hours=1.5, wage_factor=.75, include_ancillary=True):
    if not 0<=attribution<=1 or weekly_hours<0 or not 0<=wage_factor<=1: raise ValueError("Invalid parameters")
    keys=list(data)
    out=[]
    for i,y in enumerate(range(1980,2011)):
        v=[data[k][i] for k in keys]
        cash=attribution*sum(v[1:5 if include_ancillary else 4])
        time=v[5]*52*weekly_hours*wage_factor*v[6]/1000
        out.append(dict(year=y,corporate=v[0],direct=cash,time=time,combined=cash+time))
    return out
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--attribution",type=float,default=.4)
    p.add_argument("--weekly-hours",type=float,default=1.5)
    p.add_argument("--wage-factor",type=float,default=.75)
    p.add_argument("--exclude-ancillary",action="store_true")
    p.add_argument("--output",type=Path,default=Path("scenario.csv"))
    a=p.parse_args()
    data=json.loads(Path(__file__).with_name("reconciled_inputs.json").read_text(encoding="utf-8"))
    rows=calculate(data,a.attribution,a.weekly_hours,a.wage_factor,not a.exclude_ancillary)
    with a.output.open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    totals={k:sum(r[k] for r in rows) for k in ("corporate","direct","time","combined")}
    print(json.dumps(dict(totals_billions_nominal_usd=totals,combined_percent=100*totals["combined"]/totals["corporate"]),indent=2))
