---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Gabor Horvath", "Ewald Überall", "Raiffeisen Bank International"]
sched_url: https://kccnceu2026.sched.com/event/2CW1Z/from-gitops-to-aiops-evolving-rbis-kubernetes-platform-with-crossplane-and-sharded-kargo-gabor-horvath-ewald-uberall-raiffeisen-bank-international
youtube_search_url: https://www.youtube.com/results?search_query=From+GitOps+to+AIOps%3A+Evolving+RBI%27s+Kubernetes+Platform+with+Crossplane+and+Sharded+Kargo+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From GitOps to AIOps: Evolving RBI's Kubernetes Platform with Crossplane and Sharded Kargo - Gabor Horvath & Ewald Überall, Raiffeisen Bank International

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Gabor Horvath, Ewald Überall, Raiffeisen Bank International
- Schedule: https://kccnceu2026.sched.com/event/2CW1Z/from-gitops-to-aiops-evolving-rbis-kubernetes-platform-with-crossplane-and-sharded-kargo-gabor-horvath-ewald-uberall-raiffeisen-bank-international
- Busca YouTube: https://www.youtube.com/results?search_query=From+GitOps+to+AIOps%3A+Evolving+RBI%27s+Kubernetes+Platform+with+Crossplane+and+Sharded+Kargo+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From GitOps to AIOps: Evolving RBI's Kubernetes Platform with Crossplane and Sharded Kargo.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1Z/from-gitops-to-aiops-evolving-rbis-kubernetes-platform-with-crossplane-and-sharded-kargo-gabor-horvath-ewald-uberall-raiffeisen-bank-international
- YouTube search: https://www.youtube.com/results?search_query=From+GitOps+to+AIOps%3A+Evolving+RBI%27s+Kubernetes+Platform+with+Crossplane+and+Sharded+Kargo+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cqDVeqLvh00
- YouTube title: From GitOps to AIOps: Evolving RBI's Kubernetes Platform with Cross... Gabor Horvath & Ewald Überall
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-gitops-to-aiops-evolving-rbis-kubernetes-platform-with-crossplane/cqDVeqLvh00.txt
- Transcript chars: 25899
- Keywords: resources, crossplane, promotion, migration, managed, argo, cluster, platform, customers, already, version, created, namespace, information, request, deploy, infrastructure, bucket

### Resumo baseado na transcript

My name is Gabbor War and together with my colleague Evadar, we will share our journey how we moved uh from GitOps to AI ops using crossplane and shed cargo. We are working at rifles and bank international which is one of Austria's leading corporate and investment banks. In order not to break out from this name space, we also deploy Kyu policies and then the rest of the namespace is the place where crossplane resources can be created, claims can be created and other uh Kubernetes manifests are deployed. The third layer is Argo CD but we don't have one central Argo CD which handles all test production tier clusters but for each uh each uh cluster we have dedicated Argo CD and there is actually an architecture decision behind because cargo controller can to go to check what's going on with the promotion and from security aspect this is also not good because this one central uh cargo should not have access to each and every cluster and you do not you will not need to expose the API Kubernetes API on every cluster So this is a solution what we came up and um this is called cargo sharded topology or agent based architecture and uh here on the picture you can see that I'm not sure yes you can see that

### Excerpt da transcript

All right. Hi, welcome on our session. I think we are just in time. There are still people coming in but I would like to start now. Uh, welcome on our session. My name is Gabbor War and together with my colleague Evadar, we will share our journey how we moved uh from GitOps to AI ops using crossplane and shed cargo. We are working at rifles and bank international which is one of Austria's leading corporate and investment banks. We have 11 subsidiary banks in central eastern Europe and we have 18.6 million customers with around 42,000 employees. We are working in Mercury team where we develop Mercury platform which is a groupwide platform for building and running cloudnative applications. We are a team of 20 people. Out of 20 people, we have 15 engineers. Approximately 100 plus engineers are using our platform. Currently, we have thousand plus namespaces across 13 clusters. And we have three service offerings. The first one is namespace as a service where we provide a shared OKD open shift based cluster and customers can uh request their an isolated name space and then they they can run their their containerized applications.

The second offering is account as a service where we offer AWS dedicated secured account. They can deploy their cloud resources which can be consumed from the containerized applications. We also have cluster as a service here. The difference is uh we have other internal platform teams. They can reuse our stack. They can reuse our templates and code. And we already have two of such internal platform customers. Uh in all uh here in this picture you will see uh different building blocks what we have in our architecture and as you see we have all the building blocks that requires nowadays for a modern platform. In today's talk, we will focus more on GitHubs pipeline and on crossplane related uh self-service libraries. In order to understand what multi-tenency means for Mercury platform, I would like to guide you through on three distinct isolation layers which we have. The first one is the platform Kubernetes account. This is where we deploy our OKD open shift cluster and internal customers will share the uh compute resources but they don't have full access to the to the cluster.

Instead what they get is a isolated namespace and as soon as they uh onboard it and the namespace gets created then Kao will create a default deny network policy and by default there is no ingress there is no incoming traffic or outgoing traffic. We also have st
