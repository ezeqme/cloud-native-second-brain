---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["AI ML", "Observability", "SRE Reliability"]
speakers: ["Vincent Hou", "Bloomberg", "Jiří Kremser", "kedify.io"]
sched_url: https://kccnceu2025.sched.com/event/1txI4/optimizing-metrics-collection-serving-when-autoscaling-llm-workloads-vincent-hou-bloomberg-jiri-kremser-kedifyio
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+Metrics+Collection+%26+Serving+When+Autoscaling+LLM+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Optimizing Metrics Collection & Serving When Autoscaling LLM Workloads - Vincent Hou, Bloomberg & Jiří Kremser, kedify.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Vincent Hou, Bloomberg, Jiří Kremser, kedify.io
- Schedule: https://kccnceu2025.sched.com/event/1txI4/optimizing-metrics-collection-serving-when-autoscaling-llm-workloads-vincent-hou-bloomberg-jiri-kremser-kedifyio
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+Metrics+Collection+%26+Serving+When+Autoscaling+LLM+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Optimizing Metrics Collection & Serving When Autoscaling LLM Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txI4/optimizing-metrics-collection-serving-when-autoscaling-llm-workloads-vincent-hou-bloomberg-jiri-kremser-kedifyio
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+Metrics+Collection+%26+Serving+When+Autoscaling+LLM+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lefjb4Vnd8k
- YouTube title: Optimizing Metrics Collection & Serving When Autoscaling LLM Workloads - Vincent Hou & Jiří Kremser
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/optimizing-metrics-collection-serving-when-autoscaling-llm-workloads/lefjb4Vnd8k.txt
- Transcript chars: 25816
- Keywords: metrics, matrix, number, metric, autoscaling, gpu, cluster, actually, workloads, language, called, scaling, second, resource, serving, workload, another, requests

### Resumo baseado na transcript

Um but before you're doing that shall we make our session optimizing matrix collection and serving when autoscaling large language model workloads as a warm up of your fun time. My team is specializ in building and maintaining AI inference platform. We have HPA for horizontal scaler and VPA as a vertical scaler but we'll focus on the horizontal autoscaling in cube today. because we like to efficiently leverage use our resources without influencing the uh service uptime performance. They can be the custom metrics exposed by our workload and they can be metrics that possibly come from outside workload. On one end it can discover and aggregate those metrics from registry on the other end and make sure that the HPA can read the metric from it.

### Excerpt da transcript

Good afternoon. London, I would say. How's everybody doing? Come on. It's been a long day. I know you want to go home. I had to go to parties, right? Come on. Um but before you're doing that shall we make our session optimizing matrix collection and serving when autoscaling large language model workloads as a warm up of your fun time. My name is Vincent Ho. It's my honor to team up with Hey, my name is today. I'm a senior software engineer working with Bloomberg. My team is specializ in building and maintaining AI inference platform. I've been the lead of K native operation work group for six years. I've been evangelizing open technology and contributing to open source projects. During the past 10 years maybe maybe more um like open stack open kurf but don't worry we'll focus on the three dots today. Jerry. Yeah. So my name is Urka. I work on a cool company called Kify where we try to do production grade KDA and I'm also contributor to the project called KGB. I like open source 3D printing and you will see me in the uh second half of the of the session.

So see you. Okay. Thank you Jerry. This is our agenda for today. I will start with how in general autoscaling works horizontal auto scaling works in Kubernetes and talk about the challenges which large language work uh with large language model workloads and the existing autoscaling solution in the market and how we optimize the matrix collection and serving with our solutions. In the end, we'll run a demo previous episodes in CubeCon. Tell me why and tell me why. I'm sorry I cannot think here today. Uh I used to carry many questions about how we can scale large model workloads and what kind of matches we can leverage. Have fun time on that stage. And thanks to these awesome folks I met in Salt Lake City, Arshock from Google, Lumila from Microsoft and David from Red Hat. After attending their sessions, my confusion will resolved a lot. I put the links over here to their talks. You can refer to later. Okay. For our session as it's in London, let's shall we do something special for London. Huh? To be or not to be.

I am going to do it. Act one. Auto skating is heavy and light, bright and dark, hot and cold, seek and healthy, asleep and awake is everything except what it is. Oh, it is so complicated. In cloud computing, autoscaling is a method to dynamically adjust the resource based on the load automatically. In cube it means a feature that allows the cluster to increase or decrease the number of pods or jus
