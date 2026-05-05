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
speakers: ["Xing Yang", "Ashutosh Kumar", "VMware"]
sched_url: https://kccncna2022.sched.com/event/182Iw/how-to-handle-node-shutdown-in-kubernetes-xing-yang-ashutosh-kumar-vmware
youtube_search_url: https://www.youtube.com/results?search_query=How+To+Handle+Node+Shutdown+In+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How To Handle Node Shutdown In Kubernetes - Xing Yang & Ashutosh Kumar, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Xing Yang, Ashutosh Kumar, VMware
- Schedule: https://kccncna2022.sched.com/event/182Iw/how-to-handle-node-shutdown-in-kubernetes-xing-yang-ashutosh-kumar-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+Handle+Node+Shutdown+In+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How To Handle Node Shutdown In Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Iw/how-to-handle-node-shutdown-in-kubernetes-xing-yang-ashutosh-kumar-vmware
- YouTube search: https://www.youtube.com/results?search_query=How+To+Handle+Node+Shutdown+In+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=W2JCavacjf4
- YouTube title: How To Handle Node Shutdown In Kubernetes - Xing Yang & Ashutosh Kumar, VMware
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-to-handle-node-shutdown-in-kubernetes/W2JCavacjf4.txt
- Transcript chars: 22504
- Keywords: shutdown, feature, non-graceful, graceful, minutes, terminating, cubelet, delete, running, status, stateful, volume, cluster, critical, happens, happen, online, controller

### Resumo baseado na transcript

hello everyone today we are going to talk about how to handle no shout out in kubernetes my name is Xin Yang I work at VMware in the cloud native storage team I'm also a co-chair of kubernetes seek storage hi everyone I'm ashitos I work at VMware on cluster life cycle team and I'm here to talk about notes are down in communities or what using you can get started here's our agenda today we're going to talk about what is a graceful no Shadow what is non-gracefulness we

### Excerpt da transcript

hello everyone today we are going to talk about how to handle no shout out in kubernetes my name is Xin Yang I work at VMware in the cloud native storage team I'm also a co-chair of kubernetes seek storage hi everyone I'm ashitos I work at VMware on cluster life cycle team and I'm here to talk about notes are down in communities or what using you can get started here's our agenda today we're going to talk about what is a graceful no Shadow what is non-gracefulness we will talk about how to handle them we'll give a demo and we will talk about next steps in a kubernetes cluster it is possible for node to shut down this could happen either in a planned way or it could happen unexpectedly but no shutdown could happen for many reasons it could be that you need to apply a security patch you need to do your kernel upgrade you need to reboot a node or it could be due to the preemption of the VM instances or it could be that there's a harbor failure or some software problem that causes that to happen you can trigger no shutdown by around a shutdown or a part of comment or just physically push a button to shut down the the machine if you do that without joining the notes then that could cause a workload failures anoshadang could either be graceful or non-graceful let me talk about Greece for no Sharon first graceful no Shadow feature was introduced in kubernetes 1.20 release and it moved to Beta in 1.21 this allows cubelet to detect a no shutdown and properly terminate the parts make sure all the resources are released before the real shutdown and parts are terminated in two phases first the regular pots and then the critical parts to make sure that the critical function of the application can work as long as possible without this feature user have to make sure they manually join the notes before shutting down the node however no shutdown Could Happen unexpectedly in that case the parts could be evicted unsafely if the node is not drained and your application would see errors and your workloads may not function properly so let's talk about how the grace for no shutdown works for this feature cubelet relies on the system D's inhibitor lock mechanism and when cubely starts it requires this delay type initiator lock and it watches for the shutdown events when it detects a shutdown it delays the shutdown and terminate the parts make sure everything is released before the real Sharon there are two config parameters in couplet that you need to set for this feature to work
