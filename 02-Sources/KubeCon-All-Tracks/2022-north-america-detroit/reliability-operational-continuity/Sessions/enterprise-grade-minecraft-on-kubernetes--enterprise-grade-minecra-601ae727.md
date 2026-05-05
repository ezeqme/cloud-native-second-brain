---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Casey West", "Google"]
sched_url: https://kccncna2022.sched.com/event/182JH/enterprise-grade-minecraft-on-kubernetes-casey-west-google
youtube_search_url: https://www.youtube.com/results?search_query=Enterprise+Grade+Minecraft+On+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Enterprise Grade Minecraft On Kubernetes - Casey West, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Casey West, Google
- Schedule: https://kccncna2022.sched.com/event/182JH/enterprise-grade-minecraft-on-kubernetes-casey-west-google
- Busca YouTube: https://www.youtube.com/results?search_query=Enterprise+Grade+Minecraft+On+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Enterprise Grade Minecraft On Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182JH/enterprise-grade-minecraft-on-kubernetes-casey-west-google
- YouTube search: https://www.youtube.com/results?search_query=Enterprise+Grade+Minecraft+On+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ErvueBYt_HM
- YouTube title: Enterprise Grade Minecraft On Kubernetes - Casey West, Google
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/enterprise-grade-minecraft-on-kubernetes/ErvueBYt_HM.txt
- Transcript chars: 30543
- Keywords: minecraft, server, pretty, storage, running, little, question, software, actually, instance, cluster, configuration, client, manage, course, address, application, container

### Resumo baseado na transcript

all right what's up nerds yeah so I'd like to know uh did you come here because you play Minecraft raise your hand and then and then keep your hand up please alternatively did you come here because you have important customers who play Minecraft yeah I'm both um I have some kids who are uh massively obsessed with Minecraft and then I also like to play it and for me it's a resource management game I collect all the resources and my children consume them um on the game

### Excerpt da transcript

all right what's up nerds yeah so I'd like to know uh did you come here because you play Minecraft raise your hand and then and then keep your hand up please alternatively did you come here because you have important customers who play Minecraft yeah I'm both um I have some kids who are uh massively obsessed with Minecraft and then I also like to play it and for me it's a resource management game I collect all the resources and my children consume them um on the game and then I also use it as a three-dimensional programming model so I get to automate things and that's super dope so if you do uh Minecraft that's great how many of you came here because you have to manage commercial off-the-shelf software that's provided you by others with strange constraints you don't always know right cool good everyone's going to be happy there's going to be a lot more of the kubernetes than the Minecraft I hope that's all right okay this is my first talk in in an actual conference in more than two years for undisclosed reasons but I'm pretty excited you can reach out to me I'm at Casey West everywhere I recently bought the Instagram handle from the other person um you know and if you do go and follow me uh you're probably gonna see like hiking and rock climbing and stuff more than computery nerd stuff but if you're into that that's where I'm at let's start with the Minecraft architecture diagram so those of you who run a Minecraft server know that this is the architecture diagram you've got a client on the left there that's your computer and if you're running a server that's separate from that computer then you run server.jar and you connect to it right um obviously the title of this talk is Enterprise grade Minecraft on kubernetes and so I got to to thinking you know is it possible to run this server on kubernetes in a way that's resilient and we can also do things like you know data backup so that if we if we need to recover the world from a previous snapshot we could do something like that and it turns out you can so uh I work for a cloud company so my my kubernetes live in in one place yours can live wherever they want it doesn't matter this isn't a a specific talk in any way but this is roughly what the architecture is going to look like you know you so you've got your client there on the left uh there's going to be a load balancer just in front of an instance so that's fun uh an instance of This Server if you're running commercial grade software that's provided you
