---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Anish Ramasekar", "Microsoft", "James Munnelly", "Apple"]
sched_url: https://kccncna2024.sched.com/event/1i7qC/rogue-no-more-securing-kubernetes-with-node-specific-restrictions-anish-ramasekar-microsoft-james-munnelly-apple
youtube_search_url: https://www.youtube.com/results?search_query=Rogue+No+More%3A+Securing+Kubernetes+with+Node-Specific+Restrictions+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Rogue No More: Securing Kubernetes with Node-Specific Restrictions - Anish Ramasekar, Microsoft & James Munnelly, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Anish Ramasekar, Microsoft, James Munnelly, Apple
- Schedule: https://kccncna2024.sched.com/event/1i7qC/rogue-no-more-securing-kubernetes-with-node-specific-restrictions-anish-ramasekar-microsoft-james-munnelly-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Rogue+No+More%3A+Securing+Kubernetes+with+Node-Specific+Restrictions+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Rogue No More: Securing Kubernetes with Node-Specific Restrictions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qC/rogue-no-more-securing-kubernetes-with-node-specific-restrictions-anish-ramasekar-microsoft-james-munnelly-apple
- YouTube search: https://www.youtube.com/results?search_query=Rogue+No+More%3A+Securing+Kubernetes+with+Node-Specific+Restrictions+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kznxInpGet4
- YouTube title: Rogue No More: Securing Kubernetes with Node-Specific Restrictions - Anish Ramasekar, James Munnelly
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/rogue-no-more-securing-kubernetes-with-node-specific-restrictions/kznxInpGet4.txt
- Transcript chars: 24970
- Keywords: basically, permissions, actually, cluster, admission, policy, secret, account, validating, running, particular, operator, create, server, request, compromise, modify, specific

### Resumo baseado na transcript

okay uh hey everyone Welcome to our talk Rogue no more securing kubernetes with not specific restrictions um yeah um yeah thanks for coming I'm James monley I'm a software engineer in the open engineering um department at Apple and I'm Anish I'm a software engineer at Microsoft working on security I am a member of kuber seot and maintainer for Secret store CSI driver yeah so so I guess bit of background on um kind of this whole problem space so in kubernetes uh like you probably already aware combined with validating admission policies so what is validating admission policies um validating admission policies are designed to be good alternatives for validating web hooks for most common use cases um unlike web hooks which require you to run an external service um these policies

### Excerpt da transcript

okay uh hey everyone Welcome to our talk Rogue no more securing kubernetes with not specific restrictions um yeah um yeah thanks for coming I'm James monley I'm a software engineer in the open engineering um department at Apple and I'm Anish I'm a software engineer at Microsoft working on security I am a member of kuber seot and maintainer for Secret store CSI driver yeah so so I guess bit of background on um kind of this whole problem space so in kubernetes uh like you probably already aware nodes have a required set of permissions they need to interact with different resources they need to um you know take actions and they go and create make changes on the Node that they're running um accordingly so the one thing we haven't really got a good solution for or we haven't um really thought much about is you know what stops one node modifying another node's objects so the kubernetes project did Rec this um a few years back well sorry I should jump in the Cubit um has got to manage all these different objects so you've got pods nodes persistent volume claims and this is kind of all through the life cycle of starting up your workload so um included in there although not listed on here is things like Secrets config Maps very sensitive information um additionally like if you think about it if one node could go and modify another this is a really good attack Vector for one um for one uh for for attacker to kind of get from a node that they've managed to break into into a more secure place you might have different like taints tolerations and things to only run your really super sensitive uh workloads only on your specific node pool but via the API server you could Traverse get onto the next node onto the next node until you're kind of getting yourself a cluster admin super privileged uh token which is not great so this was recognized a while back um and the cubet has actually already got a solution for parts of this um and that's in the node restriction admission plug-in has anyone heard of that before yeah a few okay um so yeah this this uh admission plugin actually restricts nodes so that they can only modify or access uh resources that are relevant to them so by relevant here I mean um like if the Pod that well if you're trying to access a secret then must be a pod scheduled to that node that uh that actually references that secret and that stopped you just being able to kind of go off and grab a random thing this wasn't always the case for a while you know cube
