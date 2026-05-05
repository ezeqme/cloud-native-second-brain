---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Florian Hopfensperger", "Allianz Technology", "Yury Tsarev", "Upbound"]
sched_url: https://kccnceu2026.sched.com/event/2CVxV/api-driven-infrastructure-as-code-kubernetes-apis-as-the-contract-bridge-between-teams-florian-hopfensperger-allianz-technology-yury-tsarev-upbound
youtube_search_url: https://www.youtube.com/results?search_query=API-Driven+Infrastructure+as+Code%3A+Kubernetes+APIs+as+the+Contract+Bridge+Between+Teams+CNCF+KubeCon+2026
slides: []
status: parsed
---

# API-Driven Infrastructure as Code: Kubernetes APIs as the Contract Bridge Between Teams - Florian Hopfensperger, Allianz Technology & Yury Tsarev, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Florian Hopfensperger, Allianz Technology, Yury Tsarev, Upbound
- Schedule: https://kccnceu2026.sched.com/event/2CVxV/api-driven-infrastructure-as-code-kubernetes-apis-as-the-contract-bridge-between-teams-florian-hopfensperger-allianz-technology-yury-tsarev-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=API-Driven+Infrastructure+as+Code%3A+Kubernetes+APIs+as+the+Contract+Bridge+Between+Teams+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre API-Driven Infrastructure as Code: Kubernetes APIs as the Contract Bridge Between Teams.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxV/api-driven-infrastructure-as-code-kubernetes-apis-as-the-contract-bridge-between-teams-florian-hopfensperger-allianz-technology-yury-tsarev-upbound
- YouTube search: https://www.youtube.com/results?search_query=API-Driven+Infrastructure+as+Code%3A+Kubernetes+APIs+as+the+Contract+Bridge+Between+Teams+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=X2URIOhA6_g
- YouTube title: API-Driven Infrastructure as Code: Kubernetes APIs as the Con... Florian Hopfensperger & Yury Tsarev
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/api-driven-infrastructure-as-code-kubernetes-apis-as-the-contract-brid/X2URIOhA6_g.txt
- Transcript chars: 26740
- Keywords: provider, product, already, contract, database, crossplane, resources, control, customers, create, subscription, instance, platform, actually, customer, infrastructure, landing, manage

### Resumo baseado na transcript

Hello and welcome to our talk APIdriven infrastructures code Kubernetes APIs as a contact bridge between teams. I work for Alian technology as an lead engineer and I'm happy to share the stage with my dear friend. we enabled now across um all these products we enabled self uh self selfservice signup and therefore we have around thousand plus control planes which are used by the customers so they are using then the kubernetes API to to manage their infrastructure so and Right now we have this unified interface um where we use like um Kubernetes and in the GitHub the customers manage their automation and then Argus CD synchronized it to the control plane itself. So, let me let me show you just a quick overview of the architecture what we built. So each customer more or less has their dedicated control plane where they can then manage the infrastructure and obviously there are a lot of other components which are help us to provide the service um cubeep metrics for collecting metrics doing some reporting and

### Excerpt da transcript

Hello and welcome to our talk APIdriven infrastructures code Kubernetes APIs as a contact bridge between teams. Now I know a very long title but we get into it. My name is Floren Hoffinsburgger. I work for Alian technology as an lead engineer and I'm happy to share the stage with my dear friend. >> Hi everybody. I'm Yuri from Abound and we are creators of crossplane. So before we get started, we have a tradition to make a silly selfie with >> silly selfie. >> Nice but silly. Silly but nice together with an audience. So give us if you give us Yeah. some sign of excitement that would be great. >> Yeah. Yeah. >> Thank you so much. I appreciate it. >> Um just side info um this talk has an reference to a talk which we did last year in India. So if you if you want to deep a little bit more dive into the plat into the platform or what we built check the talk and at that talk we showed what the platform is doing. Today we want to to show you how actually teams are working on this platform. So a quick recap before we go into so I always like to compare our platform as eBay.

Okay. So, eBay has on the one hand side some some people who want to sell their products, right? So, we see on the left side, this is in our case the so-called product team. They want to sell the automation products and on the other side we have the application team. So, the actual customer who wants to to buy this product, right? And we are in the middle of this of this circle. We are um part of the the platform team. we operate and develop their platform. So so clear and on the left side the product team we have not only one product team we have multiple product teams obviously right and we are only serving internal customers so we are not exposed to the worldwide only internal just let me show you some result what we achieved the last four years since we started building up the platform so you can imagine in an in an enterprise um company like Alian everybody has like their own way to to sign you up right so what we enabled now across um all these products we enabled self uh self selfservice signup and therefore we have around thousand plus control planes which are used by the customers so they are using then the kubernetes API to to manage their infrastructure so and this comes to the second point we offer now on unified interface previously you can imagine when you have 15 20 product teams everybody has their own interface for one you need to create the GitHub issue for the other one you n
