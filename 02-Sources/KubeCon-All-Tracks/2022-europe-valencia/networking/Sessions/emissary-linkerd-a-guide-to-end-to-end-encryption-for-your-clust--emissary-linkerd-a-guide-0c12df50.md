---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Flynn", "Ambassador Labs", "Jason Morgan", "Buoyant"]
sched_url: https://kccnceu2022.sched.com/event/11LW4/emissary-+-linkerd-a-guide-to-end-to-end-encryption-for-your-cluster-flynn-ambassador-labs-jason-morgan-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Emissary+%2B+Linkerd%3A+A+Guide+to+End-to-end+Encryption+for+your+Cluster+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Emissary + Linkerd: A Guide to End-to-end Encryption for your Cluster - Flynn, Ambassador Labs & Jason Morgan, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Flynn, Ambassador Labs, Jason Morgan, Buoyant
- Schedule: https://kccnceu2022.sched.com/event/11LW4/emissary-+-linkerd-a-guide-to-end-to-end-encryption-for-your-cluster-flynn-ambassador-labs-jason-morgan-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary+%2B+Linkerd%3A+A+Guide+to+End-to-end+Encryption+for+your+Cluster+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Emissary + Linkerd: A Guide to End-to-end Encryption for your Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/11LW4/emissary-+-linkerd-a-guide-to-end-to-end-encryption-for-your-cluster-flynn-ambassador-labs-jason-morgan-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Emissary+%2B+Linkerd%3A+A+Guide+to+End-to-end+Encryption+for+your+Cluster+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3NCAUtW0sck
- YouTube title: Emissary + Linkerd: A Guide to End-to-end Encryption for your Cluster - Flynn & Jason Morgan
- Match score: 0.954
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/emissary-linkerd-a-guide-to-end-to-end-encryption-for-your-cluster/3NCAUtW0sck.txt
- Transcript chars: 33397
- Keywords: emissary, linker, actually, running, ingress, cluster, install, mesh, lingerie, certificate, traffic, question, little, browser, installed, application, couple, talking

### Resumo baseado na transcript

yeah hey folks um give you all a second to sit down uh but i want to start off with want to start off just by saying thank you so much to all of you for coming to our talk um so today you're going to hear us tell you how to do end-to-end encryption from your browser to your pod with a couple of cncf projects emissary ingress and the linker d service mesh so appreciate your time thanks i'm flynn from ambassador labs i've been working with the

### Excerpt da transcript

yeah hey folks um give you all a second to sit down uh but i want to start off with want to start off just by saying thank you so much to all of you for coming to our talk um so today you're going to hear us tell you how to do end-to-end encryption from your browser to your pod with a couple of cncf projects emissary ingress and the linker d service mesh so appreciate your time thanks i'm flynn from ambassador labs i've been working with the emissary english project since its humble beginnings in 2017. you can send me an email at planetdatawire.io or you can find me on github and you can find me probably most easily on our open source slack as flynn and we'll have links and things like that over to you thank you much my co-conspirator jason morgan uh so hey i'm jason morgan i hope this isn't as loud as it feels from right here but i am a technical evangelist for buoyant so that means it's my job to talk to you about linker d and try and convince you that it is the best service match on the market and you want to use it if you have comments you want to make about what i just said feel free to email me jason at point.io i'm looking forward to hearing from you you can also if for any reason you want to find me on github you can at jason morgan and you can find me on the cncf and linkerity slacks as at jason so we're going to be talking today about a couple of things couple of different problems you're going to hear us talk a lot about north south traffic and east-west traffic with north-south being traffic from outside your cluster coming in east-west being service-to-service within your cluster as jason mentioned we're going to be talking about how to set this up so that all of that traffic is encrypted all the way from your browser all the way back through to the services we are going to be using emissary ingress to do the tls termination and that means we're also going to be using emissary ingress to handle the certificate that secures your communication between the cluster and the browser and then we'll get onto using linker d within the cluster but important to note that you cannot do tls in any meaningful way without certificates so we're going to come back and talk about that a couple of points here so if you're not familiar with emissary ingress it is an open source cloud native self-service developer centric api gateway so if you have a cluster where's my laser pointer there we go if you have a cluster over there with a bunch of services in it and yo
