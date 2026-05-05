---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Application Development"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Ashley Cui", "Urvashi Mohnani", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CW0M/from-laptop-to-cluster-running-ai-workloads-seamlessly-from-podman-to-kubernetes-ashley-cui-urvashi-mohnani-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=From+Laptop+to+Cluster%3A+Running+AI+Workloads+Seamlessly+from+Podman+to+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Laptop to Cluster: Running AI Workloads Seamlessly from Podman to Kubernetes - Ashley Cui & Urvashi Mohnani, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ashley Cui, Urvashi Mohnani, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CW0M/from-laptop-to-cluster-running-ai-workloads-seamlessly-from-podman-to-kubernetes-ashley-cui-urvashi-mohnani-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=From+Laptop+to+Cluster%3A+Running+AI+Workloads+Seamlessly+from+Podman+to+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Laptop to Cluster: Running AI Workloads Seamlessly from Podman to Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0M/from-laptop-to-cluster-running-ai-workloads-seamlessly-from-podman-to-kubernetes-ashley-cui-urvashi-mohnani-red-hat
- YouTube search: https://www.youtube.com/results?search_query=From+Laptop+to+Cluster%3A+Running+AI+Workloads+Seamlessly+from+Podman+to+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6DkdGa2G7W0
- YouTube title: From Laptop to Cluster: Running AI Workloads Seamlessly from Podman... Ashley Cui & Urvashi Mohnani
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-laptop-to-cluster-running-ai-workloads-seamlessly-from-podman-to/6DkdGa2G7W0.txt
- Transcript chars: 20785
- Keywords: container, podman, running, llm, agentic, containers, actually, locally, inside, environment, deploy, models, artifact, working, agents, laptop, started, secure

### Resumo baseado na transcript

I am a principal software engineer at Red Hat working on container technologies and open shift. I am a software engineer at Red Hat and I am working on um, container tools such as Podman. Uh so uh podman there's a big emphasis on security with podman right and um podman is great uh for running things in a secure way and what's better uh so so ram malama actually does use podman under the hood um to run uh Um so this makes sense uh as uh because we've solved this problem before, right? Um and uh podman also is really great because it's able to bridge from local development um on your local pods in your system into uh something uh like a kubernetes pod. But uh that's kind of our end goal uh in deploying going from podman and kubernetes.

### Excerpt da transcript

Hello everyone. Welcome to our talk today. Um, thank you for showing up at 5:00 PM. I know we're standing in between you and CubeCrawl right now. Um, but my name is Roishi Manani. I am a principal software engineer at Red Hat working on container technologies and open shift. >> Um, hi everyone. Uh, my name is Ashley. I am a software engineer at Red Hat and I am working on um, container tools such as Podman. Um so our talk is going to be uh from laptop to cluster running AI workloads seamlessly from podman to kubernetes. Um so I'm going to start with just a brief overview of the timeline of uh kind of the boom in AI in the 2020s. Um starting I sure you guys know this already but starting 2022 chat GPT is released and this is kind of the start of a new era where people saw this crazy new technology and were uh generated a huge amount of interest. In 2023, um we kind of saw the AI race where uh different companies wanted to get into uh the AI uh industry and so other LLMs including Llama, Claude, Gemini enter the scene.

In 2024, we saw kind of industry adoption. Um so anti AI integration started showing up everywhere. Everybody wanted to see how they could use AI in their own businesses. And recently in 2025, we seen a shift toward agentic AI. So uh in 2022 and 2023 we saw kind of the chatbot model of AI where we would ask the uh AI questions and it would respond. But uh more recently uh we've seen the power in letting the AI actually do the work for you um in being able to execute things um and also uh you know I we've probably all uh worked with generating code um using aentic AI. Um so I seeing this shift uh go from chat bots uh into everybody being like this is a really cool technology that we want to use um into something that people use on a daily basis. Uh how how do we do this like in a way that's easy and secure. Um so there's a lot of increasing usage and adoption of AI. Uh and uh one of the things that people really like to do uh with their LLMs is to uh to custom tune them um depending on their own needs.

Um so uh what would be a good way uh to be able to kind of share uh your uh custom tuned AI needs. Um and then also the current trends toward uh moving towards agentic workflows. Um why consult an AI when it actually can execute and do the work for you? Um, of course, these agentic AIs still need an LLM in the back to do the thinking and then it and then it processes things to uh actually do the work. Um, the thing with agentic AI is with power
