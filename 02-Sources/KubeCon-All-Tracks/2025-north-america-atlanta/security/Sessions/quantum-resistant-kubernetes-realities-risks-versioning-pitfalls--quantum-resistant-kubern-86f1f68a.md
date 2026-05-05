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
themes: ["Security", "Kubernetes Core"]
speakers: ["Fabian Kammel", "ControlPlane"]
sched_url: https://kccncna2025.sched.com/event/27FZK/quantum-resistant-kubernetes-realities-risks-versioning-pitfalls-fabian-kammel-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Quantum-Resistant+Kubernetes%3A+Realities%2C+Risks+%26+%28Versioning%29+Pitfalls+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Quantum-Resistant Kubernetes: Realities, Risks & (Versioning) Pitfalls - Fabian Kammel, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Fabian Kammel, ControlPlane
- Schedule: https://kccncna2025.sched.com/event/27FZK/quantum-resistant-kubernetes-realities-risks-versioning-pitfalls-fabian-kammel-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Quantum-Resistant+Kubernetes%3A+Realities%2C+Risks+%26+%28Versioning%29+Pitfalls+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Quantum-Resistant Kubernetes: Realities, Risks & (Versioning) Pitfalls.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZK/quantum-resistant-kubernetes-realities-risks-versioning-pitfalls-fabian-kammel-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Quantum-Resistant+Kubernetes%3A+Realities%2C+Risks+%26+%28Versioning%29+Pitfalls+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3yOwAIpbuQ0
- YouTube title: Quantum-Resistant Kubernetes: Realities, Risks & (Versioning) Pitfalls - Fabian Kammel, ControlPlane
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/quantum-resistant-kubernetes-realities-risks-versioning-pitfalls/3yOwAIpbuQ0.txt
- Transcript chars: 20785
- Keywords: quantum, algorithms, algorithm, signatures, security, exchange, crypto, postquantum, called, computer, actually, client, public, computers, interesting, basically, cryptography, against

### Resumo baseado na transcript

Um I'm excited to talk to you about um quantum resistant Kubernetes uh realities especially risks and versioning pitfalls. Um I've worked before as a trainer for Kubernetes and container security. I want you to understand the challenges we face today as we progress towards postquantum secure algorithms and cryptography. And I want you to understand the risks we face today and then learn how to mitigate them down the road. Um, if you're looking to learn about quantum algorithms or quantum c computer internals, I'm sorry that's not the talk for you. This is all taken care of by the um implementers of the libraries and you as the end user need to know about the trade-offs these these algorithms have right what are they good at all right if you want to learn more about quantum

### Excerpt da transcript

Welcome everyone. Um I'm excited to talk to you about um quantum resistant Kubernetes uh realities especially risks and versioning pitfalls. So my name is Fabian. I'm a principal security consultant at control plane. Um I've worked before as a trainer for Kubernetes and container security. So for CKS for example uh security engineer we built like a confidential Kubernetes distribution and I was also guest on the Kubernetes podcast on confidential computing for example just to establish the credibilities here. Um who are we? We're control plane as I said we're a security consultancy headquartered in London but we're distributed um all over the world. So, if you need help with anything from postquantum crypto to Kubernetes or in between, um, let us know. We can we can help you out. And we're also running the CTF event downstairs right now. I just sprinted up the stairs 5 minutes ago. So, if you ever want to attack a vulnerable Kubernetes cluster, you can come with me downstairs. We will hook you up with access to a cluster and you can start working on it.

All right. So, quantum computing. What is quantum computing? Um, classical computers, the ones we use today, they work on discrete binary data, right? Bits and bytes as you know. Quantum computers on the other hand, they use quantum superposition inference and entanglement for the computations. So things that happen in in nature, in the real world, I guess. Um, and that's also why they excel at simulating nature, right? We're looking forward to using them for interesting things like biology, physics, chemistry. Basically simulating the real world and gaining some insights from that. But they also have one superstar which is called Shor's algorithm. And if we believe I mean it it not no belief it is so that it breaks cryptography we use today and a consequence it it breaks the internet and the world as we know it. So yeah panic. Uh, China breaks RSA encryption already. I'm not sure like how we're still doing internet banking and everything. Oh, yeah. If you read the articles, uh, it's 22bit RSA. Nice. No one no one will care.

Uh, today. All right. So, the goals for today are like the overview of the postquantum cryptography landscape, right? I want to provide you with enough actual information so you can read these articles and judge whether there is a risk and whether you need to become active. I want you to understand the challenges we face today as we progress towards postquantum secure algorithms and c
