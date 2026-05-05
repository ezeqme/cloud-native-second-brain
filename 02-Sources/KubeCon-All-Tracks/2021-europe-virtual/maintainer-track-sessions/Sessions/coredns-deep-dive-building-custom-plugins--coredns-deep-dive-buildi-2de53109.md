---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Yong Tang", "Ivanti"]
sched_url: https://kccnceu2021.sched.com/event/iE90/coredns-deep-dive-building-custom-plugins-yong-tang-ivanti
youtube_search_url: https://www.youtube.com/results?search_query=CoreDNS+Deep+Dive%3A+Building+Custom+Plugins+CNCF+KubeCon+2021
slides: []
status: parsed
---

# CoreDNS Deep Dive: Building Custom Plugins - Yong Tang, Ivanti

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Yong Tang, Ivanti
- Schedule: https://kccnceu2021.sched.com/event/iE90/coredns-deep-dive-building-custom-plugins-yong-tang-ivanti
- Busca YouTube: https://www.youtube.com/results?search_query=CoreDNS+Deep+Dive%3A+Building+Custom+Plugins+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre CoreDNS Deep Dive: Building Custom Plugins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE90/coredns-deep-dive-building-custom-plugins-yong-tang-ivanti
- YouTube search: https://www.youtube.com/results?search_query=CoreDNS+Deep+Dive%3A+Building+Custom+Plugins+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZffZzGbjy1k
- YouTube title: CoreDNS Deep Dive: Building Custom Plugins - Yong Tang, Ivanti
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/coredns-deep-dive-building-custom-plugins/ZffZzGbjy1k.txt
- Transcript chars: 17742
- Keywords: plugin, coding, server, coordinates, request, function, google, default, response, maintainer, github, actually, plugins, session, several, important, machine, learning

### Resumo baseado na transcript

good afternoon welcome to this session my name is yang tang i'm a maintainer of coding s project in today's session i'm going to do a deep dive on coding as discuss about building customer plugins with coding as in golang this is my profile on the github handle by the way if you have any questions you can always reach out to me on github i should be available most of time every day this is the agenda for today's session i'm going to spend several minutes to introduce local query response additional coding as community update as of now we have 249 contributors we certainly want to see this number to grow continuously so first of all big thanks to anyone who contributes to coding as and we will come any additional contributions have 30 public adopters those are the enterprise or institutions that are willing to share name with us and make their name available across the board since coding is now is a default dns server for kubernetes so the the user coordinates is much larger if it's internal we'll just reply a ip address of 1.1.1.1 on the other hand if a dns query is from external even though they are occurring the same names they're going to return differently in this demo plugin we are going to return 8.8.8.8. so this is the basic setup we are trying to achieve in order to write the demo plugin we will need to set up several functions there are three functions that we...

### Excerpt da transcript

good afternoon welcome to this session my name is yang tang i'm a maintainer of coding s project in today's session i'm going to do a deep dive on coding as discuss about building customer plugins with coding as in golang this is my profile on the github handle by the way if you have any questions you can always reach out to me on github i should be available most of time every day this is the agenda for today's session i'm going to spend several minutes to introduce codiness discuss about its history and some of the interesting stories behind it i will post some status update of coding as for the past year in pottery 20 discuss about the versions that has been released as well as the new features that have been added i will also discuss about the google summer code program with coordinates the reason google summer code is important to call dns is because quite a few features including us has been added through the contributions from google somehow code students things like dns tab and seo are plugins that has been part of the default for dns in last year the student of google somehow code successfully combined the core dns machine learning and the security into a server application it's fun to take a look finally i will work through a demo plugin in gola this is a source-based service discovery it allows you to set up a coding as server to reply dns queries with different response based on the society of the query finally it's a q a session if you have any questions you can read that out i'll try my best to answer as many of you know codiness is a flexible dna server reading go it was developed and started in 2016.

at the beginning it was really a fork of a caddy xct server over the years the relationship between coding and center caddy has been gradually decoupled although even as of now you can still find some more traces of paddy reference including as codebase unlike some other dns servers coding s has a focus on service discovery it is a plugin based which means it can be easily extended for new functionalities if you have a new feature you want to add and it's not available in default plugins then you can write on your own if you know how to write in go most importantly coding s at the moment is a default dns server in kubernetes which means if you are using kubernetes you are probably already using coding as koreans support a wide range of vm servers it have different protocol support from dns dns over tos and dns over grpc by the way dso or grpc
