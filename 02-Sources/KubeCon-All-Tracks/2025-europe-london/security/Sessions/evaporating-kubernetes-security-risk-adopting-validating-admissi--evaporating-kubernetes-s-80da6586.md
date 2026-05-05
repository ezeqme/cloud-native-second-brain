---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Kaitlyn Lee", "Jordan Conard", "Datadog"]
sched_url: https://kccnceu2025.sched.com/event/1txFk/evaporating-kubernetes-security-risk-adopting-validating-admission-policy-at-scale-kaitlyn-lee-jordan-conard-datadog
youtube_search_url: https://www.youtube.com/results?search_query=EVAPorating+Kubernetes+Security+Risk%3A+Adopting+Validating+Admission+Policy+at+Scale+CNCF+KubeCon+2025
slides: []
status: parsed
---

# EVAPorating Kubernetes Security Risk: Adopting Validating Admission Policy at Scale - Kaitlyn Lee & Jordan Conard, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Kaitlyn Lee, Jordan Conard, Datadog
- Schedule: https://kccnceu2025.sched.com/event/1txFk/evaporating-kubernetes-security-risk-adopting-validating-admission-policy-at-scale-kaitlyn-lee-jordan-conard-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=EVAPorating+Kubernetes+Security+Risk%3A+Adopting+Validating+Admission+Policy+at+Scale+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre EVAPorating Kubernetes Security Risk: Adopting Validating Admission Policy at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFk/evaporating-kubernetes-security-risk-adopting-validating-admission-policy-at-scale-kaitlyn-lee-jordan-conard-datadog
- YouTube search: https://www.youtube.com/results?search_query=EVAPorating+Kubernetes+Security+Risk%3A+Adopting+Validating+Admission+Policy+at+Scale+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OJ1WoQjYAJo
- YouTube title: EVAPorating Kubernetes Security Risk: Adopting Validating Admission P... Kaitlyn Lee & Jordan Conard
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/evaporating-kubernetes-security-risk-adopting-validating-admission-pol/OJ1WoQjYAJo.txt
- Transcript chars: 25936
- Keywords: policy, admission, policies, validating, security, resources, validation, expression, resource, gatekeeper, capabilities, little, expressions, cost, finally, single, variable, parameter

### Resumo baseado na transcript

This is evaporating Kubernetes security risk, adopting validation admission policy at scale. Um, and I work on one of our compute teams helping secure our Kubernetes control planes. So, for a little bit of background of Kubernetes here at Data Dog, we have over 2,000 employees in our engineering organization. So as such we need a granular and configurable set of security policies to match our heterogeneous workloads. And so data dog's kind of history with admission policy starts around 2020 when uh pod security policies were being deprecated uh out of kubernetes. we were looking for a replacement at the time and uh pod security and mission uh just wasn't going to be a great fit for us.

### Excerpt da transcript

Well, hello CubeCon. Thanks for saving the best talk for last. This is evaporating Kubernetes security risk, adopting validation admission policy at scale. Uh, my name is Jordan Connard. I'm a security engineer here at Data Dog. Um, and I work on one of our compute teams helping secure our Kubernetes control planes. And I'm Kaitlin Lee, a software engineer also on the comput team here at Data Dog. Um I started on the control plane team and now I focus on our workload autoscaling. Um but here at data dog we've been working with validating admission policy for a little over a year now. So today we wanted to come here and show you how you can take some tutorial policies and transform them into fully adopted validating admission policy at scale. Quick overview of what we're going to talk about today. So we're going to start out with just a little bit about what Kubernetes means at data dog. Uh then we'll transition into data dog's history with admission control kind of our motivations for migrating to validate admission policy.

We'll dive into one of our policies and kind of take it from what you might get out of the box in a tutorial into something that we feel uh is good enough to deploy out into production. Uh next we'll cover a few migration uh and monitoring strategies that we've used. And finally, we'll wrap up with some teasers to uh some day two operations and kind of next steps. So, for a little bit of background of Kubernetes here at Data Dog, we have over 2,000 employees in our engineering organization. We run multicloud with over a 100 clusters, over 10,000 nodes, and over a 100,000 pods. So, every single one of our workloads runs on Kubernetes. So it's not just our infrastructure but also all of our platforms and all of our applications. So as such we need a granular and configurable set of security policies to match our heterogeneous workloads. And so data dog's kind of history with admission policy starts around 2020 when uh pod security policies were being deprecated uh out of kubernetes. we were looking for a replacement at the time and uh pod security and mission uh just wasn't going to be a great fit for us.

Uh so around the time OPA gatekeeper was kind of the go-to default solution um in the ecosystem at the time and that's ultimately what we began with just a quick overview. OPA gatekeeper OPA or open policy agent uh is a graduated CNCF project. It aims to be a generalpurpose policy engine. Um, it primarily uses the Rego language to writ
