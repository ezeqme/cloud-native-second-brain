---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sunny Beatteay", "Airbnb"]
sched_url: https://kccnceu2026.sched.com/event/2EMyb/1000-services-1-year-0-downtime-airbnbs-zonal-cluster-migration-sunny-beatteay-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=1000+Services%2C+1+Year%2C+0+Downtime%3A+Airbnb%E2%80%99s+Zonal+Cluster+Migration+CNCF+KubeCon+2026
slides: []
status: parsed
---

# 1000 Services, 1 Year, 0 Downtime: Airbnb’s Zonal Cluster Migration - Sunny Beatteay, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sunny Beatteay, Airbnb
- Schedule: https://kccnceu2026.sched.com/event/2EMyb/1000-services-1-year-0-downtime-airbnbs-zonal-cluster-migration-sunny-beatteay-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=1000+Services%2C+1+Year%2C+0+Downtime%3A+Airbnb%E2%80%99s+Zonal+Cluster+Migration+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre 1000 Services, 1 Year, 0 Downtime: Airbnb’s Zonal Cluster Migration.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EMyb/1000-services-1-year-0-downtime-airbnbs-zonal-cluster-migration-sunny-beatteay-airbnb
- YouTube search: https://www.youtube.com/results?search_query=1000+Services%2C+1+Year%2C+0+Downtime%3A+Airbnb%E2%80%99s+Zonal+Cluster+Migration+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N3NTyUeSlaA
- YouTube title: 1000 Services, 1 Year, 0 Downtime: Airbnb’s Zonal Cluster Migration - Sunny Beatteay, Airbnb
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/1000-services-1-year-0-downtime-airbnbs-zonal-cluster-migration/N3NTyUeSlaA.txt
- Transcript chars: 27996
- Keywords: migration, essentially, cluster, regional, clusters, traffic, migrate, developers, basically, actually, running, wanted, multiple, airbnb, deployment, deployments, region, migrated

### Resumo baseado na transcript

As you can see from my top slide, my name is Sunny B, and today I'll be presenting to you 1,000 services, 1 year, zero downtime, Airbnb's zonal cluster migration. So, this is going to be a case study going over Airbnb's largest zonal cluster migration to date. Which is why when Airbnb itself decided to and have had discussions, we also decided to go with a regional architecture. For our deployments or our services, normally it was a deployment with a single horizontal pod auto auto scaler allowing to scale up and scale down, as well as a pod topology spread to allow pods to balance across the multiple AZs. Uh, we scaled up, our customer base grew, and the scale architecture scaled up with it. And so, around uh, 2023 when we had about 1,000 services running on this architecture.

### Excerpt da transcript

Um, so thank you everyone for joining me. As you can see from my top slide, my name is Sunny B, and today I'll be presenting to you 1,000 services, 1 year, zero downtime, Airbnb's zonal cluster migration. So, this is going to be a case study going over Airbnb's largest zonal cluster migration to date. I can say it's the largest cuz it's the only one we've done. Hopefully the only one we'll ever do. Um, while I'm your presenter, I'm just one piece of a larger team that did this effort. So, I just want to give them a quick shout out cuz as you'll see through this talk, we went through quite the ordeal together. Um, so since the KubeCon schedule went live, I've had a handful of people communicate to me saying they've had similar discussions in their teams around should they adopt a regional or a zonal architecture. In every case, although ultimately they picked going with a regional, which is more than fair cuz I honestly if you were to ask me, I'd probably say 99 times out of 100, you should do the same.

Uh, regional clusters are much easier to just reason about. You have for infra structure engineers, you have the one control plane spread across multiple AZs, giving you a high availability high availability setup. And same with the app developers, very similar. You have one deployments usually with possibly HPA. Um, you just scale up and scale down. So, you in both cases you have a singleton workload but still highly available. So, it's pretty good deal. And reason why AWS itself recommends this kind of architecture. Contrast that with a zonal where you have instead of having one cluster running across the entire region, you have a separate clusters per AZ. So, for infra engineers, you're dealing with multiple control plane APIs, and then essentially with your app developers, you're also dealing with essentially sharded workloads. So, instead of having one deployment image, you now have multiple. And so, you're adding a lot more complexity to your system. Which is why when Airbnb itself decided to and have had discussions, we also decided to go with a regional architecture.

And so, we essentially we had our setup kind of typical way, uh, control plane APIs spread across multiple AZs. For our deployments or our services, normally it was a deployment with a single horizontal pod auto auto scaler allowing to scale up and scale down, as well as a pod topology spread to allow pods to balance across the multiple AZs. And from about 2018 to 2023, the service ver
