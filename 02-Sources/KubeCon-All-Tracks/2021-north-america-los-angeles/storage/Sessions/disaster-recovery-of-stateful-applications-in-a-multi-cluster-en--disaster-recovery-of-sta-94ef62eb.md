---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Orit Wasserman", "Shyamsundar Ranganathan", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV0M/disaster-recovery-of-stateful-applications-in-a-multi-cluster-environment-orit-wasserman-shyamsundar-ranganathan-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Disaster+Recovery+of+Stateful+Applications+in+a+Multi-Cluster+Environment+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Disaster Recovery of Stateful Applications in a Multi-Cluster Environment - Orit Wasserman & Shyamsundar Ranganathan, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Orit Wasserman, Shyamsundar Ranganathan, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV0M/disaster-recovery-of-stateful-applications-in-a-multi-cluster-environment-orit-wasserman-shyamsundar-ranganathan-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Disaster+Recovery+of+Stateful+Applications+in+a+Multi-Cluster+Environment+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Disaster Recovery of Stateful Applications in a Multi-Cluster Environment.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0M/disaster-recovery-of-stateful-applications-in-a-multi-cluster-environment-orit-wasserman-shyamsundar-ranganathan-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Disaster+Recovery+of+Stateful+Applications+in+a+Multi-Cluster+Environment+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1TSeilqoHSg
- YouTube title: Disaster Recovery of Stateful Applications in a Multi-Cl... Orit Wasserman & Shyamsundar Ranganathan
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/disaster-recovery-of-stateful-applications-in-a-multi-cluster-environm/1TSeilqoHSg.txt
- Transcript chars: 27516
- Keywords: cluster, application, volume, replication, recovery, clusters, storage, placement, across, disaster, control, recover, resource, relocate, primary, resources, actually, workload

### Resumo baseado na transcript

hello welcome to kubecon 2021 today's topic is disaster recovery the ability to recover from a full data center loss making sure you have the data and can recover your application my name is vassalman i'm after chief data foundation architecture trader and with me today is my colleague sean ranks from where that was also an architecting astrology today i will go over the foundation of disaster recovery and then talk about storage application in kubernetes then xiaomi will go over to multi-cluster management probably relocating orchestration then we'll

### Excerpt da transcript

hello welcome to kubecon 2021 today's topic is disaster recovery the ability to recover from a full data center loss making sure you have the data and can recover your application my name is vassalman i'm after chief data foundation architecture trader and with me today is my colleague sean ranks from where that was also an architecting astrology today i will go over the foundation of disaster recovery and then talk about storage application in kubernetes then xiaomi will go over to multi-cluster management probably relocating orchestration then we'll have a short demo and talk about the future work a demo will be based on ceph with a software defined storage completely open source quite mature the idbi unsafe is installing the software on standard servers using third disk from http memory and using standard ip network to get a real very reliable highly available very scalable distributed storage system in a single step cluster you get all the storage need you get cloud object storage with redux gateway block storage from rbd and set refresh will provide you with disability file systems in order to deploy self in kubernetes we are going to use book a cncf graduated project uh it manage self def you can manage self deploy configurate activate and features like industrial recovery and replication using basic kubernetes with method operators and custom resource definition let's talk about disaster recovery disaster recovery is making sure we can serve our customers even if we lose a data center or e or a cloud do a gen and sadly this can happen on the left for example we have a photo of ovh one of the largest data center in europe that was completely destroyed by fire last year in most cases our disaster recovery site should be found and that will mean high network latency in that case we won't be able to use synchronous applications but asynchronous which means we don't you need to drive we don't wait for the ride to sink and that will mean there will be some data loss in case of recovery if you can maintain low enough network latency and using classification then we can even get high availability we in this talk we're going to focus on regional dr which means two separate remote sites with high network latency two separate kubernetes cluster two separate explorations in case we can stretch the solid system these three thunder reference method demand are on there a very important way we measure the glass recovery our rpo and rtu recovery point objective is t
