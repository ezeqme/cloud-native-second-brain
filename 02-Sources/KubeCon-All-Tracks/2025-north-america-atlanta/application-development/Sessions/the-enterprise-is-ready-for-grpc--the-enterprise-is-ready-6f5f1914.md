---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Alex Van Boxel", "Collibra"]
sched_url: https://kccncna2025.sched.com/event/27FVn/the-enterprise-is-ready-for-grpc-alex-van-boxel-collibra
youtube_search_url: https://www.youtube.com/results?search_query=The+Enterprise+Is+Ready+for+gRPC+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Enterprise Is Ready for gRPC - Alex Van Boxel, Collibra

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United States / Atlanta
- Speakers: Alex Van Boxel, Collibra
- Schedule: https://kccncna2025.sched.com/event/27FVn/the-enterprise-is-ready-for-grpc-alex-van-boxel-collibra
- Busca YouTube: https://www.youtube.com/results?search_query=The+Enterprise+Is+Ready+for+gRPC+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Enterprise Is Ready for gRPC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVn/the-enterprise-is-ready-for-grpc-alex-van-boxel-collibra
- YouTube search: https://www.youtube.com/results?search_query=The+Enterprise+Is+Ready+for+gRPC+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mbnP3jSx6fw
- YouTube title: The Enterprise Is Ready for gRPC - Alex Van Boxel, Collibra
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-enterprise-is-ready-for-grpc/mbnP3jSx6fw.txt
- Transcript chars: 18599
- Keywords: actually, important, binary, contract, contracts, everything, fields, represent, server, selling, format, numbers, unknown, filter, systems, documentation, another, interface

### Resumo baseado na transcript

So, I hope everybody knows that he wants to be here because I'm going to talk about nothing new. All the things that I'm going to talk about are ancient years ago, years old. Um there are very good um API guidelines the Google API design guidelines if you really want to stick to a good uh standard that's a good one.

### Excerpt da transcript

So, I hope everybody knows that he wants to be here because I'm going to talk about nothing new. All the things that I'm going to talk about are ancient years ago, years old. So, just to be sure, there's no AI. So, okay. Exciting. So, I'm Alex. I'm a principal architect at Calibra. We're a data governance company. Um we run our product as a SAS so we use a lot of cloud native uh CNCF technologies Kubernetes article um but uh funny thing is though um also contributor alert things the my first issue was about gRPC so funny enough um but this is not a gpc talk this goes a bit kind into the ecosystem itself because uh enterprises they don't care about technologies in generally they they want to have solutions. So I'm going to pick a few of those solutions out to hopefully kind of sell gRPC or the ecosystem to the company. It's kind of a talk out of regret. Like four years ago, I failed getting us on board. So I had hoped to have this talk four years ago and I hope to have now a better job and kind of having a cohesive cohesive story um for selling gRPC and its ecosystem.

So I'm not going to go deep into gRPC. It's a high performance open source gRPC uh framework. Um I'm going bit deeper into kind of what kind of the special things that are making it a good fit for uh enterprises. So I'm going to even go deep would be surprised into the binary format. gonna explain a few things inside because it's not because you use gRPC you know why it's doing things so not gonna go over all the complete spec but a few highlights that are important for the story um the domain specific languages why this is a good point for your enterprise and the reuse and the integration in other systems so the robust binary format let's start at the So how do we represent an int? I hope most of you know kind of how to represent something binary. Um of course everything let's say everything four four bytes if you put that in a binary format it can be huge. So one of the selling points is compactness. So we store our ins very comp compact. So in a lot of business contracts or something you have small values and you don't have need all those four bits uh four bytes to store them or eight bytes or whatever.

So if you have small numbers like 1 2 3 4 5 you don't need all those things you can get them into one bite. So let's take 150. By the way everything is kind of taken from the documentations. there are links at the bottom. Um and so in the slide deck you can go to the documentation directly
