---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Naveen Mogulla", "TikTok"]
sched_url: https://kccnceu2024.sched.com/event/1YeSX/tiktoks-edge-symphony-scaling-beyond-boundaries-with-multi-cluster-controllers-naveen-mogulla-tiktok
youtube_search_url: https://www.youtube.com/results?search_query=TikTok%E2%80%99s+Edge+Symphony%3A+Scaling+Beyond+Boundaries+with+Multi-Cluster+Controllers+CNCF+KubeCon+2024
slides: []
status: parsed
---

# TikTok’s Edge Symphony: Scaling Beyond Boundaries with Multi-Cluster Controllers - Naveen Mogulla, TikTok

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Naveen Mogulla, TikTok
- Schedule: https://kccnceu2024.sched.com/event/1YeSX/tiktoks-edge-symphony-scaling-beyond-boundaries-with-multi-cluster-controllers-naveen-mogulla-tiktok
- Busca YouTube: https://www.youtube.com/results?search_query=TikTok%E2%80%99s+Edge+Symphony%3A+Scaling+Beyond+Boundaries+with+Multi-Cluster+Controllers+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre TikTok’s Edge Symphony: Scaling Beyond Boundaries with Multi-Cluster Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSX/tiktoks-edge-symphony-scaling-beyond-boundaries-with-multi-cluster-controllers-naveen-mogulla-tiktok
- YouTube search: https://www.youtube.com/results?search_query=TikTok%E2%80%99s+Edge+Symphony%3A+Scaling+Beyond+Boundaries+with+Multi-Cluster+Controllers+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KZRi9jg2r1Q
- YouTube title: TikTok’s Edge Symphony: Scaling Beyond Boundaries with Multi-Cluster Controllers - Naveen Mogulla
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tiktoks-edge-symphony-scaling-beyond-boundaries-with-multi-cluster-con/KZRi9jg2r1Q.txt
- Transcript chars: 30901
- Keywords: clusters, cluster, manager, basically, controllers, platform, single, resources, operators, multicluster, builder, specific, create, across, started, multiple, whatever, controller

### Resumo baseado na transcript

hi everyone thanks for joining um um I want to talk quickly about scaling cluster operators Beyond boundaries that is you know single cluster boundry AKA we call it as a multicluster controller so this is more about tick tok's journey of how we implemented multicluster controllers um and also like why we ended up building multicluster controllers in the first place so by the way my name is nain nain Mula I'm a tech lead with Tik Tok at Edge platform team so let me give a little bit

### Excerpt da transcript

hi everyone thanks for joining um um I want to talk quickly about scaling cluster operators Beyond boundaries that is you know single cluster boundry AKA we call it as a multicluster controller so this is more about tick tok's journey of how we implemented multicluster controllers um and also like why we ended up building multicluster controllers in the first place so by the way my name is nain nain Mula I'm a tech lead with Tik Tok at Edge platform team so let me give a little bit of introduction about my team first uh so I'm part of the edge platform team and we are responsible for infrastructure for all the edge use cases that is you know CDN type of workloads live streaming realtime Communications upload etc etc so we basically decided to use kubernetes um on all of these we call it as a point of presence uh we have around 250 to 300 Global clusters so we use this tiny data centers and we build kubernetes on top of it and we provide it as a platform to internal engineering teams uh that is Tik Tok CDN team Tik Tok live you know upload team and all of those guys so um there are around 250 to 300 kubernetes clusters across the globe whenever I say Globe uh consider in this presentation it has a globe minus China it's non-china um in a Tik Tok so and the important thing here I want to just talk about is these are Edge clusters not main dat as inter inter clusters so some of these clusters are very tiny like could be as minimum as like 10 you know nodes to all the way to you know we have around 600 700 nodes so uh all of these are kubernetes clusters you know somewhere between like I I seen 10 node clusters and we have seen multiple 600 nodes based on the demand you know based on the popularity of geolocations or whatnot so all these um clusters have variety range of nodes and obviously uh the other one uh you know it's predominantly um we are in bare metal infrastructure business rather than the cloud business because of you know obvious reasons uh Tik Tok bandwidth uh you know uh transaction volume or whatnot so it's going to be way too expensive in the cloud so we have our own point of presence across the globe but we started exploring the cloud wherever it's possible uh you know we have presence in GK we have presence in eks OK you know uh across all these places um in high level we have the you know control plane and data plane clusters so data plane is more like where the actual um user workloads like when I say User it's more like Tik Tok CDN team o
