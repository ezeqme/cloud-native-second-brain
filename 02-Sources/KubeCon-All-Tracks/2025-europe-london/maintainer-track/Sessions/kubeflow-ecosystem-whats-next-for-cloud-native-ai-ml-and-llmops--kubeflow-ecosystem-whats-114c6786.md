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
speakers: ["Johnu George", "Nutanix", "Andrey Velichkevich", "Apple", "Yuki Iwai", "CyberAgent", "Yuan Tang", "Valentina Rodriguez", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1tcz0/kubeflow-ecosystem-whats-next-for-cloud-native-aiml-and-llmops-johnu-george-nutanix-andrey-velichkevich-apple-yuki-iwai-cyberagent-yuan-tang-valentina-rodriguez-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubeflow+Ecosystem%3A+What%E2%80%99s+Next+for+Cloud+Native+AI%2FML+and+LLMOps+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubeflow Ecosystem: What’s Next for Cloud Native AI/ML and LLMOps - Johnu George, Nutanix; Andrey Velichkevich, Apple; Yuki Iwai, CyberAgent; Yuan Tang & Valentina Rodriguez, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Johnu George, Nutanix, Andrey Velichkevich, Apple, Yuki Iwai, CyberAgent, Yuan Tang, Valentina Rodriguez, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1tcz0/kubeflow-ecosystem-whats-next-for-cloud-native-aiml-and-llmops-johnu-george-nutanix-andrey-velichkevich-apple-yuki-iwai-cyberagent-yuan-tang-valentina-rodriguez-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubeflow+Ecosystem%3A+What%E2%80%99s+Next+for+Cloud+Native+AI%2FML+and+LLMOps+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubeflow Ecosystem: What’s Next for Cloud Native AI/ML and LLMOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcz0/kubeflow-ecosystem-whats-next-for-cloud-native-aiml-and-llmops-johnu-george-nutanix-andrey-velichkevich-apple-yuki-iwai-cyberagent-yuan-tang-valentina-rodriguez-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubeflow+Ecosystem%3A+What%E2%80%99s+Next+for+Cloud+Native+AI%2FML+and+LLMOps+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gGP9QdlNr9Y
- YouTube title: Kubeflow Ecosystem: What’s Next for Cloud Native AI/ML and LLMOps
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubeflow-ecosystem-whats-next-for-cloud-native-ai-ml-and-llmops/gGP9QdlNr9Y.txt
- Transcript chars: 27530
- Keywords: training, trainer, actually, exciting, working, components, pipeline, experience, please, create, serving, operator, pipelines, runtime, created, ecosystem, notebooks, inference

### Resumo baseado na transcript

So, today we're going to share you the updates from the ecosystem at what's actually next for cloud native ML. And first of all, I think we'll spend um few minutes to introduce our panelists. You can run these components in any kubernetes cluster whether it's on-prem, third party cloud or local machines. fine-tuning and distributed training kip for model optimization architecture search for large large scale inference and the Qflow pipelines which is stitch all these pieces together also we have a model registry which allows us to store metadata and artifacts and have a sort pluggable So if you want to learn about it, please join their community calls there a lot of exciting updates coming in. So the goal of spark operator is to enable spark applications on top of kubernetes.

### Excerpt da transcript

Hello everyone. Super happy to be here in the CubeCon stage. Uh, welcome. I'm super excited to be here in London in my home city. I hope all of you enjoying the warm weather in April in London. So, my name is Andre. I work at Apple. Um, I've been this committee for the last 8 years. Right now, I'm the cubeflow steering committee. So, today we're going to share you the updates from the ecosystem at what's actually next for cloud native ML. And first of all, I think we'll spend um few minutes to introduce our panelists. So, you can start. Thank you. Uh I'm Yuki, a software engineer working for cyber agent and maintaining cubernetes cube cube for Q batch related CNC cell ecosystem tools. Hi everyone. Uh thank you for being here. My name is Yan. I'm a senior principal software engineer at Red Hat AI and I'm one of the steering committee members in Coupeflow and also a project lead for AGO and uh also co-chair in the Kubernetes working group serving. Hi everyone, I'm a technical director at Newanx AI um in open source.

I uh I'm part of the cubeflow steering committee and lead couple of AI initiatives um training and autoML and also in ML common storage. Hello and welcome. I'm Valentina Rodriguez. I'm a principal architect at Red Hat and also I contribute to QFlow on diverse projects. I'm also part of the release team and also work with the platform working groups and a case and I am a KCD organizer in New York. So thank you. Thanks you. Please welcome these amazing speakers to the panel. All right, so let's talk about Cubeflow. So first of all, let me ask you, how many of you actually know about Cubeflow? All right, how many of you actually successfully run this in production? All right, I see a few hands here. So just to remind everyone, uh Qflow is an ecosystem of open source projects. Uh so the goal of our community is to make it simple, uh to make AI and ML compares simple, portable, and scalable. You can run these components in any kubernetes cluster whether it's on-prem, third party cloud or local machines. Uh the beauty of the Qflow is composable platform.

So you can use individual components as a standalone application or as a complete end to- end platform. So this session will be focusing on GNI and LLM ops and our community in the quite recent years work really hard to actually enable Qflow components for geni and I think we can say that similar to AI and ML right now we all live in this new world and all these components actually you know you can e
