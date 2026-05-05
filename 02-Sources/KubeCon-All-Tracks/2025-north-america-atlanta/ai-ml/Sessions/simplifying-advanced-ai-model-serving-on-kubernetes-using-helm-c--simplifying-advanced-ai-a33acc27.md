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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Ajay Vohra", "Amazon", "Tianlu Caron Zhang", "Apple"]
sched_url: https://kccncna2025.sched.com/event/27FVb/simplifying-advanced-ai-model-serving-on-kubernetes-using-helm-charts-ajay-vohra-amazon-tianlu-caron-zhang-apple
youtube_search_url: https://www.youtube.com/results?search_query=Simplifying+Advanced+AI+Model+Serving+on+Kubernetes+Using+Helm+Charts+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Simplifying Advanced AI Model Serving on Kubernetes Using Helm Charts - Ajay Vohra, Amazon & Tianlu Caron Zhang, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Ajay Vohra, Amazon, Tianlu Caron Zhang, Apple
- Schedule: https://kccncna2025.sched.com/event/27FVb/simplifying-advanced-ai-model-serving-on-kubernetes-using-helm-charts-ajay-vohra-amazon-tianlu-caron-zhang-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Simplifying+Advanced+AI+Model+Serving+on+Kubernetes+Using+Helm+Charts+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Simplifying Advanced AI Model Serving on Kubernetes Using Helm Charts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVb/simplifying-advanced-ai-model-serving-on-kubernetes-using-helm-charts-ajay-vohra-amazon-tianlu-caron-zhang-apple
- YouTube search: https://www.youtube.com/results?search_query=Simplifying+Advanced+AI+Model+Serving+on+Kubernetes+Using+Helm+Charts+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PVB2hW8PuAM
- YouTube title: Simplifying Advanced AI Model Serving on Kubernetes Using Helm... Ajay Vohra & Tianlu Caron Zhang
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/simplifying-advanced-ai-model-serving-on-kubernetes-using-helm-charts/PVB2hW8PuAM.txt
- Transcript chars: 28397
- Keywords: inference, basically, cluster, server, worker, leader, models, actually, solution, examples, running, values, serving, actual, across, context, multi-node, essentially

### Resumo baseado na transcript

Uh my name is Karen John and currently I'm working as a senior machine learning engineer at Apple. >> So yeah, today jointly we'll be talking about simplifying advanced AI model serving on Kubernetes using Helmcharts. So what does a typical stack look like in serving AI models on Kubernetes? And then on top of that sits the deployment orchestration workflows which deploys the actual workflows to the Kubernetes cluster. And this layer is usually operated by the site reliability engineering team or also known as S SR. And this layer is usually implemented by machine learning engineers and used by application developers.

### Excerpt da transcript

Good afternoon everyone. Thank you for coming out to join our session during lunchtime. Uh my name is Karen John and currently I'm working as a senior machine learning engineer at Apple. >> And I'm AJ Vora. I'm a principal generative AI applied engineer at AWS. >> So yeah, today jointly we'll be talking about simplifying advanced AI model serving on Kubernetes using Helmcharts. As we all know, AI is evolving faster than ever. But to reliably serve the diverse types of models ranging from LLMs to multimodal models to stable diffusion models and so many more on Kubernetes still remains a very challenging task. So in today's talk we'll be sharing about some of the common challenges uh in bringing up this stack in Kubernetes faced by ML engineers like myself and the operations team and then we'll propose a solution. We'll also show you a demo in the end to see how everything comes together and we also will be sharing a QR code pointing to our GitHub repository for this project. So then you can go home and try it out yourself.

So hopefully at the end of the talk you can walk away with some practical ideas and tips that you can apply to your daily work right away. So this is a quick look into our agenda today. We'll kick things off by sh uh providing an overview of the Kubernetes AI model serving stack and this should be broadly applicable to all types of diverse models. Um and then we'll talk about the challenges in stack standing up such a stack in the realm of fast evolving AI space and then I'll hand it over to AJ who will talk about our solution and with two advanced examples and in the end we'll conclude with a recorded demo. So what does a typical stack look like in serving AI models on Kubernetes? Well, at a high level um at the most foundational layer, we have the hardware clusters consisting of machines, accelerators, network infrastructure pieces and this layer is usually provisioned and managed by the infrastructure engineering team. And then on top of that sits the deployment orchestration workflows which deploys the actual workflows to the Kubernetes cluster.

And this layer is usually operated by the site reliability engineering team or also known as S SR. And finally at the top we have inference servers, backends, the models of our choice and various a IML frameworks to run the actual model inference. And this layer is usually implemented by machine learning engineers and used by application developers. So the focus of today's talk will be mainl
