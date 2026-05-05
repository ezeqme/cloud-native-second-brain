---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQho/advanced-multi-cluster-scheduling-with-open-cluster-management-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Advanced+Multi+Cluster+Scheduling+with+Open+Cluster+Management+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Advanced Multi Cluster Scheduling with Open Cluster Management | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQho/advanced-multi-cluster-scheduling-with-open-cluster-management-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Advanced+Multi+Cluster+Scheduling+with+Open+Cluster+Management+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Advanced Multi Cluster Scheduling with Open Cluster Management | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQho/advanced-multi-cluster-scheduling-with-open-cluster-management-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Advanced+Multi+Cluster+Scheduling+with+Open+Cluster+Management+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cN7pXnOqt2Y
- YouTube title: Advanced Multi Cluster Scheduling with Open Cluster Management | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/advanced-multi-cluster-scheduling-with-open-cluster-management-project/cN7pXnOqt2Y.txt
- Transcript chars: 6017
- Keywords: cluster, management, clusters, workload, managed, manager, specific, resource, called, manifest, status, placement, advanced, scheduling, multicluster, supposed, matter, inventory

### Resumo baseado na transcript

hello hello everybody uh welcome welcome to the advanced multicluster scheduling with open cluster management um just a quick question how many of you know open cluster management the cncf project a few hands yeah it's going to be a good session um I'm LS I work for Red Hats and also for the open cluster management project this is Dario my colleague you want to introduce yourself yeah I'm Dario I work for for I work at for open class management for a while in the latest months a

### Excerpt da transcript

hello hello everybody uh welcome welcome to the advanced multicluster scheduling with open cluster management um just a quick question how many of you know open cluster management the cncf project a few hands yeah it's going to be a good session um I'm LS I work for Red Hats and also for the open cluster management project this is Dario my colleague you want to introduce yourself yeah I'm Dario I work for for I work at for open class management for a while in the latest months a little bit less but I'm going to say something concerning over clust management normally you should know that about yeah thanks um let's let's Dive Right In um we don't have a lot of time so I'll go straight to this slide which is what is open cluster management for those who doesn't know what it is it's a cncf Sandbox sandbox project it's supposed to provide vendor neutral apis for multicluster kubernetes management so what does that mean if you can handle multiple clusters at once uh open cluster management can help you right there right so uh sorry doesn't matter where it's located doesn't matter the infrastructure doesn't matter which flavor of kuber is it's supposed to have multiple apis for helping with multicluster management what are these apis I'll speak about the main ones uh the main features one uh open cluster management is going to give you a cluster inventory so if you manage 10 clusters you have a list of 10 manage clusters like a cluster inventory so that's one um second one it's called workload definition Dario is going to talk more about this um and it's supposed to help with uh with workload placements that's why the title of the call is Advanced to scheduling because it it's going to help you schedule and place workloads in the right clusters so that's one of the main apis and plus where it's going to land which Nam space which clusters is it going to be a static workload it's going to be a dynamic workload so there are many apis that we are going to explore in this uh lightning talk D you want to go ahead yeah as Louise mention it cluster inventory is one of the main topic of of open cluster management fundamentally you have to think a single pain of class that show all your managed cluster the manager cluster has to be registered so open cluster management doesn't come with something that create provision the cluster for you but you can create a cluster a recent a recent kubernetes cluster is enough to be registered normally to register a cluster you need to
