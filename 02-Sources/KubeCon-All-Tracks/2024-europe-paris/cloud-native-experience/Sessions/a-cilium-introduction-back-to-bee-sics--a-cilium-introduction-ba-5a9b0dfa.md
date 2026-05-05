---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Experience"
themes: ["Networking"]
speakers: ["Nico Vibert", "Dan Finneran", "Isovalent"]
sched_url: https://kccnceu2024.sched.com/event/1YeMX/a-cilium-introduction-back-to-bee-sics-nico-vibert-dan-finneran-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=A+Cilium+Introduction%3A+Back+to+Bee-Sics+CNCF+KubeCon+2024
slides: []
status: parsed
---

# A Cilium Introduction: Back to Bee-Sics - Nico Vibert & Dan Finneran, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Nico Vibert, Dan Finneran, Isovalent
- Schedule: https://kccnceu2024.sched.com/event/1YeMX/a-cilium-introduction-back-to-bee-sics-nico-vibert-dan-finneran-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=A+Cilium+Introduction%3A+Back+to+Bee-Sics+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre A Cilium Introduction: Back to Bee-Sics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMX/a-cilium-introduction-back-to-bee-sics-nico-vibert-dan-finneran-isovalent
- YouTube search: https://www.youtube.com/results?search_query=A+Cilium+Introduction%3A+Back+to+Bee-Sics+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KZzNm5ntRbo
- YouTube title: A Cilium Introduction: Back to Bee-Sics - Nico Vibert & Dan Finneran, Isovalent
- Match score: 0.765
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/a-cilium-introduction-back-to-bee-sics/KZzNm5ntRbo.txt
- Transcript chars: 32037
- Keywords: network, traffic, cluster, access, networking, running, celium, within, address, gateway, actually, policy, ebpf, policies, ingress, applications, around, fighter

### Resumo baseado na transcript

hi everyone hi can you hear us okay at the back oh brilliant yeah thank you so much for everybody squeezing in um clearly a bit of an over subscrib session but we're so thankful that you're you're here and uh yeah hopefully you enjoy this talk awesome so uh we start with a quick intro uh I'm Nico I work for ISO venant well Dan and I me work for isov venant the creators of celium and I'm a senior staff Tech technical marketing engineer Dan uh yeah so I think additionally as well there's going to be learning guides that are being written as we speak um so the learning guides plus all of the labs are effectively a fantastic way for you to learn all about both kubernetes networking and cium networking

### Excerpt da transcript

hi everyone hi can you hear us okay at the back oh brilliant yeah thank you so much for everybody squeezing in um clearly a bit of an over subscrib session but we're so thankful that you're you're here and uh yeah hopefully you enjoy this talk awesome so uh we start with a quick intro uh I'm Nico I work for ISO venant well Dan and I me work for isov venant the creators of celium and I'm a senior staff Tech technical marketing engineer Dan uh yeah so my name is Dan fan I'm part of the community team focusing on open source soyum ebpf uh Lely find me the San booth in the project Pavilion for any other questions that you may have later on awesome um so why are we here we're here to answer uh a quick question now look at this and tell me is this you [Laughter] people not raising your hands you're all kubernetes networking experts you can come on stage now no no um kuber networking is hard I'm like a network I've been in networking for about 20 years and I still find it really scary intimidating and we're here to help you uh understand makes the most of it and maybe explain why celium is the answer so Dan is going to start by explaining why kubernetes networking is so hard uh and he's going to try to explain kubernetes networking without any of the jargon any acronyms or very few acronyms we'll try definitely going to fail and uh and really talk about you know what is the network um meant to do what do we need the network to do for our kubernetes cluster and again explain some of the reasons why has become the de facto kubernetes networking platform and uh we we'll do a demo later on and we'll talk about the newly announced and released celium certified associate certification and uh you take a few questions if we have the chance now done good luck mer see so uh kubernetes networking not a small topic but we're going to try and cover it as quickly as we can and as mentioned with uh minimal jargon and no acronyms so uh as Nico mentioned networking is a tough subject um and kubernetes doesn't really help uh with that so out of the box kubernetes doesn't even provide any networking if you've been using eks AKs Etc you probably have just been using clusters without kind of having to worry about these sorts of things but if you spin up a cluster by yourself a lot of things don't come out of the box and networking is one of those things and it kind of gets even worse so kubernetes networking introduces a whole other network that exists within the cluster itself so yo
