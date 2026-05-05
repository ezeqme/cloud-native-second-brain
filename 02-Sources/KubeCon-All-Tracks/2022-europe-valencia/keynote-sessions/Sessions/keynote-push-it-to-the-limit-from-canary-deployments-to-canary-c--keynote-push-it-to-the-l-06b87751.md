---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Keynote Sessions"
themes: ["Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Henrik Høegh", "Platform Engineer", "Lunar"]
sched_url: https://kccnceu2022.sched.com/event/yuG5/keynote-push-it-to-the-limit-from-canary-deployments-to-canary-clusters-henrik-hoegh-platform-engineer-lunar
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Push+It+to+the+Limit%3A+From+Canary+Deployments+to+Canary+Clusters+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Keynote: Push It to the Limit: From Canary Deployments to Canary Clusters - Henrik Høegh, Platform Engineer, Lunar

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Henrik Høegh, Platform Engineer, Lunar
- Schedule: https://kccnceu2022.sched.com/event/yuG5/keynote-push-it-to-the-limit-from-canary-deployments-to-canary-clusters-henrik-hoegh-platform-engineer-lunar
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Push+It+to+the+Limit%3A+From+Canary+Deployments+to+Canary+Clusters+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Keynote: Push It to the Limit: From Canary Deployments to Canary Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yuG5/keynote-push-it-to-the-limit-from-canary-deployments-to-canary-clusters-henrik-hoegh-platform-engineer-lunar
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Push+It+to+the+Limit%3A+From+Canary+Deployments+to+Canary+Clusters+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NpdHcrakhmo
- YouTube title: Keynote: Push It to the Limit: From Canary Deployments to Canary Clusters - Henrik Høegh, Lunar
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keynote-push-it-to-the-limit-from-canary-deployments-to-canary-cluster/NpdHcrakhmo.txt
- Transcript chars: 12132
- Keywords: cluster, weight, routing, remove, failover, flux, basically, clusters, called, actually, awesome, complexity, branch, external, weights, shuttle, annotations, canary

### Resumo baseado na transcript

hi what's an i.t crowd i'm going to talk about how we went from canary deployments to canary clusters basically how we do failover clusters in luna it will be slightly technical but i hope that's okay i work at a company called luna no i don't think many people here know about it so i took the liberty to post this slide we have half a million customers uh 650 employees almost 700 now we make a app with a bank and you can invest in stocks and stuff

### Excerpt da transcript

hi what's an i.t crowd i'm going to talk about how we went from canary deployments to canary clusters basically how we do failover clusters in luna it will be slightly technical but i hope that's okay i work at a company called luna no i don't think many people here know about it so i took the liberty to post this slide we have half a million customers uh 650 employees almost 700 now we make a app with a bank and you can invest in stocks and stuff like that we are a tech company so at luna i guess you can call me a lunatec or something yeah we are apparently a unicorn now it's something about evaluation i'm not an expert and apparently we are times two i don't know how that works with unicorn but yeah we'll look at that my name is henrik who i'm from the nordics slightly different climate my genes are not made for this climate at least i learned so that's it i'm a co-organizer at the cloud native or whose group together with my colleague casper who's the organizer um yeah i speak at different meetups conferences and stuff i really like doing that sharing knowledge um i worked as a consultant for many years but now i work at luna i've been there for nine months and my hobby is dungeon and dragons so i basically so basically in to people who don't know what that is i paint small plastic stuff and then with other grown-ups we play with them roughly yeah one of the things i really like about dungeon and dragons is that one thing you learn is that a strong team is a diverse team four wizards won't survive the tavern so and everybody that's apparent to everyone who played it so so yeah that's me um this is the meetup groups we have in the nordics and we actually combine them to the cloud native nordics so if you like cold weather or rain or in the area by all means join us go to cloudnativenordics.com and we have a slack work group i think it's called where we communicate and exchange speakers and stuff like that so it's really awesome community so the at the end of today i'll talk about our tech stack i'll talk about what how we did failovers basically how did we achieve the the capability of doing a failover using githubs because that's not as easy as we thought it was and then some of the key changes to get speed and get more confident and remove complexity um and then i'll talk just about what we are planning on doing on the road ahead so it was a journey i tried to separate dungeon and dragons and work so you know um but basically casper and bian did an ama
