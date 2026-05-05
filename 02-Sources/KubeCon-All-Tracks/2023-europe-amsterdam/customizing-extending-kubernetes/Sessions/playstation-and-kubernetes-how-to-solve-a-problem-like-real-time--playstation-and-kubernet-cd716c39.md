---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Joseph Irving", "PlayStation"]
sched_url: https://kccnceu2023.sched.com/event/1HyWs/playstation-and-kubernetes-how-to-solve-a-problem-like-real-time-joseph-irving-playstation
youtube_search_url: https://www.youtube.com/results?search_query=PlayStation+and+Kubernetes%3A+How+to+Solve+a+Problem+Like+Real-Time+CNCF+KubeCon+2023
slides: []
status: parsed
---

# PlayStation and Kubernetes: How to Solve a Problem Like Real-Time - Joseph Irving, PlayStation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joseph Irving, PlayStation
- Schedule: https://kccnceu2023.sched.com/event/1HyWs/playstation-and-kubernetes-how-to-solve-a-problem-like-real-time-joseph-irving-playstation
- Busca YouTube: https://www.youtube.com/results?search_query=PlayStation+and+Kubernetes%3A+How+to+Solve+a+Problem+Like+Real-Time+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre PlayStation and Kubernetes: How to Solve a Problem Like Real-Time.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWs/playstation-and-kubernetes-how-to-solve-a-problem-like-real-time-joseph-irving-playstation
- YouTube search: https://www.youtube.com/results?search_query=PlayStation+and+Kubernetes%3A+How+to+Solve+a+Problem+Like+Real-Time+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pklRTQoRrNY
- YouTube title: PlayStation and Kubernetes: How to Solve a Problem Like Real-Time - Joseph Irving, PlayStation
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/playstation-and-kubernetes-how-to-solve-a-problem-like-real-time/pklRTQoRrNY.txt
- Transcript chars: 36418
- Keywords: server, players, servers, playing, player, cluster, running, another, matchmaker, deployment, question, generally, around, experience, allocator, actually, connect, concept

### Resumo baseado na transcript

let's go um hello everyone thanks for coming out today my name is Joseph Irving I work at PlayStation uh give you a little bit of context about what I do I work in a kind of centralized team at PlayStation called online technology and we assist the various PlayStation Studios with doing online stuff and that's generally like hosting services like back in terms of the games or also infrastructure and best practices around doing that kind of thing so and what I mean by Studios these are Studios

### Excerpt da transcript

let's go um hello everyone thanks for coming out today my name is Joseph Irving I work at PlayStation uh give you a little bit of context about what I do I work in a kind of centralized team at PlayStation called online technology and we assist the various PlayStation Studios with doing online stuff and that's generally like hosting services like back in terms of the games or also infrastructure and best practices around doing that kind of thing so and what I mean by Studios these are Studios such as Gorilla Games who make a horizon they're based in Amsterdam some of them are here today and Studios like Santa Monica who make God of War Insomniac make Spider-Man Etc these are what we call PlayStation Studios collectively so there's many of them but when I when I'm talking about them that's the one that's who I'm talking about um so we don't make any games ourselves we just assist these teams with doing their online side of things especially as PlayStation traditionally is more of a at least these days considered more of a single player company but we're moving into doing more live servicing multiplayer game style things and that's what the talk today is going to be about like what are the kind of challenges of running these multiplayer games especially if you want to do it in a kubernetes cluster like the Mad Men that we are so here is um the like level level the table of contents for today which I'm going to take you through um about all the challenges of running these things in kubernetes and but like all video games we have a mandatory unskippable tutorial that we're going to do first and that is um just to explain why is that what is a real-time game server what am I talking about um and I will start by saying what isn't a real-time game server so a lot of games though the game client is what the the thing that actually runs on your machine whether that be A PS5 a PC on your phone that's what we call the game client and that runs the game and these often talk to a variety of different back-end services that are running in the cloud or a data center these could be like a leaderboard service with the highest scores or the fastest times a racing game it could be things like in Little Big Planet you've got player generated content player levels or it could be an in-game store where you can purchase items or something these are can be ran quite easily in kubernetes they're they they see themselves without there's an API probably grpc or HTTP API running in a
