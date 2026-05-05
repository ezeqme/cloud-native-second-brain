---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Kazuki Yamamoto", "NTT"]
sched_url: https://kccncna2025.sched.com/event/27Fe1/effortlessly-build-high-performance-aiml-processing-pipelines-within-the-ml-lifecycles-kazuki-yamamoto-ntt
youtube_search_url: https://www.youtube.com/results?search_query=Effortlessly+Build+High-Performance+AI%2FML+Processing+Pipelines+Within+the+ML+Lifecycles+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Effortlessly Build High-Performance AI/ML Processing Pipelines Within the ML Lifecycles - Kazuki Yamamoto, NTT

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Kazuki Yamamoto, NTT
- Schedule: https://kccncna2025.sched.com/event/27Fe1/effortlessly-build-high-performance-aiml-processing-pipelines-within-the-ml-lifecycles-kazuki-yamamoto-ntt
- Busca YouTube: https://www.youtube.com/results?search_query=Effortlessly+Build+High-Performance+AI%2FML+Processing+Pipelines+Within+the+ML+Lifecycles+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Effortlessly Build High-Performance AI/ML Processing Pipelines Within the ML Lifecycles.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fe1/effortlessly-build-high-performance-aiml-processing-pipelines-within-the-ml-lifecycles-kazuki-yamamoto-ntt
- YouTube search: https://www.youtube.com/results?search_query=Effortlessly+Build+High-Performance+AI%2FML+Processing+Pipelines+Within+the+ML+Lifecycles+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8s87fSa_Qmw
- YouTube title: Effortlessly Build High-Performance AI/ML Processing Pipelines Within the ML Life... Kazuki Yamamoto
- Match score: 0.971
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/effortlessly-build-high-performance-ai-ml-processing-pipelines-within/8s87fSa_Qmw.txt
- Transcript chars: 16050
- Keywords: pipeline, processing, second, gpu, performance, inference, deploy, explain, running, within, accelerators, infrastructures, finally, processed, deployed, update, manifest, stream

### Resumo baseado na transcript

I'd like to start my presentation titled a photo build high performance a IML processing pipeline within the ML life cycles. My research area is distributed systems and virtualization and I'm currently working on dataentric infrastructure which is promoted by Ibon global forum. So, we believe that the performance per power consumption is still insufficient compared with accelerators. Therefore, we see a room for performance improvement in the parts that are still processed by the CPU. To improve performance, we propose an execution model called the processing pipeline. So the processing pipeline can achieve high performance per power consumption.

### Excerpt da transcript

Hello everyone. I'd like to start my presentation titled a photo build high performance a IML processing pipeline within the ML life cycles. Okay. Yeah. Let me briefly introduce myself. I'm Yamamoto and a researcher at LT Corporation in Japan. My research area is distributed systems and virtualization and I'm currently working on dataentric infrastructure which is promoted by Ibon global forum. In short, my research focuses on control software for ICT infrastructures and today's presentation is also part of the work. Here's today's agenda. First, I'll explain the introduction and the talk. Next I'll show you a demonstration and finally I'll talk about our future work. Now let's move on to the introduction. Yeah, let's start with the current issue and requirements faced by ICT infrastructures. We're seeing advances in sensing, networking and AI technologies and they are driving the demand for realtime air processing in ICD infrastructures. The amount of data in these infrastructures keeps growing and we we process more and more data.

The power consumption keeps increasing. Therefore, both high performance and power efficiency are now required in ICT infrastructures. Let's take a look at current execution model. So, we believe that the performance per power consumption is still insufficient compared with accelerators. The CPU provides lower performance per power consumption. Yet it still has many tasks such as prep-processing and post-processing. At the same time, power efficient accelerators are mainly used only for specific tasks such as inference. Therefore, we see a room for performance improvement in the parts that are still processed by the CPU. To improve performance, we propose an execution model called the processing pipeline. In this model, each task uses the most suitable obser. So the processing pipeline can achieve high performance per power consumption. The reason behind this proposal is a recent emergence of accelerators such as TPU and TPU and so on. Based on this, we believe that tasks executed on CPUs will be shifted to more specialized hardware.

However, this also raises an important question. Since the processing pipeline use multiple and heterogeneous, users might wonder if using multiple seems challenging. They may also worry that this approach could increase development development cost or reduce usability. But don't worry, the concept of processing pipeline is rooted in dataentric approach. In other words, application side users can
