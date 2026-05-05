---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Arka Saha", "VMware by Broadcom", "Chun-Hung (Henry) Tseng", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tx8m/dont-let-your-kubernetes-cluster-go-wild-ensuring-etcd-reliability-arka-saha-vmware-by-broadcom-chun-hung-henry-tseng-google
youtube_search_url: https://www.youtube.com/results?search_query=Don%27t+Let+Your+Kubernetes+Cluster+Go+Wild%3A+Ensuring+Etcd+Reliability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Don't Let Your Kubernetes Cluster Go Wild: Ensuring Etcd Reliability - Arka Saha, VMware by Broadcom & Chun-Hung (Henry) Tseng, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Arka Saha, VMware by Broadcom, Chun-Hung (Henry) Tseng, Google
- Schedule: https://kccnceu2025.sched.com/event/1tx8m/dont-let-your-kubernetes-cluster-go-wild-ensuring-etcd-reliability-arka-saha-vmware-by-broadcom-chun-hung-henry-tseng-google
- Busca YouTube: https://www.youtube.com/results?search_query=Don%27t+Let+Your+Kubernetes+Cluster+Go+Wild%3A+Ensuring+Etcd+Reliability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Don't Let Your Kubernetes Cluster Go Wild: Ensuring Etcd Reliability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8m/dont-let-your-kubernetes-cluster-go-wild-ensuring-etcd-reliability-arka-saha-vmware-by-broadcom-chun-hung-henry-tseng-google
- YouTube search: https://www.youtube.com/results?search_query=Don%27t+Let+Your+Kubernetes+Cluster+Go+Wild%3A+Ensuring+Etcd+Reliability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J93U9n_qxSI
- YouTube title: Don't Let Your Kubernetes Cluster Go Wild: Ensuring Etcd Reli... Arka Saha & Chun-Hung (Henry) Tseng
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dont-let-your-kubernetes-cluster-go-wild-ensuring-etcd-reliability/J93U9n_qxSI.txt
- Transcript chars: 22801
- Keywords: client, actually, request, robustness, basically, revision, requests, operation, framework, correct, mentioned, random, reproduce, cluster, consistency, response, output, traffic

### Resumo baseado na transcript

So if you're an end user or a direct customer of ATC or indirectly using ATC as one of your Kubernetes distribution, this is the right place for you. currently contributing to ATCD and also responsible for downstream releases of ATC and Kubernetes. uh with the problem of the revision going back in time there can be real world problems like uh network connection uh errors. So that's what we uh need to check but for robustnesses it's a little bit different because we need to validate the random input that was given uh and that's what the challenge becomes and for the uh environment uh basically unit tests first tests And one of the main direction of our test is to make sure that we are as reliable as Kubernetes would expect us to be. So we set foot by understanding how CD is used by Kubernetes which is documented in this contract.

### Excerpt da transcript

Hello everyone. Uh thank you for coming to our talk. Uh don't let your cubernetes cluster go wild. Ensuring at city reliability. So if you're an end user or a direct customer of ATC or indirectly using ATC as one of your Kubernetes distribution, this is the right place for you. Uh so a little about ourselves. Uh I'm Oro Shaha, a software engineer VMware by Broadcom. currently contributing to ATCD and also responsible for downstream releases of ATC and Kubernetes. I'm Henry. I'm a software engineer at Google and I also contribute to ATCD. So before we start, we would like to extend our sincere thanks to Benjamin Marik uh for laying the foundation and maintaining the CD and its uh testing framework as well as supporting this talk with their invaluable knowledge. Uh so in this session we will introduce what a distributed key value store is the design principles of the robustness test and the deep dive of it and finally we are going to demo on how to run a robustness test. A good reference of handling the data cons inconsistencies in ATCD uh via robustness test framework has been covered by Marik around two years ago when it was designed and implemented.

Uh you can refer to that. Also if you are looking for a beginner friendly primer of what robustness test is and how you can use it too, you can refer to our talk from last year in OSS Japan. Uh with that over to Henry for more about HCD and its constraints. So let's have a quick intro on distributed key value store. So Etsy ensures strict serializability. But what does that actually mean? So let's take a step back and think about what uh correctness actually is. So let's say we have two operations. We have put a equals to two and we have a get a out of the key value store and we execute them sequentially. So intuitively we would expect that the get result would be the value that we did the put with the last one that we put in. So that's how intuitively we think of how the value will be getting out of the key value store. Right? But if the thing if the requests are actually overlapping like when they're being executed concurrently how would you define the correctness? So before that let's discuss the representation that we'll be using throughout the the site deck um on how we represent the operation history.

So on the left you can see that we have clients zero and one. So we have two clients in this in this graph and each of the client they can only execute one thing at a time. So if there's a request in flig
