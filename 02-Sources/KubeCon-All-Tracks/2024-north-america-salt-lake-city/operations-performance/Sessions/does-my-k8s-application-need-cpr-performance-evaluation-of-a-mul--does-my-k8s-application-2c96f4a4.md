---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Braulio Dumba", "Ezra Silvera", "IBM"]
sched_url: https://kccncna2024.sched.com/event/1i7lN/does-my-k8s-application-need-cpr-performance-evaluation-of-a-multi-cluster-workload-management-app-braulio-dumba-ezra-silvera-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Does+My+K8s+Application+Need+CPR%3F+Performance+Evaluation+of+a+Multi-Cluster+Workload+Management+App+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Does My K8s Application Need CPR? Performance Evaluation of a Multi-Cluster Workload Management App - Braulio Dumba & Ezra Silvera, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Braulio Dumba, Ezra Silvera, IBM
- Schedule: https://kccncna2024.sched.com/event/1i7lN/does-my-k8s-application-need-cpr-performance-evaluation-of-a-multi-cluster-workload-management-app-braulio-dumba-ezra-silvera-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Does+My+K8s+Application+Need+CPR%3F+Performance+Evaluation+of+a+Multi-Cluster+Workload+Management+App+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Does My K8s Application Need CPR? Performance Evaluation of a Multi-Cluster Workload Management App.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lN/does-my-k8s-application-need-cpr-performance-evaluation-of-a-multi-cluster-workload-management-app-braulio-dumba-ezra-silvera-ibm
- YouTube search: https://www.youtube.com/results?search_query=Does+My+K8s+Application+Need+CPR%3F+Performance+Evaluation+of+a+Multi-Cluster+Workload+Management+App+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PEMo5WVNzJg
- YouTube title: Does My K8s Application Need CPR? Performance Evaluation of a Multi-Cluster... B. Dumba, E. Silvera
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/does-my-k8s-application-need-cpr-performance-evaluation-of-a-multi-clu/PEMo5WVNzJg.txt
- Transcript chars: 25116
- Keywords: application, experiment, performance, workload, closer, cluster, management, clusters, single, policy, deploy, resources, transport, workloads, number, across, multicluster, important

### Resumo baseado na transcript

hello everyone I'm Bru Dumba St St scientist at IBM research hi I'm isra Sila I'm a senior technical staff member at IBM research yeah welcome to this talk yeah title yeah does my kubernets CPR performance evaluation of the M closa workload management application we are going to start this talk uh with G an overview of the importance and challenge of managing uh workloads across cluster then we are going to give you an overview of an application that manage workloads across CLA afterwards we're going to share

### Excerpt da transcript

hello everyone I'm Bru Dumba St St scientist at IBM research hi I'm isra Sila I'm a senior technical staff member at IBM research yeah welcome to this talk yeah title yeah does my kubernets CPR performance evaluation of the M closa workload management application we are going to start this talk uh with G an overview of the importance and challenge of managing uh workloads across cluster then we are going to give you an overview of an application that manage workloads across CLA afterwards we're going to share our experience in conducting performance experiments in the M closer workload management application show show some experimental results and and and and discuss yeah some lesson now I'm going now I'm going to hand over to to to my colle here Ezra we're going to explain to us the motivation for this talk and provide us with some background yes so hi everyone I hope you are having a great time here I'm very exciting to be here so as you saw we're talking to we are going to talk about um performance evaluation of multicluster H framework multicluster workload management F and the initial question is why why do we think it's important why do we think it's interesting and secondly why do we think um there is an issue that we need to actually resolve so let's me share with you H our motivation so first we already see a lot of people using multiple clusters it can be for various reasons some use multiple clusters in order to better isolate and have better security between for example different tenants different groups different department and isolate them into different kubernetes clusters another issue is compliance we already see government regulations and other requirement that force you to use specific cluster or even specific location another ER things that we recently see is that in many cases users and especially administrators prefer to expose special Hardware capabilities through dedicated clusters especially in the AA case another evidence for the at least for us for the importance and interest in this area is that we can already see several applications and solution that Target the exact same area like Cellar kada ocm and others regarding the what is the issue here so we all know that performance is a key factor in adopting such Technologies and this is obvious because users do expect their workloads to be deployed rapidly and get the status immediately and they do not really care that this is multicluster right we want it to be have as if it's a
