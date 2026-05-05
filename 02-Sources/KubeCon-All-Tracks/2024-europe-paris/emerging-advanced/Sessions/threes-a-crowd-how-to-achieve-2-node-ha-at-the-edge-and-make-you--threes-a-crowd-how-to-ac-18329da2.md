---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Tyler Gillson", "Pedro Oliveira", "Spectro Cloud"]
sched_url: https://kccnceu2024.sched.com/event/1YeQq/threes-a-crowd-how-to-achieve-2-node-ha-at-the-edge-and-make-your-cfo-smile-tyler-gillson-pedro-oliveira-spectro-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Three%E2%80%99s+a+Crowd%3A+How+to+Achieve+2-Node+HA+at+the+Edge+and+Make+Your+CFO+Smile+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Three’s a Crowd: How to Achieve 2-Node HA at the Edge and Make Your CFO Smile - Tyler Gillson & Pedro Oliveira, Spectro Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: France / Paris
- Speakers: Tyler Gillson, Pedro Oliveira, Spectro Cloud
- Schedule: https://kccnceu2024.sched.com/event/1YeQq/threes-a-crowd-how-to-achieve-2-node-ha-at-the-edge-and-make-your-cfo-smile-tyler-gillson-pedro-oliveira-spectro-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Three%E2%80%99s+a+Crowd%3A+How+to+Achieve+2-Node+HA+at+the+Edge+and+Make+Your+CFO+Smile+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Three’s a Crowd: How to Achieve 2-Node HA at the Edge and Make Your CFO Smile.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQq/threes-a-crowd-how-to-achieve-2-node-ha-at-the-edge-and-make-your-cfo-smile-tyler-gillson-pedro-oliveira-spectro-cloud
- YouTube search: https://www.youtube.com/results?search_query=Three%E2%80%99s+a+Crowd%3A+How+to+Achieve+2-Node+HA+at+the+Edge+and+Make+Your+CFO+Smile+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BHDuy43k42A
- YouTube title: Three’s a Crowd: How to Achieve 2-Node HA at the Edge and Make Your CFO Smile
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/threes-a-crowd-how-to-achieve-2-node-ha-at-the-edge-and-make-your-cfo/BHDuy43k42A.txt
- Transcript chars: 30486
- Keywords: leader, available, running, highly, follower, actually, basically, obviously, liveness, applications, machine, questions, application, cluster, replication, checks, little, database

### Resumo baseado na transcript

today what we will cover most is obviously why and the motivation of why we're doing this today and and then we're going to take you take you guys through the different architecture that we've built we are trying to set up a demo for you live um we'll see we'll see if the the demo gods are with us we did sacrifice a few closers this morning so let's see if that comes through and um and then obviously we'll we'll have some questions and uh and and we'll

### Excerpt da transcript

today what we will cover most is obviously why and the motivation of why we're doing this today and and then we're going to take you take you guys through the different architecture that we've built we are trying to set up a demo for you live um we'll see we'll see if the the demo gods are with us we did sacrifice a few closers this morning so let's see if that comes through and um and then obviously we'll we'll have some questions and uh and and we'll have some fun together so my name is PED Aliva I'm a Senior Solutions architect at spectr cloud and I'm joined here today with my esteemed friend Tyler hi everyone I'm Tyler live yeah um pleased to be here today honored to be presenting here at cucon um I'm a principal software engineer at Spectre cloud and I manage our Advanced projects team so we get to build PC's with all the latest greatest exciting kubernetes Tech and then sometimes integrate it with the core platform one example being two node ha you get to play with the cool stuff yeah that's what I means cool so let's uh let's take a a step back and try to picture the scene that we're an Enterprise that effectively is managing or running different petrol station stores or maybe different coffee shops or perhaps a retailer right and in this scenario the matter of the fact is that you will have a lot of locations right so perhaps you want to deploy uh kubernetes applications there at the edge because you're going through some transformation and you want to give your customers a better user experience or perhaps you're running inferencing at the edge because these days everything is about Ai and as you do that your applications need to be highly available okay so because they're critical there are are situations where you might be able to get away with a one node um running those applications and if that's the case and your meantime to resolution if the application goes down is a few hours or maybe a few days and you can sustain that then that's okay but what we see actually with most of our customers and Enterprises that we work with is that there's a massive need to actually run business critical applications at the edge and when this comes you actually need to have highly available infrastructure and obviously highly available applications what this means is things really start to stack up okay if we're in the data center things are easy right we have highly available power we have highly available virtual machines bare metal nodes life is good but a
