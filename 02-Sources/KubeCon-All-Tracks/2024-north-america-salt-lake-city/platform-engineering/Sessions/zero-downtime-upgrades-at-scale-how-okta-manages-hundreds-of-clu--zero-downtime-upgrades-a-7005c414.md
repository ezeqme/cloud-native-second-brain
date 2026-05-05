---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Jérémy Albuixech", "Kahou Lei", "Okta"]
sched_url: https://kccncna2024.sched.com/event/1i7s6/zero-downtime-upgrades-at-scale-how-okta-manages-hundreds-of-clusters-daily-jeremy-albuixech-kahou-lei-okta
youtube_search_url: https://www.youtube.com/results?search_query=Zero+Downtime+Upgrades+at+Scale%3A+How+Okta+Manages+Hundreds+of+Clusters+Daily+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Zero Downtime Upgrades at Scale: How Okta Manages Hundreds of Clusters Daily - Jérémy Albuixech & Kahou Lei, Okta

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Jérémy Albuixech, Kahou Lei, Okta
- Schedule: https://kccncna2024.sched.com/event/1i7s6/zero-downtime-upgrades-at-scale-how-okta-manages-hundreds-of-clusters-daily-jeremy-albuixech-kahou-lei-okta
- Busca YouTube: https://www.youtube.com/results?search_query=Zero+Downtime+Upgrades+at+Scale%3A+How+Okta+Manages+Hundreds+of+Clusters+Daily+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Zero Downtime Upgrades at Scale: How Okta Manages Hundreds of Clusters Daily.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7s6/zero-downtime-upgrades-at-scale-how-okta-manages-hundreds-of-clusters-daily-jeremy-albuixech-kahou-lei-okta
- YouTube search: https://www.youtube.com/results?search_query=Zero+Downtime+Upgrades+at+Scale%3A+How+Okta+Manages+Hundreds+of+Clusters+Daily+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p5owrjrBm2w
- YouTube title: Zero Downtime Upgrades at Scale: How Okta Manages Hundreds of Clusters Daily - J. Albuixech, K. Lei
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/zero-downtime-upgrades-at-scale-how-okta-manages-hundreds-of-clusters/p5owrjrBm2w.txt
- Transcript chars: 36042
- Keywords: cluster, deployment, release, custer, environment, control, customer, application, traffic, platform, deploy, version, workflow, update, basically, create, switch, clusters

### Resumo baseado na transcript

so yeah hi I'm Jeremy and I'm a Staff engineer with the oero platform team hi my name is kah I'm a ppal engineer in offal platform team uh thank you for joining with us today uh we are excited to share how we manage and upgrade hundreds of kubernetes Custer daily without any service Interruption okay so let's go through the agenda first so we'll talk about the context and our challenges then we will briefly introduce our platform and then we will spend a large trunk of time

### Excerpt da transcript

so yeah hi I'm Jeremy and I'm a Staff engineer with the oero platform team hi my name is kah I'm a ppal engineer in offal platform team uh thank you for joining with us today uh we are excited to share how we manage and upgrade hundreds of kubernetes Custer daily without any service Interruption okay so let's go through the agenda first so we'll talk about the context and our challenges then we will briefly introduce our platform and then we will spend a large trunk of time to talk about our Solutions finally we will talk about some outcome and the result last but not least we will have a Q&A [Music] section so um our offal platform has two offering we have a public car offering which is a um multi-tenant multi subscriber and it support multiple customer per environment also we have a private car offering which has uh which is dedicated for One customer per environment and we have hundreds of them across the RO on top of that for the pirate car it also W on different car provider currently it w on ad and assure as well so um with a big picture of like how many Custer that we spend globally right so uh let me summarize like how we like what's the management challenge that we Face daily so first as I mentioned from the previous slides we have hundreds of environment and we are globally distributed and also we have hundreds of deployment that happen daily and they happen like 24 hour 7 and each customer environment are they different like they have different infrastructure size like they have different kubernetes size different DB size and they run on different application stack that serve different purpose and they are multi as well and also really to like make sure that our infrastructure version always up to dat so let's say right eks release a new kubernetes version we need to upgrade yway without any down time finally we need to have a constant security update that means that our OS level and our application stack level security patch need to up toate y away so our pass it to Jeremy to introduce platform thanks so before we get into more technical details about our deploy strategies we wanted to quickly go over our platform uh just to give you some important context about what we built so our platform runs all zero for all our customers it unifies many different customer offerings into a modern automated and scalable platform that is built for the future our goals were to increase uh business agility developer productivity scalability reliability and sec
