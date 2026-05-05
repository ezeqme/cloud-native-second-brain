---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Zhang Zhen", "Alibaba Cloud", "Vec Sun", "Xiaohongshu(RedNote)"]
sched_url: https://kccnceu2026.sched.com/event/2EF4p/operationalizing-ai-workloads-on-kubernetes-with-openkruise-zhang-zhen-alibaba-cloud-vec-sun-xiaohongshurednote
youtube_search_url: https://www.youtube.com/results?search_query=Operationalizing+AI+Workloads+on+Kubernetes+With+OpenKruise+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen, Alibaba Cloud & Vec Sun, Xiaohongshu(RedNote)

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Zhang Zhen, Alibaba Cloud, Vec Sun, Xiaohongshu(RedNote)
- Schedule: https://kccnceu2026.sched.com/event/2EF4p/operationalizing-ai-workloads-on-kubernetes-with-openkruise-zhang-zhen-alibaba-cloud-vec-sun-xiaohongshurednote
- Busca YouTube: https://www.youtube.com/results?search_query=Operationalizing+AI+Workloads+on+Kubernetes+With+OpenKruise+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Operationalizing AI Workloads on Kubernetes With OpenKruise.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4p/operationalizing-ai-workloads-on-kubernetes-with-openkruise-zhang-zhen-alibaba-cloud-vec-sun-xiaohongshurednote
- YouTube search: https://www.youtube.com/results?search_query=Operationalizing+AI+Workloads+on+Kubernetes+With+OpenKruise+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0JT8iDDS74k
- YouTube title: Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen & Vec Sun
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/operationalizing-ai-workloads-on-kubernetes-with-openkruise/0JT8iDDS74k.txt
- Transcript chars: 13745
- Keywords: actually, another, inference, cruise, operation, update, introduce, training, agents, recreate, sandbox, containers, container, cost, called, sample, operations, application

### Resumo baseado na transcript

Uh yeah I'm the maintainer and today I will share with you uh how some some experience and features we provide in open cruise and its sub projects to operate to operate the AI workload. First I will introduce some the challenge of the AI work clothes including the uh training inference and agents and then I will go to the the different the operations for different kind of of applications. Uh in previously if you want to update a a port in Kubernetes you just uh delete the port and just recreate the port. For example uh additional cost of scheduling IP allocation and volume mounting is just saved. Yeah, with image pool drop uh the open cruise demon run in every node we'll just pull the related image beforehand so that when the ports get uh the real port get scheduled they can get every image is already already there almost no image So uh we actually we are having uh a proposal and a working uh a working patch that are working on this problem.

### Excerpt da transcript

Uh okay let's start. Hello uh hello everyone. Uh I'm John from open cruise from open cruise community. Uh yeah I'm the maintainer and today I will share with you uh how some some experience and features we provide in open cruise and its sub projects to operate to operate the AI workload. Uh we uh we have some outlines here. First I will introduce some the challenge of the AI work clothes including the uh training inference and agents and then I will go to the the different the operations for different kind of of applications. Yeah. Uh actually there are two kinds of application from my point of view. First is that the training and inference. Yeah. They just contains a lot of datas. Yeah. Mostly in most uh uh practice some of will put data or in in the image and use the image as a as a as a source of data and then the horse will just some of the training or inference will just run and die in groups because they rely on some some uh some communication library uh such as nickel sometime such some something like that also the this application may rely on some devis that that is slow to allocate uh for example they need to allocate the GPU or some uh high performance uh comm communication devis the second type of agent uh application is agents or it's related sandboxes uh for agents uh or especially agent sandboxes they need a very fast creation uh demands.

Yeah, they mostly need they need to get the sandbox under one second. And then another thing is that the the command and file system operation is a must for this uh for for the agents because the agents may need some do some uh op do some uh token injection or some file system operation uh preparation uh before do some code uh code generation or code code running. And third is that uh now with agent sandbox uh many many operation previous happens in the virtual machine now becomes a master for for the containers things like hibernate and resume become a must. So we have to deal with that. Uh the first operations I'd like to introduce is impl update. uh it is actually can be used for faster inference uh inference service update. Uh I'd like to introduce some the concept of in place update. Uh in previously if you want to update a a port in Kubernetes you just uh delete the port and just recreate the port. Uh in in such cases you get a new port uh you get a you get the new IP and then he he may schedule to a different node.

Uh yeah with imp place update you just it doesn't delete the port at all. It just del
