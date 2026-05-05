---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jim Bugwadia", "Nirmata", "Nischay Goyal", "JP Morgan Chase"]
sched_url: https://kccnceu2026.sched.com/event/2CW2L/audit-ready-kubernetes-how-chase-uk-leveraged-policy-as-code-for-continuous-compliance-jim-bugwadia-nirmata-nischay-goyal-jp-morgan-chase
youtube_search_url: https://www.youtube.com/results?search_query=Audit-Ready+Kubernetes%3A+How+Chase+UK+Leveraged+Policy+as+Code+for+Continuous+Compliance+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Audit-Ready Kubernetes: How Chase UK Leveraged Policy as Code for Continuous Compliance - Jim Bugwadia, Nirmata & Nischay Goyal, JP Morgan Chase

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jim Bugwadia, Nirmata, Nischay Goyal, JP Morgan Chase
- Schedule: https://kccnceu2026.sched.com/event/2CW2L/audit-ready-kubernetes-how-chase-uk-leveraged-policy-as-code-for-continuous-compliance-jim-bugwadia-nirmata-nischay-goyal-jp-morgan-chase
- Busca YouTube: https://www.youtube.com/results?search_query=Audit-Ready+Kubernetes%3A+How+Chase+UK+Leveraged+Policy+as+Code+for+Continuous+Compliance+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Audit-Ready Kubernetes: How Chase UK Leveraged Policy as Code for Continuous Compliance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2L/audit-ready-kubernetes-how-chase-uk-leveraged-policy-as-code-for-continuous-compliance-jim-bugwadia-nirmata-nischay-goyal-jp-morgan-chase
- YouTube search: https://www.youtube.com/results?search_query=Audit-Ready+Kubernetes%3A+How+Chase+UK+Leveraged+Policy+as+Code+for+Continuous+Compliance+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=B01BQ60PLqM
- YouTube title: Audit-Ready Kubernetes: How Chase UK Leveraged Policy as Code for Co... Jim Bugwadia & Nischay Goyal
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/audit-ready-kubernetes-how-chase-uk-leveraged-policy-as-code-for-conti/B01BQ60PLqM.txt
- Transcript chars: 28001
- Keywords: policy, kyverno, policies, actually, resources, cluster, security, reporting, platform, resource, compliance, always, write, environment, running, engineers, mentioned, process

### Resumo baseado na transcript

Today, we're going to talk about getting your Kubernetes clusters audit ready. And of course, as platform engineers, our focus is going to be on how you can automate this process as much as possible. I think the first key thing is when you think about Kubernetes, suddenly we start thinking about scalability, reliability, networking, all these challenges. So, it was launched back in September 2021, and in less than 5 years, we have more than 2.5 million customers, with 20 billion plus deposits as customers' money, and this is the scale what we are working upon. And this is where things gets interesting if you merge that scale of the customers with the technology scale we are running at. Your security teams, your auditor teams, or some other teams are coming and asking you questions about how you're doing this in your environment.

### Excerpt da transcript

Today, we're going to talk about getting your Kubernetes clusters audit ready. And of course, as platform engineers, our focus is going to be on how you can automate this process as much as possible. So, in terms of the topics what we'll cover, first we'll go over some of the key challenges that you see in regulated environments, what it means to get audit ready, and also some of the, you know, decision processes involved. Then we're going to talk about one of the key tools today, which will be Kyverno, a policy engine which we'll use for, you know, the audit and compliance process. And then finally, we'll go through the full stack and and talk a little bit about what other tools are involved, how you can, you know, do this end to end. So, quick introductions. I'm Jim Bugwadia, co-founder CEO at Nirmata, and also a maintainer of Kyverno. And along with me, I have Nishant. Um thanks, Jim. Hi, guys. I'm Nishant Goel, working as a senior lead platform engineer at JP Morgan Chase, and specifically for Chase UK.

Glad to be here. So, as Jim mentioned, we're going to talk about Kubernetes in a highly regulated environment, right? I think the first key thing is when you think about Kubernetes, suddenly we start thinking about scalability, reliability, networking, all these challenges. But when we are in banking or in financial regulatory industry, the first thing is will this pass an audit? That's the first thing what we think about, right? With that, who are we? Chase UK, right? So, it was launched back in September 2021, and in less than 5 years, we have more than 2.5 million customers, with 20 billion plus deposits as customers' money, and this is the scale what we are working upon. Now, along with that, think about thousands of nodes with multiple clusters, around 15 our environment running in different environments with different configurations. And this is where things gets interesting if you merge that scale of the customers with the technology scale we are running at. Now, if you think about when you are in this financial regulated environment, right?

There's always strong audit expectations, because you're actually working for the real customer money. You want to protect their money as well, right? And if you've been in this space, you know that speed and sort of where engineering teams want to ship fast independently because they want to go to market, versus with expectations of are they secure, are they safe, are they compliant? So, we as platform eng
