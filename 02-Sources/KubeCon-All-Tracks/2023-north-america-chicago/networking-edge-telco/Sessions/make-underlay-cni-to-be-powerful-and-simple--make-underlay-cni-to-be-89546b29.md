---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Networking + Edge + Telco"
themes: ["AI ML", "Networking"]
speakers: ["Lan Weizhou", "Qiuping Dai", "Daocloud"]
sched_url: https://kccncna2023.sched.com/event/1R2sl/make-underlay-cni-to-be-powerful-and-simple-lan-weizhou-qiuping-dai-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=Make+Underlay+CNI+to+Be+Powerful+and+Simple+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Make Underlay CNI to Be Powerful and Simple - Lan Weizhou & Qiuping Dai, Daocloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Lan Weizhou, Qiuping Dai, Daocloud
- Schedule: https://kccncna2023.sched.com/event/1R2sl/make-underlay-cni-to-be-powerful-and-simple-lan-weizhou-qiuping-dai-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=Make+Underlay+CNI+to+Be+Powerful+and+Simple+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Make Underlay CNI to Be Powerful and Simple.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sl/make-underlay-cni-to-be-powerful-and-simple-lan-weizhou-qiuping-dai-daocloud
- YouTube search: https://www.youtube.com/results?search_query=Make+Underlay+CNI+to+Be+Powerful+and+Simple+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KqfzkOGObCQ
- YouTube title: Make Underlay CNI to Be Powerful and Simple - Lan Weizhou & Qiuping Dai, Daocloud
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/make-underlay-cni-to-be-powerful-and-simple/KqfzkOGObCQ.txt
- Transcript chars: 18611
- Keywords: network, application, traffic, interface, create, scenario, performance, spider, figure, cluster, address, another, course, underlay, second, communication, affinity, multiple

### Resumo baseado na transcript

and uh today um M wiel and I will cooperate to finish this session okay let me take a bit time to introduce ourselves um weo is a senior uh architecture leader in Dark Cloud and he is responsible for all the network project in dad and I am the product manager in dad and I'm responsible for uh container platform in darkcloud okay then let's we uh let's start firstly let's take a look at the cnis uh currently available and in cetes we can categorize the uh this

### Excerpt da transcript

and uh today um M wiel and I will cooperate to finish this session okay let me take a bit time to introduce ourselves um weo is a senior uh architecture leader in Dark Cloud and he is responsible for all the network project in dad and I am the product manager in dad and I'm responsible for uh container platform in darkcloud okay then let's we uh let's start firstly let's take a look at the cnis uh currently available and in cetes we can categorize the uh this cnis into two TPS underlay cni and overlay c um over that's over are more popular than underl uh for example the uh the wiely used Carle and celum with the ebpf uh acceleration capabilities compared to the underlaying um overl has a lower dependency to underlaying uh to underlay physical Network and it's easy for use however in some scenario um under cannot be replaced so next uh let's move to the scenario the first scenario is about the TR traditional application which is migrated from the host to the kubernetes um there are uh oh sorry um there are some um typical uh characteristics for the network of the traditional application uh let's look at the uh righted side we can say um the multic cost and the group cost uh is required and the ARP is necessary and the second part um some of their application is exposed so it's by the IP address of VM or physcal ser and uh it is isolated by the f f uh F policy with no net through the physical Network and last the network of this Parts uh application is isolated um by villain sub nness uh for business uh uh for business traffic isolation for example um application has two interfaces uh one is for TCP uh traffic and another is for the uh UDP traffic and sometimes the lock traffic is very inh humorous so it is uh should be it should be um isolated to avoid impacting uh the business traffic and um when this part of application uh is moved uh is migrated to the uh kubernetes some company May uh uh want to save the cost so they will keep the uh same pattern um as the orange Network pattern so there are two ways to uh migrate the first way is um we can look at it um the application is M the to the kubernetes uh but without any architecture transformation and the second way is the uh application which is deported on the VM um when they moved to the kubernetes we can oh sorry uh we can use the technology such CU word um that means after the migration uh is still run on the VM but the VM is managed by the uh by the kubernetes in these two case um both of their uh the
