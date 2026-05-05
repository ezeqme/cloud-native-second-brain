---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccncna2025.sched.com/event/27NmD/emissary-ingress-version-4-and-the-road-ahead-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+the+Road+Ahead+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Emissary-ingress: Version 4 and the Road Ahead - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Flynn, Buoyant
- Schedule: https://kccncna2025.sched.com/event/27NmD/emissary-ingress-version-4-and-the-road-ahead-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+the+Road+Ahead+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Emissary-ingress: Version 4 and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NmD/emissary-ingress-version-4-and-the-road-ahead-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+the+Road+Ahead+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7U6nAxUxG6c
- YouTube title: Emissary-ingress: Version 4 and the Road Ahead - Flynn, Buoyant
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/emissary-ingress-version-4-and-the-road-ahead/7U6nAxUxG6c.txt
- Transcript chars: 17531
- Keywords: emissary, actually, ingress, ambassador, support, present, cluster, endpoint, license, version, interesting, little, resource, question, developer, anymore, probably, having

### Resumo baseado na transcript

All right, I think we're actually live now and I don't have to yell quite so much. So, this is the Emissary Ingress maintainer talk where we will be talking about version 4 in the road ahead. Um, this class of thing is basically called an Ingress controller named after the old Ingress resource and the Ingress problem because the old Ingress resource was a way to try to talk about solving the Ingress problem. The point here is that Jane the application developer is a person who tends to think of Kubernetes as pure friction. Um, this led to some interesting design decisions in the original API where we did things that simply don't work with CRDs today. Kubernetes versioning doesn't actually work the way most people think it works.

### Excerpt da transcript

All right, I think we're actually live now and I don't have to yell quite so much. So, this is the Emissary Ingress maintainer talk where we will be talking about version 4 in the road ahead. Um, quick show of hands. How many of you have worked with Emissary or running it? Okay, a much higher percentage than usual, which is interesting. Um, I do have some slides and I'm Flynn. You can reach me as Flynn at.io. Everybody here probably already knows that the uh the takeaway from these slides really boils down to yeah we don't have enough people to get get done what we want to get done. So now is an excellent time to come and help. For the rest of this bit we will talk about the purpose of the project for people who are new to it. We'll talk about the past the present and the future. And then there will be a bit for I think I labeled it discussion because usually in this particular crowd is one that wants a little bit more than just asking questions and having answers shouted at them from the stage. For anyone who's not familiar with this, the purpose of emissary is fairly easy to state.

If you have a cluster, you have things running inside the cluster and you have users outside the cluster. You would like your users outside the cluster to be able to use things that are inside the cluster. However, clusters don't like that. This is what we basically call the ingress problem. How do you arrange it so that it's possible for people to use the things in your cluster safely from outside the cluster? And the usual way we deal with this is just to put something here at the edge that can then go and mediate all of your requests safely. Emissary is a thing to do that. Um, this class of thing is basically called an Ingress controller named after the old Ingress resource and the Ingress problem because the old Ingress resource was a way to try to talk about solving the Ingress problem. Uh, emissary doesn't really have a lot to do with the ingress resource. As a class, ingress controllers including emissary are always able to do basic routing saying, "Hey, take this piece of the URL space and send it over to this service." Emissary can also do authentication and authorization and traffic splitting and canaries and AB testing, which is really the same thing as canaries, just slightly different logic.

uh retries, circuit breaking, rate limiting, lots of other things. Because emissary is an English controller that can do all these things, we tend to refer to it as an API g
