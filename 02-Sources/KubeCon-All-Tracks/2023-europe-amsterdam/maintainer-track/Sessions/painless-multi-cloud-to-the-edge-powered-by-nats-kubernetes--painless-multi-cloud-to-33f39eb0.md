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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Tomasz Pietrek", "David Gee", "Synadia"]
sched_url: https://kccnceu2023.sched.com/event/1HyUn/painless-multi-cloud-to-the-edge-powered-by-nats-kubernetes-tomasz-pietrek-david-gee-synadia
youtube_search_url: https://www.youtube.com/results?search_query=Painless+Multi-Cloud+to+the+Edge+Powered+by+NATS+%26+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Painless Multi-Cloud to the Edge Powered by NATS & Kubernetes - Tomasz Pietrek & David Gee, Synadia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tomasz Pietrek, David Gee, Synadia
- Schedule: https://kccnceu2023.sched.com/event/1HyUn/painless-multi-cloud-to-the-edge-powered-by-nats-kubernetes-tomasz-pietrek-david-gee-synadia
- Busca YouTube: https://www.youtube.com/results?search_query=Painless+Multi-Cloud+to+the+Edge+Powered+by+NATS+%26+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Painless Multi-Cloud to the Edge Powered by NATS & Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUn/painless-multi-cloud-to-the-edge-powered-by-nats-kubernetes-tomasz-pietrek-david-gee-synadia
- YouTube search: https://www.youtube.com/results?search_query=Painless+Multi-Cloud+to+the+Edge+Powered+by+NATS+%26+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZQeNj8IVKOg
- YouTube title: Painless Multi-Cloud to the Edge Powered by NATS & Kubernetes - Tomasz Pietrek & David Gee, Synadia
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/painless-multi-cloud-to-the-edge-powered-by-nats-kubernetes/ZQeNj8IVKOg.txt
- Transcript chars: 37590
- Keywords: cluster, stream, clusters, actually, client, question, server, subject, little, simple, depends, active, subjects, create, factory, streams, request, running

### Resumo baseado na transcript

hey everybody welcome to this talk on painless multi-cloud to the edge powered by Nats and kubernetes this is going to be a co-driven talk I'm going to take the first part I'm going to give you the thousand foot drop of nats and my colleague will take you through all of the interesting things so I'm the dumb guy doing the warm-up and then yep oh thank you Nigel yeah so I'm the dumb guy I'm going to do the thousand foot drop on Nats um I'm gonna just

### Excerpt da transcript

hey everybody welcome to this talk on painless multi-cloud to the edge powered by Nats and kubernetes this is going to be a co-driven talk I'm going to take the first part I'm going to give you the thousand foot drop of nats and my colleague will take you through all of the interesting things so I'm the dumb guy doing the warm-up and then yep oh thank you Nigel yeah so I'm the dumb guy I'm going to do the thousand foot drop on Nats um I'm gonna just do some I'm going to give you some warnings there's going to be some audience participation nothing too embarrassing they might be the arm raise here and there and we've got a demo app which I expect some of you will want to get your phone out there's a bit of a bribe we've got an awesome prize to give away for one of your lucky winners so and there's another ask as well you need to put a name in so if you are British or uh I don't know a little bit Brave if you don't want to put anything rude in put a number in because the last thing I want to do is say hey sudden such you've won a prize it's happened this week um so just remember we're on video it's being recorded right okay so I'm David G I'm part of the solution engineering team for sineadia this is Thomas pietric did I pronounce that right yeah close enough it's good enough okay we both work for cenadia um I'd say we're in the Nats team but the whole company's kind of the Nats team so cenadia uh Senator CEO is Derek Collison he's the creator of natso back in 2010 he created it and then rewrote it in go in 2013 so we've got the absolute luxury of working with some of the best brains in this uh kind of area and that's is one of those Technologies where if you ask somebody do you know Nats yeah we know Nas and it's kind of like going to like one of those or You Can Eat World buffet restaurants where you've got 40 or 50 different Cuisines and if it's like me with my you know chiseled figure I go straight for the Chinese noodles I love them I go hey did you go to the restaurant you go yeah I ate the Chinese food what about the Korean what about the vegetarian so you have a main dish and you take small spoons of other main dishes and you put them on one plate and that says kind of like that hey you know that's yeah we use it for a request reply hey we use it for Pub sub and it's not that Nats doesn't do any of that poorly I think it's just that us humans have got this kind of mental state to pick something for one job and then tie all the things together to to b
