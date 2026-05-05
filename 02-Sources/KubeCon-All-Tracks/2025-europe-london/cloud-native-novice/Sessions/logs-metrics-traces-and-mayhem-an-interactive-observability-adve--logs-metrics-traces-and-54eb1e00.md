---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["Observability"]
speakers: ["Jay Clifford", "Tom Glenn", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1txG5/logs-metrics-traces-and-mayhem-an-interactive-observability-adventure-game-jay-clifford-tom-glenn-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Logs%2C+Metrics%2C+Traces+and+Mayhem%3A+An+Interactive+Observability+Adventure+Game+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Logs, Metrics, Traces and Mayhem: An Interactive Observability Adventure Game - Jay Clifford & Tom Glenn, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Jay Clifford, Tom Glenn, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1txG5/logs-metrics-traces-and-mayhem-an-interactive-observability-adventure-game-jay-clifford-tom-glenn-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Logs%2C+Metrics%2C+Traces+and+Mayhem%3A+An+Interactive+Observability+Adventure+Game+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Logs, Metrics, Traces and Mayhem: An Interactive Observability Adventure Game.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txG5/logs-metrics-traces-and-mayhem-an-interactive-observability-adventure-game-jay-clifford-tom-glenn-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Logs%2C+Metrics%2C+Traces+and+Mayhem%3A+An+Interactive+Observability+Adventure+Game+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D8r5j_R9QsA
- YouTube title: Logs, Metrics, Traces and Mayhem: An Interactive Observability Adventure... Jay Clifford & Tom Glenn
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/logs-metrics-traces-and-mayhem-an-interactive-observability-adventure/D8r5j_R9QsA.txt
- Transcript chars: 27774
- Keywords: logs, traces, metrics, adventure, observability, blacksmith, actually, basically, accept, wizard, little, seconds, probably, enough, awesome, grafana, another, happened

### Resumo baseado na transcript

I know it's uh it's late in the day and I think everyone's probably very exhausted and uh ready for the cube crawl. So, we'll try and keep this nice one quick and uh a little bit light-hearted and entertaining. We'll talk about our tools of the trade on our adventure, the metrics, logs, and traces. And we do this with observability tools like logs, metrics, and traces. But the problem is it can go wrong when we don't have these things in place. Uh so Cyber Punk is one that I'm hugely into at the moment, but when it first came out, there were massive performance problems, mostly on the last gen consoles, but when it first came out, people were basically saying it just didn't work.

### Excerpt da transcript

Hey everyone, thanks for joining. I know it's uh it's late in the day and I think everyone's probably very exhausted and uh ready for the cube crawl. So, we'll try and keep this nice one quick and uh a little bit light-hearted and entertaining. We're not going to go through any crazy complicated theory stuff. It's a bit of an interactive and fun session for you all. So, we're here today to talk about logs, metrics, and traces and a little bit of mayhem for you. So, before we get started, I just want to go through who we are. I'm Tom Glenn. I'm a senior developer advocate for Grafana Labs. I've been a software engineer for the last sort of 18 years and my background is predominantly in um game development. So I worked on backend game software and um I'm a hobbyist game developer as well. So Jay, my name is Jay Clifford and funny enough I'm also a developer advocate at Grafana Labs. Um at Grafana Labs I mainly deal with our log aggregation database Loki. to write a lot of the documentation, do a lot of the education and then in my past I worked for Influx Data, did a lot with Telegraph and Influx DB.

Um, and loved Grafana so much I ended up here. Um, so setting the scene, uh, if you're going to buy into our theme today, you are all heroes on an adventure with us. We have a series of quests. We're going to talk a little bit about what observability is, where it can go wrong. We'll talk about our tools of the trade on our adventure, the metrics, logs, and traces. And then what you're all here for, the actual game itself, the interactive adventure, all textbased with a bit of an observability twist. Hey, Tom. Yep. Then we'll talk about takeaways, how you can get hold of the game yourself. So, we will save the GitHub repo to the very end, and then any questions that you might have. Wicked. So, can I get a quick show of hands? Not that I can see anyone because of the bright light. Um, but who here um is comfortable with the term obser observability? Like what do you know what we mean when we're talking about that? Okay, cool. I I think that's like half of the room, but I can't actually see. Um, so basically what we're talking about when we uh when we say observability is monitoring a system and understanding what it does based on its inputs and its outputs.

So typically uh a system may uh appear as a sort of a black box and it it can be sometimes difficult to know what's going on inside of that. And so when we're uh let's say we're debugging an application, how
