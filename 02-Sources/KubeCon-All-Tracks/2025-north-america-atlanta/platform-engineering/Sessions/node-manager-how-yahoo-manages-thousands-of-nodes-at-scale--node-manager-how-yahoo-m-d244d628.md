---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Payal Patel", "Yahoo"]
sched_url: https://kccncna2025.sched.com/event/27Fad/node-manager-how-yahoo-manages-thousands-of-nodes-at-scale-payal-patel-yahoo
youtube_search_url: https://www.youtube.com/results?search_query=Node+Manager+-+How+Yahoo+Manages+Thousands+of+Nodes+at+Scale%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Node Manager - How Yahoo Manages Thousands of Nodes at Scale? - Payal Patel, Yahoo

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Payal Patel, Yahoo
- Schedule: https://kccncna2025.sched.com/event/27Fad/node-manager-how-yahoo-manages-thousands-of-nodes-at-scale-payal-patel-yahoo
- Busca YouTube: https://www.youtube.com/results?search_query=Node+Manager+-+How+Yahoo+Manages+Thousands+of+Nodes+at+Scale%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Node Manager - How Yahoo Manages Thousands of Nodes at Scale?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fad/node-manager-how-yahoo-manages-thousands-of-nodes-at-scale-payal-patel-yahoo
- YouTube search: https://www.youtube.com/results?search_query=Node+Manager+-+How+Yahoo+Manages+Thousands+of+Nodes+at+Scale%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_kAI0qEuoFA
- YouTube title: Node Manager - How Yahoo Manages Thousands of Nodes at Scale? - Payal Patel, Yahoo
- Match score: 0.946
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/node-manager-how-yahoo-manages-thousands-of-nodes-at-scale/_kAI0qEuoFA.txt
- Transcript chars: 40590
- Keywords: maintenance, upgrade, cluster, simply, perform, status, resource, remediation, custom, action, controller, administrator, worker, remedy, running, operator, sometimes, detector

### Resumo baseado na transcript

I'm a principal software development engineer working for core infrastructure team at Yahoo. How Yahoo manages thousands of node at scale on Kubernetes ecosystem on prem. And as a cluster administrator I have a need where I want to perform OS upgrade, firmware upgrade, Kubernetes version upgrade and maybe any security fix is coming on the way. So it's a Kubernetes operator helps us to manage or maintain this maintenance related task automatically. So as I mentioned earlier node mentor is a Kubernetes operator like any other Kubernetes operator. And third one is the node agent which runs on each and every Kubernetes worker node and actually helps you to execute that targeted maintenance task.

### Excerpt da transcript

I am pile Patel. I'm a principal software development engineer working for core infrastructure team at Yahoo. And topic for today's presentation is node manager. How Yahoo manages thousands of node at scale on Kubernetes ecosystem on prem. Here is a brief agenda for uh today's presentation where we'll go over node maintenance/ node manager architecture followed by node auto remediation. We will go into details of some metrics and visualization related to it and we'll conclude with the major key takeaways from this. So before I get started I want to give you brief introduction to Yahoo's journey into Kubernetes. Yahoo started its journey into Kubernetes almost a decade ago and with that today we have 35 plus Kubernetes cluster which contains about 8,000 plus physical host and we are running 2400 plus application live in production recently we also embarked our journey into cloud as well with that we have 35 plus EKS clusters and 16 plus GK cluster which also contains about thousand plus nodes So I just mentioned we have 8,000 plus physical host.

Now managing these nodes can be quite errorprone and timeconuming and it can be quite daunting as well and there are some challenges related to it. And as a cluster administrator I have a need where I want to perform OS upgrade, firmware upgrade, Kubernetes version upgrade and maybe any security fix is coming on the way. you just want to apply that on your entire clusters. Now managing this kind of task manually can be time consuming and errorprone at the same time as well. In addition to that, we needed some solution which is network aware as well. So how do we solve this? We came up with a node maintainer/node manager. What is node manager? It's a Kubernetes operator. Some of the folks we were just sitting in the previous session there that was a deep dive into the what is operator. So it's a Kubernetes operator helps us to manage or maintain this maintenance related task automatically. Not only it helps us to perform this automatically it does in a controlled fashion meaning that as a cluster administrator I want to ensure that while I perform this maintenance live in production we want to maintain the healthy cluster capacity at any given time.

And while we were building this we had top three requirements in our mind. First is that as a cluster administrator the operator should have a cap should have a capability where I can provide list of nodes on which I want to perform the maintenance task. It should allow
