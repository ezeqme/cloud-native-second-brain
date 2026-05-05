---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Rob Scott", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7q1/upgrade-safely-avoid-the-pitfalls-of-kubernetes-versioning-rob-scott-google
youtube_search_url: https://www.youtube.com/results?search_query=Upgrade+Safely%3A+Avoid+the+Pitfalls+of+Kubernetes+Versioning+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Upgrade Safely: Avoid the Pitfalls of Kubernetes Versioning - Rob Scott, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Rob Scott, Google
- Schedule: https://kccncna2024.sched.com/event/1i7q1/upgrade-safely-avoid-the-pitfalls-of-kubernetes-versioning-rob-scott-google
- Busca YouTube: https://www.youtube.com/results?search_query=Upgrade+Safely%3A+Avoid+the+Pitfalls+of+Kubernetes+Versioning+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Upgrade Safely: Avoid the Pitfalls of Kubernetes Versioning.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7q1/upgrade-safely-avoid-the-pitfalls-of-kubernetes-versioning-rob-scott-google
- YouTube search: https://www.youtube.com/results?search_query=Upgrade+Safely%3A+Avoid+the+Pitfalls+of+Kubernetes+Versioning+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xg0NWtSgmUE
- YouTube title: Upgrade Safely: Avoid the Pitfalls of Kubernetes Versioning - Rob Scott, Google
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/upgrade-safely-avoid-the-pitfalls-of-kubernetes-versioning/Xg0NWtSgmUE.txt
- Transcript chars: 31912
- Keywords: version, versions, gateway, storage, upgrade, channel, standard, actually, controller, ingress, stored, experimental, understand, feature, painful, deprecation, basically, support

### Resumo baseado na transcript

my name is Rob Scott I work at Google I've been working on kubernetes networking for a little over five years uh most recently I've been doing a lot of Gateway API things and so I'll be using some Gateway API examples in here um but really before I worked uh on kubernetes I spent a lot of time as an end user of kubernetes actually trying to run the thing and so I'm very familiar with some of the painful things that can happen when things don't go quite we never have bugs and kubernetes there's always enough content to go into a patch release so what happened here was in kubernetes one9 we finally graduated Ingress to V1 now Ingress had existed at V1 beta 1 for nearly 5 years which at that stored versions and what crpc route would have looked like as V1 Alpha 2 and V1 and kubernetes is not going to let you upgrade to a crd that doesn't include some definition of the versions it has stored somewhere so if it says I is so in this case V1 Alpha 2 I'm going to just not let you do that because I need a way to know how to get this out of at CD storage but you're going to say well all my manifests say V1 and again just reminder this is just how you're communicating between you and the API server nothing to do with API server to etcd nothing to do with storage version so where on Earth is storage version actually defined if you dig into crds I know

### Excerpt da transcript

my name is Rob Scott I work at Google I've been working on kubernetes networking for a little over five years uh most recently I've been doing a lot of Gateway API things and so I'll be using some Gateway API examples in here um but really before I worked uh on kubernetes I spent a lot of time as an end user of kubernetes actually trying to run the thing and so I'm very familiar with some of the painful things that can happen when things don't go quite as expect and so today I'm going to be talking about how you can upgrade safely and avoid the many pitfalls of kubernetes versioning and maybe hopefully also understand what's happening behind the scenes because there's a lot of confusing terms in kubernetes versioning so to start off how many people here have been burned by some kind of kubernetes upgrade gone wrong okay I definitely myself and it seems like most of you I'm hoping this talk will help many of us avoid future pain that's the goal hopefully we can we can get there and to do that I want to walk through three distinct painful upgrades and I'm going to focus on painful upgrades that I'm at least partially responsible for myself so I'm going to be making fun of myself here a lot uh but we're going to start with Ingress API so how many people here were around for kubernetes 122 okay that's great that's great if you are around for kubernetes 122 this story may sound familiar to you I hope it doesn't but we'll just say so you upgrade your kubernetes cluster to 122 you're feeling good you finally got your upgrade process down you're feeling confident about how you can do kubernetes upgrades and then your pager starts going off prod is down your boss is calling everything is not going right right after you've upgraded and you have no idea what to do but you remember reading well I can't go back words I can't roll back a kubernetes upgrade what am I supposed to do and after a bunch of digging you start noticing look my Ingress controller it's in a crash loop back off for anyone at Family Feud in the Keynotes crash loop back off top kubernetes error so yeah we've we've all seen that I imagine and so it's about time to panic because well what else do you do um so what on Earth went wrong here well you probably know this is really related to Ingress so to understand let's let's take a few steps back and understand the terminology we're going to use throughout this talk so first off we've got API Group and version so in your kubernetes yaml manifest you've
