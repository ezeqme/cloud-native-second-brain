---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Jingming Guo", "Airbnb"]
sched_url: https://kccncna2024.sched.com/event/1i7mK/dns-deep-dive-in-kubernetes-with-coredns-jingming-guo-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=DNS+Deep+Dive+in+Kubernetes+with+CoreDNS+CNCF+KubeCon+2024
slides: []
status: parsed
---

# DNS Deep Dive in Kubernetes with CoreDNS - Jingming Guo, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Jingming Guo, Airbnb
- Schedule: https://kccncna2024.sched.com/event/1i7mK/dns-deep-dive-in-kubernetes-with-coredns-jingming-guo-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=DNS+Deep+Dive+in+Kubernetes+with+CoreDNS+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre DNS Deep Dive in Kubernetes with CoreDNS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mK/dns-deep-dive-in-kubernetes-with-coredns-jingming-guo-airbnb
- YouTube search: https://www.youtube.com/results?search_query=DNS+Deep+Dive+in+Kubernetes+with+CoreDNS+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lAUmdIGP_fE
- YouTube title: DNS Deep Dive in Kubernetes with CoreDNS - Jingming Guo, Airbnb
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/dns-deep-dive-in-kubernetes-with-coredns/lAUmdIGP_fE.txt
- Transcript chars: 22582
- Keywords: cluster, server, configuration, domain, record, request, search, resolver, resolve, plugin, airbnb, mesh, contains, applications, multicluster, policy, evaluate, running

### Resumo baseado na transcript

good afternoon everyone welcome to the talk I'm timing a software engineer of airb B I work in Cloud infra team I'm currently focusing on building a high performance and reliable system for Airbnb internal DNS previously in AWS I worked on their blog storage platform I love my current job as it motivates me every day to learn think and explore something new I outside of work I enjoy baking hiking skiing and growing tomatoes and sunflowers in my yard today I'm going to talk about their DNS in and the option section allows modification to certain internal resolver settings the commonly use option like OSS time out attempts and do Define the threshold for the number of dot which must appear in your name before an initial absolute query will be made time out sets amount of time the resolver will wait for a response from a remote name server before retrying the query via a different name server at times set their number of times the resolver will send a query to its name servers before giving airbnb.com there are two dots in this record which meets the UND do Strat cold that the query will be directly sent to the name server and the DS server used here is Route 53 which can response with a result great let's see another as configuration settings both pqdn and fqdn can be resolve to the IPS successfully kubernetes defined DS record of service in format of service name.

### Excerpt da transcript

good afternoon everyone welcome to the talk I'm timing a software engineer of airb B I work in Cloud infra team I'm currently focusing on building a high performance and reliable system for Airbnb internal DNS previously in AWS I worked on their blog storage platform I love my current job as it motivates me every day to learn think and explore something new I outside of work I enjoy baking hiking skiing and growing tomatoes and sunflowers in my yard today I'm going to talk about their DNS in kubernetes and share about the Airbnb kubernetes DNS use cases and solutions here is our agenda today first I will talk about their DNS functionality inside kubernetes then I'm going to share how CS works as a cluster DS server some takeaways of integration of cordings in airbnb's kubernetes infrastructure also share some major DS use cases in Airbnb and our Solutions finally I'm going to talk about some multic claster DS Explorations before I start let me ask a question how many of you have had to deal with or troubleshoot DNS issues in kubernetes and found it confusing wow I see so many hands thank you then today we are going to break it down by the end of the talk we will have a better understanding of kubernetes DNS so let's have a look together of how a DS request is generally resolved in the kubernetes cluster the DS request is sent out by the application running kubernetes pod the resolver is a first step of DS look up here the resolver refers to the DS resolver library that runs in the system to provide core functionalities for resolving domain names into IP addresses the actual resolver Library usage can be various depending on the programming language and operating system example in go there are two type of resolvers one is CTO resolver that calls standard C library GC and the other is pure gold DS resolver the resolver consumes the DNS configuration on the pod which is are specified in the resolve file the DNS configuration file contains the name server IP that the resolver will send the query to if we are using a cluster d as server this name server IP should be the cluster IP of the cluster DS service example the service is is called kubs with class IP 10.

32.0 do10 that resolver will send the traffic to this IP after the request reaches C Service CP proxy will route the traffic to Cluster DS server pod if your coup proxy runs in I table mode that traffic will be R via app table rules here the cluster DS server is cor DS C DS is a flexible extensible DS s
