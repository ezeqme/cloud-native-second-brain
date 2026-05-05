---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Open Interfaces + Interoperability"
themes: ["AI ML"]
speakers: ["Melanie Cebula", "Airbnb"]
sched_url: https://kccncna2022.sched.com/event/182Ih/whats-going-arm-adopting-arm64-at-airbnb-melanie-cebula-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+Going+ARM%3A+Adopting+ARM64+At+Airbnb+CNCF+KubeCon+2022
slides: []
status: parsed
---

# What's Going ARM: Adopting ARM64 At Airbnb - Melanie Cebula, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[AI ML]]
- País/cidade: United States / Detroit
- Speakers: Melanie Cebula, Airbnb
- Schedule: https://kccncna2022.sched.com/event/182Ih/whats-going-arm-adopting-arm64-at-airbnb-melanie-cebula-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+Going+ARM%3A+Adopting+ARM64+At+Airbnb+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre What's Going ARM: Adopting ARM64 At Airbnb.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ih/whats-going-arm-adopting-arm64-at-airbnb-melanie-cebula-airbnb
- YouTube search: https://www.youtube.com/results?search_query=What%27s+Going+ARM%3A+Adopting+ARM64+At+Airbnb+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tKpvFWO3Ejk
- YouTube title: What's Going ARM: Adopting ARM64 At Airbnb - Melanie Cebula, Airbnb
- Match score: 0.864
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/whats-going-arm-adopting-arm64-at-airbnb/tKpvFWO3Ejk.txt
- Transcript chars: 26305
- Keywords: support, architecture, multi-arch, performance, actually, images, platform, running, binaries, update, packages, infrastructure, analysis, pretty, software, application, manifest, probably

### Resumo baseado na transcript

hi I'm Melanie I'm here to talk about what's going on adopting arm64 at Airbnb so for the agenda I'm going to first give an overview of arm then the pitfalls and challenges we face and finally how we designed multi-arch support at Airbnb so what is going on arm armed is a company that designs the arm architecture and licenses licenses it to other vendors and who then develop their own arm-based processors lots of companies have worked with arm for example Qualcomm ampere Amazon and Nvidia Apple Etc another challenge is the high surface area so anything running on your servers is affected for example everything including the base infrastructure build tool chain applications common functionality running on machines such as security and observability and more so this makes the challenge a full stack and cost-functional team effort that requires expertise Staffing commitment and coordination a pitfall we ran into early on is that a lot of our migrations are sort of treated as All or Nothing migrations but for arm we don't actually need a scope to on the right Hardware based on their price performance needs so it makes sense for some but maybe not the others um I included a diagram that has priced on the y-axis and perf on x-axis and on the right I have a few choices of Hardware I could run my workload on these each will land somewhere on the graph in the end I will choose to...

### Excerpt da transcript

hi I'm Melanie I'm here to talk about what's going on adopting arm64 at Airbnb so for the agenda I'm going to first give an overview of arm then the pitfalls and challenges we face and finally how we designed multi-arch support at Airbnb so what is going on arm armed is a company that designs the arm architecture and licenses licenses it to other vendors and who then develop their own arm-based processors lots of companies have worked with arm for example Qualcomm ampere Amazon and Nvidia Apple Etc and I want to give a brief history of two architectures so we start with IA 32s which started out as a workstation and PC optimized um architecture and then that evolved into xa664 which won the server Market while competing architectures failed to capture that market arm32 however had a foothold where Energy Efficiency matters for example with mobile and embedded devices but then arm 64 came out whereas before I'm 30 arm 32 targets efficiency now there is a competitive arm design that targets both Energy Efficiency and performance so who here has an apple M1 laptop okay great so these new advantages combined with licensing terms allows other vendors like apple to switch out their Intel processor for their own custom Arm based processor so if you're a developer that uses the MacBook M1 I'm sure you've noticed that Apple switched completely from their Intel based processors to their own M1 design so now developers are exposed to arm 64 as they had to build some developer support for Darwin and arm in their tool chains so like Apple Cloud vendors want to create their own processors similarly they work with arm to create custom systems on Chip's designs and sell it to the consumer all major Cloud providers now have custom arm-based VMS and generally they advertise Energy Efficiency and performance and our price varies deeply compared to the other instances this encourages customers to adopt arm support to run on cheaper Hardware however there are pitfalls and challenges with arm okay so firstly the architecture you're using and developing for uh historically is x8664 which is not compatible with arm 64.

in the past you may have switched between maybe AMD and Intel instances for example but that's less challenging because the instruction set is pretty much the same Additionally the main part of this incompatibility for Apple was masked largely because of their fancy Rosetta technology which automatically detects and translates x8664 binaries and translates them to
