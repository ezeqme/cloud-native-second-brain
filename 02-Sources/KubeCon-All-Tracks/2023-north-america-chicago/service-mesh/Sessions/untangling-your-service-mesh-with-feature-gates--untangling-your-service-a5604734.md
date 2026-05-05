---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Niranjan Shankar", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2v6/untangling-your-service-mesh-with-feature-gates-niranjan-shankar-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Untangling+Your+Service+Mesh+with+Feature+Gates+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Untangling Your Service Mesh with Feature Gates - Niranjan Shankar, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Niranjan Shankar, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2v6/untangling-your-service-mesh-with-feature-gates-niranjan-shankar-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Untangling+Your+Service+Mesh+with+Feature+Gates+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Untangling Your Service Mesh with Feature Gates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2v6/untangling-your-service-mesh-with-feature-gates-niranjan-shankar-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Untangling+Your+Service+Mesh+with+Feature+Gates+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BuChyhnmHeA
- YouTube title: Untangling Your Service Mesh with Feature Gates - Niranjan Shankar, Microsoft
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/untangling-your-service-mesh-with-feature-gates/BuChyhnmHeA.txt
- Transcript chars: 34512
- Keywords: mesh, feature, features, envoy, configuration, resource, policy, platform, resources, gatekeeper, config, custom, abstraction, values, complex, control, configurations, developers

### Resumo baseado na transcript

hey everyone and uh thanks a lot for joining me in this session today uh I'm nanin I'm a software engineer on the Azure kubernetes service team at Microsoft um I'm currently working on the itdo add-on for AKs um previously I was on the container Upstream team uh working on the open service mesh project uh so I I have experience working uh both on managed and uh Open Source service meshes and uh one of my focuses more recently uh working on manage itso has been uh deciding

### Excerpt da transcript

hey everyone and uh thanks a lot for joining me in this session today uh I'm nanin I'm a software engineer on the Azure kubernetes service team at Microsoft um I'm currently working on the itdo add-on for AKs um previously I was on the container Upstream team uh working on the open service mesh project uh so I I have experience working uh both on managed and uh Open Source service meshes and uh one of my focuses more recently uh working on manage itso has been uh deciding which features do we want to incorporate into our add-on and which features do we want to disallow and how to go about doing so so in this presentation I wanted to share some of those lessons to help you untangle your service mesh with feature Gates so first I'm going to touch on the general problem of service mesh complexity and why users often end up with what I would call a tangled service mesh and then I'm going to to explain how to use quote unquote feature Gates uh to help solve this problem then um I'm going to discuss some helpful criteria uh to help you decide what kinds of features or configurations to allow or disallow in your environments and um finally I'll conclude by reiterating some of the general takeaways uh from all this and um highlight some recent developments to watch out for so over the past few years um service meshes have a mass a wide array of features and configuration options um of course a lot of this has to do with the fact that they are built on top of the envoy proxy with the sidecar model and Envoy is very powerful um and it has a lot of advanced capabilities that operators want to leverage um obviously the exceptions here are Linker D which has its own rust based proxy um and uh as you may have heard if you attended the battle cars discussion on Tuesday we also have ebpf and side car free service meshes um although uh not all the sidecar lless models are production ready just yet like it's Deo ambient and not only can there be so much to configure but there are often multiple ways of configuring a service mesh uh we have installation values we have annotations crds and so on um so this example on the top right there is how you define the mesh wide configuration for console service mesh um and below that is an example of how you would uh configure the linkerd proxy with resource annotations and for a service mesh like itdo a lot of these configuration Pathways uh can be overlapping and um I'm going to be giving a few examples of those later in the presenta
