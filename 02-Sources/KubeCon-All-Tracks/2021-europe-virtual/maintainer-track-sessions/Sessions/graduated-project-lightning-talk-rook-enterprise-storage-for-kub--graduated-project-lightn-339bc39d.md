---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Travis Nielsen", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iaAi/graduated-project-lightning-talk-rook-enterprise-storage-for-kubernetes-travis-nielsen-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Rook%3A+Enterprise+Storage+for+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Graduated Project Lightning Talk: Rook: Enterprise Storage for Kubernetes - Travis Nielsen, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Travis Nielsen, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iaAi/graduated-project-lightning-talk-rook-enterprise-storage-for-kubernetes-travis-nielsen-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Rook%3A+Enterprise+Storage+for+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Graduated Project Lightning Talk: Rook: Enterprise Storage for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iaAi/graduated-project-lightning-talk-rook-enterprise-storage-for-kubernetes-travis-nielsen-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Rook%3A+Enterprise+Storage+for+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x0Bm9Gi8xg0
- YouTube title: Graduated Project Lightning Talk: Rook: Enterprise Storage for Kubernetes - Travis Nielsen, Red Hat
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/graduated-project-lightning-talk-rook-enterprise-storage-for-kubernete/x0Bm9Gi8xg0.txt
- Transcript chars: 6963
- Keywords: storage, platform, running, cluster, clusters, graduated, available, limitations, provide, stable, production, provides, provider, external, finally, already, write, releases

### Resumo baseado na transcript

hello welcome to this lightning talk uh presenting on rook enterprise storage for kubernetes i'm travis nielsen one of the original rook maintainers and i work for red hat happy to be here with you today virtually and hope to meet you soon in person at some point so let's dive right in all right so who needs storage we all need storage right applications require persistence that's just what it comes down to now depending on where you're running you have different solutions available for storage if you're running

### Excerpt da transcript

hello welcome to this lightning talk uh presenting on rook enterprise storage for kubernetes i'm travis nielsen one of the original rook maintainers and i work for red hat happy to be here with you today virtually and hope to meet you soon in person at some point so let's dive right in all right so who needs storage we all need storage right applications require persistence that's just what it comes down to now depending on where you're running you have different solutions available for storage if you're running a cloud provider now you have options available available for storage you might also be finding limitations with them or each cloud provider is different you don't have a consistent platform there or if you go into your own data center you kind of fall off a cliff and you say wait what do i do for storage now i have to go find some external solution to provide storage to my kubernetes cluster what do i do third point storage is traditionally not part of your kubernetes cluster it's treated as an external plug-in but why really should storage be external to kubernetes shouldn't we be able to manage storage as any other kubernetes application inside the same cluster and finally a question we started with was well if you're building a data platform can you really trust a new data platform something built from scratch or is there a way we can bring in a stable data platform that's been around for years already so we don't have to go rewrite that data later so we set out with some goals early in the book project and we said we want to make storage available natively to your grenade's cluster of course it'll be consumed like any other storage plug-in they'll use storage classes and pvcs and pvs and all that goodness so it will be consumed the same with the same patterns that you've already been using a second storage should be automated and it should be done in a way that is native to kubernetes the way you do things in kubernetes and you add onto kubernetes is with operators and with custom resource definitions or crds so if you have those the operator can take care of all the deployment the configuration the upgrades perform all the automation you need to take care of your your data platform and so with those requirements we said well where is a stable data platform and how can we integrate it with kubernetes uh we looked at a few and we started with ceph we said okay we believe in ceph it's been around for a long time so we're going to take sef we're
