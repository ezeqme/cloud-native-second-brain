---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Networking"
themes: ["Networking"]
speakers: ["Jussi Nummelin", "Mirantis", "Rastislav Szabo", "Kubermatic"]
sched_url: https://kccncna2022.sched.com/event/182ID/remote-control-planes-with-konnectivity-what-why-and-how-jussi-nummelin-mirantis-rastislav-szabo-kubermatic
youtube_search_url: https://www.youtube.com/results?search_query=Remote+Control+Planes+With+Konnectivity%3B+What%2C+Why+And+How%3F+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Remote Control Planes With Konnectivity; What, Why And How? - Jussi Nummelin, Mirantis & Rastislav Szabo, Kubermatic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Jussi Nummelin, Mirantis, Rastislav Szabo, Kubermatic
- Schedule: https://kccncna2022.sched.com/event/182ID/remote-control-planes-with-konnectivity-what-why-and-how-jussi-nummelin-mirantis-rastislav-szabo-kubermatic
- Busca YouTube: https://www.youtube.com/results?search_query=Remote+Control+Planes+With+Konnectivity%3B+What%2C+Why+And+How%3F+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Remote Control Planes With Konnectivity; What, Why And How?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182ID/remote-control-planes-with-konnectivity-what-why-and-how-jussi-nummelin-mirantis-rastislav-szabo-kubermatic
- YouTube search: https://www.youtube.com/results?search_query=Remote+Control+Planes+With+Konnectivity%3B+What%2C+Why+And+How%3F+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0yltsB3Cbr4
- YouTube title: Remote Control Planes With Konnectivity; What, Why And How? - Jussi Nummelin & Rastislav Szabo
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/remote-control-planes-with-konnectivity-what-why-and-how/0yltsB3Cbr4.txt
- Transcript chars: 28363
- Keywords: cluster, actually, control, connectivity, server, course, components, clusters, worker, working, running, master, already, connection, network, agents, remote, component

### Resumo baseado na transcript

welcome everyone for our session we're going to talk about remote control planes and and how to build those or construct them with with a component called connectivity and of course we'll start with uh what it is and why would you do something like this and and and then we'll focus a bit also on the the sort of building blocks that that how to do how to do things so I'm yusi from manantis working mostly with the our kzer Cube drro hi my name is m kazm

### Excerpt da transcript

welcome everyone for our session we're going to talk about remote control planes and and how to build those or construct them with with a component called connectivity and of course we'll start with uh what it is and why would you do something like this and and and then we'll focus a bit also on the the sort of building blocks that that how to do how to do things so I'm yusi from manantis working mostly with the our kzer Cube drro hi my name is m kazm and I am uh working by cuber medic and uh mainly working on cluster provisioning cluster networking and life cycle glad to be here all right so as said the the kind of outline for our session is is focusing first on what we actually mean when we talk about a concept called remote remote control plan uh we'll have a look at couple of uh different use cases where would you actually want to do something like this and then what are the building plugs and and Concepts in in in kubernetes and and in other components that you can actually actually kind of pull this off in a way and of course we'll we'll have a bit of bit of kind of a history lesson too that that what what has been there and what what what is there now in kubernetes and a couple of real world integration examples on on on this uh of course as always we're standing on shoulders of giants here so uh we're as as two we're not really the sort of inventors of of of this stuff uh like more like happy users of of what what the community is is building uh why we wanted to have this sort of a talk is is uh the main thing is that that there's very very little documentation and knowledge on this topic so we want to raise the awareness that that okay you can actually do something like this whether it makes sense for you your use case or not that's that's a different discussion so basically kudos to the all the original inventors and and people that have been working on the different caps in the in the past and to to make this actually happen all right okay so um as what you say already spoke about we're we're not going to dive into the whole um technical backgrounds of how we achieve things so usually a catus cluster just looks like this you have have a master control playe component it's a node and you have other worker nodes as well where you have you know your API server or the whole control plane components deployed uh on the same node and then your worker noes just keep talking with that guy now this was working still working it has you know as what we say
