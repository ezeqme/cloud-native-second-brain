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
themes: ["AI ML", "Runtime Containers", "Kubernetes Core"]
speakers: ["Samuel Veloso", "Cast AI", "Lucas Fernández", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1tx97/orchestrating-ai-models-in-kubernetes-deploying-ollama-as-a-native-container-runtime-samuel-veloso-cast-ai-lucas-fernandez-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Orchestrating+AI+Models+in+Kubernetes%3A+Deploying+Ollama+as+a+Native+Container+Runtime+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Orchestrating AI Models in Kubernetes: Deploying Ollama as a Native Container Runtime - Samuel Veloso, Cast AI & Lucas Fernández, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Samuel Veloso, Cast AI, Lucas Fernández, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1tx97/orchestrating-ai-models-in-kubernetes-deploying-ollama-as-a-native-container-runtime-samuel-veloso-cast-ai-lucas-fernandez-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Orchestrating+AI+Models+in+Kubernetes%3A+Deploying+Ollama+as+a+Native+Container+Runtime+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Orchestrating AI Models in Kubernetes: Deploying Ollama as a Native Container Runtime.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx97/orchestrating-ai-models-in-kubernetes-deploying-ollama-as-a-native-container-runtime-samuel-veloso-cast-ai-lucas-fernandez-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Orchestrating+AI+Models+in+Kubernetes%3A+Deploying+Ollama+as+a+Native+Container+Runtime+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zLpUJBU6sT4
- YouTube title: Orchestrating AI Models in Kubernetes: Deploying Ollama as a Nati... Samuel Veloso & Lucas Fernández
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/orchestrating-ai-models-in-kubernetes-deploying-ollama-as-a-native-con/zLpUJBU6sT4.txt
- Transcript chars: 26806
- Keywords: container, runtime, create, models, containerd, everything, sandbox, containers, deployment, request, available, cluster, custom, binary, interface, running, format, registry

### Resumo baseado na transcript

We are talking about orchestrating AI models in Kubernetes specifically deploying Olama as a native container runtime. I am in the security team where we are building a product to find and fix vulnerabilities and anomalies in Kubernetes environments. So when h we were experimenting with Olama the one question that came to our mind was okay this is for local but what happens with kubernetes how can we run in kubernetes so the first option is there is a a helm chart that you can use it's it works pretty well and it's really well maintained so it's a a very valid options but we were thinking about can we do it in a more kubernetes native way can we use a deployment? What happens if we put the model that we are pulling locally but in the deployment image as we are doing with any other Kubernetes application okay and it's possible we need to set in our deployment uh this runtime class name okay that we uh it was introduced in Kubernetes 120 so while back ago and actually it's the way that for example containerd one of the most famous uh container runtimes it's the way it implements the runc so when containerd needs to create a container it to

### Excerpt da transcript

Okay, let's start. We are talking about orchestrating AI models in Kubernetes specifically deploying Olama as a native container runtime. So my name is Samuel Beloso. I work as a software engineer at cast AI. I am in the security team where we are building a product to find and fix vulnerabilities and anomalies in Kubernetes environments. Yeah. And I'm Lucas. I work at Red Hat in the Roy Red Hat AI platform and I'm also a QFlow contributor member. Yeah. So I work in security but today I'm going to talk about AI or more about Kubernetes. Okay. And how Kubernetes works internally. So let's start. So if you have never used Olama, if it's the first time you hear uh this tool, Olama is a CLI tool to run models, AI models locally in a very simple way. Okay, this is the GitHub repository of Olama and you can run the most famous model like deepse lama and any other AI models and it's uh very popular. I don't know if you are aware but the number of stars in the GitHub repository in the Olama GitHub repository is 134K it's even more than Kubernetes so it's yeah it's crazy and only in the last year or year and a half and why is that I mean the AI hype is real and also I think it's because of the simplicity because if uh if you want to run a model locally with Ola.

What you have to do is first you need to download and install the Olama binary from the Olama website. You need to start the Olama server in the background and then you download your model with Olama pool. For example, in this case it's uh the Lama 3 8 billion parameters model and to use the model you only need just to execute run and the name of the model you recently pulled and that's it. Then you can start talking with your LLM as you are doing with satp. But locally you can also consume the APIs for example and integrate copilot or any other tool with the with with the model locally. So you don't need to send your data to an external or to a third party server. So and if you this could sounds familiar to you because the pool and run is very similar to docker. So the ui ux is pretty much uh the same. So is to models what docker is to containers. It's a a tool that simplifies the yeah the deployment of models. So when h we were experimenting with Olama the one question that came to our mind was okay this is for local but what happens with kubernetes how can we run in kubernetes so the first option is there is a a helm chart that you can use it's it works pretty well and it's really well maintained so it'
