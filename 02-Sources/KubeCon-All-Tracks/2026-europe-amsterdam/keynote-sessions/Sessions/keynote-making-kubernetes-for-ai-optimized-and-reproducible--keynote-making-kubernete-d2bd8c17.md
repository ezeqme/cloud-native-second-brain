---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Nathan Taber", "Director of Product", "NVIDIA", "Mark Chmarny", "Sr. Principal Engineer", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2Ioch/keynote-making-kubernetes-for-ai-optimized-and-reproducible-nathan-taber-director-of-product-nvidia-mark-chmarny-sr-principal-engineer-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Making+Kubernetes+for+AI+Optimized+and+Reproducible+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Keynote: Making Kubernetes for AI Optimized and Reproducible - Nathan Taber, Director of Product, NVIDIA & Mark Chmarny, Sr. Principal Engineer, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nathan Taber, Director of Product, NVIDIA, Mark Chmarny, Sr. Principal Engineer, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2Ioch/keynote-making-kubernetes-for-ai-optimized-and-reproducible-nathan-taber-director-of-product-nvidia-mark-chmarny-sr-principal-engineer-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Making+Kubernetes+for+AI+Optimized+and+Reproducible+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Keynote: Making Kubernetes for AI Optimized and Reproducible.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2Ioch/keynote-making-kubernetes-for-ai-optimized-and-reproducible-nathan-taber-director-of-product-nvidia-mark-chmarny-sr-principal-engineer-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Making+Kubernetes+for+AI+Optimized+and+Reproducible+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RsF1-Jt-2G8
- YouTube title: Keynote: Making Kubernetes for AI Optimized and Reproducible - Nathan Taber & Mark Chmarny
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/keynote-making-kubernetes-for-ai-optimized-and-reproducible/RsF1-Jt-2G8.txt
- Transcript chars: 6368
- Keywords: cluster, recipe, recipes, nvidia, components, bundle, across, values, provide, optimized, number, gpu, training, validate, actual, conformance, actually, configuration

### Resumo baseado na transcript

I'm Nathan Taber and I'm joined with Mark Smalley and we are both building Kubernetes at Nvidia. And so we we're really interested in how can we make Kubernetes easier to run for AI? One of the responsibilities of the team that Mark and I work on is to not just help make Kubernetes better, but also to run the accelerated Kubernetes infrastructure for all of the different workloads that Nvidia does that span from world model and simulation building all the way to robotics. validations that demonstrate or validate the actual cluster once the recipe is deployed on a cluster spanning from everything from the actual components and their readiness all the way to a CNCF AI conformance readiness. And because ACRE encodes the entire graph of that knowledge inside of the binary, you can actually query that graph in real time in your CI/CD pipeline without connection to the outside world. And we're excited to work with hyperscalers, AI clouds, developers, and users to add new recipes and new capabilities into ACRE across all types of different environments.

### Excerpt da transcript

I I think this is my favorite event of the year. I'm Nathan Taber and I'm joined with Mark Smalley and we are both building Kubernetes at Nvidia. And so we we're really interested in how can we make Kubernetes easier to run for AI? When we look out across the community, we've been doing a number of investments across Nvidia. We've been working at projects like the DRA driver, the GPU operator, Kai scheduler. A few moments ago Aaron was talking about all the work that Nvidia has been investing in and we know when we look at GPU accelerated that these things are just the start. When you go and you stand up an AI cluster for Kubernetes, you have to install all of these components in your cluster and more. And we know that installation is just the beginning. So when you go ahead and you want to do let's say a workload on EKS with an H100 accelerator and you add in your operating system, let's say Ubuntu and then you say you're going to do training. There's over 250 different configuration values that you have to make across 15 plus components.

And then let's say you want to change, you want to go from training to inference. Well, that's swapping out five components and additional 40 plus configuration values. And so there's a lot of work that you have to do to manage and make an optimally tuned cluster to run AI. And so what we've been doing at Nvidia, we we feel this pain every single day. One of the responsibilities of the team that Mark and I work on is to not just help make Kubernetes better, but also to run the accelerated Kubernetes infrastructure for all of the different workloads that Nvidia does that span from world model and simulation building all the way to robotics. And we've realized that these tuning and this optimal configuration is locked behind the walls at Nvidia and we want to open that up and we want to bring the community in. And so we're proud to introduce this project AI cluster runtime which brings our knowledge about how to configure AI clusters for GPU training and inference into machine readable recipes.

And so I'm going to turn it over to Mike, he's going to talk to you Mark. He's going to talk to you a little bit about how ACRE works. >> [laughter] >> I'm Mark. Hi. So like Nathan was talking about these recipes, they represent a very validated, optimized, and reproducible set of knowledge that we've acquired over many years and wanted to share with the with the rest of the community. These recipes represent a set of components t
