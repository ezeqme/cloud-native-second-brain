---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Geeta Gharpure", "Chao Chen", "Amazon"]
sched_url: https://kccnceu2023.sched.com/event/1HyXn/tales-from-on-call-fun-with-operating-etcd-at-scale-geeta-gharpure-chao-chen-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Tales+from+on-Call%3A+Fun+with+Operating+Etcd+at+Scale+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tales from on-Call: Fun with Operating Etcd at Scale - Geeta Gharpure & Chao Chen, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Geeta Gharpure, Chao Chen, Amazon
- Schedule: https://kccnceu2023.sched.com/event/1HyXn/tales-from-on-call-fun-with-operating-etcd-at-scale-geeta-gharpure-chao-chen-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Tales+from+on-Call%3A+Fun+with+Operating+Etcd+at+Scale+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tales from on-Call: Fun with Operating Etcd at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXn/tales-from-on-call-fun-with-operating-etcd-at-scale-geeta-gharpure-chao-chen-amazon
- YouTube search: https://www.youtube.com/results?search_query=Tales+from+on-Call%3A+Fun+with+Operating+Etcd+at+Scale+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p4o0eSS_ANI
- YouTube title: Tales from on-Call: Fun with Operating Etcd at Scale - Geeta Gharpure & Chao Chen, Amazon
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tales-from-on-call-fun-with-operating-etcd-at-scale/p4o0eSS_ANI.txt
- Transcript chars: 21287
- Keywords: request, revision, server, memory, cluster, typically, defrag, divergence, workload, upstream, updates, object, please, operation, second, version, database, multiple

### Resumo baseado na transcript

let's get started so our talk is called Tales from On Call fun with operating at CD at scale my name is Gita and I will be joined over video by ciao Chen both of us work at Amazon web services so let me introduce a little bit about us we work for eks eks is a managed kubernetes service what that means is eks manages the control plane for you all aspects of it performance scalability and availability so all the components here in the blue rectangle are owned

### Excerpt da transcript

let's get started so our talk is called Tales from On Call fun with operating at CD at scale my name is Gita and I will be joined over video by ciao Chen both of us work at Amazon web services so let me introduce a little bit about us we work for eks eks is a managed kubernetes service what that means is eks manages the control plane for you all aspects of it performance scalability and availability so all the components here in the blue rectangle are owned and managed by eks customers don't have access to those they typically just manage their workloads and sometimes the worker nodes So within the control plane the team I am from is the hcd team which focuses on operations and contributions to etcd now let's hear from ciao about our hcd environment uh thank you Akita good afternoon everyone my name is ciao a software engineer at Amazon I've been activated working uh in the operation of SCD the distributed key value store that is used by kubernetes as its primary data store in my virtual talk today I'll be sharing some of some of my experiences and insights of operating SCD in kubernetes clusters now SCD at eks eks SCD each SCD cluster is a three node cluster evenly distributed across three availability zones in a region availability results are isolated data center located with specific regions in which public cloud services originate and operate now the second uh eks ACD uses static IP to advertise SD client what endpoint it should connect to and for peer communication we also use static volumes to store wall and DB files well static here means every SED node where we use the same IP and volume after the previous node is terminated it guarantees data durability even if SCD Chrome is lost permanently it also indicates the sad membership is static there's no membership or reconfiguration simplifies our the operation eks SCD supports version downgrade from three five to three four it's a e case private patch and there is a reference published in Upstream um eks scd3435 and 33 does not have star region API layer schema incompatible issues for example the difference between the three three and a three four rafter internal protocol buffer schema change is a list checkpoint request uh if Venus 3-4 liter the experimental release checkpoint feature is enabled once it starts to replicate the entry to the 3-3 follower the follower is it server cannot understand the entry schema and and we're just Panic during deserialization yeah of course uh eks LCD are runs as a
