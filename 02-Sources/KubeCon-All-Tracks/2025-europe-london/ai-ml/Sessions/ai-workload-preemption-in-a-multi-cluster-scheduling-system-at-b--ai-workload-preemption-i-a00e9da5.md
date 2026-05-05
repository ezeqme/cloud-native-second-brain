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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Leon Zhou", "Wei-Cheng Lai", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1tx7W/ai-workload-preemption-in-a-multi-cluster-scheduling-system-at-bloomberg-leon-zhou-wei-cheng-lai-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=AI+Workload+Preemption+in+a+Multi-Cluster+Scheduling+System+at+Bloomberg+CNCF+KubeCon+2025
slides: []
status: parsed
---

# AI Workload Preemption in a Multi-Cluster Scheduling System at Bloomberg - Leon Zhou & Wei-Cheng Lai, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Leon Zhou, Wei-Cheng Lai, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1tx7W/ai-workload-preemption-in-a-multi-cluster-scheduling-system-at-bloomberg-leon-zhou-wei-cheng-lai-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=AI+Workload+Preemption+in+a+Multi-Cluster+Scheduling+System+at+Bloomberg+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre AI Workload Preemption in a Multi-Cluster Scheduling System at Bloomberg.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7W/ai-workload-preemption-in-a-multi-cluster-scheduling-system-at-bloomberg-leon-zhou-wei-cheng-lai-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=AI+Workload+Preemption+in+a+Multi-Cluster+Scheduling+System+at+Bloomberg+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LrL5AcS2d5g
- YouTube title: AI Workload Preemption in a Multi-Cluster Scheduling System at Bloomberg - Leon Zhou & Wei-Cheng Lai
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ai-workload-preemption-in-a-multi-cluster-scheduling-system-at-bloombe/LrL5AcS2d5g.txt
- Transcript chars: 23803
- Keywords: priority, workloads, resource, scheduling, training, clusters, workload, preeemption, cluster, platform, gpu, resources, business, bloomberg, critical, source, preemption, experience

### Resumo baseado na transcript

Today we're excited to share how Bloomber manages AI workflow fiction in a mill cluster scheduling system. And in this talk we'll discuss how we schedule and prioritize thousands of AI training jobs across mul kubernetes. So to understand our challenges, it helps to know a bit about Bloomberg. We heavily leverage AI and machine learning to deliver timely and accountable insights to our clients. We leverage Kubernetes for managing GPU intensive workloads and utilize tools like Jupyter notebooks, Carmada, Qflow, Ker and Argo workflow for model development, training, deployment and automatic workflows. In short, our data science platform is a central open source power asset that empowers Bloomer's teams to rapidly build, deploy and scale AIdriven products.

### Excerpt da transcript

Hello everyone. Thank you for joining us. My name is Way Chanai and my name is Leon. Today we're excited to share how Bloomber manages AI workflow fiction in a mill cluster scheduling system. And in this talk we'll discuss how we schedule and prioritize thousands of AI training jobs across mul kubernetes. Oh, at Bloomberg. Our goal is to show you how we improve system reliability and business agility by ensuring critical AI workloads get the resources they need when they need them. Uh let me start by outlining the road map for today's presentation. First, I will briefly introduce Bloomberg and the critical role AI plays within our business. Then we'll discuss our data science platform and describe our advanced millluster training infrastructure built on Kubernetes. I'll introduce Carmada, an open source orchestration tool we use to efficiently manage these multiple clusters and highlights key concepts and APIs. Next, we'll explore the resource allocation challenges we encountered as demand for our AI workloads grew, emphasizing why establishing clear workflow priorities became essential.

Finally, I'll explain our need for priority based scheduling and preeemption which ensures critical tests get the resources they require promply. At that point, I'll hand over to Leon who will dive deeper into the implementation details, share our experience and insights and outline our community collaboration and future road map. So to understand our challenges, it helps to know a bit about Bloomberg. Bloomberg is a global financial technology company known primarily for the Bloomberg terminal. Widely used by financial professionals, the terminal provides real-time access to market data, news, analytics, research and communication tools, enabling informed decision making, handling vast streams of data daily. We heavily leverage AI and machine learning to deliver timely and accountable insights to our clients. So, how does Bloomberg use AI to enhance its products and services? Here are a few key examples. For extra extraction, we use AI to parse financial documents and new articles, accurately identifying and linking important details like companies prices and dates.

And we enhance extracted data to improve discoverability, such as adding metadata or linking related content. We also use AI to power personalized and efficient searches within our vest data, helping users and relevant information quickly to tackle information overload. AI provides concise summaries of news
