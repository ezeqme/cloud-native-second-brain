---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Paco Xu", "DaoCloud", "Saiyam Pathak", "Loft Labs"]
sched_url: https://kccnceu2025.sched.com/event/1tx9S/a-huge-cluster-or-multi-clusters-identifying-the-bottleneck-paco-xu-daocloud-saiyam-pathak-loft-labs
youtube_search_url: https://www.youtube.com/results?search_query=A+Huge+Cluster+or+Multi-Clusters%3F+Identifying+the+Bottleneck+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Huge Cluster or Multi-Clusters? Identifying the Bottleneck - Paco Xu, DaoCloud & Saiyam Pathak, Loft Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Paco Xu, DaoCloud, Saiyam Pathak, Loft Labs
- Schedule: https://kccnceu2025.sched.com/event/1tx9S/a-huge-cluster-or-multi-clusters-identifying-the-bottleneck-paco-xu-daocloud-saiyam-pathak-loft-labs
- Busca YouTube: https://www.youtube.com/results?search_query=A+Huge+Cluster+or+Multi-Clusters%3F+Identifying+the+Bottleneck+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Huge Cluster or Multi-Clusters? Identifying the Bottleneck.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9S/a-huge-cluster-or-multi-clusters-identifying-the-bottleneck-paco-xu-daocloud-saiyam-pathak-loft-labs
- YouTube search: https://www.youtube.com/results?search_query=A+Huge+Cluster+or+Multi-Clusters%3F+Identifying+the+Bottleneck+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6l5zCt5QsdY
- YouTube title: A Huge Cluster or Multi-Clusters? Identifying the Bottleneck - Paco Xu & Saiyam Pathak
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-huge-cluster-or-multi-clusters-identifying-the-bottleneck/6l5zCt5QsdY.txt
- Transcript chars: 26479
- Keywords: cluster, clusters, control, version, vcluster, mentioned, having, server, namespace, sometimes, another, create, connect, solutions, management, versions, related, running

### Resumo baseado na transcript

I hope some of your questions get answered else we are here for today tomorrow as well. Um I'm from Loft Labs uh creators of vCluster and I'm joined by I'm principal developer advocate um founder of um cube simplify build safe I'm a cubestronaut you can connect with me at the sai impart on any of the social platforms I'm pretty there's ungroup and openi and also the bayer uh they have about uh uh 10k or uh 15k uh nodes uh for their cluster and uh uh later for bounce they use crew crew brain to scale to 20k nodes and uh last uh last year in kcon North America uh TKE has announced this scaling to the 65k uh nodes and there's a demo yesterday if you see uh you are in their demo later. the EDC this is talked many times uh and also uh DS and storage challenges are uh one of the key uh issue on bottleneck and uh node management and monitoring is also uh a problem when uh at scale uh so uh here's a higher uh buildings uh uh and also uh people like uh huge clusters sometimes and uh this may reduce the maintenance costs and uh uh centralized the management and enforce the policies.

### Excerpt da transcript

Hello. Hello everyone. Well, that's a massive crowd. So, uh, welcome to this session. A huge cluster or multiclusters identifying the bottleneck. We'll try to squeeze as much as we can in the 30 minutes. I hope some of your questions get answered else we are here for today tomorrow as well. Um, my name is Sam Paruk. Um I'm from Loft Labs uh creators of vCluster and I'm joined by I'm principal developer advocate um founder of um cube simplify build safe I'm a cubestronaut you can connect with me at the sai impart on any of the social platforms I'm pretty active over there and I'm joined by I'm from China and I work in docloud uh I'm a member of kernetes steering committee and also a crew maintainer Yeah. U so we have a small uh kind of um not a quiz obviously but we just want to take some idea of where things are. So if you can just scan and uh there are just two questions. If you can just it's a anonymous votes no sign up and stuff. I hope there is no sign up. Uh so anonymous vote if you can just do it that would help us understand the dynamics of u Kubernetes clusters the size of Kubernetes clusters how many Kubernetes clusters you are using.

All right we do have 44 participants responding 39. That's cool. Okay we'll not we'll not take much time though. Uh so we'll just see the results of where we are. Well, that's a very good number of uh people having Kubernetes clusters greater than 100 nodes and out of 239 it's 40% which is a like very massive number. Let's go to the next one. and having more than 30 clusters in your organization. Well, that's again a very huge number. So, everyone has those huge multicluster and big cluster problems. Well, that's cool. Uh that's what we are here for. And let's get started. Let me share the slides again. You can take this uh uh this is a page from the kubernetes.io. Uh it's about consideration for light clusters. Uh I think most of you may uh have already see this uh uh here we recommended to for uh 5,000 nodes. Uh this is a tested number by kubernetesci uh by sik scalability and uh this this means those uh this member is tested already tested and meanwhile these numbers here uh have not been updated for a long time.

So uh here we have um some updates or uh and uh for the previous public blocks uh early days uh open eye has scaling their to uh two uh 2,00 and 500 nodes in uh 2018 and uh later uh we can see uh there's ungroup and openi and also the bayer uh they have about uh uh 10k or uh 15k uh nodes uh for their cl
