---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Sheng Yang", "Rancher"]
sched_url: https://kccnceu2021.sched.com/event/igUt/sponsored-session-an-open-source-hci-platform-built-on-kubernetes-sheng-yang-rancher
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Session%3A+An+Open-source+HCI+Platform+Built+on+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Session: An Open-source HCI Platform Built on Kubernetes - Sheng Yang, Rancher

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Sheng Yang, Rancher
- Schedule: https://kccnceu2021.sched.com/event/igUt/sponsored-session-an-open-source-hci-platform-built-on-kubernetes-sheng-yang-rancher
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Session%3A+An+Open-source+HCI+Platform+Built+on+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Session: An Open-source HCI Platform Built on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/igUt/sponsored-session-an-open-source-hci-platform-built-on-kubernetes-sheng-yang-rancher
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Session%3A+An+Open-source+HCI+Platform+Built+on+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ThYN6b0-2mc
- YouTube title: Sponsored Session: An Open-source HCI Platform Built on Kubernetes - Sheng Yang, Rancher
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-session-an-open-source-hci-platform-built-on-kubernetes/ThYN6b0-2mc.txt
- Transcript chars: 14194
- Keywords: harvester, create, cluster, network, backup, storage, software, virtual, already, created, machine, restore, server, applications, multiple, networking, harvest, address

### Resumo baseado na transcript

hi welcome to this session i'm shenyang from rancho labs now a part of sousa today in this session we'll talk about a new project we have started recently it's a hyper-converged infrastructure software but also it's a little bit more than that a few years back the concept of hyper-converged infrastructure was proposed by combining the server and the storage into a distributed infrastructure platform the h2ci software reduce the burden of it means to manage the server and storage separately even with the commodity hardware the software layer

### Excerpt da transcript

hi welcome to this session i'm shenyang from rancho labs now a part of sousa today in this session we'll talk about a new project we have started recently it's a hyper-converged infrastructure software but also it's a little bit more than that a few years back the concept of hyper-converged infrastructure was proposed by combining the server and the storage into a distributed infrastructure platform the h2ci software reduce the burden of it means to manage the server and storage separately even with the commodity hardware the software layer is intelligent enough to figure out where to put the data to keep everything highly available no special storage or server will be needed it sounds like a pad with a cattle by switching to hci you no longer need to treat your storage as a patch and not worry about if you are operating the right or not and also just in case you know patch with cattle is also where the name of the rancher come from i mean the ranch part of course so in the data center hci software is driving but from sofia operator's perspective there's still more left to be designed you cannot run your application directly and on the hci since the software is more likely to be designed on top of the vms it's because the software hasn't been programmed to know how to spin up vms or connect to the storage provided by different hci solutions and that is because of each these sgi solutions speak a different api language which is a part of their proprietary api the result is ipa means still need to operate our software differently based on what hci or virtualization solution they have chosen terraform and other technology are created to help but still the idea means need to learn a lot about how to upgrade softwares and then writing a lot of customized script to maintain it properly that is not easy work fast forward to now we see kubernetes taking the word by storm we no longer need to treat applications paths things container and kubernetes become the de facto application api as long as the application works on kubernetes they can be treated as cattle and no one needs to worry about what hardware is running on top of or what storage is using or how to spin up multiple vm to run it since all of this has been taken care of by the kubernetes we want to introduce the concept hci 2.0 by 2.0 we mean we're not only going to integrate servers and storage but also going to integrate applications on top of it through the kubernetes api we will replace the proprietary
