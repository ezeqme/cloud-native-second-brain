---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Nicole van der Hoeven", "Grafana Labs"]
sched_url: https://kccncna2024.sched.com/event/1i7m6/watching-the-watchers-how-we-do-continuous-reliability-at-grafana-labs-nicole-van-der-hoeven-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Watching+the+Watchers%3A+How+We+Do+Continuous+Reliability+at+Grafana+Labs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Watching the Watchers: How We Do Continuous Reliability at Grafana Labs - Nicole van der Hoeven, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Nicole van der Hoeven, Grafana Labs
- Schedule: https://kccncna2024.sched.com/event/1i7m6/watching-the-watchers-how-we-do-continuous-reliability-at-grafana-labs-nicole-van-der-hoeven-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Watching+the+Watchers%3A+How+We+Do+Continuous+Reliability+at+Grafana+Labs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Watching the Watchers: How We Do Continuous Reliability at Grafana Labs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7m6/watching-the-watchers-how-we-do-continuous-reliability-at-grafana-labs-nicole-van-der-hoeven-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Watching+the+Watchers%3A+How+We+Do+Continuous+Reliability+at+Grafana+Labs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pCxmwvqTklo
- YouTube title: Watching the Watchers: How We Do Continuous Reliability at Grafana Labs - Nicole van der Hoeven
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/watching-the-watchers-how-we-do-continuous-reliability-at-grafana-labs/pCxmwvqTklo.txt
- Transcript chars: 24577
- Keywords: grafana, actually, mimir, observability, continuous, testing, reliability, cluster, everything, customers, logs, within, having, engineers, production, prometheus, monitoring, monitor

### Resumo baseado na transcript

hey everyone I'm Dutch so I'm starting on time I had to check what time it was because I don't know when I am I am Nicole ven I am a senior developer Advocate at grafana Labs so I think it's really hard to be here at cubec con without hearing the word observability it's such a weird word because it's something that we don't typically use in our our ordinary lives but when we're talking about the health of our systems for some reason it's everywhere we turn into

### Excerpt da transcript

hey everyone I'm Dutch so I'm starting on time I had to check what time it was because I don't know when I am I am Nicole ven I am a senior developer Advocate at grafana Labs so I think it's really hard to be here at cubec con without hearing the word observability it's such a weird word because it's something that we don't typically use in our our ordinary lives but when we're talking about the health of our systems for some reason it's everywhere we turn into voyur we don't just want to watch we also want to watch the Watchers in fact we're so paranoid about it that we employ all sorts of things just so just to make sure that we can observe everything but I want to challenge that because I don't think observability should be the goal I think in fact that we're focusing on the wrong thing if observability is your end goal then there's something wrong with your plan so this is an actual screenshot of a production incident that we faced at grafana Labs hi Paul thanks for joining um this is uh something that happened at grafana to one of our clusters our mimir clusters so this is a a metric time series database and um you can see they're very scary scary things there there are three spikes for some reason we experienced a surge in traffic bad stuff happened we did the thing of turning it off and on again that worked a little bit for a while and then suddenly it worked it recovered we had everything instrumented everything was observable we had the data we could graph it we could visualize it did we fix it no observable usable not really because this was a recurring issue in fact this issue cost us $100,000 over a couple of years and yet we are very observable we are the observability company so should observability be the end goal I don't think so I think the end goal should be something like continuous reliability it's kind of like actually when you think about it saying that the grade that you give to a student is you're very gradable what does that mean that means absolutely nothing useful is what it means anyone who's played a fantasy RPG knows that you get the best weapons at a blacksmith that's because a blacksmith has a forge a forge is something like a furnace where you go to get your metal hammered and heated into something better into something harder it could be a sword or a battle axe or something even more awesome um but the thing is we when we think of our systems we almost expect them to be perfect right away when in fact they have to go throu
