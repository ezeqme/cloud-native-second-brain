---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Tim Ramlot", "Maël Valais", "Palo Alto Networks"]
sched_url: https://kccnceu2026.sched.com/event/2EF73/cert-manager-project-update-beyond-2026-tim-ramlot-mael-valais-palo-alto-networks
youtube_search_url: https://www.youtube.com/results?search_query=Cert-manager+%E2%80%93+Project+Update%3A+Beyond+2026+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cert-manager – Project Update: Beyond 2026 - Tim Ramlot & Maël Valais, Palo Alto Networks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tim Ramlot, Maël Valais, Palo Alto Networks
- Schedule: https://kccnceu2026.sched.com/event/2EF73/cert-manager-project-update-beyond-2026-tim-ramlot-mael-valais-palo-alto-networks
- Busca YouTube: https://www.youtube.com/results?search_query=Cert-manager+%E2%80%93+Project+Update%3A+Beyond+2026+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cert-manager – Project Update: Beyond 2026.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF73/cert-manager-project-update-beyond-2026-tim-ramlot-mael-valais-palo-alto-networks
- YouTube search: https://www.youtube.com/results?search_query=Cert-manager+%E2%80%93+Project+Update%3A+Beyond+2026+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vzBGkY_HIyM
- YouTube title: Cert-manager – Project Update: Beyond 2026 - Tim Ramlot & Maël Valais, Palo Alto Networks
- Match score: 0.75
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cert-manager-project-update-beyond-2026/vzBGkY_HIyM.txt
- Transcript chars: 17443
- Keywords: manager, search, certificates, gateway, security, certificate, ingress, projects, working, already, release, dependencies, resource, update, maintainers, controller, across, releases

### Resumo baseado na transcript

So Milo and I we will be talking today about sort manager about what we have done in the last year and what our vision is for the future. There are a few links in the presentation that are useful and through that uh link through the PDF you can actually also get access to those links. One of them is trust manager and trust manager is this autocontroller which is responsible for distributing trust across all your workloads in a Kubernetes cluster. Something I heard I hear all the time is why isn't manager built into Kubernetes? I still don't have an answer to that and we haven't even started talking about like like to the Kubernetes team. the pro the problem we found the pro the major problem we had with sub measure that this gateway API integration dates back to 2021 that's so we didn't know anything back then and we didn't know specifically that when someone who is using the

### Excerpt da transcript

Okay, welcome everyone. Welcome to our presentation. So Milo and I we will be talking today about sort manager about what we have done in the last year and what our vision is for the future. You can uh download the presentation also using the QR codes. There are a few links in the presentation that are useful and through that uh link through the PDF you can actually also get access to those links. Right. Let's maybe start with a little show of hands. Who knows what search manager is? >> Okay, great. >> The opposite. >> Who is uh who is using Manager in production? Okay, almost everyone. Great. So, basically search manager um for those who maybe not know it. It's a group of people. It's a community. lots of people that are very interested in X509 certificates in the Kubernetes world. And what we do is we um we try to create controllers, all kinds of Kubernetes uh things that are very useful for our users and we publish them on GitHub so that they can be used by almost a million people per day. and this group of people that are very interested in this and they're that are writing codes we're with almost 500 people um and of course we also have our own structure we have like maintainers contributors and so on um and all of this has been recognized by the CNCF and so we are a CNCF graduated project so the most um popular control that we make is also called search manager and And this controller basically issues certificates for you.

So in your Kubernetes cluster you can ask search manager to issue a certificate for you so that in your workloads you can actually use that certificate. So your workload can be a pot an ingress a gateway a service mesh. Search manager when it sees that you requested that certificate it will give you a certificate by asking a CA to um issue a certificate for you. So I think a lot of you will uh know laticrypt that's one of the CAS one of the most popular ones but you can also um issue private CAS using fault or uh cyber arc. So that's our most popular controller but we also have some other projects that we're working on. One of them is trust manager and trust manager is this autocontroller which is responsible for distributing trust across all your workloads in a Kubernetes cluster. You can define what uh certificates to trust by using a set of secrets config maps. You can also tell it to trust the um Mozilla public CAS and then trust manager will kind of combine all those certificates into one trust bundle and distribute this bund
