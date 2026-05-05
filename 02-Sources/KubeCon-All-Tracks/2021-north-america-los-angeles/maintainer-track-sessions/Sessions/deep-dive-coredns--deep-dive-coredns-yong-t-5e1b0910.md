---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Yong Tang", "Ivanti Inc.", "Miek Gieben", "Independent", "John Belamaric", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV75/deep-dive-coredns-yong-tang-ivanti-inc-miek-gieben-independent-john-belamaric-google
youtube_search_url: https://www.youtube.com/results?search_query=Deep+Dive+CoreDNS+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Deep Dive CoreDNS - Yong Tang, Ivanti Inc.; Miek Gieben, Independent; John Belamaric, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Yong Tang, Ivanti Inc., Miek Gieben, Independent, John Belamaric, Google
- Schedule: https://kccncna2021.sched.com/event/lV75/deep-dive-coredns-yong-tang-ivanti-inc-miek-gieben-independent-john-belamaric-google
- Busca YouTube: https://www.youtube.com/results?search_query=Deep+Dive+CoreDNS+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Deep Dive CoreDNS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV75/deep-dive-coredns-yong-tang-ivanti-inc-miek-gieben-independent-john-belamaric-google
- YouTube search: https://www.youtube.com/results?search_query=Deep+Dive+CoreDNS+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Yj0cj2oymqY
- YouTube title: Deep Dive: CoreDNS - Yong Tang, Infoblox
- Match score: 0.722
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/deep-dive-coredns/Yj0cj2oymqY.txt
- Transcript chars: 21536
- Keywords: actually, plug-in, server, coding, discovery, plugin, always, simple, another, quoting, maintenance, public, organization, according, probably, essentially, record, coordinates

### Resumo baseado na transcript

it looks like if we can just get started by the way doing the talk if you have any questions you can always raise hand anytime you like okay let's let's get started so good afternoon thanks everyone for coming to this talk again my name is Yong Chun and I'm in Tina of coordinates project in today's talk my focus is deep dive into coordinates and also showcased how to just implement our audience plugins in like five to ten minutes here's going to be the agenda of today's

### Excerpt da transcript

it looks like if we can just get started by the way doing the talk if you have any questions you can always raise hand anytime you like okay let's let's get started so good afternoon thanks everyone for coming to this talk again my name is Yong Chun and I'm in Tina of coordinates project in today's talk my focus is deep dive into coordinates and also showcased how to just implement our audience plugins in like five to ten minutes here's going to be the agenda of today's talk first I'm going to briefly introduce coordinates and its background and its demand for the past couple years then I'm gonna discuss posterity discovery which is the focus of quoting as also the 4,000 plugins finally I'm gonna show a plugin demo which is really a source based survey discovery this is a simple plugin but I'll just show kids how you can implement that in like a several minutes so first coordinate coding us is a flexible DNS server written in cow it has a focus on survey discovery coding as a plug-in base architecture which means it could be easily extended with new functional taste by customized plugins coding has supported DNS es / tos and the DNS over G RPC the one thing I want to point out is post eNOS and eNOS over TOS us dear standard but Deena has over G RPC is only a customer customer eyes implementation by coordinates itself it's another standard by DNS the Kadena's project started and led by me Cheban a couple of years ago we we study the project in 2016 in 2017 we entered into seeing stuff and now we are looking for graduation one interesting about coding assays that cody has initially is just a fork of caddy HTP server a caddy is very interesting HTP server written go it's very popular in some say in : : community it has a similar plugin base architecture so we mix that is Cody as he actually just a fox caddy ATP Silva and make some change and somehow make it a walk with the ass so that's actually shows how you could reuse the code base in Gollum actually doing my implementation at the end of the talk about demo plug-in you will notice that you still see some referencing caddy and that's by purpose good like I said according a study in 2016 but in 2017 we are they reach the inception level in since EF we I believe coding acid is a seventh project and into CN CF so that's probably the one of the early is a project in since yeah we reached the level of incubating in 2018 and we actually planning on graduation for now so hopefully we can graduate the versal well t
