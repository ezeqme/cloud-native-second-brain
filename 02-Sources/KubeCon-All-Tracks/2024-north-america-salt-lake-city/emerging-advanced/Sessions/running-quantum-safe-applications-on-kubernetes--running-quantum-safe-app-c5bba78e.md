---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Paul Schweigert", "Michael Maximilien", "IBM Quantum"]
sched_url: https://kccncna2024.sched.com/event/1i7nn/running-quantum-safe-applications-on-kubernetes-paul-schweigert-michael-maximilien-ibm-quantum
youtube_search_url: https://www.youtube.com/results?search_query=Running+Quantum-Safe+Applications+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Running Quantum-Safe Applications on Kubernetes - Paul Schweigert & Michael Maximilien, IBM Quantum

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Paul Schweigert, Michael Maximilien, IBM Quantum
- Schedule: https://kccncna2024.sched.com/event/1i7nn/running-quantum-safe-applications-on-kubernetes-paul-schweigert-michael-maximilien-ibm-quantum
- Busca YouTube: https://www.youtube.com/results?search_query=Running+Quantum-Safe+Applications+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Running Quantum-Safe Applications on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nn/running-quantum-safe-applications-on-kubernetes-paul-schweigert-michael-maximilien-ibm-quantum
- YouTube search: https://www.youtube.com/results?search_query=Running+Quantum-Safe+Applications+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6eQA15r6IHY
- YouTube title: Running Quantum-Safe Applications on Kubernetes - Paul Schweigert & Michael Maximilien, IBM Quantum
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/running-quantum-safe-applications-on-kubernetes/6eQA15r6IHY.txt
- Transcript chars: 35892
- Keywords: quantum, cryptography, actually, question, little, computer, computers, problems, client, across, laptop, numbers, course, algorithms, internet, cluster, postquantum, application

### Resumo baseado na transcript

I'm Max and this is Paul my colleague and we're from IBM research and we're going to talk to you about how to run Quantum safe application especially for kubernetes so we've been uh experimenting in that space for a while obviously IBM has a big Quantum uh division we're actually part of that division but we're also doing um AI which is kind of weird why we doing AI in Quantum well there's good reasons we're not going to talk about that but of course ask question later if

### Excerpt da transcript

I'm Max and this is Paul my colleague and we're from IBM research and we're going to talk to you about how to run Quantum safe application especially for kubernetes so we've been uh experimenting in that space for a while obviously IBM has a big Quantum uh division we're actually part of that division but we're also doing um AI which is kind of weird why we doing AI in Quantum well there's good reasons we're not going to talk about that but of course ask question later if you're interested so this is who we are there's a lot to cover I'm going to do the first part which is sort of the basics of quantum Computing uh the what we're doing in Quantum safe why you want to be Quantum safe and then I'll pass it to Paul who's going to do the hard report where he's going to talk about how we took our platform our quum platform uh so if you go to ibm.com Quantum we have a platform that you can actually use right now and it's obviously running on kubernetes for the uh Services parts and we converted that or we made it quantum safe so he's going to go into the details of that so hopefully that gives you a complete overview so with that let's get started so this is the agenda right understanding the risk becoming Quantum safe and what you can do like the open source stuff that we're doing we're very excited about that and uh of course the protecting applications next steps so let's let's get started so why Quantum right which is kind of the first thing I I think the way to remember I don't know how many of you have have seen the movie Imitation games you know a little bit so that goes with the that that tries to retrace a lot of things but one of the main character there is the father of computer science right on entering uh and he helps save the world he's amazing but I think one of the things to remember in that movie is that he actually built a computer and if you remember the computer they built was using uh vacuum tubes we're kind of in that stage for Quantum Computing so we understand the theory obviously not Alan uh Alan tring that created that so there's lots of research that created sort of the quantum theory but we're building the computers now uh so it's kind of similar in terms of in your mind but why Quantum Computing right compared to like say biological Computing or the ones that we know right now which are sort of like the classical touring uh computers so it gets you into a little bit of complexity theory in a sense that you have to understand that com
