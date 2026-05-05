---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Experience"
themes: ["SRE Reliability"]
speakers: ["Berkay Uckac", "Futureplay Games"]
sched_url: https://kccnceu2026.sched.com/event/2CVxP/what-survived-production-operating-game-backends-at-million-player-scale-berkay-uckac-futureplay-games
youtube_search_url: https://www.youtube.com/results?search_query=What+Survived+Production%3A+Operating+Game+Backends+at+Million-Player+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# What Survived Production: Operating Game Backends at Million-Player Scale - Berkay Uckac, Futureplay Games

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Berkay Uckac, Futureplay Games
- Schedule: https://kccnceu2026.sched.com/event/2CVxP/what-survived-production-operating-game-backends-at-million-player-scale-berkay-uckac-futureplay-games
- Busca YouTube: https://www.youtube.com/results?search_query=What+Survived+Production%3A+Operating+Game+Backends+at+Million-Player+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre What Survived Production: Operating Game Backends at Million-Player Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxP/what-survived-production-operating-game-backends-at-million-player-scale-berkay-uckac-futureplay-games
- YouTube search: https://www.youtube.com/results?search_query=What+Survived+Production%3A+Operating+Game+Backends+at+Million-Player+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Aa04SuPhxtA
- YouTube title: What Survived Production: Operating Game Backends at Million-Player Scale - Berkay Uckac
- Match score: 0.997
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/what-survived-production-operating-game-backends-at-million-player-sca/Aa04SuPhxtA.txt
- Transcript chars: 26978
- Keywords: course, within, players, everything, reason, already, decided, important, change, everybody, decision, simple, single, experiences, wanted, analytics, starting, actually

### Resumo baseado na transcript

Uh, today I'll be talking to you about our backend experiences over the last three years and what we've built. And hopefully uh the time is going to be enough because there's a lot to go through over the the things that we've done over the last three years. Everything was going well and then after a while like with everything else the metrics were kind of plateaued over the years and in 2023 we decided to revamp the merch gardens and you know with new marketing, new ads, new everything that you might think about. Um so with all that marketing challenges and I guess the art and the story and everything that is beautiful and good-looking um the question is of course raised towards the tech side. off with the the architecture um the so we decided to have microservices but those are in like quote uncult status uh because like like you know I guess everybody knows that there there's like you can spawn up 10,000 different micros microservices and um So for example we have a service called tournament service that is quite self-explanatory and then when we have tournaments running during the schedule we can scale that up differently compared to a I guess a different service that we might have.

### Excerpt da transcript

So, welcome everybody to CubeCon 2026 Amsterdam. So far, I hope everybody's having a great time here. Uh, my name is Barai. Uh, today I'll be talking to you about our backend experiences over the last three years and what we've built. And hopefully uh the time is going to be enough because there's a lot to go through over the the things that we've done over the last three years. So, it's it's quite packed. Hopefully, there's going to be enough time at the end to ask quick questions. So uh if not then you know where to find me and anywhere within the uh conference or after the conference. Uh so let's get started. uh I wanted to I guess contain this talk in general to the small teams or even if you are working at a um bigger place where it's like you you might need to expand your horizons a bit because we kind of gone through few challenges um and and there is also a phenomenon these days that you know there's an understanding of of of course like we do love CNCF and the main reason that we are here is because that I guess we do love that Um but there's also the perspective of um you know within the industry that you can just spawn up a Hester VPS and it's going to be okay.

Um and and I I think the reality is going to be like somewhere in between for uh smaller organizations or teams like us where you need to kind of think about the the operational complexities. Um so I would like to start off with our story a bit and you know why we are here today. Um without going into the full details about our you know game or anything um so our game in focus today is March Gardens. It it it is a mobile game that launched in 2020. Originally it had a promising scale and it had a promising numbers. Everything was going well and then after a while like with everything else the metrics were kind of plateaued over the years and in 2023 we decided to revamp the merch gardens and you know with new marketing, new ads, new everything that you might think about. And of course as a result um everything was perfect. Um we had thousand% more downloads. Players are just like running in. It's all great. And the reason that we do that is for those unfamiliar with like the gaming landscape here.

Uh to go I guess this is a really high level summary of what liveops is. But it is the time that is after a game has been launched these days. So uh in the past you would have a game you launch it and that's about it. You make your sales. And these days even the paid games you see a lot of liv
