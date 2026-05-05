---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Andrew Newdigate", "GitLab"]
sched_url: https://kccnceu2021.sched.com/event/iE3d/how-we-are-dealing-with-metrics-at-scale-on-gitlabcom-andrew-newdigate-gitlab
youtube_search_url: https://www.youtube.com/results?search_query=How+We+are+Dealing+with+Metrics+at+Scale+on+GitLab.com+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How We are Dealing with Metrics at Scale on GitLab.com - Andrew Newdigate, GitLab

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Andrew Newdigate, GitLab
- Schedule: https://kccnceu2021.sched.com/event/iE3d/how-we-are-dealing-with-metrics-at-scale-on-gitlabcom-andrew-newdigate-gitlab
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+are+Dealing+with+Metrics+at+Scale+on+GitLab.com+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How We are Dealing with Metrics at Scale on GitLab.com.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3d/how-we-are-dealing-with-metrics-at-scale-on-gitlabcom-andrew-newdigate-gitlab
- YouTube search: https://www.youtube.com/results?search_query=How+We+are+Dealing+with+Metrics+at+Scale+on+GitLab.com+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6sfr2IGJQXk
- YouTube title: How We are Dealing with Metrics at Scale on GitLab.com - Andrew Newdigate, GitLab
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-we-are-dealing-with-metrics-at-scale-on-gitlab-com/6sfr2IGJQXk.txt
- Transcript chars: 18431
- Keywords: metrics, prometheus, alerts, slo, monitoring, recording, dashboards, single, thanos, approach, alerting, component, dashboard, configuration, better, instances, instead, requests

### Resumo baseado na transcript

welcome this session is how we're dealing with metrics at scale on gitlab.com my name is andrew nudigate and i'm an engineer at gitlab where i work in the infrastructure team and i help work help build gitlab.com this talk is about how we've scaled our monitoring to support a site that has over the past few years grown rapidly in size and complexity to illustrate that growth here are some figures to show how things have changed since i joined back in 2017 we'd only recently adopted prometheus and easier for operators and engineers to understand and in particular reducing the time to diagnosis on our slo alerts one of the big differences between the old way that we alerted with causal alerts and our slo loads is that when an slo alert fires it's not always immediately apparent what the problem is it's up to the operator to understand the sli then investigate the problem by digging through metrics logs and other signals until the cause becomes apparent so our goal here is to give the operator the

### Excerpt da transcript

welcome this session is how we're dealing with metrics at scale on gitlab.com my name is andrew nudigate and i'm an engineer at gitlab where i work in the infrastructure team and i help work help build gitlab.com this talk is about how we've scaled our monitoring to support a site that has over the past few years grown rapidly in size and complexity to illustrate that growth here are some figures to show how things have changed since i joined back in 2017 we'd only recently adopted prometheus and were migrating off influx db we had a single prometheus server six infrastructure engineers a handful of alerting rules and recording rules we only had 21 dashboards and we were processing about 100 000 samples per second roll forward 400 years and we now run thanos federated cluster deployed into kubernetes using tanka the infrastructure department is around 40 people so six times bigger we have over 2 600 recording rules 400 grafana dashboards and we're ingesting about 2.8 million samples per second so it's important to state this what worked for us then worked fine for us at that scale it was the right solution at the time but that approach wouldn't work for us now and this talk is about some of the tools and techniques that we've used to go from that scale to where we are today so what prompted our efforts to improve our alerting we were seeing numerous problems that indicated that our approach to monitoring was no longer working for us one of these problems was low precision alerting by this we mean that the proportion of alerts that was actionable was low and we're seeing a high number of false positives at any time many of the alerting rules inadvertently generated low quality unactionable flappy alerts very often the engineer on call would determine that users were not being impacted that everything seemed okay and they would acknowledge the alert and effectively ignore it not only was the precision of our alerts very poor but so was the recall recall refers to the proportion of user impacting events that are detected by the alerting system this means that instead of finding out about incidents through an alert we would sometimes be made aware of the incident by people rather than the software that we'd built to detect these incidents in other cases the alert would fire but too late and we already knew that there was a problem and now it was just extra noise while we were trying to solve the issue yet another problem we found was that the dashboards were v
