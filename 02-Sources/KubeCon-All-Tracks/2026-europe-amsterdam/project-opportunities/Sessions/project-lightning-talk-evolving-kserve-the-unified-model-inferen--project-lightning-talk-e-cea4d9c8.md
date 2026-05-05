---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Yuan Tang", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyW/project-lightning-talk-evolving-kserve-the-unified-model-inference-platform-for-both-predictive-and-generative-ai-yuan-tang-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Evolving+KServe%3A+The+Unified+Model+Inference+Platform+For+Both+Predictive+And+Generative+AI+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Evolving KServe: The Unified Model Inference Platform For Both Predictive And Generative AI - Yuan Tang, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yuan Tang, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyW/project-lightning-talk-evolving-kserve-the-unified-model-inference-platform-for-both-predictive-and-generative-ai-yuan-tang-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Evolving+KServe%3A+The+Unified+Model+Inference+Platform+For+Both+Predictive+And+Generative+AI+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Evolving KServe: The Unified Model Inference Platform For Both Predictive And Generative AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyW/project-lightning-talk-evolving-kserve-the-unified-model-inference-platform-for-both-predictive-and-generative-ai-yuan-tang-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Evolving+KServe%3A+The+Unified+Model+Inference+Platform+For+Both+Predictive+And+Generative+AI+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kE6lNBA56vM
- YouTube title: Project Lightning Talk: Evolving KServe: The Unified Model Inference Platform For Both... Yuan Tang
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-evolving-kserve-the-unified-model-inference-pla/kE6lNBA56vM.txt
- Transcript chars: 3526
- Keywords: predictive, kserve, inference, generative, serving, language, models, ai, supports, runtimes, autoscaling, amazing, contributors, features, request, support, improve, platform

### Resumo baseado na transcript

Kserve is a standardized, distributed and scalable model inference platform on Kubernetes for both predictive AI and generative AI. It supports a wide range of uh serving runtimes such as VRM for generative AI and XG boosts psych learn for predictive AI. So things like scaling to or front zero and request batching and uh security through o n and o z distributed tracing and autoscaling based on request uh on GPU and CPU uh usage logging of oh okay uh logging of uh request and response traffic management and out ofbox metric support. Uh so it we in order to scale better for large language models we have metrics based auto scaling. So for example you can use ka autoscaling to uh p basically autoscale based on metrics uh bas uh from your uh serving runtimes and we also support additional like geni runtimes such as VRM TRT RM and RMD to improve the efficiency of model serving and we also support pump caching to reduce the cost and also improve the throughput through features like intelligent routing and traffic management.

### Excerpt da transcript

Hello everyone. Uh can you hear me? Okay. Uh okay, cool. Before I start, uh I have one simple question. How many of you are running model inference in production today? What about predict predictive AI workloads? Okay. Large language models. Okay. Interesting to know. Uh so, okay. My name is Yantan. I'm a senior principal software engineer at Red Hat. I'm also a project lead for Kserve. So today I'm going to talk about Kserve. So what is Kserve? Kserve is a standardized, distributed and scalable model inference platform on Kubernetes for both predictive AI and generative AI. It supports a wide range of uh serving runtimes such as VRM for generative AI and XG boosts psych learn for predictive AI. Uh it also supports um integrates well with genai solutions such as LMD envoy AI gateway and RM cache. It's also integrated with cloudnative technologies uh such as K native and ka for autoscaling and u it supports gateway API from kubernetes uh so that it's compatible with esttol and envoy and everything is based on kubernetes so you can run it wherever kubernetes can be run so we joined the cncf as an incubating project uh in September last year and it's amazing to see so planning uh community adopters and organizations adopting and contributing to Kerve.

Uh we have 19 amazing maintainers so far and over 300 contributors accumulated over the years. So if you've been following Queso's history for a while, uh we started as a model serving project uh focused on predictive AI. uh we still have the features there in case you have predictive value workloads. So things like scaling to or front zero and request batching and uh security through o n and o z distributed tracing and autoscaling based on request uh on GPU and CPU uh usage logging of oh okay uh logging of uh request and response traffic management and out ofbox metric support. Um, and today we've been uh we've been actually working on generative AI features for long for a while ever since it got the traction from the uh the community. Uh so it we in order to scale better for large language models we have metrics based auto scaling. So for example you can use ka autoscaling to uh p basically autoscale based on metrics uh bas uh from your uh serving runtimes and we also support additional like geni runtimes such as VRM TRT RM and RMD to improve the efficiency of model serving and we also support pump caching to reduce the cost and also improve the throughput through features like intelligent routing and traffic
