---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Ashutosh Kumar", "Elastic", "Anish Ramasekar", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2uM/oidc-and-workload-identity-in-kubernetes-ashutosh-kumar-elastic-anish-ramasekar-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=OIDC+and+Workload+Identity+in+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# OIDC and Workload Identity in Kubernetes - Ashutosh Kumar, Elastic & Anish Ramasekar, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Ashutosh Kumar, Elastic, Anish Ramasekar, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2uM/oidc-and-workload-identity-in-kubernetes-ashutosh-kumar-elastic-anish-ramasekar-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=OIDC+and+Workload+Identity+in+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre OIDC and Workload Identity in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uM/oidc-and-workload-identity-in-kubernetes-ashutosh-kumar-elastic-anish-ramasekar-microsoft
- YouTube search: https://www.youtube.com/results?search_query=OIDC+and+Workload+Identity+in+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eyj0UCmJfjo
- YouTube title: Zero Trust Workload Identity in Kubernetes - Michael Peters, Red Hat
- Match score: 0.728
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/oidc-and-workload-identity-in-kubernetes/eyj0UCmJfjo.txt
- Transcript chars: 35676
- Keywords: identity, spiffy, workload, server, talking, security, running, identities, everything, secret, signed, credentials, workloads, certificates, attestation, whatever, software, systems

### Resumo baseado na transcript

all right welcome everyone um my name is Michael Peters I'm an engineer at Red Hat I work primarily in the security space in emerging Technologies I'm a member of the keyline project if you're not familiar with key lime we'll touch briefly on key lime in a bit um but uh today's talk is zero trust workload identity in kubernetes is really Broad and all of the pretty much every slide I have in here could be a whole talk in and of itself um just the the ideas

### Excerpt da transcript

all right welcome everyone um my name is Michael Peters I'm an engineer at Red Hat I work primarily in the security space in emerging Technologies I'm a member of the keyline project if you're not familiar with key lime we'll touch briefly on key lime in a bit um but uh today's talk is zero trust workload identity in kubernetes is really Broad and all of the pretty much every slide I have in here could be a whole talk in and of itself um just the the ideas and Concepts behind zero trust what is identity um and and how that integrates with everything in the in the cloud native space is tricky and Myriad and so we're just going to be sort of doing a general overview of all that if you want more information I'll try to answer that so I'm going to make some assumptions as we go if those assumptions prove incorrect just let me know wait wave your hand and say something uh have me back up whatever that'll work so talking about zero trust it's kind of a misnomer zero trust actually means zero implicit trust it's not as um people don't want to go around like ZT is a better acronym than zit right um so uh but when we're talking about zero trust you can't have zero trust you have to trust something but what we're saying is we don't trust things just by where they are on the network so this is an architectural pattern where we apply security at the asset level not the location level so in the past a lot of things were set up in this castle and moat scenario where the castle is your data center and you're trying to protect it and you have you know a moat and walls uh and guards around the the data center um so your your firewalls your network segmentation your ACLS your vpns and so everything was focused on this perimeter security if we lock everything out then we can trust everything inside and that turns out to not be the case for lots of reasons um and even when this was implemented if it was done well then it was actually a burden and very strict and rigid in how things could be set up and this led to a lot of the conflict that exists between developers and operations and developers and security people um and when it wasn't super well done when it was lacks it led Intruders in and there were lots of holes in in the castle so as things started to grow and and the modern world started to change a bit right we have a whole bunch of things coming into microservices and bring your own devices and API gateways multi-cloud setups and serverless functions running all over
