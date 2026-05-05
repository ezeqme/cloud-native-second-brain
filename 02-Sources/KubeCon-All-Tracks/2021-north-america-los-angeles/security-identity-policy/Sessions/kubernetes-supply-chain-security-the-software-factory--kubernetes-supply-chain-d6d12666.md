---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Kubernetes Core"]
speakers: ["Andrew Martin", "Control Plane"]
sched_url: https://kccncna2021.sched.com/event/lUzv/kubernetes-supply-chain-security-the-software-factory-andrew-martin-control-plane
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Supply+Chain+Security%3A+The+Software+Factory+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes Supply Chain Security: The Software Factory - Andrew Martin, Control Plane

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Andrew Martin, Control Plane
- Schedule: https://kccncna2021.sched.com/event/lUzv/kubernetes-supply-chain-security-the-software-factory-andrew-martin-control-plane
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Supply+Chain+Security%3A+The+Software+Factory+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes Supply Chain Security: The Software Factory.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzv/kubernetes-supply-chain-security-the-software-factory-andrew-martin-control-plane
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Supply+Chain+Security%3A+The+Software+Factory+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7CMhIDAPjEs
- YouTube title: Kubernetes Supply Chain Security: The Software Factory - Andrew Martin, Control Plane
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-supply-chain-security-the-software-factory/7CMhIDAPjEs.txt
- Transcript chars: 30443
- Keywords: software, supply, security, attack, course, infrastructure, malicious, signing, difficult, control, server, factory, running, reverse, looking, package, privileged, actually

### Resumo baseado na transcript

I'm very pleased to see people uh in person as opposed to on the other side of some amorphous internet screen. Um we're going to talk about the software factory today, some supply chain fun, and uh yeah, thank you for coming to my talk in advance. Then we will look concretely at how to attack a couple of different supply chains, specifically um at install time for a package, and secondarily, if I can get malicious code running in your Kubernetes clusters, what can I do? There was a supply chain security con on Monday, six security or tag security as they are now ran the security day yesterday. In the Kubernetes world, everything is declarative, and therefore, we can define what a good baseline state looks like and test it. Artifacts, the the um actual deployment into clouds that we're that we're doing into some of those platforms, all the way through infrastructure, and especially our security and NFRs.

### Excerpt da transcript

Hello, good morning, and welcome. I'm very pleased to see people uh in person as opposed to on the other side of some amorphous internet screen. Um we're going to talk about the software factory today, some supply chain fun, and uh yeah, thank you for coming to my talk in advance. So, Kubernetes supply chain security, the software factory, aka who is afraid of the big bad supply chain. Hi, I'm Andy. I'm from Control Plane. We are a cloud-native security consultancy. We have audit, pen test, and engineering capabilities, and I have a wonderful team. Uh I've I've done lots of development. That's kind of where the background comes from. Security is a steep passion, and operations, of course, is necessary as the strong baseline on which which to build solid security engineering practices. I am very lucky to have had the opportunity to write SANS SEC584, attacking and defending containers and Kubernetes uh with my preeminent co-author, Mr. Michael Hassonblass. I have written the book Hacking Kubernetes. It has gone into print today.

It will be available on ebook by the end of the week. It's already available on early access, and uh yeah, huge thanks to Michael. It is a step-by-step guide to attacking, defending, and ultimately securely deploying Kubernetes um for regulated environments and everywhere else. And today, we are going to talk about the supply chain. What is it? Why is it a problem? Then we will look concretely at how to attack a couple of different supply chains, specifically um at install time for a package, and secondarily, if I can get malicious code running in your Kubernetes clusters, what can I do? We will look at signing. Signing is the fated mechanism by which to fix all these things. Signing is easy, verification is hard, and finally, draw everything together with the software factory pattern. The panacea? Potentially not, but certainly a useful advancement in our journey. There has been so much chat about the supply chain already at KubeCon. There was a supply chain security con on Monday, six security or tag security as they are now ran the security day yesterday.

And there's so much going on in the ecosystem right now. We're really moving forward after a difficult, I guess, kind of uh few years of stasis as we build out new package managers, and kind of since OCI existed. So, there is a lot here. I will be referencing other talks throughout. So, what is a supply chain? It is anything that we depend upon. In a military context, this cou
