---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Brandt Keller", "Defense Unicorns", "Merijn Keppel", "TrueFullstaq"]
sched_url: https://kccnceu2026.sched.com/event/2CW0J/declarative-edge-kubernetes-immutable-clusters-with-talos-+-zarf-brandt-keller-defense-unicorns-merijn-keppel-truefullstaq
youtube_search_url: https://www.youtube.com/results?search_query=Declarative+Edge+Kubernetes%3A+Immutable+Clusters+with+Talos+%2B+Zarf+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Declarative Edge Kubernetes: Immutable Clusters with Talos + Zarf - Brandt Keller, Defense Unicorns & Merijn Keppel, TrueFullstaq

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Brandt Keller, Defense Unicorns, Merijn Keppel, TrueFullstaq
- Schedule: https://kccnceu2026.sched.com/event/2CW0J/declarative-edge-kubernetes-immutable-clusters-with-talos-+-zarf-brandt-keller-defense-unicorns-merijn-keppel-truefullstaq
- Busca YouTube: https://www.youtube.com/results?search_query=Declarative+Edge+Kubernetes%3A+Immutable+Clusters+with+Talos+%2B+Zarf+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Declarative Edge Kubernetes: Immutable Clusters with Talos + Zarf.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0J/declarative-edge-kubernetes-immutable-clusters-with-talos-+-zarf-brandt-keller-defense-unicorns-merijn-keppel-truefullstaq
- YouTube search: https://www.youtube.com/results?search_query=Declarative+Edge+Kubernetes%3A+Immutable+Clusters+with+Talos+%2B+Zarf+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6Ss9wMZhMJc
- YouTube title: Declarative Edge Kubernetes: Immutable Clusters with Talos + Zarf - Brandt Keller & Merijn Keppel
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/declarative-edge-kubernetes-immutable-clusters-with-talos-zarf/6Ss9wMZhMJc.txt
- Transcript chars: 26776
- Keywords: package, deploy, cluster, actually, application, running, registry, applications, declarative, around, images, create, environments, process, update, environment, ultimately, already

### Resumo baseado na transcript

Welcome, welcome everyone uh if you want to hit uh to this discussion on declarative edge Kubernetes. I'm a staff software engineer at Defense Unicorns, a CNCF ambassador and a maintainer in the open SSF. So whether you're running Kubernetes on a windmill on the North Sea, Kubernetes on spaceships, or perhaps something more challenging at a conference, I know everyone knows Wi-Fi here. Um the challenge is similar, bad or no connectivity, and we're trying to run a piece of cloudnative software that was designed to run on a connected system like the internet. And you know for air gap Kubernetes Kubernetes now you know well over a decade running it in the air gap running it at the edge isn't necessarily new right we're not going to come up here and stand up here and be the we're the first to do this we're not um but I think that we've seen many examples of this many of you have seen possibly airgap deployments of Kubernetes how you deploy applications to airgapped Kubernetes and kind of the synonymous uh relation that has to

### Excerpt da transcript

Welcome, welcome everyone uh if you want to hit uh to this discussion on declarative edge Kubernetes. Uh I myself am Brent Keller. I'm a staff software engineer at Defense Unicorns, a CNCF ambassador and a maintainer in the open SSF. >> My name is Marell. I'm a principal consultant at True Fullstack. Um this is my first time speaking at CubeCon, so stoked. Um thank you. Thank you. Um, big crowd at 5:00 p.m. So, uh, you're all welcome. Um, because we're doing a live demo, I brought some hardware. It's a home lab that we get at True Full Stack. Uh, well, you can get it if you want to, uh, to think around with stuff like Kubernetes or other CNCF stuff. Um, and I pre-provisioned these nodes with Talos Linux. Uh, it's a maintenance mode. We will talk about Talos Linux a little bit more later on but um for the sake of demos I will not boot them via USB stick. It takes too much time. So take it away. All right. So today I'm going to walk you through a bit of a journey from kind of the things we prepare for all the way out to orbit.

Um you're going to see our spaceship if you will taking off through each of these stages and we'll walk you through each of them. Um, this is a bit of a disclaimer that uh the slides are not going to be very useful. They're going to be just generic high level stuff. Um, we really want to show off that we can do all of this live. We can do all of it here with this hardware. And, you know, kind of for CubeCon North America, I really want to create shirts that say, you know, friends don't let friends do recorded presentations. And so uh with further ado um I think we can move over to oh uh each of these stages right and I think we I mean we kind of talked about them um prep we'll go through real quickly take off um why Talis Linux is really a great fit for us um for particularly thinking about like declarative deterministic immutable um that's important uh ascent is like how do we get our workloads deployed um Zarf as a declarative package package management tool will kind of help us do this. And really once we get to operation in orbit, we're going to see that like we want to treat these things in a sustainable fashion.

We want to make it so that when you're doing an application update, it feels the same as if you're doing an operating system update. And those kind of at times can feel very conflicting. Uh they can be very different. They can be managed in different ways. And so how can we how can we bring this experience back in such
