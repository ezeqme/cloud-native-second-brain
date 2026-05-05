---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Lucas Käldström", "Upbound", "Micah Hausler", "AWS"]
sched_url: https://kccncna2025.sched.com/event/27FdC/tools-and-strategies-for-making-the-most-of-kubernetes-access-control-lucas-kaldstrom-upbound-micah-hausler-aws
youtube_search_url: https://www.youtube.com/results?search_query=Tools+and+Strategies+for+Making+the+Most+of+Kubernetes+Access+Control+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Tools and Strategies for Making the Most of Kubernetes Access Control - Lucas Käldström, Upbound & Micah Hausler, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Lucas Käldström, Upbound, Micah Hausler, AWS
- Schedule: https://kccncna2025.sched.com/event/27FdC/tools-and-strategies-for-making-the-most-of-kubernetes-access-control-lucas-kaldstrom-upbound-micah-hausler-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Tools+and+Strategies+for+Making+the+Most+of+Kubernetes+Access+Control+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Tools and Strategies for Making the Most of Kubernetes Access Control.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FdC/tools-and-strategies-for-making-the-most-of-kubernetes-access-control-lucas-kaldstrom-upbound-micah-hausler-aws
- YouTube search: https://www.youtube.com/results?search_query=Tools+and+Strategies+for+Making+the+Most+of+Kubernetes+Access+Control+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JBM0PRyDaPs
- YouTube title: Tools and Strategies for Making the Most of Kubernetes Access Con... Lucas Käldström & Micah Hausler
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tools-and-strategies-for-making-the-most-of-kubernetes-access-control/JBM0PRyDaPs.txt
- Transcript chars: 26932
- Keywords: policy, request, actually, arbback, access, authorization, create, admission, control, write, secret, another, server, policies, bindings, cluster, reference, object

### Resumo baseado na transcript

Hi and welcome everyone to this session about Kubernetes access control. Um today yeah that was um yeah hopefully you're going to have a good time following some of the recent developments within Kubernetes access control or some new methodologies you can use. Uh on top of all of this you need to make sure that it's actually correct whatever you're u you're designing and implementing. So uh when you make a Kubernetes request whether you're using cubecuddle or uh kind of any any other client of Kubernetes uh there's a whole uh path that goes through the API server. And so, today in Kubernetes, most clusters are going to be using uh arbback. And then Kubernetes also in a couple releases ago added cell the common expression language uh engine so that you can do you can write cell functions and with validating mission policy in the API server and have those executed in the API server.

### Excerpt da transcript

Hi and welcome everyone to this session about Kubernetes access control. Um today yeah that was um yeah hopefully you're going to have a good time following some of the recent developments within Kubernetes access control or some new methodologies you can use. Um I'm Lucas at working at Upbound as a staff software engineer and um previously I've been contributing to Kubernetes forum for quite a while uh doing different things. And I'm uh Mike Hler. I'm a principal engineer at AWS. Uh I work on Kubernetes security and container security. I also volunteer upstream. I'm on the Kubernetes uh security response committee as well as one of the co-chairs of SIGO off. >> Cool. So let's uh let's kick off kick us off. Uh we're going to start by an introduction to Kubernetes access control. Then look at the most widely deployed uh method today which is cube arbback role based access control um and a couple of tools that could be useful for managing that. And then we're going to look at in second half a new kubernetes enhancement proposal or cap for short which uh or a couple actually u which kind of provide more finer grained alternatives to the existing stuff.

So in an authorization system you have kind of conflicting requirements. You want it to be expressive but on the other hand it has to be fast. It has to be safe to execute and also ideally analyzable so you can kind of know what's going on. And um these are well at odds with each other. So designing this is a delicate balance. Uh on top of all of this you need to make sure that it's actually correct whatever you're u you're designing and implementing. So um on a kind of high level overview um arbback is fast, safe and analyzable um not but not as expressive. Then we have uh another method that we'll cover in a bit which is called validating admission policy which is way more um expressive but um not as easy to like not as fast and safe and so on. Um, and then if you need even more expressivity, you can do web hooks. So you can just um tell a cube API server to to just like ask this thing for whether it's deni allowed or denied. Uh, but then we we don't we can't analyze it. We can't know what this web hook is doing.

Um, and it's also kind of well can be prone to failures and and stuff like that during runtime. Um so today we're going to look at so is there something in the middle that we could do where we kind of preserve some of the the advantages um and and balance balance this this kind of these trade-offs.
