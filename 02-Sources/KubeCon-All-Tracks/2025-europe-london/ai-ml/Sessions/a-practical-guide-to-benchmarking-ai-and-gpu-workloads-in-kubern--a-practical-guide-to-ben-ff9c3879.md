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
speakers: ["Yuan Chen", "NVIDIA", "Chen Wang", "IBM Research"]
sched_url: https://kccnceu2025.sched.com/event/1tx7Q/a-practical-guide-to-benchmarking-ai-and-gpu-workloads-in-kubernetes-yuan-chen-nvidia-chen-wang-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=A+Practical+Guide+To+Benchmarking+AI+and+GPU+Workloads+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Practical Guide To Benchmarking AI and GPU Workloads in Kubernetes - Yuan Chen, NVIDIA & Chen Wang, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Yuan Chen, NVIDIA, Chen Wang, IBM Research
- Schedule: https://kccnceu2025.sched.com/event/1tx7Q/a-practical-guide-to-benchmarking-ai-and-gpu-workloads-in-kubernetes-yuan-chen-nvidia-chen-wang-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=A+Practical+Guide+To+Benchmarking+AI+and+GPU+Workloads+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Practical Guide To Benchmarking AI and GPU Workloads in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7Q/a-practical-guide-to-benchmarking-ai-and-gpu-workloads-in-kubernetes-yuan-chen-nvidia-chen-wang-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=A+Practical+Guide+To+Benchmarking+AI+and+GPU+Workloads+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OnqzoBf7dUE
- YouTube title: A Practical Guide To Benchmarking AI and GPU Workloads in Kubernetes - Yuan Chen & Chen Wang
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-practical-guide-to-benchmarking-ai-and-gpu-workloads-in-kubernetes/OnqzoBf7dUE.txt
- Transcript chars: 24892
- Keywords: server, performance, request, workload, triton, benchmarking, models, gpu, inference, benchmark, simple, actually, client, nvidia, library, deployment, already, python

### Resumo baseado na transcript

Uh I'm working and with the Nvidia DJX cloud to build Kubernetes optimized AI infrastructure platform and for AI and GPU workload. I've been a very active contributors to kubernetes and six kubernetes including the autoscaling scheduling community and now uh I'm contributing to the working group of serving as well uh like this benchmarking tool. Then the second is deploy the Triton server instance itself also and Triton provide and there are some client or workload generation tool and the performance uh collection tool uh core performance analyzer can collect send request and collect all this performance data. So a lot of models and available online you can just download it and uh yeah store and uh in a storage or file system. tool is called a performance and analyzer it can generate the request sent to the triton and the inference server it's also support tensson flow and the torch ser as well. want to measure the performance here is some sample and the output right how many requests you send also the latency different percentile percentile 50 percentile 99 percentile and detail and also the different concurrency level.

### Excerpt da transcript

Good morning. Welcome to our session. I'm Yen Chen from Nvidia. Okay, let's echo from another room. Uh I'm working and with the Nvidia DJX cloud to build Kubernetes optimized AI infrastructure platform and for AI and GPU workload. Hello, I'm Chen uh a senior research scientist from uh IBM research. I've been a very active contributors to kubernetes and six kubernetes including the autoscaling scheduling community and now uh I'm contributing to the working group of serving as well uh like this benchmarking tool. Okay. So in today's session we are going to walk through how to run model inference benchmarking use the Triton inference server and uh FM performance tools. We will also cover how to run the GPU intensive workload. In this talk we'll also cover some of the monitoring tool like the Nvidia SMI and another tool called GPU stats. uh we'll briefly and uh overview give an overview of all the benchmark tools hopefully and uh you will find this session helpful. Okay, let me start it and uh so firstly the Triton inference server is very popular and uh inference server and it's open source tool can run and uh a bunch of different models and uh from like uh the typical and uh uh all this and popular models and you can use it.

It supported x86 and ARM also provide uh uh some client library and the tools including uh running on the edge and mobile devices. Uh also recently Nvidia announced and advanced version called Dynamo. It extend and uh optimize the Triton uh with advanced features for improved scalability and performance. So in order to set up a triton uh inference so there are three and key steps the firstly and you need to create a model repository and populate and with all kind of different models I will cover next the some details how to do that. Then the second is deploy the Triton server instance itself also and Triton provide and there are some client or workload generation tool and the performance uh collection tool uh core performance analyzer can collect send request and collect all this performance data. So I will go through each of them one by one. So for model and uh uh deployment and Triton support and all different models from PyTorch and uh to like the standard OMX models and not VLM. So some example models like Nama and FCON and other thing.

So if you look at the the the structure of the model repository basically and you can populate and deploy and all different models. So each model is a subdirectory you name and the models under each
