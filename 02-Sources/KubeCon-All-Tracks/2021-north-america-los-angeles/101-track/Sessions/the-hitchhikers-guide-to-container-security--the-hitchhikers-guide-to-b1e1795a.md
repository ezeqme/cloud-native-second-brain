---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Tunde Olu-Isa", "Oteemo", "Jed Salazar", "Isovalent"]
sched_url: https://kccncna2021.sched.com/event/lV3t/the-hitchhikers-guide-to-container-security-tunde-olu-isa-oteemo-jed-salazar-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=The+Hitchhikers+Guide+to+Container+Security+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Hitchhikers Guide to Container Security - Tunde Olu-Isa, Oteemo & Jed Salazar, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Tunde Olu-Isa, Oteemo, Jed Salazar, Isovalent
- Schedule: https://kccncna2021.sched.com/event/lV3t/the-hitchhikers-guide-to-container-security-tunde-olu-isa-oteemo-jed-salazar-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hitchhikers+Guide+to+Container+Security+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Hitchhikers Guide to Container Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3t/the-hitchhikers-guide-to-container-security-tunde-olu-isa-oteemo-jed-salazar-isovalent
- YouTube search: https://www.youtube.com/results?search_query=The+Hitchhikers+Guide+to+Container+Security+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YgxUVTx1FEs
- YouTube title: The Hitchhikers Guide to Container Security - Tunde Olu-Isa, Oteemo & Jed Salazar, Isovalent
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-hitchhikers-guide-to-container-security/YgxUVTx1FEs.txt
- Transcript chars: 20569
- Keywords: actually, container, basically, namespace, running, paulie, containers, directory, constraint, resources, configurations, network, called, privileged, directly, security, gatekeeper, cluster

### Resumo baseado na transcript

hi everyone welcome to a hitchhiker's guide to container security today we're going to be talking about container security through the eyes of a couple of characters in the story that we created also be showing a couple of demos but before we get started on the talk just wanted to give a brief introduction so hi i'm jed salazar uh i like mountains dogs and security keys uh i currently work for a company called i surveillance as a security engineer where i'm focused on kubernetes security hi everyone

### Excerpt da transcript

hi everyone welcome to a hitchhiker's guide to container security today we're going to be talking about container security through the eyes of a couple of characters in the story that we created also be showing a couple of demos but before we get started on the talk just wanted to give a brief introduction so hi i'm jed salazar uh i like mountains dogs and security keys uh i currently work for a company called i surveillance as a security engineer where i'm focused on kubernetes security hi everyone i'm tinder luisa i enjoy teaching and also solving complex problems i currently work with a company called ultimo where it's a consulting company that specializes in solving cloud native problems and working with modern technology we do this within enterprise i.t companies and also the federal government space um i i work as a managing consultant i'm also a chief architect at the u.s air force dod platform one currently and we both formally used to work together at a small startup called heptio that was a great kubernetes company um however both at otimo and at i surveillance we're both hiring of course so let's get started with the story so once upon a time containers which are in this story known as remora fish would hitchhike on nodes or sharks across the seas in a symbiotic relationship over the years containers ran in a variety of risky ways such as running as root and privileged containers use the shared node's operating system kernel for their resources so they were known as hitchhikers meet paulie a hitchhiker who runs an nginx web server with just a few pages poly used to run in a dedicated vm environment and in many ways things were easier for them in a vm because of a lack of choices they didn't have to worry about resources networking and security configurations however the environment that they were provisioned was too large for the just few pages that they served so paulie made the decision to hitchhike on a node as a container let's meet our node this is gnome the kubernetes control plane node gnome is super laid back and will run any containerized workload that is scheduled to them also like other nodes they'll run workloads with any settings the containers ask even if they're risky or dangerous gnome always runs the newest version of kubernetes and they take pride in providing a safe environment for their hitchhiker friends so we've talked about containers a couple times but we haven't touched on what a container actually is so what is a contai
