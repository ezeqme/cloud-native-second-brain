---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Kubernetes Core"]
speakers: ["Rob Esker", "NetApp"]
sched_url: https://kccnceu2021.sched.com/event/igUu/sponsored-lightning-talk-wielding-the-power-potential-of-kubernetes-for-mere-mortals-deities-for-whom-time-is-precious-rob-esker-netapp
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Wielding+the+Power+%26+Potential+of+Kubernetes+for+Mere+Mortals+%28%26+Deities+for+Whom+Time+is+Precious%29+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Lightning Talk: Wielding the Power & Potential of Kubernetes for Mere Mortals (& Deities for Whom Time is Precious) - Rob Esker, NetApp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Rob Esker, NetApp
- Schedule: https://kccnceu2021.sched.com/event/igUu/sponsored-lightning-talk-wielding-the-power-potential-of-kubernetes-for-mere-mortals-deities-for-whom-time-is-precious-rob-esker-netapp
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Wielding+the+Power+%26+Potential+of+Kubernetes+for+Mere+Mortals+%28%26+Deities+for+Whom+Time+is+Precious%29+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Lightning Talk: Wielding the Power & Potential of Kubernetes for Mere Mortals (& Deities for Whom Time is Precious).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/igUu/sponsored-lightning-talk-wielding-the-power-potential-of-kubernetes-for-mere-mortals-deities-for-whom-time-is-precious-rob-esker-netapp
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Wielding+the+Power+%26+Potential+of+Kubernetes+for+Mere+Mortals+%28%26+Deities+for+Whom+Time+is+Precious%29+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dTm0cTpI3cM
- YouTube title: Sponsored Lightning Talk: Wielding the Power & Potential of Kubernetes for Mere Mortals... Rob Esker
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-lightning-talk-wielding-the-power-potential-of-kubernetes-fo/dTm0cTpI3cM.txt
- Transcript chars: 4764
- Keywords: netapp, storage, actually, necessarily, application, access, course, little, customers, capabilities, public, lightning, worked, ourselves, epiphany, understanding, strictly, thought

### Resumo baseado na transcript

welcome to cubecon emilia 2021 and my lightning talk i'm rob esker from netapp i'd like to offer to the extent that i can within five minutes a few of our observations from netapp in our our years of having worked with deployers and of course as practitioners ourselves a few things primarily from the lens of storage and data management that hopefully can inform how you look at and approach and operate kubernetes let me just start with a little bit about netapp i mentioned or alluded to you

### Excerpt da transcript

welcome to cubecon emilia 2021 and my lightning talk i'm rob esker from netapp i'd like to offer to the extent that i can within five minutes a few of our observations from netapp in our our years of having worked with deployers and of course as practitioners ourselves a few things primarily from the lens of storage and data management that hopefully can inform how you look at and approach and operate kubernetes let me just start with a little bit about netapp i mentioned or alluded to you know we worked with many thousands of customers since the inception we contribute to the storage sigs uh data protection working group and of course the continued storage uh interface specification as well um you know our customers brought us to the conversation we use kubernetes ourselves to power many of our cloud services more to talk about on that uh in actually the coming months uh so this is not just a scenario we're providing capabilities vis-a-vis kubernetes but also building our own products based in part on kubernetes um so a little bit about um i guess on the editorial and about kubernetes i'd offer um that we have seen from our customers uh kind of a realization or epiphany process of epiphany where there's there's an understanding that kubernetes is maybe not necessarily strictly just an evolution of more hypervisor vm based uh classic infrastructure as a service that indeed it's a predominantly a desired state machine uh particularly useful for you know automating scaling and you know life cycle of applications mostly thought to be predicated on containers but actually not entirely confined to that when you look at things like verb that said it's it's an important sort of calibration at the outset that there are some things that are a little bit different about kubernetes than than what you might have expected from a vm and a surrounding ecosystem as a runtime so just to start with that uh one of the things uh in particular if you add kind of a time dimension to understanding kubernetes is at the beginning it was really built of can i take a quote-unquote cloud-native application built of a 12-factor application model which maybe didn't necessarily uh you know really kind of thought that the only way to persist data was in an object and and can i deliver it of course it did that well but that was a bit limiting in terms of the style and kind of computational problem for which kubernetes could be applied so uh it was certainly the case that from the outset w
