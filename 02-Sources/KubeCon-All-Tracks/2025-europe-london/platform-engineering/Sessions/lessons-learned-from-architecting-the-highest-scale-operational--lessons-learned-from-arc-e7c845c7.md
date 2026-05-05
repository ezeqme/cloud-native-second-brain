---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Artur Bergman", "Fastly"]
sched_url: https://kccnceu2025.sched.com/event/1tx9q/lessons-learned-from-architecting-the-highest-scale-operational-systems-in-the-world-artur-bergman-fastly
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Learned+From+Architecting+the+Highest-scale+Operational+Systems+in+the+World+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Lessons Learned From Architecting the Highest-scale Operational Systems in the World - Artur Bergman, Fastly

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Artur Bergman, Fastly
- Schedule: https://kccnceu2025.sched.com/event/1tx9q/lessons-learned-from-architecting-the-highest-scale-operational-systems-in-the-world-artur-bergman-fastly
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Learned+From+Architecting+the+Highest-scale+Operational+Systems+in+the+World+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Lessons Learned From Architecting the Highest-scale Operational Systems in the World.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9q/lessons-learned-from-architecting-the-highest-scale-operational-systems-in-the-world-artur-bergman-fastly
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Learned+From+Architecting+the+Highest-scale+Operational+Systems+in+the+World+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XelZnqurT2s
- YouTube title: Lessons Learned From Architecting the Highest-scale Operational Systems in the World - Artur Bergman
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/lessons-learned-from-architecting-the-highest-scale-operational-system/XelZnqurT2s.txt
- Transcript chars: 22814
- Keywords: platform, actually, little, probably, global, fastly, network, vacuum, promise, outliers, started, second, important, festival, pretty, config, source, around

### Resumo baseado na transcript

Uh I'm uh Arur Bergman uh founder and uh CTO of Pasti and uh it's uh 2025 and uh connectors are still uh not working well. Um I started off in open source of the PL5 core team uh in the previous uh century uh and uh has ever since been involved in a in a lot of different uh open source projects, products and uh events and uh 2011 I started Fastly where we make the internet a better place. Now the network peaks at the 40 million requests per second probably uh and uh total network capacity is about 400 uh a little over 400 terabs per second uh worldwide and uh that's been a a long uh journey of learning uh in how to to operate at scale but also learning that I I wasn't you know if you ask me 14 years ago that becoming a platform that our customers rely on uh is a is a different was a separate uh parallel journey because it's one These are very very good vacuum cleaners and amazingly enough cost about as much as a Dyson. Uh, apparently it turns out that making like a 2 m rail straight and shipping it is a really hard like physical engineering problem.

### Excerpt da transcript

Hi everyone. Uh I'm uh Arur Bergman uh founder and uh CTO of Pasti and uh it's uh 2025 and uh connectors are still uh not working well. Uh so I founded Fastly in 2011. Um it's uh it's a honor to be here. I have been an open source developer for a very very long time. Um I started off in open source of the PL5 core team uh in the previous uh century uh and uh has ever since been involved in a in a lot of different uh open source projects, products and uh events and uh 2011 I started Fastly where we make the internet a better place. All experiences are fast, safe and engaging. And so what is Fastly? We are a uh network around the world with servers that sit between users and the central cloud locations providing uh a whole bunch of services and you're like Arer this is a really boring marketing slide and I'll be like that's true just wait uh what we actually are right is we have about a 100 locations around the world these locations all have physical servers Um I understand today a lot of uh software developers have actually never been in a data center.

Uh which lucky you uh but we still have uh plenty of them. And as a you know someone who's benefited immensely from open source uh and I think to really kind of explain more what we do to this audience we have a program called uh fast forward where we sponsor uh all these wonderful projects with hosting. Uh so essentially whenever you download a software package uh on the internet it probably comes from a faster service. I have some quotes here from three of the different uh projects that use us. Uh and this is something we're we're immensely proud of to be able to offer. Um because we've as a company and as individuals, me, the founding team and everyone else has uh benefited immensely from from the infrastructure. So we serve at peak today about a million requests per second of open source uh software packages uh around the world and uh it's uh so when you when your build systems are fast because they're pulling content really fast like that's us. uh also when you watch lots of live streams uh VOD surf the web buy stuff online that's also us but for this audience and for me I think uh this part of the business is really important uh so we we started uh 2011 and we started with uh five pops five locations couple of servers uh and uh a fairly small network.

Now the network peaks at the 40 million requests per second probably uh and uh total network capacity is about 400 uh a little over 400 terabs per secon
