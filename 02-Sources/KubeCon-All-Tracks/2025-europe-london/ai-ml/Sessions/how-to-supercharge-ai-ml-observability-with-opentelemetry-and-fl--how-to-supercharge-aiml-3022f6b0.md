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
themes: ["AI ML", "Observability"]
speakers: ["Celalettin Calis", "Chronosphere"]
sched_url: https://kccnceu2025.sched.com/event/1txAi/how-to-supercharge-aiml-observability-with-opentelemetry-and-fluent-bit-celalettin-calis-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=How+To+Supercharge+AI%2FML+Observability+With+OpenTelemetry+and+Fluent+Bit+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How To Supercharge AI/ML Observability With OpenTelemetry and Fluent Bit - Celalettin Calis, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Celalettin Calis, Chronosphere
- Schedule: https://kccnceu2025.sched.com/event/1txAi/how-to-supercharge-aiml-observability-with-opentelemetry-and-fluent-bit-celalettin-calis-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+Supercharge+AI%2FML+Observability+With+OpenTelemetry+and+Fluent+Bit+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How To Supercharge AI/ML Observability With OpenTelemetry and Fluent Bit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAi/how-to-supercharge-aiml-observability-with-opentelemetry-and-fluent-bit-celalettin-calis-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=How+To+Supercharge+AI%2FML+Observability+With+OpenTelemetry+and+Fluent+Bit+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DVFQ20OrEFk
- YouTube title: How To Supercharge AI/ML Observability With OpenTelemetry and Fluent Bit - Celalettin Calis
- Match score: 0.974
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-to-supercharge-ai-ml-observability-with-opentelemetry-and-fluent-b/DVFQ20OrEFk.txt
- Transcript chars: 11509
- Keywords: logs, metrics, traces, observability, fluent, application, models, instrumentation, platform, basically, resource, llm, matrix, monitoring, invisible, context, multiple, issues

### Resumo baseado na transcript

So, today just we are going to talk about how you can just supercharge your AIM ML observability. So uh for the first talk we're just going to talk about uh practical strategies for monitoring a IML workloads on Kubernetes environments and at the end I'm going to show you a pretty quick demo. You can just forecast your traffic and just scale based on that earlier or you can do workload isolation. So for example unified telemetry collection serve uh collecting telemetry across heterogenous components is really hard and there's an issue with the kubernetes a context pro uh propagation. So specialized monitoring for machine learning components and you have to just connect your infrastructure metrics with the machine learning outcomes. Uh so do you have any issues with the model performance with input tracking?

### Excerpt da transcript

Okay. Yeah. So, hello everyone. So, welcome to last session of CubeCon. I hope it was a good experience for you. So, today just we are going to talk about how you can just supercharge your AIM ML observability. uh using open telemetry and fluently. So uh for the first talk we're just going to talk about uh practical strategies for monitoring a IML workloads on Kubernetes environments and at the end I'm going to show you a pretty quick demo. So a little bit about me. So uh for the last six years uh I'm just focusing on Kubernetes reliability and cloud infrastructure. So I'm working at Chronosphere. Uh so Chronosphere is observable platform. So I'm just contributing uh that observes the platform. I am also open source contributor. Uh so Fluent B beat CI/CD maintainer. And you can just see me on the fluent bit with select channels and my personal mission is like making invisible intelligence visible and action actionable for everyone. So there are a couple of challenges with the Kubernetes. So for example, ephemeral compute.

So ports come and go quickly. They they just basically take their logs and context with them. uh resource organiz orchestration. So there's a dynamic scheduling shift workloads across nodes constantly and autoscaling. Uh so training and inference workloads just scale differently based on their patterns and multi-tenency. You can just deploy multiple ML models and share same infrastructure with different priorities. I think we already have a solution for them. So you can just purchase your logs to some external log storage. You can just detect for example lemon nodes if you have issues with the nodes. You can just do predictive scaling. You can just forecast your traffic and just scale based on that earlier or you can do workload isolation. Those are the known issues. But there are some technical gaps uh with the aiml application that I am going to mention more. So for example unified telemetry collection serve uh collecting telemetry across heterogenous components is really hard and there's an issue with the kubernetes a context pro uh propagation.

uh maintaining context as requests travel through the services. You have multiple services and there are very different ML framework specific instrumentation. So specialized monitoring for machine learning components and you have to just connect your infrastructure metrics with the machine learning outcomes. So these gaps are basically create create a blind spot in ML operations team just str
