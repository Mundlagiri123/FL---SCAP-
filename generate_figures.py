"""Reproducible FL-SCAP figures. Source CSVs supplied by researcher, not independently rerun.
Run: python generate_figures.py
Requires: pandas, numpy, matplotlib. Generates PNG (300 dpi) and SVG plots.
"""
from pathlib import Path
import numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'; OUT=ROOT/'figures'; OUT.mkdir(exist_ok=True)
KEEP=['Static','Greedy','GA','PSO','DQN','PPO','COS-DQN','FL-SCAP']

def df(name): return pd.read_csv(DATA/name)
def val(v):
    if isinstance(v,(int,float,np.number)): return float(v)
    return float(str(v).split('±')[0].strip())
def err(v):
    s=str(v)
    return float(s.split('±')[1].strip()) if '±' in s else 0.0
def save(fig,stem):
    fig.savefig(OUT/(stem+'.png'),dpi=300,bbox_inches='tight')
    fig.savefig(OUT/(stem+'.svg'),bbox_inches='tight')
    plt.close(fig)
def filtered(d): return d[d.Algorithm.isin(KEEP)].set_index('Algorithm').reindex(KEEP)

def bar_metric(name,col,stem,ylabel,title):
    d=filtered(df(name)); y=np.array([val(v) for v in d[col]]); e=np.array([err(v) for v in d[col]])
    fig,ax=plt.subplots(figsize=(10,4.8)); ax.bar(range(len(y)),y,yerr=e,capsize=3,edgecolor='none')
    ax.set_xticks(range(len(y)),d.index,rotation=25,ha='right');ax.set_ylabel(ylabel);ax.set_title(title)
    ax.grid(axis='y',alpha=.25);ax.set_axisbelow(True)
    fig.text(.5,-.012,'Source: uploaded FL-SCAP CSVs. Error bars: reported seed-level SD; no new simulation performed.',ha='center',fontsize=8)
    save(fig,stem)

# 01 schematic: illustrates software modules, not a simulator-generated topology capture
fig,ax=plt.subplots(figsize=(10,5.3));ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis('off')
blocks=[(0.4,4.35,2.45,.95,'20 FL clients\nnon-IID MNIST'),(3.72,4.35,2.45,.95,'4 Fog nodes\n4 microservices'),(7.05,4.35,2.45,.95,'Global coordinator\nFedAvg'),(3.72,2.55,2.45,.85,'Objective-1 telemetry\nRCT, PR, SR, FRU...'),(3.72,.65,2.45,.9,'FL-SCAP\nStress + GRU + masked DDQN')]
for x,y,w,h,t in blocks:
    box=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#e8eef5',edgecolor='#536878',linewidth=1.1);ax.add_patch(box)
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=11)
for a,b in [((2.96,4.82),(3.61,4.82)),((6.3,4.82),(6.95,4.82)),((4.945,4.3),(4.945,3.54)),((4.945,2.48),(4.945,1.65))]:
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,linewidth=1.5))
ax.add_patch(FancyArrowPatch((3.7,1.05),(2.45,4.23),arrowstyle='-|>',mutation_scale=14,linewidth=1.3,connectionstyle='arc3,rad=-.28'))
ax.text(1.35,2.35,'orchestration action',fontsize=9,rotation=66)
ax.set_title('Implementation-aligned FL-SCAP system schematic',fontsize=14)
save(fig,'01_system_architecture_schematic')

# 02 algorithm pipeline
fig,ax=plt.subplots(figsize=(11,3.2));ax.set_xlim(0,12.4);ax.set_ylim(0,3.4);ax.axis('off')
parts=['Observe\nFL metrics','Encode\nstress','Predict\nper action','Estimate\nuncertainty','Masked\nDouble DQN','Execute /\nNoOp']
for j,t in enumerate(parts):
 x=.2+2.05*j;box=FancyBboxPatch((x,1.2),1.78,1,boxstyle='round,pad=.08',facecolor='#ebf0f6',edgecolor='#566a7b');ax.add_patch(box);ax.text(x+.89,1.7,t,ha='center',va='center',fontsize=10)
 if j<5:ax.add_patch(FancyArrowPatch((x+1.8,1.7),(x+2.03,1.7),arrowstyle='-|>',mutation_scale=12))
ax.text(6.2,.62,'Executed action changes the fog environment; next FL round supplies new observations.',ha='center',fontsize=10)
ax.set_title('FL-SCAP decision pipeline (method schematic)',fontsize=14)
save(fig,'02_flscap_decision_pipeline')

