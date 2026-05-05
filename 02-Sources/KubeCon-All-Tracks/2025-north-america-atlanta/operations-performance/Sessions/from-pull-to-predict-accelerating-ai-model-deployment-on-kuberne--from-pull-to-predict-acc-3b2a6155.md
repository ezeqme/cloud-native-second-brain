---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Lucas Duarte", "Tiago Reichert", "AWS"]
sched_url: https://kccncna2025.sched.com/event/27Fdm/from-pull-to-predict-accelerating-ai-model-deployment-on-kubernetes-lucas-duarte-tiago-reichert-aws
youtube_search_url: https://www.youtube.com/results?search_query=From+Pull+To+Predict%3A+Accelerating+AI+Model+Deployment+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Pull To Predict: Accelerating AI Model Deployment on Kubernetes - Lucas Duarte & Tiago Reichert, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Lucas Duarte, Tiago Reichert, AWS
- Schedule: https://kccncna2025.sched.com/event/27Fdm/from-pull-to-predict-accelerating-ai-model-deployment-on-kubernetes-lucas-duarte-tiago-reichert-aws
- Busca YouTube: https://www.youtube.com/results?search_query=From+Pull+To+Predict%3A+Accelerating+AI+Model+Deployment+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Pull To Predict: Accelerating AI Model Deployment on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fdm/from-pull-to-predict-accelerating-ai-model-deployment-on-kubernetes-lucas-duarte-tiago-reichert-aws
- YouTube search: https://www.youtube.com/results?search_query=From+Pull+To+Predict%3A+Accelerating+AI+Model+Deployment+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MdudBbHyb84
- YouTube title: From Pull To Predict: Accelerating AI Model Deployment on Kubernetes - Lucas Duarte & Tiago Reichert
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-pull-to-predict-accelerating-ai-model-deployment-on-kubernetes/MdudBbHyb84.txt
- Transcript chars: 31084
- Keywords: seconds, cluster, inference, storage, gpu, container, minutes, already, parallel, running, carpenter, loading, improve, models, actually, workloads, instances, important

### Resumo baseado na transcript

In this session today, we will speak a bit more about how you can improve your model deployments and reduce the cold start when you're scaling or deploying AI models on Kubernetes because it shouldn't take like 10 minutes for you to get your models up and running to do inference. My name is Lucas Darte, container specialist SA as covering ISV customers just like Thiago and yes, yet another talk about AI, but we promise to you that we're going to focus on infrastructure size of AI and how we can actually reduce the code start period. And then with more parameters, you require more >> storage >> storage as well. So if you consider like storage requirement, let's take an example like a 7 billion parameter model like Mistro, it can take up like from 3 GB into like 20 or even more GB in storage depending on the precision that you are using for that model. is Joe Martinez Joe Martinez is a leader at DevOps a DevOps leader at Octink Retail he has been running Kubernetes for a while now but he's new into a IML workloads you know just like us we are just getting started Joe Martinez has been running rock solid Kubernetes for the past eight years and guess what he also have a IDP and he doesn't have problems with upgrades.

### Excerpt da transcript

So welcome everyone. I hope you are enjoying KubeCon so far. In this session today, we will speak a bit more about how you can improve your model deployments and reduce the cold start when you're scaling or deploying AI models on Kubernetes because it shouldn't take like 10 minutes for you to get your models up and running to do inference. I'm Thiago Riker, solutions architect covering Latin America startups. And here with me I have Lucas. >> Hey folks, how you doing? My name is Lucas Darte, container specialist SA as covering ISV customers just like Thiago and yes, yet another talk about AI, but we promise to you that we're going to focus on infrastructure size of AI and how we can actually reduce the code start period. Any of you here is deploying inference workloads on top of Kubernetes? >> Yes. No. >> Yeah, like few people. Awesome. But if you are looking to get started, you can get started in a good way. Right, Chiago? >> Right. So, let's dive into it. >> Let's get into it. So before we go into the technical part itself, I think it's important to just notice how the customer experience is important for our businesses and latency directly impacts that customer experience.

If you think about like a web page when you're trying to browse something or like try to buy something in an e-commerce, if the page takes like four or five minutes to load, what will you do? I will probably go to the next page and buy it there. And there's a study that shows that 53% of people will go to another page if it's taking more than 3 seconds. And it's not just about seconds. Even 100 milliseconds can already influence your conversion rates by up to 7% according to this study from Makami. But Lucas, we are talking about latency. We are talking about customer experience. Why does this matter for the AI workloads? >> Yeah, before we understand why is it matter for the AI world, I think we already talked about that we're going to talk how to reduce code start. So it's essentially the time that it takes to deploy your inference endpoint on top of your cluster and the time that it takes for you to do the first inference request to your model. If we look at how AI has been evolving over the time over the years, we can look into 2018 with Bbas small language models the number of parameters was like were very few right and more the time passes more parameters the models are having.

So the models are becoming more generalist. Maybe someday we're going to end up in a terminator that
