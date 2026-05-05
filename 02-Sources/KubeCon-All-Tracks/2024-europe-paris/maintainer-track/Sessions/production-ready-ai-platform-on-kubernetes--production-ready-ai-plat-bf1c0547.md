---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core", "Community Governance"]
speakers: ["Yuan Tang", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YhjF/production-ready-ai-platform-on-kubernetes-yuan-tang-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Production-Ready+AI+Platform+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Production-Ready AI Platform on Kubernetes - Yuan Tang, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Yuan Tang, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YhjF/production-ready-ai-platform-on-kubernetes-yuan-tang-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Production-Ready+AI+Platform+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Production-Ready AI Platform on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhjF/production-ready-ai-platform-on-kubernetes-yuan-tang-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Production-Ready+AI+Platform+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_RthQ01bwU8
- YouTube title: Production-Ready AI Platform on Kubernetes - Yuan Tang, Red Hat
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/production-ready-ai-platform-on-kubernetes/_RthQ01bwU8.txt
- Transcript chars: 28457
- Keywords: training, models, learning, machine, distributed, platform, native, workflow, frameworks, production, especially, basically, supports, working, cluster, tuning, serving, consider

### Resumo baseado na transcript

how's everyone doing I'm surprised that the room is still occupied at one of the last talks thank you for sticking around and I hope you are enjoying the week so let's get started is the recording on okay first of all let me introduce myself my name is Yen and I'm a principal engineer at red hat and I just joined red hat at about 3 months ago and I I'm also a a project lead for Argo and cflow and today I'm going to talk about production ready

### Excerpt da transcript

how's everyone doing I'm surprised that the room is still occupied at one of the last talks thank you for sticking around and I hope you are enjoying the week so let's get started is the recording on okay first of all let me introduce myself my name is Yen and I'm a principal engineer at red hat and I just joined red hat at about 3 months ago and I I'm also a a project lead for Argo and cflow and today I'm going to talk about production ready AI platform on kubernetes so today's agenda uh first I'll be talking about the AI landcape and ecosystem and I'll be talking about some of the elements to consider for production Readiness when you are building building an AI platform on kubernetes keep in mind that this won't be an exhaustive list as there are obviously many other things to consider in production especially when dealing with kubernetes and Cloud native Technologies and at the very last end I'll be talking about a reference platform using some of the Tex Stacks uh that um and uh for different components uh so I'd like to spend a few moment to introduce my book that's recently released uh this this year called distributed machine learning patterns so each will talk about different patterns that's involved when building a large scale distributed machine Learning System and at the very last section of the book it will also talk about a reference implementation um that provides an opportunity for readers to build a u a real life production level machine Learning System uh hands on and take a moment to scan the QR code if you're interested in learning more about the book okay let's dive into the content so uh the AI landscape and ecosystem is getting larger and L larger uh especially since the uh the birth of the large language models and GPT type of models before that it may be known as statistics data science or machine learning deep learning now the all the words are getting blur and blury and there are here are the two uh screenshots one is from the Linux Foundation Ai and data uh uh the second one is from cncf it has a larger scope but it also contains categories for machine learning and AI definitely check out the links uh for this two landscape if you want to learn more about it and if you ever missed uh priyanka's opening keynote she also me mentioned uh she also has a nice uh picture of the landscape uh for AI related projects in the ecosystem yeah definitely worth checking out and here are just some example projects that are used very frequently
