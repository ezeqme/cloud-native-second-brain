---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Brian Mason", "NetApp"]
sched_url: https://kccncna2021.sched.com/event/lV5C/nats-sync-secure-multi-tenant-cross-cluster-message-routing-brian-mason-netapp
youtube_search_url: https://www.youtube.com/results?search_query=NATS-Sync%3A+Secure%2C+Multi-Tenant%2C+Cross+Cluster+Message+Routing+CNCF+KubeCon+2021
slides: []
status: parsed
---

# NATS-Sync: Secure, Multi-Tenant, Cross Cluster Message Routing - Brian Mason, NetApp

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Brian Mason, NetApp
- Schedule: https://kccncna2021.sched.com/event/lV5C/nats-sync-secure-multi-tenant-cross-cluster-message-routing-brian-mason-netapp
- Busca YouTube: https://www.youtube.com/results?search_query=NATS-Sync%3A+Secure%2C+Multi-Tenant%2C+Cross+Cluster+Message+Routing+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre NATS-Sync: Secure, Multi-Tenant, Cross Cluster Message Routing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5C/nats-sync-secure-multi-tenant-cross-cluster-message-routing-brian-mason-netapp
- YouTube search: https://www.youtube.com/results?search_query=NATS-Sync%3A+Secure%2C+Multi-Tenant%2C+Cross+Cluster+Message+Routing+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EDzuRpKTvJc
- YouTube title: NATS-Sync: Secure, Multi-Tenant, Cross Cluster Message Routing - Brian Mason, NetApp
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/nats-sync-secure-multi-tenant-cross-cluster-message-routing/EDzuRpKTvJc.txt
- Transcript chars: 33652
- Keywords: client, server, message, running, messages, public, cluster, netapp, course, private, encrypted, testing, actually, clients, security, network, desktop, source

### Resumo baseado na transcript

hello i'm brian mason and welcome to the lecture mat sync for kubecon 2021 i want to acknowledge my two co-workers that have been instrumental in helping me create this presentation and of course our major code contributors to the nazi project itself john and raghu thank you both so here's a quick agenda what we'll talk about today obviously we're going to talk about problem we're trying to solve the design we came up with to solve that problem we're going to do a demo of it because everybody

### Excerpt da transcript

hello i'm brian mason and welcome to the lecture mat sync for kubecon 2021 i want to acknowledge my two co-workers that have been instrumental in helping me create this presentation and of course our major code contributors to the nazi project itself john and raghu thank you both so here's a quick agenda what we'll talk about today obviously we're going to talk about problem we're trying to solve the design we came up with to solve that problem we're going to do a demo of it because everybody loves demos i'm going to talk about where we're going in the future with this project and how you can get involved and help if you're so inclined the problem we're trying to solve is basically we love the gnats we love the asynchronous messaging model but we want to extend this paradigm out to being able to send a message from a public cloud or something running up in a cloud environment down to a device or some software running on a private cluster or in on-prem even in somebody's house in the enterprise in a data center that's protected by firewall nats doesn't really solve that problem and that's okay it doesn't need to i think it would be overkill for most situations if it did try to solve that problem so what we're really in need of is basically a secure scalable multi-tenant that's cluster exchange so we also want this to scale down for simplified development so we can keep that simple view of just using that and have all the complexities of that secure scalable multi-tenant environment hidden from us or at least taken care of out of our view in short we want it all we took a quick look around to see if there was a solution already out there and we actually of course found some this is not treading on new territory but they didn't work with nats it's like a message a rabbit mq had a solution but we wanted to say with nats because we really like maths so what we wanted to do is share what we've built and i'll see if you want to join and help us with it okay let's jump into the design the solution that we came up with so your basics environment we like it where you have some random service wants to emit and receive gnats messages to that's cluster that are received by another service out there it's a great model we just want to extend it so this works across clusters and across private networks so a distributed design it's fairly simple you've got a cloud side you know imagine a service running up in aws or azure or google and you've got something in somebody's ho
