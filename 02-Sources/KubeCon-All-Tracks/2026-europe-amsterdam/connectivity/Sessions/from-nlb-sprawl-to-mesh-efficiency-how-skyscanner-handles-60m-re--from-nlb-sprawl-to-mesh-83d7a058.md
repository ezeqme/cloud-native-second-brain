---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Connectivity"
themes: ["AI ML", "Networking"]
speakers: ["John Clark", "Skyscanner", "Steven Thwaites", "Solo.io"]
sched_url: https://kccnceu2026.sched.com/event/2CVxS/from-nlb-sprawl-to-mesh-efficiency-how-skyscanner-handles-60m-requests-per-minute-with-istio-john-clark-skyscanner-steven-thwaites-soloio
youtube_search_url: https://www.youtube.com/results?search_query=From+NLB+Sprawl+To+Mesh+Efficiency%3A+How+Skyscanner+Handles+60M+Requests+Per+Minute+With+Istio+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From NLB Sprawl To Mesh Efficiency: How Skyscanner Handles 60M Requests Per Minute With Istio - John Clark, Skyscanner & Steven Thwaites, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: John Clark, Skyscanner, Steven Thwaites, Solo.io
- Schedule: https://kccnceu2026.sched.com/event/2CVxS/from-nlb-sprawl-to-mesh-efficiency-how-skyscanner-handles-60m-requests-per-minute-with-istio-john-clark-skyscanner-steven-thwaites-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=From+NLB+Sprawl+To+Mesh+Efficiency%3A+How+Skyscanner+Handles+60M+Requests+Per+Minute+With+Istio+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From NLB Sprawl To Mesh Efficiency: How Skyscanner Handles 60M Requests Per Minute With Istio.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxS/from-nlb-sprawl-to-mesh-efficiency-how-skyscanner-handles-60m-requests-per-minute-with-istio-john-clark-skyscanner-steven-thwaites-soloio
- YouTube search: https://www.youtube.com/results?search_query=From+NLB+Sprawl+To+Mesh+Efficiency%3A+How+Skyscanner+Handles+60M+Requests+Per+Minute+With+Istio+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2ZvvGdHfknM
- YouTube title: From NLB Sprawl To Mesh Efficiency: How Skyscanner Handles 60M Reque... John Clark & Steven Thwaites
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-nlb-sprawl-to-mesh-efficiency-how-skyscanner-handles-60m-requests/2ZvvGdHfknM.txt
- Transcript chars: 25633
- Keywords: cluster, clusters, multicluster, ambient, gateway, everything, single, sidecar, mesh, gateways, waypoint, tunnel, skyscanner, another, traffic, having, server, request

### Resumo baseado na transcript

Um, today we're going to be talking about how Sky Scanner have made their mesh more efficient by moving from load balancers through to multicluster and then through to ambient mesh. I'm a senior software engineer at Skyscanner with a focus on Kubernetes and STO. The control plane SDOD watches for changes in the Kubernetes API server and then it generates envoy uh proxy configs and certificates and then pushes them down to each of those proxies over XDS. So main reasons people will adopt will be around you know connecting services securing them controlling their behavior and getting observab observability benefits and most what we see at solo is that people will adopt for one of those reasons probably security or observability and um they get automatic failover so they can if the request hits a cluster that's having problems it will automatically bounce over to another cluster and this all happens in in a single request behind Sky Scanner IO to go into a bit more of But when more and more services start to use this architecture, those costs quickly started to go up until they cost 10% of our entire cloud bill.

### Excerpt da transcript

Good morning. Um, today we're going to be talking about how Sky Scanner have made their mesh more efficient by moving from load balancers through to multicluster and then through to ambient mesh. A little bit more about me. My name is John. I'm a senior software engineer at Skyscanner with a focus on Kubernetes and STO. Hi everyone, I'm Steven. I'm a solutions architect at Solo. um and I work with my team and with Skyscanner on their ISTO feature needs and designs. >> So uh a bit more about Skyscanner. We run everything across four production regions. Each region gets six um clusters that we run on AWS. We split these across our availability zones. So each a gets two clusters that we keep isolated into the a we fully on spot with Carpenter. We connect everything together across the globe with ISTO and um we yeah we serve about 600 services at any given time 35,000 pods and about 60 million requests a minute. So going back to the origins of how Skyscanner set up their mesh um in 2019 we have a project globe which is essentially to modernize what our mixed cluster ECS mix was.

We've decided to split large clusters into smaller single A clusters to reduce our blast radius, allow us to do phased upgrades without risking breaking a whole region. One of the challenges with doing something like that with splitting out clusters is how do you connect everything together? So at the time we chose ESTO and STO 1.4 which gave us MTLS. It gives us all the DNS abstraction that we want and telemetry out the box. So Steven's going to talk a bit more about itself. Yeah. So many of you will already be familiar with STTO. So I'll keep this really brief and just tie it into Sky Scanner story. Soto sits your in your infrastructure layer and it handles all of your servicetoervice traffic transparently. So you your application doesn't really know it's there. You don't need to add any libraries or any SDKs and no code changes. A sidecar proxy is injected into each pod in the mesh. Um and that from that point forward every bite benefits from having uh being secured with mutual TLS. Um it emits telemetry so everything is observable.

Um and is controllable as well. You can control how the map traffic moves. The control plane SDOD watches for changes in the Kubernetes API server and then it generates envoy uh proxy configs and certificates and then pushes them down to each of those proxies over XDS. So main reasons people will adopt will be around you know connecting services securi
