---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Tim Ramlot", "Maël Valais", "Ashley Davis", "Venafi"]
sched_url: https://kccncna2023.sched.com/event/1R2rN/project-maintainers-explain-cert-manager-in-5-levels-of-difficulty-tim-ramlot-mael-valais-ashley-davis-venafi
youtube_search_url: https://www.youtube.com/results?search_query=Project+Maintainers+Explain+Cert-Manager+in+5+Levels+of+Difficulty+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Project Maintainers Explain Cert-Manager in 5 Levels of Difficulty - Tim Ramlot, Maël Valais & Ashley Davis, Venafi

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Tim Ramlot, Maël Valais, Ashley Davis, Venafi
- Schedule: https://kccncna2023.sched.com/event/1R2rN/project-maintainers-explain-cert-manager-in-5-levels-of-difficulty-tim-ramlot-mael-valais-ashley-davis-venafi
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Maintainers+Explain+Cert-Manager+in+5+Levels+of+Difficulty+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Project Maintainers Explain Cert-Manager in 5 Levels of Difficulty.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rN/project-maintainers-explain-cert-manager-in-5-levels-of-difficulty-tim-ramlot-mael-valais-ashley-davis-venafi
- YouTube search: https://www.youtube.com/results?search_query=Project+Maintainers+Explain+Cert-Manager+in+5+Levels+of+Difficulty+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OxGWG6CD1iU
- YouTube title: Project Maintainers Explain Cert-Manager in 5 Levels of D... Tim Ramlot, Maël Valais & Ashley Davis,
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/project-maintainers-explain-cert-manager-in-5-levels-of-difficulty/OxGWG6CD1iU.txt
- Transcript chars: 28791
- Keywords: certificate, manager, actually, resource, certificates, secret, private, issuer, request, driver, client, requests, ingress, thanks, basically, question, application, create

### Resumo baseado na transcript

hello okay that sounds correct uh we're going to get started so hello everyone thank you for coming um I'm Ash I'll be starting us off and as you can see I need a new picture on this slide I've had a bit of a haircut since then um welcome to C manager in five levels of difficulty uh today we're going to be taking you through C manager in five levels of difficulty you got me you got M here and Tim we're all at Veni we're all manager Distributing trust so don't you don't use the C ca.crt and you'll see how to use this properly uh in the next level so to summarize in level two we learned that the certificate resource gives you more C uh makes it uh possible to

### Excerpt da transcript

hello okay that sounds correct uh we're going to get started so hello everyone thank you for coming um I'm Ash I'll be starting us off and as you can see I need a new picture on this slide I've had a bit of a haircut since then um welcome to C manager in five levels of difficulty uh today we're going to be taking you through C manager in five levels of difficulty you got me you got M here and Tim we're all at Veni we're all manager maintainers uh which is good because of the content matter um to start us off uh we've got the typical slide where we show you a load of numbers um we like all of these numbers one of my favorite numbers on this is 1 million plus daily downloads uh the problem with that number is we don't actually know if it's true well we know it's not true actually we know it's bigger than that we don't know how big because um our container images are hosted on key. or Quay I don't know how you meant to pronounce it um and every time we try and look at the analytics we actually crash the analytics page we get a 500 error so if anyone is from Red Hat and could tell us how many downloads We have we'd love to know but we we I think we're the second biggest project we don't we'd love to know um the other important thing on this slide obviously is that we're a cncf incubating project that's why we're here today that's why you're here today I assume at least in part um we're really hoping at the moment that we're going to be hitting graduated status soon obviously that's the same level that kubernetes itself is at it'll be awesome to get there we're really hoping we'll get there before cubec Con in Paris next year um but yeah the security audit for that is currently ongoing which is awesome and uh watch this space hope hopefully uh the next time we're giving a talk will be a graduated project so here are the five levels of difficulty that we're going to be talking about um I'm going to do a little bit of audience interaction not much if you think you're at one of these levels uh just raise your hand and then put your hand down if uh you no longer understand what we're talking about so if you've used SE manager at all um you've probably done something like Ingress and Gateway annotations if you've ever issued a certificate using C manager put your hand up lots of hands that's great uh have you used a certificate resource yeah private pki anyone doing private pki and especially if you're using trust manager yeah few hands there um CSI drivers approve
