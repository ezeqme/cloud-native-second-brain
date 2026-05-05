---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Customizing + Extending Kubernetes"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Conor Nolan", "Dave Cremins", "Intel"]
sched_url: https://kccnceu2021.sched.com/event/iE1t/k8s-labels-everywhere-decluttering-with-node-profile-discovery-conor-nolan-dave-cremins-intel
youtube_search_url: https://www.youtube.com/results?search_query=K8s+Labels+Everywhere%21+Decluttering+With+Node+Profile+Discovery.+CNCF+KubeCon+2021
slides: []
status: parsed
---

# K8s Labels Everywhere! Decluttering With Node Profile Discovery. - Conor Nolan & Dave Cremins, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Conor Nolan, Dave Cremins, Intel
- Schedule: https://kccnceu2021.sched.com/event/iE1t/k8s-labels-everywhere-decluttering-with-node-profile-discovery-conor-nolan-dave-cremins-intel
- Busca YouTube: https://www.youtube.com/results?search_query=K8s+Labels+Everywhere%21+Decluttering+With+Node+Profile+Discovery.+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre K8s Labels Everywhere! Decluttering With Node Profile Discovery..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1t/k8s-labels-everywhere-decluttering-with-node-profile-discovery-conor-nolan-dave-cremins-intel
- YouTube search: https://www.youtube.com/results?search_query=K8s+Labels+Everywhere%21+Decluttering+With+Node+Profile+Discovery.+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y4UF9ML0BDw
- YouTube title: K8s Labels Everywhere! Decluttering With Node Profile Discovery. - Conor Nolan & Dave Cremins, Intel
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/k8s-labels-everywhere-decluttering-with-node-profile-discovery/y4UF9ML0BDw.txt
- Transcript chars: 21624
- Keywords: profile, feature, labels, features, worker, workload, discovery, individual, performance, platform, workloads, cluster, particular, specific, policy, topology, manager, profiles

### Resumo baseado na transcript

hi welcome to kubecon cloud nativecon europe 2021 virtual today's talk is going to be focused on kubernetes labels everywhere decluttering with node profile discovery my name is dave kremens i'm a cloud software architect in the network platform group at intel and today i'm going to be joined by connor nolan who's a senior engineer in the orchestration team at intel so for today's agenda we're going to cover node feature discovery an overview or background on nfd and the problem statement associated with it we also have an

### Excerpt da transcript

hi welcome to kubecon cloud nativecon europe 2021 virtual today's talk is going to be focused on kubernetes labels everywhere decluttering with node profile discovery my name is dave kremens i'm a cloud software architect in the network platform group at intel and today i'm going to be joined by connor nolan who's a senior engineer in the orchestration team at intel so for today's agenda we're going to cover node feature discovery an overview or background on nfd and the problem statement associated with it we also have an example of a complex node specification we also intend to provide a conceptual overview of node profiles and we have orchestrated a very simple demo that highlights the the problem and presents a possible resolution to the to the issue and finally we will have some key takeaway summaries for you guys too so before discussing the problem statement at hand let's focus on what nfd is today so nfd is a known feature discovery component available in kubernetes that detects hardware features and advertises those features using node labels and these particular features can be categorized under numerous specific domains such as cpu io mmu kernel memory network storage pci system usb etc and it's an important component in the kubernetes ecosystem given that numerous different types of workloads need to ha or have uh need special attention let's say to uh specific features of a platform um so for instance you know if some platform had um a particular feature that was required as part of your workload then we want to ensure that the workload lands on a compute node that has the the intended feature available but again even though this helped in the the placement of workloads um or at least complemented the placement of the workloads it still kind of promoted this tight coupling to individual platform capabilities and you know if i drill into that what i'm really saying is is that your workload was very individual feature aware so each feature that was required or intended to be leveraged by your workload needs to be specified up front and that's what i mean by thai coupling and when we look at this across numerous different types of workloads and especially from my background where it's really based in telco workloads um there are a lot of features required from the platform in order for a workload to run deterministically and with the right level of performance and throughput and when we look at what's expected um of the platform it can become a c
