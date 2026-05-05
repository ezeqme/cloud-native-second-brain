---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Boaz Michaely", "Red Hat", "Adi Sosnovich", "IBM Research"]
sched_url: https://kccncna2025.sched.com/event/27FUs/demonstration-of-automatic-kubernetes-network-policies-generation-boaz-michaely-red-hat-adi-sosnovich-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=Demonstration+of+Automatic+Kubernetes+Network+Policies+Generation+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Demonstration of Automatic Kubernetes Network Policies Generation - Boaz Michaely, Red Hat & Adi Sosnovich, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Boaz Michaely, Red Hat, Adi Sosnovich, IBM Research
- Schedule: https://kccncna2025.sched.com/event/27FUs/demonstration-of-automatic-kubernetes-network-policies-generation-boaz-michaely-red-hat-adi-sosnovich-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=Demonstration+of+Automatic+Kubernetes+Network+Policies+Generation+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Demonstration of Automatic Kubernetes Network Policies Generation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FUs/demonstration-of-automatic-kubernetes-network-policies-generation-boaz-michaely-red-hat-adi-sosnovich-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=Demonstration+of+Automatic+Kubernetes+Network+Policies+Generation+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MD9f9Y-kems
- YouTube title: Demonstration of Automatic Kubernetes Network Policies Generation - Boaz Michaely & Adi Sosnovich
- Match score: 0.903
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/demonstration-of-automatic-kubernetes-network-policies-generation/MD9f9Y-kems.txt
- Transcript chars: 28302
- Keywords: network, policies, policy, allowed, question, connectivity, connections, ingress, application, connection, analysis, analyze, namespace, denied, understand, actually, default, generate

### Resumo baseado na transcript

I'm from IBM research working on open source projects for cloud networking resources. And today we're going to talk about Kubernetes network policies, the challenges and present and demonstrate as promised a analytica solution that was developed by the IBM research team on a project called NPARD. So, way back in 2017, the community developed this specification for Kubernetes network policies, which is a pod level firewall that allows you to restrict pod level communication. It's easy to get lost without tooling and there is no tooling built into Kubernetes or open shift for that matter. We've run this demo on many many many projects and it typically just works. If you compare this to the demo application, you'll see that it actually looks pretty similar.

### Excerpt da transcript

Right, good morning and welcome. My name is Boaz. I'm a product manager with Red Hat ACS team and with me is Adi. >> Hi, I'm Adi. I'm from IBM research working on open source projects for cloud networking resources. And today we're going to talk about Kubernetes network policies, the challenges and present and demonstrate as promised a analytica solution that was developed by the IBM research team on a project called NPARD. We integrated it into stack rocks redat ACS and we're going to show you how that works and at the end will actually um show you a comparison that she did recently because this was developed like a year ago. How does that compete with AI to tools or other can AI do the job? Um, so before we jump in just uh well, if you're here, you probably know something about Kubernetes network policies, but how many people are would say they're familiar with network policies? Terrific. Well, thanks for coming. Well, we'll just do a quick reminder. Even if you've been working on this for a while, it's often that you need a reminder.

But for the people who are not on the day-to-day, Kubernetes was designed to be simple. As part of that, it was decided all communication is allowed just to get to work. Very very quickly, it was realized by the community that this presents a significant security threat. Without data segmentation, with no limits, you're more exposed to data leakage, unauthorized access. Obviously, it makes it easier for lateral movement, penetrate a pod, jump to the other, denial of service attacks. So, way back in 2017, the community developed this specification for Kubernetes network policies, which is a pod level firewall that allows you to restrict pod level communication. It's implemented by the CNI plug-in as opposed to the Kubernetes core. Now, the concept of the network policy model is it focuses on the pod. It is a namespace resource. It talks about what do I want to allow my pod to do. I can specify for TCP, UDP and SCTP which ports I allow for ingress and which I allow for egress. And the source and destination are specified for a port, a uh a namespace or a port, sorry, a pod or a namespace or a pod in a namespace.

The specification also allows you to talk about external communications with IP ranges somewhat limited but some capabilities are there. So if you look at the concepts that network policy introduces is there's first the question of scoping. So the policy scope is done through a selector. As I just mentioned, the pol
