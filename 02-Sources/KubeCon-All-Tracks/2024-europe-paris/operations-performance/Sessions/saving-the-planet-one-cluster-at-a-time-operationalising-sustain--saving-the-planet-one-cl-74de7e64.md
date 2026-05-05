---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Sustainability"]
speakers: ["Gabi Beyer", "Brendan Kamp", "re:cinq"]
sched_url: https://kccnceu2024.sched.com/event/1YeR6/saving-the-planet-one-cluster-at-a-time-operationalising-sustainability-in-kubernetes-gabi-beyer-brendan-kamp-recinq
youtube_search_url: https://www.youtube.com/results?search_query=Saving+the+Planet+One+Cluster+at+a+Time%3A+Operationalising+Sustainability+in+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Saving the Planet One Cluster at a Time: Operationalising Sustainability in Kubernetes - Gabi Beyer & Brendan Kamp, re:cinq

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Sustainability]]
- País/cidade: France / Paris
- Speakers: Gabi Beyer, Brendan Kamp, re:cinq
- Schedule: https://kccnceu2024.sched.com/event/1YeR6/saving-the-planet-one-cluster-at-a-time-operationalising-sustainability-in-kubernetes-gabi-beyer-brendan-kamp-recinq
- Busca YouTube: https://www.youtube.com/results?search_query=Saving+the+Planet+One+Cluster+at+a+Time%3A+Operationalising+Sustainability+in+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Saving the Planet One Cluster at a Time: Operationalising Sustainability in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeR6/saving-the-planet-one-cluster-at-a-time-operationalising-sustainability-in-kubernetes-gabi-beyer-brendan-kamp-recinq
- YouTube search: https://www.youtube.com/results?search_query=Saving+the+Planet+One+Cluster+at+a+Time%3A+Operationalising+Sustainability+in+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Yp_kiukE5gE
- YouTube title: Saving the Planet One Cluster at a Time: Operationalising Sustainability in Kubernetes
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/saving-the-planet-one-cluster-at-a-time-operationalising-sustainabilit/Yp_kiukE5gE.txt
- Transcript chars: 28096
- Keywords: carbon, emissions, energy, actually, utilization, consumption, intensity, workloads, providers, servers, running, started, measure, server, workload, looking, around, research

### Resumo baseado na transcript

okay I think we're going to get started if everyone's okay with that um hi everyone thank you for coming to our talk today on operationalizing uh sustainability in kubernetes in other words how to care about the planet from behind your desk uh just to give a brief intro so my stunning colleague on the right here is ohly too stunning um is Gabby Gabby is a amazing platform engineer incredible system engineer and a very mediocre snowboarder uh this is why she's actually interested in Saving the planet that's essentially what uh my workload would be using if we shifted it to our Northern neighbors still in Europe still under gdpr um I do understand that running your workloads in different regions does come with some comp compliance and security concerns uh we

### Excerpt da transcript

okay I think we're going to get started if everyone's okay with that um hi everyone thank you for coming to our talk today on operationalizing uh sustainability in kubernetes in other words how to care about the planet from behind your desk uh just to give a brief intro so my stunning colleague on the right here is ohly too stunning um is Gabby Gabby is a amazing platform engineer incredible system engineer and a very mediocre snowboarder uh this is why she's actually interested in Saving the planet she needs all the practice she can get well he's not wrong I'm better than him uh Brendan is a very versatile engineer front end backend networking Telecom you name it he's probably done it and well um his passion his passion for knowledge EMB bettering himself and those around him which really feeds into his work that we do at resync and his own personal blog called the green cod. so that's a little about us and uh we work for a company called resync so uh this is kind of why we wanted to do a talk uh on this specific topic um we've been doing research into um just the impact on the climate that uh it has had um as part of our work at resync and resync is just a consultancy that's looking to reduce it related uh impact on the environment um and mostly just Consulting on best practices great so before we dive in um we're going to get on the same page and provide a bit of context uh specifically why are we bothering to talk about this um what are co2e or what is co2e and how do you measure sustainability and how do you measure that in a full system and in a virtualized system so just bear with us through the theory we do have some pretty cool experimentations at the end um so to start off what is carbon equivalent emissions so generally we talk about carbon equivalence which is um an overarching term for um any kind of greenhouse gas so methane nitrous oxide carbon dioxide obviously and um we call it carbon equivalent specifically because we yeah sorry first time on stage just um we call a carbon equivalent because essentially we measure all of these gases in terms of their heating emission compared to carbon dioxide um and obviously everybody's heard of the big bad carbon dioxide now if you see any of these two symbols these designate any greenhouse gases and not only carbon dioxide um right why should anybody care about this well the it sector currently uses around 5 to 10% of uh the world's electricity um we then change that into greenhouse gas emissions that
