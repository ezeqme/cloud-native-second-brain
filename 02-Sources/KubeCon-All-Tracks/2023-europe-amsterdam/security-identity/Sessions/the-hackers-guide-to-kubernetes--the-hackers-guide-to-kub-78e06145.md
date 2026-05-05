---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Kubernetes Core"]
speakers: ["Patrycja Wegrzynowicz", "Form3"]
sched_url: https://kccnceu2023.sched.com/event/1HyYW/the-hackers-guide-to-kubernetes-patrycja-wegrzynowicz-form3
youtube_search_url: https://www.youtube.com/results?search_query=The+Hacker%27s+Guide+to+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Hacker's Guide to Kubernetes - Patrycja Wegrzynowicz, Form3

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Patrycja Wegrzynowicz, Form3
- Schedule: https://kccnceu2023.sched.com/event/1HyYW/the-hackers-guide-to-kubernetes-patrycja-wegrzynowicz-form3
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hacker%27s+Guide+to+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Hacker's Guide to Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYW/the-hackers-guide-to-kubernetes-patrycja-wegrzynowicz-form3
- YouTube search: https://www.youtube.com/results?search_query=The+Hacker%27s+Guide+to+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Hf5qRgxjPLQ
- YouTube title: The Hacker's Guide to Kubernetes - Patrycja Wegrzynowicz, Form3
- Match score: 0.769
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-hackers-guide-to-kubernetes/Hf5qRgxjPLQ.txt
- Transcript chars: 18941
- Keywords: basically, security, server, application, cluster, another, cubelet, available, however, number, usually, better, remote, access, command, running, workload, simple

### Resumo baseado na transcript

hello everyone fantastic to be here even better to stitch it to see such an awesome audience I'm really impressed and scared my name is Patricia and today we are gonna explore live kubernetes hacking together so get ready for ride first a brief introduction I've been doing professional software development for over 20 years yep sometimes I do feel like a vintage dinosaur but hey who doesn't love a classic I've always been close to cold and that Bond still arrives today however almost two years ago I joined

### Excerpt da transcript

hello everyone fantastic to be here even better to stitch it to see such an awesome audience I'm really impressed and scared my name is Patricia and today we are gonna explore live kubernetes hacking together so get ready for ride first a brief introduction I've been doing professional software development for over 20 years yep sometimes I do feel like a vintage dinosaur but hey who doesn't love a classic I've always been close to cold and that Bond still arrives today however almost two years ago I joined the Dark Side of platform engineering at form three and guess what I absolutely loved it today I'm a lead SRE engineer though so what do we do at form three in short form free is a financial cloud we provide a payment as a platform model for quick and easy integration with various payment schemes via rest API we are technology oriented poly remote cloud-based with microservices architectures we trade our infrastructure as code almost religiously terraforming everything possible lately we are building a new multi-cloud payment platform based on kubernetes and free clouds so obviously kubernetes kubernetes security is super important to us what am I gonna talk about today just a splash of theory in the ocean of practice the key part of today's talk features two demos to hijack your accounts exploiting various security issues in auburnities application as well as in cluster but before the fun begins let's do a quick review of the kubernetes architecture there's two main Concepts in kubernetes the control plane and worker nodes the control plane basically manages the entire cluster the heart here is an API server and when we want to create or update any kubernetes resource we need to communicate with that server it exposes a kubernetes HTTP API that way we can interact with the cluster using tools like Cube CTL and who doesn't know Cube CTL worker nodes are the place where the real work happens the actual Parts run over there cubelet is a main component responsible for instantiation and execution of parts and like the API server cubelet also exposes a rest API but it's only like internal API however sneak peek we will exploit an unsecured cubelet API to gain unauthorized access to the cluster what other kind of security issues can we see in our case clusters it oops sorry [Applause] yeah hopefully it won't happen again but you never know fingers crossed and we were just at our slide so nope it's not gonna work that way um okay so it's time to dive into our t
