---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Marius Tanawa Tsamo", "Gustav Rasmussen", "Novo Nordisk"]
sched_url: https://kccnceu2025.sched.com/event/1tx9b/empowering-ai-driven-drug-discovery-overcoming-challenges-in-building-a-ml-platform-on-kubernetes-marius-tanawa-tsamo-gustav-rasmussen-novo-nordisk
youtube_search_url: https://www.youtube.com/results?search_query=Empowering+AI-Driven+Drug+Discovery%3A+Overcoming+Challenges+in+Building+a+ML+Platform+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Empowering AI-Driven Drug Discovery: Overcoming Challenges in Building a ML Platform on Kubernetes - Marius Tanawa Tsamo & Gustav Rasmussen, Novo Nordisk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Marius Tanawa Tsamo, Gustav Rasmussen, Novo Nordisk
- Schedule: https://kccnceu2025.sched.com/event/1tx9b/empowering-ai-driven-drug-discovery-overcoming-challenges-in-building-a-ml-platform-on-kubernetes-marius-tanawa-tsamo-gustav-rasmussen-novo-nordisk
- Busca YouTube: https://www.youtube.com/results?search_query=Empowering+AI-Driven+Drug+Discovery%3A+Overcoming+Challenges+in+Building+a+ML+Platform+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Empowering AI-Driven Drug Discovery: Overcoming Challenges in Building a ML Platform on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9b/empowering-ai-driven-drug-discovery-overcoming-challenges-in-building-a-ml-platform-on-kubernetes-marius-tanawa-tsamo-gustav-rasmussen-novo-nordisk
- YouTube search: https://www.youtube.com/results?search_query=Empowering+AI-Driven+Drug+Discovery%3A+Overcoming+Challenges+in+Building+a+ML+Platform+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FC5TAGsBbRQ
- YouTube title: Empowering AI-Driven Drug Discovery: Overcoming Challenges... Marius Tanawa Tsamo & Gustav Rasmussen
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/empowering-ai-driven-drug-discovery-overcoming-challenges-in-building/FC5TAGsBbRQ.txt
- Transcript chars: 23325
- Keywords: gpu, platform, course, sitting, cluster, workload, models, hardware, basically, inference, already, called, research, working, gravity, nvidia, discovery, company

### Resumo baseado na transcript

Hello and welcome to our presentation about extending kubernetus with AI capabilities. My name is Costto Rasmusen and I'm joined by my colleague Mario Tanava. Luckily, AI is very capable of scanning massive amounts of data, and it's starting to overtake the best human performance across a number of areas such as image recognition, language understanding, and reading comprehension in more and more being added to the list. So, in fact, it's a must-win battle for us to efficiently adopt and scale out AI to the entire company. we can predict the three-dimensional structure of a protein and then there are things in between such as forecasting models or chatbots and each of the steps in the spectrum comes with its own unique challenges in terms of hosting adding connectivity compute data etc We work with them typically in shorter twoe hackathons or rapid uh iteration sprints and deliver for them the state-of-the-art infrastructure to scale out AI.

### Excerpt da transcript

Hello and welcome to our presentation about extending kubernetus with AI capabilities. My name is Costto Rasmusen and I'm joined by my colleague Mario Tanava. He's our senior platform engineer and I'm tech lead of our containerization team at Novanorisk research and development. We'll begin with a quick look at the agenda. I will introduce you to the company and how AI is relevant for us. Then dive a bit into our technical foundation of container images and some data perspectives. Then I will hand over to Marios who will tell you more about Geon the new exciting AI supercomputer based in Denmark that's currently ranked the 21st in the world based on the global 500 ranking. Marios will tell you about user journeys, challenges we encountered, and solutions we came up with. And then we'll round off taking a quick look into the future and some questions at the end. So, who are we and how can we benefit from AI? We are a large pharmaceutical company that specialize in treating diabetes and obesity, but also other therapy areas such as non-alcoholic, fatty liver, chronic kidney disease, cardiovascular disease, and some brain disorders, Parkinson and Alzheimer.

We also treat some more rare endocrine and bleeding disorders such as hemophilia. And as IT professionals, we are then building the technological platforms to enable our researchers to innovate and improve on these uh treatments. We have a global organization with expertise and knowledge across the entire farmer value chain. Several of our sites operate as transformational research units being semiautonomous in relation to the global R&D organization. This allows them to make datadriven decisions quickly and focus their efforts on research. Data is growing rapidly globally at an exponential pace. It's shown here annually in settans to go through. Luckily, AI is very capable of scanning massive amounts of data, and it's starting to overtake the best human performance across a number of areas such as image recognition, language understanding, and reading comprehension in more and more being added to the list. So, in fact, it's a must-win battle for us to efficiently adopt and scale out AI to the entire company.

And AI of course exists on a spectrum from very commonly available or citizen AI things like chat GBT or co-pilot that we all love working with daily for text summarization code generation and much more other end of the spectrum however in research we have very hetrogeneous data and due to this very
