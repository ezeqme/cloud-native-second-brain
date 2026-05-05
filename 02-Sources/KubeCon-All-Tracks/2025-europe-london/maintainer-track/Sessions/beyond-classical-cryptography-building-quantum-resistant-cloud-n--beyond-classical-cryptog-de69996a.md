---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Andrés Vega", "M42", "Hugo Landau", "Messier42"]
sched_url: https://kccnceu2025.sched.com/event/1td1H/beyond-classical-cryptography-building-quantum-resistant-cloud-native-infrastructure-with-spiffe-andres-vega-m42-hugo-landau-messier42
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Classical+Cryptography%3A+Building+Quantum-Resistant+Cloud+Native+Infrastructure+With+SPIFFE+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Beyond Classical Cryptography: Building Quantum-Resistant Cloud Native Infrastructure With SPIFFE - Andrés Vega, M42 & Hugo Landau, Messier42

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Andrés Vega, M42, Hugo Landau, Messier42
- Schedule: https://kccnceu2025.sched.com/event/1td1H/beyond-classical-cryptography-building-quantum-resistant-cloud-native-infrastructure-with-spiffe-andres-vega-m42-hugo-landau-messier42
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Classical+Cryptography%3A+Building+Quantum-Resistant+Cloud+Native+Infrastructure+With+SPIFFE+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Beyond Classical Cryptography: Building Quantum-Resistant Cloud Native Infrastructure With SPIFFE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td1H/beyond-classical-cryptography-building-quantum-resistant-cloud-native-infrastructure-with-spiffe-andres-vega-m42-hugo-landau-messier42
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Classical+Cryptography%3A+Building+Quantum-Resistant+Cloud+Native+Infrastructure+With+SPIFFE+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LEiFzJnqU-E
- YouTube title: Beyond Classical Cryptography: Building Quantum-Resistant Cloud Native... Andrés Vega & Hugo Landau
- Match score: 0.874
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/beyond-classical-cryptography-building-quantum-resistant-cloud-native/LEiFzJnqU-E.txt
- Transcript chars: 26776
- Keywords: quantum, algorithms, postquantum, secure, cryptography, actually, exchange, spiffy, computers, crypto, computer, algorithm, systems, future, cryptographic, threat, policy, resistant

### Resumo baseado na transcript

This talk was originally aimed at being sharing our end user story as end users of the project and contributors to Spiffy Inspire. Now, after chatting throughout the conference with different folks throughout the week, we feel there's still a lot of skepticism and lack of understanding, possibly even fear, doubt, and certainty around quantum computers and quantum resistant algorithms. The cubit allows for states like get zero plus get one divided by the square root of two which means it's in a state where both it's zero and one will equal probability and more importantly that property scales. They offer strong security reductions to problems like learning with errors and are built in linear algebra over np heart lattice problems structured as n dimensional grids as you see on the slide. There's a lot of errors during computation and challenges in scaling up this quantum computer systems. But quantum computers aside, if a quantum computer never is realized, what is the value of these algorithms given that there's enough attention to the problem?

### Excerpt da transcript

Thank you for coming out. This talk was originally aimed at being sharing our end user story as end users of the project and contributors to Spiffy Inspire. Now, after chatting throughout the conference with different folks throughout the week, we feel there's still a lot of skepticism and lack of understanding, possibly even fear, doubt, and certainty around quantum computers and quantum resistant algorithms. So we shifted things a little bit last minute to explain some more of the case in the background was the impetus behind it. I will preface with I am not a cryptographer but over the past year working with Hugo and closer to the cryptography community I have come to learn the most dreaded situation for a cryptographer to be in is to have to explain the math of a cris crypto system to a lawyer and why is that math secure? I recently found myself only a couple weeks ago having to explain it to a lawyer myself and to my surprise he was able to grasp it and he hit me back with a great analogy of cy cyber attacks used to be very much like a bank heist against the clock quick frantic loud they only had as much time to like detection meant failure now these attacks have turned a lot like forklift jobs the attacker lifts the entire safe the data, the credentials, the systems and takes it somewhere quiet.

No alarms, no rush, just a slow, methodical decryption and exploitation. A blast open safe does bear a lot of resemblance to unscrambled data from a Kubernetes container. Forward secrecy protects past and future data even if long-term keys are compromised. This is especially critical in systems where confidentiality needs to last for decades, like in healthcare, finance, or defense. While current cryptographic systems are still holding strong, the rise of quantum computers could change that dramatically. Even though we don't have large enough quantum computers yet, the threat is there. A quantum computer operates over cubits. A single ideal cubit exists in a superposition of the basis states of K0 and K one which correspond to the classical binary bytes zero and one. But instead of these being just values, these basis states are actually orthogonal vectors and they form the basis for linear vector space. What that means is a single cubit can express any linear combination of the vectors K0 and K 1.

So let's look at the composition of a cubit which we call phi. We will write this as KFI equals alpha K0 plus beta K 1. Although by definition alpha and beta are
