---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Networking"]
speakers: ["Leonardo da Mata", "Spotify"]
sched_url: https://kccnceu2026.sched.com/event/2EFzX/cloud-native-theater-envoycon-inside-spotifys-envoy-architecture-what-we-learned-the-hard-way-leonardo-da-mata-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+Inside+Spotify%E2%80%99s+Envoy+Architecture%3A+What+We+Learned+the+Hard+Way+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | EnvoyCon: Inside Spotify’s Envoy Architecture: What We Learned the Hard Way - Leonardo da Mata, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Leonardo da Mata, Spotify
- Schedule: https://kccnceu2026.sched.com/event/2EFzX/cloud-native-theater-envoycon-inside-spotifys-envoy-architecture-what-we-learned-the-hard-way-leonardo-da-mata-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+Inside+Spotify%E2%80%99s+Envoy+Architecture%3A+What+We+Learned+the+Hard+Way+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | EnvoyCon: Inside Spotify’s Envoy Architecture: What We Learned the Hard Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzX/cloud-native-theater-envoycon-inside-spotifys-envoy-architecture-what-we-learned-the-hard-way-leonardo-da-mata-spotify
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+Inside+Spotify%E2%80%99s+Envoy+Architecture%3A+What+We+Learned+the+Hard+Way+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CAn22mnA6kE
- YouTube title: Cloud Native Theater | EnvoyCon: Inside Spotify’s Envoy Architecture: What We Le... Leonardo da Mata
- Match score: 0.956
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-envoycon-inside-spotifys-envoy-architecture-what/CAn22mnA6kE.txt
- Transcript chars: 12393
- Keywords: envoy, actually, requests, process, everything, request, filters, version, sidecar, second, wanted, spotify, architecture, features, running, inside, questions, learned

### Resumo baseado na transcript

I'm going to share you to you, um some learnings that we had, uh using Envoy on production and maybe you can learn from us our mistakes. I'm going to tell you why uh we had to what is architecture uh why we did to had to improve it the plan that we chose to improve it uh the problems that we face and uh if it's worth it to run me So we wanted to be more involved with envoy community and also we wanted to make more standardized we are actually abusing this uh uh x outc uh decorating the requests um and we wanted to be more uh uh close to the uh architecture itself where we have the um filters in the chain to change the requests. Uh one of the things that we learned uh throughout this process is that uh we were just doing 500 requests per second per CPU. So I mean everyone sees this like uh if they're doing a migration deployment or anything like this on scale uh you you you put a plan and you decide okay I'm going to put on one region check how it is put on canaries check how it goes and then follow a process. We had uh two different uh the request was going to through two different paths uh duplicated uh one with the old uh version and one with the new version with the filters and we're simply uh comparing metrics counting the difference between the headers that we're adding.

### Excerpt da transcript

Yeah. So, uh I'm Leonardo Damata, uh and I'm an engineer at Spotify. I'm going to share you to you, um some learnings that we had, uh using Envoy on production and maybe you can learn from us our mistakes. So, oh my god, how do I going to pass the the slide? There you go. Yeah. So, um here's a summary of my presentation. I'm going to tell you why uh we had to what is architecture uh why we did to had to improve it the plan that we chose to improve it uh the problems that we face and uh if it's worth it to run me in production spoiler yes um yeah in case you don't know Spotify is the largest uh digital audio streaming and one in 11 people in the world uh uses our services but I don't know if you know And the parimeter what is it like I mean very simplified version but you can see what it is. Um every request goes through GCO GCB and then reached our version of envoy proxy uh where we make some uh decoration on it and sends to to our backend uh services with this internal information that is used by envoy.

You can think like a a motorcycle with this side car with cool features that carries the request through our infrastructure and it's the front door right we are handling 10 million requests per second actually 11 million uh I got uh someone updated the number yesterday on the presentation thanks Yanik and Ana um and it is powered by this custo custom version of envoy and also has uh and on the side used to have this sidecar which is a Java process that we used to call using X out Z uh do to do our decoration. So it means like adding Spotify authentication information, some metadata that we needed and so on. Right? Historically this is uh every request we're going to this path and we were um calling this uh JVM uh process to in every in each request increasing our latency the Yes. So as I mentioned uh we wanted to be more involved to uh I didn't mention that yet. So we wanted to be more involved with envoy community and also we wanted to make more standardized we are actually abusing this uh uh x outc uh decorating the requests um and we wanted to be more uh uh close to the uh architecture itself where we have the um filters in the chain to change the requests.

So we decided to we saw opportunities here to change things. Uh one of the things that we learned uh throughout this process is that uh we were just doing 500 requests per second per CPU. Uh whereas the community had the benchmark of uh 10,000 requests per second per CPU core. So we were way below
