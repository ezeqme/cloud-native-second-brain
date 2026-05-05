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
themes: ["Observability"]
speakers: ["Prashant Gupta", "Kruthika Prasanna Simha", "Apple"]
sched_url: https://kccnceu2025.sched.com/event/1txE3/first-day-foresight-anomaly-detection-for-observability-prashant-gupta-kruthika-prasanna-simha-apple
youtube_search_url: https://www.youtube.com/results?search_query=First+Day+Foresight%3A+Anomaly+Detection+for+Observability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# First Day Foresight: Anomaly Detection for Observability - Prashant Gupta & Kruthika Prasanna Simha, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Prashant Gupta, Kruthika Prasanna Simha, Apple
- Schedule: https://kccnceu2025.sched.com/event/1txE3/first-day-foresight-anomaly-detection-for-observability-prashant-gupta-kruthika-prasanna-simha-apple
- Busca YouTube: https://www.youtube.com/results?search_query=First+Day+Foresight%3A+Anomaly+Detection+for+Observability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre First Day Foresight: Anomaly Detection for Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txE3/first-day-foresight-anomaly-detection-for-observability-prashant-gupta-kruthika-prasanna-simha-apple
- YouTube search: https://www.youtube.com/results?search_query=First+Day+Foresight%3A+Anomaly+Detection+for+Observability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jiT7kGqcpR4
- YouTube title: First Day Foresight: Anomaly Detection for Observability - Prashant Gupta & Kruthika Prasanna Simha
- Match score: 0.818
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/first-day-foresight-anomaly-detection-for-observability/jiT7kGqcpR4.txt
- Transcript chars: 28778
- Keywords: detection, anomaly, models, learning, simple, actually, cubeflow, production, metrics, metric, finally, development, training, machine, already, anomalies, complex, engineering

### Resumo baseado na transcript

All right, so today we're going to talk about day one anomaly detection for observability. But before we get started, we'll take a quick moment to introduce ourselves. In today's talk, we'll talk about how combining metrics, models, and modern-day observability tools can actually shift your approach from being reactive to proactive. Uh we'll talk about the cold start problem and how to overcome it with like a simple demo. You want to ensure that your product has good reliability um availability and performance. We also track some low-level infrastructure metrics like memory, bit rate, etc.

### Excerpt da transcript

Okay, good morning everyone. Thank you for being here with us today. Um, I hope you're all enjoying CubeCon so far. Yes, I will take that as a yes. All right, so today we're going to talk about day one anomaly detection for observability. But before we get started, we'll take a quick moment to introduce ourselves. Hi, I'm Kitika. I'm a machine learning engineer at Apple and I work with the observability team and my background is in observability, machine learning and data science. Prashant. Hello everyone. Uh, I'm Prashant. I'm also a machine learning engineer at Apple. I also am a part of the observability team and my background is in machine learning, natural language processing and observability. All right. Okay. So for those of you who attended our talk last year in CubeCon uh Salt Lake City, we spoke about how we can leverage anomaly detection to not just improve MTD which is meantime to detect but also improve meanantime to resolve by just ingesting some additional information and bootstrapping the anomaly detection models.

But for those of you who did not attend our talk, there is a QR code up there which you guys can just take a picture of. Um it's on YouTube, you can watch it. So now Prashant will go into what we're going to talk about today. All right, thank you Critica. So we, as Kitika mentioned, we previously talked about anomaly detection and how it helps to detect and resolve incidents faster. But we actually wanted to take it a step further and see if we can actually increase the time between failures. That is if you can improve the mean time between failures. In today's talk, we'll talk about how combining metrics, models, and modern-day observability tools can actually shift your approach from being reactive to proactive. We'll start with a case study of day one anomaly detection. Uh we'll talk about the cold start problem and how to overcome it with like a simple demo. And then we can also talk about how to train and serve more complex models with CubeFlow. So here's what we are hoping you'll walk away with.

First, anomaly detection isn't just a post-production tool. It should be a day one decision. Second, great anomaly detection starts with great observability. And that's not just metrics, but meaningful metrics. Your feature engineering should be your first model. Next, your model should align with your operational reality. You need models that strike the right balance between accuracy, latency, and interpretability to drive the max
