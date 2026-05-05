---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Christian Posta", "Solo.io"]
sched_url: https://kccnceu2024.sched.com/event/1YeRx/comparing-sidecar-less-service-mesh-from-cilium-and-istio-christian-posta-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Comparing+Sidecar-Less+Service+Mesh+from+Cilium+and+Istio+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Comparing Sidecar-Less Service Mesh from Cilium and Istio - Christian Posta, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Christian Posta, Solo.io
- Schedule: https://kccnceu2024.sched.com/event/1YeRx/comparing-sidecar-less-service-mesh-from-cilium-and-istio-christian-posta-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Comparing+Sidecar-Less+Service+Mesh+from+Cilium+and+Istio+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Comparing Sidecar-Less Service Mesh from Cilium and Istio.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRx/comparing-sidecar-less-service-mesh-from-cilium-and-istio-christian-posta-soloio
- YouTube search: https://www.youtube.com/results?search_query=Comparing+Sidecar-Less+Service+Mesh+from+Cilium+and+Istio+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=91oylZSoYzM
- YouTube title: Comparing Sidecar-Less Service Mesh from Cilium and Istio - Christian Posta, Solo.io
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/comparing-sidecar-less-service-mesh-from-cilium-and-istio/91oylZSoYzM.txt
- Transcript chars: 32444
- Keywords: mesh, traffic, network, control, sidecar, envoy, authentication, application, capabilities, mutual, proxies, identity, approach, policy, ebpf, psyllium, tunnel, implemented

### Resumo baseado na transcript

thank you all for for joining me here I think this is the last session before alcohol right I think I'm gon to talk very fast okay so I'm going to be talking about service mesh um specifically two open source projects that Implement a sidecar less version of service mesh my name is Christian I'm a global field CTO at a company called solo.io I've been involved in the open source for a long time uh service mesh for the last seven years I guess since uh early 2017

### Excerpt da transcript

thank you all for for joining me here I think this is the last session before alcohol right I think I'm gon to talk very fast okay so I'm going to be talking about service mesh um specifically two open source projects that Implement a sidecar less version of service mesh my name is Christian I'm a global field CTO at a company called solo.io I've been involved in the open source for a long time uh service mesh for the last seven years I guess since uh early 2017 uh been involved with kubernetes since before it was uh 1.0 I worked at Red Hat before this and uh was very involved in messaging and integration and all kinds of stuff before that so distributed systems is uh is my background and specifically application layer application Level uh distributed systems so um service mesh is part of the uh the cloud native networking Journey um it does provide a lot of value and we've been working at at solo and even before that um working with organizations that adopt this technology for um reasons like security compliance zero trust mandates um multicloud initiatives uh capabilities like obviously the some that we'll talk about today like mtls and and Mutual authentication observability uh things like traffic control so you deploy into these public clouds and uh you want to deploy new apis new Services you need to control traffic split traffic Blu green and Canary traffic uh Implement things like locality aware and zonal aware affinity and uh the mesh helps at the application layer to uh to do that but we can't start talking about service mesh um and some of the architectural tradeoffs that we'll look at these two projects without looking at a little bit of History right Linker D was the first service mesh or modern service mesh that we know today and it was actually the first sidecar list service mesh that we know today uh excuse me linkerd 1.x to be specific was implemented as the finagle application libraries that were wrapped in deployed into a container and in kubernetes what this looks like is you deploy it as a Damon set again this is linkerd 1.x this is not the current uh iteration of linker D which is two two do something 2.15 um but in the original architecture it was deployed as a Damon set applications sort of opted in to uh routing their traffic through the proxy by using things like the HTP proxy environment variable and it would you know traffic goes to the proxy the proxy would then do things like timeouts retries circuit breaking service discovery
