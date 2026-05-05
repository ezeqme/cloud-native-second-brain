---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Matt Turner", "Tetrate", "Francesco Beltramini", "Control Plane"]
sched_url: https://kccnceu2023.sched.com/event/1HyZ9/automated-cloud-native-incident-response-with-kubernetes-and-service-mesh-matt-turner-tetrate-francesco-beltramini-control-plane
youtube_search_url: https://www.youtube.com/results?search_query=Automated+Cloud-Native+Incident+Response+with+Kubernetes+and+Service+Mesh+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Automated Cloud-Native Incident Response with Kubernetes and Service Mesh - Matt Turner, Tetrate & Francesco Beltramini, Control Plane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matt Turner, Tetrate, Francesco Beltramini, Control Plane
- Schedule: https://kccnceu2023.sched.com/event/1HyZ9/automated-cloud-native-incident-response-with-kubernetes-and-service-mesh-matt-turner-tetrate-francesco-beltramini-control-plane
- Busca YouTube: https://www.youtube.com/results?search_query=Automated+Cloud-Native+Incident+Response+with+Kubernetes+and+Service+Mesh+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Automated Cloud-Native Incident Response with Kubernetes and Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZ9/automated-cloud-native-incident-response-with-kubernetes-and-service-mesh-matt-turner-tetrate-francesco-beltramini-control-plane
- YouTube search: https://www.youtube.com/results?search_query=Automated+Cloud-Native+Incident+Response+with+Kubernetes+and+Service+Mesh+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vor-xiV25xM
- YouTube title: Automated Cloud-Native Incident Response with Kubernetes and Service Mesh - M Turner & F Beltramini
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/automated-cloud-native-incident-response-with-kubernetes-and-service-m/vor-xiV25xM.txt
- Transcript chars: 41177
- Keywords: response, security, actually, attack, native, deployment, traffic, incident, little, getting, envoy, container, probably, anything, firewall, control, operations, infrastructure

### Resumo baseado na transcript

all right well thanks for coming guys and welcome to automated Cloud native instant response with kubernetes and service mesh Matt and I will introduce ourselves momentarily for now we would like to thank the cloud native computer Foundation event team for yet another great cubicon my friend cool so I'm mattena I'm a software engineer at tetrate we are a company that looks at helping Enterprises with identity based application micro segmentation so we use istio and Envoy in all those texts as an implementation detail to help you

### Excerpt da transcript

all right well thanks for coming guys and welcome to automated Cloud native instant response with kubernetes and service mesh Matt and I will introduce ourselves momentarily for now we would like to thank the cloud native computer Foundation event team for yet another great cubicon my friend cool so I'm mattena I'm a software engineer at tetrate we are a company that looks at helping Enterprises with identity based application micro segmentation so we use istio and Envoy in all those texts as an implementation detail to help you scale your organization scale your security as you've got multiple clusters multiple regions multiple meshes and I'm Francesca I'm a security engineering manager at control plane I spent a few years at University then I moved into the IT OT security spaces then I stood up the security operations center and incident response capability for a large satellite mobile provider I work for control play now because I didn't want to see a network cable anymore in my life uh control plane is a cloud native security consultancy established in 2017 based in London but we have offices in North America and APAC as well security specialists in kubernetes container and open source in general we train on all the above as well and we focus on deeply threat model the secuba design and scuba default Cloud native architectures and more recently we stood up a new service which consists of helping customers Bridging the Gap between infrastructure Cloud native infrastructure and security operations so what will we be talking about today we'll go through some basic concepts about security incident response to make sure that people in the room and they have the again the basic concept that they we speak a Common Language and then we'll go through a story where in organizations more recently start adopting a more proactive approach to incense response and bring and brought some automation as well to help them counter attacking and then the thumb will begin Matt will walk you through some Cloud native technology and Concepts through an incident response lens and then there will be a walkthrough literally of a response on a reference architecture on a kubernetes cluster cool so apologies to the Security Professionals in the room but we have to do this so I'll start from the definitions that most professionals disagree on incident and response I like these two incident an event that could lead to the loss of or disruption to in organizations operations data ser
