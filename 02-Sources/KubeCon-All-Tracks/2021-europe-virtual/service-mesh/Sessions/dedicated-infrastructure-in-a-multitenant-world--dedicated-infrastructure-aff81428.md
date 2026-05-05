---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Carlos Sanchez", "Adobe"]
sched_url: https://kccnceu2021.sched.com/event/iE3m/dedicated-infrastructure-in-a-multitenant-world-carlos-sanchez-adobe
youtube_search_url: https://www.youtube.com/results?search_query=Dedicated+Infrastructure+in+a+Multitenant+World+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Dedicated Infrastructure in a Multitenant World - Carlos Sanchez, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: Virtual / Virtual
- Speakers: Carlos Sanchez, Adobe
- Schedule: https://kccnceu2021.sched.com/event/iE3m/dedicated-infrastructure-in-a-multitenant-world-carlos-sanchez-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=Dedicated+Infrastructure+in+a+Multitenant+World+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Dedicated Infrastructure in a Multitenant World.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3m/dedicated-infrastructure-in-a-multitenant-world-carlos-sanchez-adobe
- YouTube search: https://www.youtube.com/results?search_query=Dedicated+Infrastructure+in+a+Multitenant+World+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Kvog7aZ3esY
- YouTube title: Dedicated Infrastructure in a Multitenant World - Carlos Sanchez, Adobe
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/dedicated-infrastructure-in-a-multitenant-world/Kvog7aZ3esY.txt
- Transcript chars: 19700
- Keywords: traffic, envoy, virtual, network, dedicated, private, running, tenant, cluster, connect, balancer, connection, sidecar, machines, manager, customer, configuration, coming

### Resumo baseado na transcript

hello my name is carlos sanchez and i'm here to talk to you about dedicated infrastructure in a multi-tenant world i work at adobe and i'm going to talk to you about some of the things we are building there in one of the services i'm a cloud engineer at the adobe experience manager cloud service and i'm a long time open source contributor i started the jenkins kubernetes plugin that allow you to run jenkins agents on kubernetes but i've been a long time contributor at other projects like

### Excerpt da transcript

hello my name is carlos sanchez and i'm here to talk to you about dedicated infrastructure in a multi-tenant world i work at adobe and i'm going to talk to you about some of the things we are building there in one of the services i'm a cloud engineer at the adobe experience manager cloud service and i'm a long time open source contributor i started the jenkins kubernetes plugin that allow you to run jenkins agents on kubernetes but i've been a long time contributor at other projects like apache maven puppet and a few other things just so you know i'm gonna do a brief introduction on what adopt experience manager is this is a content management system um that does digital asset management digital enrollment forms and it's used by many fortune 100 companies this is the product that i work on at adobe and my team it's um from a technical point of view it's an existing distributed java osgi application that uses a lot of open source components from the apache software foundation it also has a huge market for extension developers that write modules that run in process on adobe experience manager and this is important uh you'll see later we are running a adobe experience manager cloud on kubernetes and this has been launched over a year ago and this is all running on asia we have more than 14 clusters right now and growing multiple regions united states europe australia japan and wikipedi more and also something to note is that adobe has a dedicated team managing clustering clusters for multiple products so we are one of the customers of this other theme so we get the clusters and this uh defines what we can do in the clusters right so we don't have full access to to the kubernetes clusters important thing customers can run their own code we have limited cluster permissions for security and another requirement is that traffic leaving the the classes must be encrypted for for compliance so again it's going to be uh interesting later on as as i explained what we built we use namespaces to provide scopes so the new spaces increments give us network isolation quartus permissions and if you want to know more details on what our kubernetes setup you can watch my kubecon 2020 talk and you'll find there that i went over all the things that we have built on top of kubernetes to to support the am and this talk is gonna just focus on the on what we are doing with with envoy the requirement we got from customers is that they wanted to have a dedicated infrastructure a dedic
