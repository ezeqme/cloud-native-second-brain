---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Dave Smith-Uchida", "Veeam"]
sched_url: https://kccnceu2024.sched.com/event/1Yhh4/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Data Protection WG Deep Dive - Dave Smith-Uchida, Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Dave Smith-Uchida, Veeam
- Schedule: https://kccnceu2024.sched.com/event/1Yhh4/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhh4/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2rfMgYRNoPo
- YouTube title: Kubernetes Data Protection WG Deep Dive - Dave Smith-Uchida, Veeam
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-data-protection-wg-deep-dive/2rfMgYRNoPo.txt
- Transcript chars: 18870
- Keywords: snapshot, volume, backup, storage, working, application, feature, change, protection, blocks, actually, repository, bucket, server, workloads, restore, driver, snapshots

### Resumo baseado na transcript

hello everyone thank you for coming to the session today uh Dave and I will be giving a deep dive of kubernetes data protection working group my name is shinyang I work at vwell in the cloud native story team I'm also a co-chair of kuet six storage and the data protection working group working with Dave I'm Dave Smith Ida I'm a technical leader at vhm working on the Caston K10 product here is today's agenda we will give key updates of the working group we will talk about

### Excerpt da transcript

hello everyone thank you for coming to the session today uh Dave and I will be giving a deep dive of kubernetes data protection working group my name is shinyang I work at vwell in the cloud native story team I'm also a co-chair of kuet six storage and the data protection working group working with Dave I'm Dave Smith Ida I'm a technical leader at vhm working on the Caston K10 product here is today's agenda we will give key updates of the working group we will talk about who we are and uh uh what is the motivation for establishing the working group and we will discuss some of the projects that we are working on and finally how to get involved here are some of the key updates we wrote a white paper on on the data protection workflows in kubernetes and here's a link to the annual report and also some of the previous talks at ccom here you can see the companies who are supporting this working group if your compan also is supporting the sing group but not showing on this list please let us know and we can get you added in kubernetes the dean operations for state for work cloths are well supported we have positionist volumes and POS volume claims for the volume operations we have workload apis such as deployments and state for set that you can use to manage your workloads according to the 2022 survey by data on kubernetes community more and more ster workloads are moving to c8s there are different typ typ of workloads there are database workloads there are AI machine learning U messaging streaming and other type of workloads as well this St workloads are moving to kubernetes to take advantage of kubernetes self-healing ability portability scalability agile deployment and so on on the other hand dayto operations such as data protection is still limited G Ops workflow has limitations for stfe for application Secrets config maps and your precious data sted in the Precision volumes are not on the G so we still need to figure out how to better support data protection in kues that's why we formed this working group we we do work with other groups S Storage and S apps are sponsors of this working group we also work with the tech storage on data protection related topics this shows the backup workflow with existing and missing building blocks in kubernetes the blue color shows the process the green color shows existing building blocks and yellow ones are uh uh work in progress and then uh the orange ones are missing building blocks when you take a backup of an applicat
