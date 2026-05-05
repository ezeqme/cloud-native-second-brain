---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["AI ML"]
speakers: ["Jean-François Hubert", "Development Director", "Ubisoft Entertainment", "Mark Mandel", "Staff Developer Advocate", "Discord"]
sched_url: https://kccnceu2026.sched.com/event/2HgQn/keynote-how-ubisoft-orchestrates-global-multiplayer-games-with-agones-jean-francois-hubert-development-director-ubisoft-entertainment-mark-mandel-staff-developer-advocate-discord
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+How+Ubisoft+Orchestrates+Global+Multiplayer+Games+with+Agones+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Keynote: How Ubisoft Orchestrates Global Multiplayer Games with Agones - Jean-François Hubert, Development Director, Ubisoft Entertainment & Mark Mandel, Staff Developer Advocate, Discord

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jean-François Hubert, Development Director, Ubisoft Entertainment, Mark Mandel, Staff Developer Advocate, Discord
- Schedule: https://kccnceu2026.sched.com/event/2HgQn/keynote-how-ubisoft-orchestrates-global-multiplayer-games-with-agones-jean-francois-hubert-development-director-ubisoft-entertainment-mark-mandel-staff-developer-advocate-discord
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+How+Ubisoft+Orchestrates+Global+Multiplayer+Games+with+Agones+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Keynote: How Ubisoft Orchestrates Global Multiplayer Games with Agones.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgQn/keynote-how-ubisoft-orchestrates-global-multiplayer-games-with-agones-jean-francois-hubert-development-director-ubisoft-entertainment-mark-mandel-staff-developer-advocate-discord
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+How+Ubisoft+Orchestrates+Global+Multiplayer+Games+with+Agones+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rZDvc_1FyHE
- YouTube title: Keynote: How Ubisoft Orchestrates Global Multiplayer Games with Ago... J.F. Hubert & M. Mandel (ASL)
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/keynote-how-ubisoft-orchestrates-global-multiplayer-games-with-agones/rZDvc_1FyHE.txt
- Transcript chars: 3369
- Keywords: server, ubisoft, multiplayer, players, global, agones, provider, contributors, rainbow, mobile, software, infrastructure, source, instead, operational, workload, projects, playing

### Resumo baseado na transcript

Hi, my name is Joffis software software development director at Ubisoft. Uh, today I'm not here representing Discord but as founder of Agonz and today we'll show you how we've been building a truly global multiplayer infrastructure by leaning into cloudnative and open source technologies. Enter Gonz, the open source project that teaches Kubernetes how to host, scale, and orchestrate game servers. This architecture gave Rainbow 6 mobile a stable global launch and the ability to scale fast when players wanted to play. So, if you want to learn more about Agones, go to the links above or come say hi. And if you want to learn more about Ubisoft latest game or if you want to be part of the great Ubisoft family, please visit us at ubi.com or just come talk to me directly.

### Excerpt da transcript

Hi, my name is Joffis software software development director at Ubisoft. Hello everyone, my name is Mark Mandal. Uh, today I'm not here representing Discord but as founder of Agonz and today we'll show you how we've been building a truly global multiplayer infrastructure by leaning into cloudnative and open source technologies. Building tailored integration for each cloud provider just isn't sustainable. The gap between providers keep growing. So the amount of custom code required to keep up becomes a real drag on innovation. So instead of chasing those differences, we flipped the model. We decided that our operational model will be defined by Kubernetes and the CNCF ecosystem. We can then adopt a build once deploy everywhere mindset as a real strategy. We can take our workload and run them on any cloud provider or on prem with almost no friction. CNCF projects can also evolve faster than any in-house solutions ever could as we benefit from the improvements driven by thousands of contributors. So instead of playing the catchup game, we now stands on the shoulders of CNCF projects.

This is what allows us to have the operational maturity we need to support worldwide massive multiplayer games. But let's talk a little bit about authoritative multiplayer game server workloads because those are a little bit special. These power some of your favorite real-time multiplayer games where all players connect to a single server and that server is the authority over what is happening inside your game. What's fun about them though is they do this all in memory. So if players are playing on the game server, you can't shut it down because that's going to crash the game. Enter Gonz, the open source project that teaches Kubernetes how to host, scale, and orchestrate game servers. And we're very excited to be a brand new sandbox project in the CNCF. As of literally last week, agonized and communities really shine for us. For real-time gameplay, latency is key. So deploying our game server worldwide around the world close to our players is a hard requirement. Agonize allows us to easily place capacity where players actually are.

One of the best recent example of this is Rainbow 6 mobile. Since its launch last month, millions of game sessions have been served across multiple regions. This is important because different regions, different peaks, different availability conditions and our infrastructure could adapt dynamically. We could route traffic, capacity, supporting worklo
