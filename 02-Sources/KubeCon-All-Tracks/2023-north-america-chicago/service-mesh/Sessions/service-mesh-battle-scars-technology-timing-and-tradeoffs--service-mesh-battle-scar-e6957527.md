---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Keith Mattix", "Microsoft", "John Howard", "Google", "Lin Sun", "solo.io", "Thomas Graf", "Isovalent", "Flynn", "Buoyant"]
sched_url: https://kccncna2023.sched.com/event/1R2ts/service-mesh-battle-scars-technology-timing-and-tradeoffs-keith-mattix-microsoft-john-howard-google-lin-sun-soloio-thomas-graf-isovalent-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Service+Mesh+Battle+Scars%3A+Technology%2C+Timing%2C+and+Tradeoffs+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Service Mesh Battle Scars: Technology, Timing, and Tradeoffs - Keith Mattix, Microsoft; John Howard, Google; Lin Sun, solo.io; Thomas Graf, Isovalent; Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Keith Mattix, Microsoft, John Howard, Google, Lin Sun, solo.io, Thomas Graf, Isovalent, Flynn, Buoyant
- Schedule: https://kccncna2023.sched.com/event/1R2ts/service-mesh-battle-scars-technology-timing-and-tradeoffs-keith-mattix-microsoft-john-howard-google-lin-sun-soloio-thomas-graf-isovalent-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Service+Mesh+Battle+Scars%3A+Technology%2C+Timing%2C+and+Tradeoffs+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Service Mesh Battle Scars: Technology, Timing, and Tradeoffs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ts/service-mesh-battle-scars-technology-timing-and-tradeoffs-keith-mattix-microsoft-john-howard-google-lin-sun-soloio-thomas-graf-isovalent-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Service+Mesh+Battle+Scars%3A+Technology%2C+Timing%2C+and+Tradeoffs+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fOZ2jCechns
- YouTube title: Service Mesh Battle Scars: Technology, Timing, and Tradeoffs - Panel
- Match score: 1.03
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/service-mesh-battle-scars-technology-timing-and-tradeoffs/fOZ2jCechns.txt
- Transcript chars: 38401
- Keywords: ebpf, actually, mesh, secure, encryption, handshake, linker, question, transport, thomas, google, working, functionality, everybody, kernel, authentication, protocol, talking

### Resumo baseado na transcript

good evening folks we're going to go ahead and get started um wanted to welcome you uh to service mesh battlecars Tech uh we're going to be talking about technology timing and tradeoff tonight want to thank you all for being here uh this late y'all could be off drinking somewhere so thank you for being here and uh as a result as a as a reward we want to try to make this exciting and hopefully you can learn something as well I'm super excited to be here with

### Excerpt da transcript

good evening folks we're going to go ahead and get started um wanted to welcome you uh to service mesh battlecars Tech uh we're going to be talking about technology timing and tradeoff tonight want to thank you all for being here uh this late y'all could be off drinking somewhere so thank you for being here and uh as a result as a as a reward we want to try to make this exciting and hopefully you can learn something as well I'm super excited to be here with my esteemed panelist and I'm going to go ahead and let them introduce themselves uh start with Thomas first of all this was the best intro ever to a panel this is crazy good hello everybody I'm Thomas uh CTO and co-founder of is surveillance uh creators of the cni recently graduated I also wrote cycl as blog post a while ago that triggered a lot of the conversations that we will talk about today yeah I'm John Howard I'm a software engineer at Google and I've been working on EO for a long time about five years years now hi my name is Lena I'm the head of Open Source at a small company soloo I've been working is still a little bit longer than John since one of the founding member but I'm not as productive as him I'm Flynn I'm uh I actually work in marketing am I supposed to be on this stage I'm a technical evangelist for linardy at buyant before that I was the original author of Emissary Ingress I'm one of the gamma co-leads over with the Gateway API people and I'm pretty sure I've been working in engineering possibly longer than some of yall have been alive actually so yeah and last I am Keith Maddox engineering lead at Microsoft uh I am also your way too excited to be doing this panel uh this is all fake I'm tired but we're going to have a good time anyway um yeah as a disclaimer I didn't want to say I uh we have multiple service meses represented here uh I disclaimer I'm a maintainer of iso service mesh but I promise to remain impartial throughout the contents of this uh of this panel uh Microsoft uses all three of these Technologies in production uh so take that for what it's worth I plan to you say that like it wouldn't happen anyway so why are we here why are we having this talk about technology timing and trade-offs well as you can see these are three uh cncf graduated projects three cncf graduated Technologies first of all let's get a round of applause for these three incredible Technologies powering Innovation and productivity and organizations across the world love what the cncf does and so we'r