bar_metric('table6a_overall_fl.csv','RCT_mean','03_mean_round_completion_time','RCT (s)','Mean round completion time by algorithm')
bar_metric('table6a_overall_fl.csv','SR','04_straggler_ratio','Straggler ratio','Straggler ratio')
bar_metric('table6b_overall_fog.csv','peak_cpu','05_peak_cpu','CPU utilization (fraction)','Peak CPU utilization')
bar_metric('table8_orchestration.csv','unnecessary','06_unnecessary_actions','Unnecessary actions per episode','Unnecessary orchestration actions')
bar_metric('table8_orchestration.csv','mig_cost','07_migration_cost','Migration cost (reported units)','Migration cost')

# 08 by-scenario heatmap, using actual reported RCT
p=df('table7_per_scenario.csv');p=p[p.Algorithm.isin(KEEP)].copy();p['mean']=p.RCT.map(val)
q=p.pivot(index='Algorithm',columns='Scenario',values='mean').reindex(KEEP)
fig,ax=plt.subplots(figsize=(9,5.3));im=ax.imshow(q.values,aspect='auto',cmap='viridis');ax.set_xticks(range(len(q.columns)),q.columns);ax.set_yticks(range(len(q.index)),q.index)
for (i,j),v in np.ndenumerate(q.values):ax.text(j,i,f'{v:.2f}',ha='center',va='center',color='white' if v>np.nanmedian(q.values) else 'black',fontsize=8)
fig.colorbar(im,ax=ax,label='Mean RCT (s)');ax.set_title('Round completion time by stress scenario')
save(fig,'08_scenario_RCT_heatmap')

# 09 prediction errors
p=df('table5_predictor.csv');fig,ax=plt.subplots(figsize=(9,4.4));x=np.arange(len(p));w=.36
ax.bar(x-w/2,p.RCT_MAE,w,label='RCT MAE');ax.bar(x+w/2,p.RCT_RMSE,w,label='RCT RMSE')
ax.set_xticks(x,p.Model,rotation=15,ha='right');ax.set_ylabel('Seconds');ax.set_title('Next-round RCT prediction errors (held-out data)');ax.legend();ax.grid(axis='y',alpha=.2);save(fig,'09_predictor_errors')

# 10 ablation without OA
p=df('table9_ablation.csv');p=p[p.Algorithm.str.startswith('FL-SCAP')].copy();fig,ax=plt.subplots(figsize=(8.6,4.5));
labels={'FL-SCAP-noStress':'No stress','FL-SCAP-noUnc':'No uncertainty','FL-SCAP-noSafe':'No safeguards','FL-SCAP':'Full FL-SCAP'}
p['label']=p.Algorithm.map(labels);y=p.RCT_mean.map(val);e=p.RCT_mean.map(err)
ax.bar(p.label,y,yerr=e,capsize=4);ax.set_ylabel('Mean RCT (s)');ax.set_title('FL-SCAP ablation: reported RCT');ax.tick_params(axis='x',labelrotation=12);ax.grid(axis='y',alpha=.2);save(fig,'10_flscap_ablation')

# 11 scalability
p=df('table11_scalability.csv');p=p[p.Algorithm.isin(['Greedy','GA','DQN','FL-SCAP'])].copy();p['mean']=p.RCT.map(val)
fig,ax=plt.subplots(figsize=(8,4.8)); order=['20 clients / 4 fogs','50 clients / 8 fogs','100 clients / 12 fogs']
for alg,g in p.groupby('Algorithm'):
 g=g.set_index('Topology').reindex(order);ax.plot(range(3),g['mean'],marker='o',label=alg)
ax.set_xticks(range(3),['20/4','50/8','100/12']);ax.set_xlabel('Clients / fog nodes');ax.set_ylabel('Mean RCT (s)');ax.legend();ax.grid(alpha=.2);ax.set_title('RCT with increasing system size')
save(fig,'11_scalability_RCT')

# 12 learning vs resource QoS tradeoff
p=filtered(df('table8_orchestration.csv'));fig,ax=plt.subplots(figsize=(8,5))
for a,row in p.iterrows():
 x=val(row['mig_cost']);y=val(row['sla_rate']);ax.scatter(x,y,s=65);ax.annotate(a,(x,y),xytext=(5,3),textcoords='offset points',fontsize=9)
ax.set_xlabel('Migration cost (reported units)');ax.set_ylabel('SLA violation rate');ax.set_title('Migration-cost and SLA trade-off');ax.grid(alpha=.2)
save(fig,'12_migration_SLA_tradeoff')
print('Generated',len(list(OUT.glob('*.png'))),'PNG files and SVG counterparts')
