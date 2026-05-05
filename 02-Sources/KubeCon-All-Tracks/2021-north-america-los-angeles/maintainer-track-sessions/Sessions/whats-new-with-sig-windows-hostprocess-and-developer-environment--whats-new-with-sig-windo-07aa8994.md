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
speakers: ["Brandon Smith", "Danny Canter", "Microsoft", "Jay Vyas", "VMware", "Friedrich Wilken", "SAP Hybrid"]
sched_url: https://kccncna2021.sched.com/event/lV6S/whats-new-with-sig-windows-hostprocess-and-developer-environments-brandon-smith-danny-canter-microsoft-jay-vyas-vmware-friedrich-wilken-sap-hybrid
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+With+SIG-Windows%3A+HostProcess+and+Developer+environments+CNCF+KubeCon+2021
slides: []
status: parsed
---

# What's New With SIG-Windows: HostProcess and Developer environments - Brandon Smith & Danny Canter, Microsoft; Jay Vyas, VMware; Friedrich Wilken, SAP Hybrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Brandon Smith, Danny Canter, Microsoft, Jay Vyas, VMware, Friedrich Wilken, SAP Hybrid
- Schedule: https://kccncna2021.sched.com/event/lV6S/whats-new-with-sig-windows-hostprocess-and-developer-environments-brandon-smith-danny-canter-microsoft-jay-vyas-vmware-friedrich-wilken-sap-hybrid
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+With+SIG-Windows%3A+HostProcess+and+Developer+environments+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre What's New With SIG-Windows: HostProcess and Developer environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6S/whats-new-with-sig-windows-hostprocess-and-developer-environments-brandon-smith-danny-canter-microsoft-jay-vyas-vmware-friedrich-wilken-sap-hybrid
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+With+SIG-Windows%3A+HostProcess+and+Developer+environments+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fSmDmwKwFfQ
- YouTube title: What's New With SIG-Windows: HostProcess and Developer... B. Smith, D. Canter, J. Vyas, F. Wilken
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/whats-new-with-sig-windows-hostprocess-and-developer-environments/fSmDmwKwFfQ.txt
- Transcript chars: 22806
- Keywords: windows, container, process, containers, server, calico, working, running, available, access, basically, cluster, getting, everybody, scenarios, install, awesome, actually

### Resumo baseado na transcript

hello everybody and welcome to cubecon north america 2021 this is the maintainer series talk for sig windows and let's get started first i'm going to introduce all of the speakers i'll start with myself my name is mark rossetti i am a software engineer at microsoft i am currently the co-chair for sig windows i work in azure and there are is my github and slack handles next is danny cantor hello hello my name is danny cantor i am also a software engineer at microsoft um i'm a logs this is going to address some feedback we've had that it's kind of hard to debug issues with windows systems services on kubernetes uh all right i'm going to hand it over to brendan to talk about what's new for windows server 2022. this you can deploy a consistent network policy with calico across hybrid kubernetes clusters um so alongside this we we have included many features available in in previous sac releases into this this ws 2022 um so all of those features that were available in

### Excerpt da transcript

hello everybody and welcome to cubecon north america 2021 this is the maintainer series talk for sig windows and let's get started first i'm going to introduce all of the speakers i'll start with myself my name is mark rossetti i am a software engineer at microsoft i am currently the co-chair for sig windows i work in azure and there are is my github and slack handles next is danny cantor hello hello my name is danny cantor i am also a software engineer at microsoft um i'm a member of the container platform team within hyper-v my github handle is decanter a little pun on my name and you can find me at danny cantor on the cage slide hey i'm jay jay unit 100 and i hang out with mark and james and friedrich too sick windows lead and the tech lead for kubernetes on windows at vmware and yeah someday i think the coop proxy for windows will be cleaned up and moved somewhere fancy we're not sure yet hopefully the kaping project and juno 100 on twitter hey everyone my name is brandon i'm a pm on the microsoft container platform team um i pretty much deal with all things containers and windows so i think ranging from windows sandbox to windows server containers and and onwards hi my name is christopher i'm a software engineer at sap hybris currently working on the akuma platform and you can find me on github or on slack all right thank you everybody um here's a brief overview of the agenda we're going to be talking about what's new in sig windows i'm going to give some updates about windows server 2022 and then talk about the new windows developer environment that we've been working on to make it easier to spin up windows clusters and then talk about host process containers so here's a kind of brief overview of everything that's happened since the last kubecon talk the first is csi plugin support for windows is now generally available there's a link to the enhancement for anybody who's interested uh this means that all csi plugins now are compatible with windows nodes next is um host process containers or as most people refer to them the equivalent of privileged containers on linux uh hit alpha in 122.

this is a huge milestone for windows we can and enables us to support many other scenarios uh next is the for 123 we're pursuing a number of different caps the first one is a way to identify windows pods at api admission time this will make it so that policies can choose to enforce specific uh settings on pod specs for windows versus linux pods and most importantly
