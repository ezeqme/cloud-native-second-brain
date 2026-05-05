---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Deutsche Kreditbank AG"]
sched_url: https://kccnceu2023.sched.com/event/1HySE/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-upbound-christopher-haar-dkb-deutsche-kreditbank-ag
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+-+Jared+Watts%2C+Upbound+%26+Christopher+Haar%2C+DKB+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework - Jared Watts, Upbound & Christopher Haar, DKB - Deutsche Kreditbank AG

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Deutsche Kreditbank AG
- Schedule: https://kccnceu2023.sched.com/event/1HySE/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-upbound-christopher-haar-dkb-deutsche-kreditbank-ag
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+-+Jared+Watts%2C+Upbound+%26+Christopher+Haar%2C+DKB+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework - Jared Watts, Upbound & Christopher Haar, DKB.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HySE/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-upbound-christopher-haar-dkb-deutsche-kreditbank-ag
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+-+Jared+Watts%2C+Upbound+%26+Christopher+Haar%2C+DKB+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5WRkVUlEgHI
- YouTube title: Crossplane Intro and Deep Dive - the Cloud Native Control Plane... - Jared Watts & Christopher Haar
- Match score: 0.971
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framewor/5WRkVUlEgHI.txt
- Transcript chars: 35438
- Keywords: resources, provider, providers, resource, create, cluster, control, observe, cross-plane, available, policy, together, infrastructure, function, metrics, little, composition, manage

### Resumo baseado na transcript

so we have I think like 45 slides three demos and two people uh in 35 minutes so I think we need to just jump on into it and uh keep the pace going pretty quickly we're gonna try to make sure that there's time at the end for questions also uh because typically with these sessions we've had lots and lots of questions we want to make sure that there's time for that too um so yeah so this is the cross plain projects uh introduction session and deep

### Excerpt da transcript

so we have I think like 45 slides three demos and two people uh in 35 minutes so I think we need to just jump on into it and uh keep the pace going pretty quickly we're gonna try to make sure that there's time at the end for questions also uh because typically with these sessions we've had lots and lots of questions we want to make sure that there's time for that too um so yeah so this is the cross plain projects uh introduction session and deep dive sessions so it's you know kind of a combined thing which is always interesting because we get to cover the full spectrum of cross-plane stuff but um you know for people that are already already familiar with it there's kind of some introductory material you may have heard a few times by now and then folks that are new on their cross-plane Journey might get a little lost later on but we'll try to keep everybody all together through this whole thing so my name is Jared uh one of the creators of the crossbane project and I have my my friend here Chris Christopher who's a prolific maintainer on the project as well all right so introductory material let's talk about what crossbane actually is and the best way to think about it is that it is a framework in order to help you build a cloud native control plane uh so you know we talk about control planes you know Cloud providers have been managing their infrastructure with control planes for years and years right that's not a New Concept itself but we wanted to be able to and you know create a framework so that all of you could build your own control planes to manage your infrastructure and your resources Etc and inject your own opinions into it as well um you know and have a nice framework to do that with so kind of think about the top and the bottom of the cross-plane project so on the bottom here there is you know you can manage any type of infrastructure it's not very extensible there so you can talk to any Cloud providers on-premises stuff it's very extensible and on the front end you can you know bring together those resources and kind of declare your own platform apis your own infrastructure apis so highly extensible on the both the front and the bottom so just a quick history about the project so this is the cncf project right that's why we have this maintainer track talk um and we're looking at it as a neutral place for companies and you know organizations individuals Etc to all come together and work on you know this mission of enabling cloudative control pla
